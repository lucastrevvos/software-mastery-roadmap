# RabbitMQ retry com atraso de 5s — checkpoint comprovado

## Objetivo
Substituir o hot retry (`nack(..., requeue=true)`) por retry assíncrono com atraso controlado pelo RabbitMQ.

## Topologia comprovada

```text
payments_queue
  -- NACK requeue=false --> payments.retry
  --> payments_retry_5s
  -- TTL 5000ms / expired --> payments.return
  --> payments_queue
```

## Comandos executados

### 1. Inspecionar policies existentes

```bash
docker compose exec rabbitmq rabbitmqctl list_policies
```

Objetivo: verificar a policy anterior de DLX aplicada à `payments_queue` antes de alterar a estratégia de falha.

### 2. Remover temporariamente a policy antiga da fila principal

```bash
docker compose exec rabbitmq rabbitmqctl clear_policy payments-dlx
```

Objetivo: deixar de mandar `payments_queue` diretamente para a DLQ final enquanto o laboratório de retry é montado.

### 3. Criar o exchange de retry

```bash
curl -u app:app -X PUT http://localhost:15672/api/exchanges/%2F/payments.retry -H "Content-Type: application/json" -d '{"type":"direct","durable":true,"auto_delete":false,"internal":false,"arguments":{}}'
```

### 4. Criar o exchange de retorno

```bash
curl -u app:app -X PUT http://localhost:15672/api/exchanges/%2F/payments.return -H "Content-Type: application/json" -d '{"type":"direct","durable":true,"auto_delete":false,"internal":false,"arguments":{}}'
```

### 5. Criar a fila de retry de 5 segundos

```bash
curl -u app:app -X PUT http://localhost:15672/api/queues/%2F/payments_retry_5s -H "Content-Type: application/json" -d '{"durable":true,"auto_delete":false,"arguments":{}}'
```

### 6. Binding: exchange de retry -> fila de retry

```bash
curl -u app:app -X POST http://localhost:15672/api/bindings/%2F/e/payments.retry/q/payments_retry_5s -H "Content-Type: application/json" -d '{"routing_key":"payments.retry","arguments":{}}'
```

Resultado lógico:

```text
payments.retry
  -- routing key payments.retry --> payments_retry_5s
```

### 7. Binding: exchange de retorno -> fila principal

```bash
curl -u app:app -X POST http://localhost:15672/api/bindings/%2F/e/payments.return/q/payments_queue -H "Content-Type: application/json" -d '{"routing_key":"payments.return","arguments":{}}'
```

Resultado lógico:

```text
payments.return
  -- routing key payments.return --> payments_queue
```

### 8. Configurar TTL e dead-letter da fila de retry

```bash
docker compose exec rabbitmq rabbitmqctl set_policy payments-retry-5s "^payments_retry_5s$" '{"message-ttl":5000,"dead-letter-exchange":"payments.return","dead-letter-routing-key":"payments.return"}' --apply-to queues --priority 20
```

Significado:
- a mensagem permanece em `payments_retry_5s` por até 5000 ms;
- quando expira, RabbitMQ faz dead-letter para `payments.return`;
- `payments.return` roteia a mensagem de volta para `payments_queue`.

### 9. Configurar a fila principal para enviar rejeições ao retry

```bash
docker compose exec rabbitmq rabbitmqctl set_policy payments-main-retry "^payments_queue$" '{"dead-letter-exchange":"payments.retry","dead-letter-routing-key":"payments.retry"}' --apply-to queues --priority 20
```

Com essa policy, o consumer pode usar:

```ts
channel.nack(message, false, false);
```

O terceiro argumento `false` evita requeue imediato. Como a fila possui DLX, RabbitMQ encaminha a mensagem para `payments.retry`.

### 10. Verificar exchanges

```bash
docker compose exec rabbitmq rabbitmqctl list_exchanges name type
```

Exchanges esperados:

```text
payments.retry   direct
payments.return  direct
payments.dlx     direct
```

### 11. Verificar bindings

```bash
docker compose exec rabbitmq rabbitmqctl list_bindings source_name destination_name destination_kind routing_key
```

Bindings relevantes esperados:

```text
payments.retry   payments_retry_5s  queue  payments.retry
payments.return  payments_queue     queue  payments.return
```

### 12. Verificar policies

```bash
docker compose exec rabbitmq rabbitmqctl list_policies
```

Policies relevantes esperadas:

```text
payments-main-retry -> payments_queue -> payments.retry
payments-retry-5s   -> payments_retry_5s -> TTL 5000 ms -> payments.return
```

### 13. Publicar mensagem de teste

```bash
curl -X POST http://localhost:3000/orders/async -H "Content-Type: application/json" -d '{"amount":888,"simulateFailure":true}'
```

### 14. Observar estado das filas durante o atraso

```bash
docker compose exec rabbitmq rabbitmqctl list_queues name messages_ready messages_unacknowledged consumers
```

Durante os 5 segundos, a expectativa era observar a mensagem em `payments_retry_5s`, enquanto o consumer ficava livre.

## Código relevante do consumer

Leitura do histórico de dead-lettering:

```ts
const headers = message.properties.headers ?? {};
const xDeath = headers['x-death'] ?? [];

console.log('X-DEATH:', JSON.stringify(xDeath));
```

Detecção de retorno da fila de retry:

```ts
const alreadyRetried = xDeath.some(
  (death: any) =>
    death.queue === 'payments_retry_5s' &&
    death.reason === 'expired',
);
```

Falha transitória simulada, sem requeue imediato:

```ts
if (body.simulateFailure && !alreadyRetried) {
  console.log(
    'SIMULATED TRANSIENT FAILURE:',
    body.orderId,
    new Date().toISOString(),
  );

  console.log('SENDING TO 5S RETRY QUEUE');

  channel.nack(message, false, false);
  return;
}
```

## Evidência observada

Primeira entrega:
- `REDELIVERED: false`
- `X-DEATH: []`
- falha transitória simulada
- envio para a fila de retry às `2026-09-15T19:17:04.337Z`

Retorno após o atraso:
- nova entrega às `2026-09-15T19:17:09.344Z`
- atraso observado de aproximadamente 5 segundos
- `REDELIVERED: false`
- `x-death` registrou:
  - `payments_queue`, reason `rejected`, count 1
  - `payments_retry_5s`, reason `expired`, count 1
- pagamento criado no PostgreSQL
- mensagem confirmada com ACK

Trecho observado:

```text
X-DEATH: [
  {"count":1,"reason":"expired","queue":"payments_retry_5s",...},
  {"count":1,"reason":"rejected","queue":"payments_queue",...}
]
RETRY ARRIVED AFTER DELAY
PROCESS PAYMENT
DB PAYMENT CREATED
MESSAGE ACKED
```

## Modelo mental

```text
payments_queue
    |
    | NACK(message, false, false)
    | x-death: rejected
    v
payments.retry
    v
payments_retry_5s
    |
    | TTL 5000 ms
    | x-death: expired
    v
payments.return
    v
payments_queue
    |
    v
consumer tenta novamente
```

## Aprendizado
- `redelivered` não é o contador apropriado para retries baseados em DLX/TTL.
- `x-death` preserva o histórico de dead-lettering e pode substituir contadores locais em memória.
- O atraso não deve ser implementado com `sleep()` dentro do consumer; a fila de retry segura a mensagem enquanto o worker fica livre.
- `nack(message, false, false)` combinado com DLX permite encaminhar a mensagem a uma estratégia de retry em vez de requeue imediato.
- Exchanges fazem roteamento; queues armazenam mensagens.
- Policy permite alterar DLX/TTL sem acoplar esses detalhes diretamente à declaração da queue no código da aplicação.

## Próximo passo
Eliminar `failureAttempts` em memória e construir backoff real baseado em `x-death`, com sequência planejada:

```text
falha -> retry 5s -> falha -> retry 30s -> falha -> DLQ
```
