# RabbitMQ — ACK manual e mensagem unacknowledged

Checkpoint executado em 2026-09-13 no laboratório `distributed-workshop`.

## Configuração relevante

No consumidor Payments:

```ts
noAck: false,
prefetchCount: 1,
```

O handler processou a mensagem, mas o `channel.ack(message)` foi temporariamente removido.

## Resultado observado

Com uma mensagem publicada em `payments_queue`, o comando:

```bash
docker compose exec rabbitmq \
  rabbitmqctl list_queues \
  name messages_ready messages_unacknowledged consumers
```

retornou:

```text
name            messages_ready  messages_unacknowledged  consumers
payments_queue  0               1                        1
```

## Interpretação

- `messages_ready = 0`: a mensagem já foi entregue ao consumidor.
- `messages_unacknowledged = 1`: o RabbitMQ ainda não recebeu confirmação de conclusão.
- `consumers = 1`: Payments continua conectado.

Modelo mental:

```text
RabbitMQ entrega
  ↓
Payments recebe e processa
  ↓
ACK não é enviado
  ↓
RabbitMQ mantém a entrega como unacknowledged
```

Próximo experimento: restaurar o ACK, reiniciar/recriar Payments e observar a mesma mensagem ser redelivered (`redelivered: true`). Como a idempotência atual está apenas em memória, o restart também apaga o `Map`, expondo novamente o risco de efeito colateral duplicado.