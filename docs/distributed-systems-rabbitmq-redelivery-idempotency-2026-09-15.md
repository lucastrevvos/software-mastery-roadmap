# RabbitMQ redelivery + idempotência persistente

Checkpoint prático do workshop distribuído.

## Experimento confirmado

Fluxo observado:

1. RabbitMQ entregou `payment_requested`.
2. Payments persistiu o pagamento no PostgreSQL.
3. O processo consumidor morreu antes do `ACK`.
4. RabbitMQ voltou a mensagem para `messages_ready` porque a conexão do consumer desapareceu sem confirmação.
5. Após reiniciar o Payments, a mesma mensagem foi entregue com `REDELIVERED: true`.
6. `PaymentService` detectou o pagamento já persistido via idempotência no PostgreSQL (`ON CONFLICT` / hit idempotente).
7. Nenhum pagamento duplicado foi criado.
8. O consumer enviou `ACK` e a fila voltou para `messages_ready=0`, `messages_unacknowledged=0`, `consumers=1`.

Logs-chave observados:

```text
EVENT RECEIVED: { orderId: '1a708c15-30cd-4de9-838e-aadc68ae7f1b', amount: 777, simulateCrashAfterPersist: true }
REDELIVERED: true
PROCESS PAYMENT: 1a708c15-30cd-4de9-838e-aadc68ae7f1b
CONCURRENT IDEMPOTENT HIT: 1a708c15-30cd-4de9-838e-aadc68ae7f1b
MESSAGE ACKED: 1a708c15-30cd-4de9-838e-aadc68ae7f1b
```

Fila após o processamento final:

```text
payments_queue       messages_ready=0  messages_unacknowledged=0  consumers=1
payments_dead_queue  messages_ready=0  messages_unacknowledged=0  consumers=0
```

## Modelo mental

- `delivered` não significa `processed`.
- Sem `ACK`, RabbitMQ considera o trabalho não concluído.
- Se o consumer/conexão morre, uma entrega não confirmada volta a ficar disponível.
- RabbitMQ trabalha naturalmente com semântica **at-least-once**.
- Portanto consumers importantes devem ser idempotentes.
- Duplicata já processada é sucesso lógico, então deve terminar em `ACK`, não em `NACK`.

## Descoberta adicional

O container permaneceu `Up` enquanto o consumer RabbitMQ já havia morrido, porque o ambiente dev usa `nest start --watch` e o watcher/pai podia continuar vivo. Isso mostrou que `container Up` não garante aplicação saudável, conectando diretamente com conceitos futuros de health checks, readiness e liveness em Kubernetes.

## Próxima melhoria

O retry atual com `NACK + requeue=true` é imediato. Isso pode causar hot loop e martelar uma dependência degradada. Próximo passo: retry com delay/backoff e limite de tentativas, preferencialmente usando filas de retry com TTL + DLX e contagem persistida em metadados da mensagem, seguido de DLQ quando esgotado.
