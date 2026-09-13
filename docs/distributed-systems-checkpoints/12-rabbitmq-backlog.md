# RabbitMQ — backlog drenado

## Observado

Com `payments` parado, `orders` continuou publicando eventos no RabbitMQ. Ao religar `payments`, o consumidor recebeu e processou os três eventos acumulados:

```text
EVENT RECEIVED: { orderId: '530a6aa4-3ab7-43ff-98c6-fee27dd232ea', amount: 100 }
ASYNC PAYMENT APPROVED: 60a32dec-dce6-4a3a-8306-41ee473e1ff9
EVENT RECEIVED: { orderId: 'e4e2c71d-fb79-4d2c-8764-a42053969531', amount: 100 }
ASYNC PAYMENT APPROVED: 4979b142-0f3d-485c-bb99-271c69614b68
EVENT RECEIVED: { orderId: '73740285-137d-43cd-9d43-7c51d513ef87', amount: 100 }
ASYNC PAYMENT APPROVED: dc135e69-2bed-466c-badb-539afb70608b
```

## Modelo mental

```text
Orders -> RabbitMQ -> Payments
```

O broker desacopla produtor e consumidor no tempo. `Orders` não precisa que `Payments` esteja disponível naquele instante; o RabbitMQ pode reter o trabalho até existir consumidor.

## Comandos úteis

```bash
docker compose stop payments

docker compose exec rabbitmq rabbitmqctl list_queues name messages_ready messages_unacknowledged consumers

docker compose start payments

docker compose logs -f payments rabbitmq
```

## Próximo experimento

Habilitar ACK manual no consumidor (`noAck: false`), limitar `prefetchCount`, observar mensagens `unacknowledged`, testar `nack(..., requeue=true)` e redelivery. Depois, introduzir DLQ para mensagens que falham repetidamente.
