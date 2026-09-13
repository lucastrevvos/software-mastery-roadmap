# Checkpoint — Primeiro evento assíncrono com RabbitMQ

Data: 2026-09-13

## Resultado observado

O fluxo assíncrono funcionou ponta a ponta:

```text
Orders -> RabbitMQ -> Payments
```

Logs observados:

```text
rabbitmq-1 | user 'app' authenticated and granted access to vhost '/'
orders-1   | [ClientProxy] Successfully connected to RMQ broker
payments-1 | EVENT RECEIVED: { orderId: '0fc898cb-d7d1-4495-bc45-38c01a6a0763', amount: 100 }
payments-1 | ASYNC PAYMENT APPROVED: dca5f7c8-ad3d-4c59-9614-97d194f3c9b0
```

## Modelo mental

Antes, com HTTP síncrono:

```text
Orders -> Payments -> resposta -> Orders termina
```

Agora, com broker:

```text
Orders -> RabbitMQ -> Orders pode responder
                    -> Payments consome depois
```

A dependência temporal direta entre Orders e Payments foi removida. Orders ainda depende do broker para publicar a mensagem, mas não precisa que Payments esteja disponível naquele instante.

## Próximo experimento

Parar Payments, continuar publicando pedidos, observar mensagens acumuladas na fila e religar Payments para consumir o backlog.

Comandos úteis:

```bash
docker compose stop payments

docker compose start payments

docker compose logs -f orders payments rabbitmq

docker compose exec rabbitmq rabbitmqctl list_queues name messages_ready messages_unacknowledged consumers
```
