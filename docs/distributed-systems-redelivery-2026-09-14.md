# RabbitMQ: ACK manual, unacknowledged e redelivery

## Experimento executado

Configuramos o consumer do Payments com:

- `noAck: false`
- `prefetchCount: 1`
- ACK manual via `channel.ack(message)`

Depois removemos temporariamente o ACK.

Com uma mensagem entregue ao Payments, o RabbitMQ mostrou:

```text
payments_queue  0  1  1
```

Interpretação:

- `messages_ready = 0`: a mensagem já saiu da fila pronta para entrega;
- `messages_unacknowledged = 1`: foi entregue ao consumer, mas ainda não foi confirmada;
- `consumers = 1`: havia um consumer conectado.

Em seguida restauramos `channel.ack(message)` e recriamos o container Payments. Como a conexão antiga morreu sem ACK, o RabbitMQ reentregou a mesma mensagem.

Logs observados:

```text
EVENT RECEIVED: { orderId: '67eef5ca-108d-4946-9ce9-0bbf520ee6fc', amount: 100 }
REDELIVERED: true
ASYNC PAYMENT APPROVED: e40a7590-3836-4467-b38a-58dccf8a5228
MESSAGE ACKED: 67eef5ca-108d-4946-9ce9-0bbf520ee6fc
```

Depois do ACK:

```text
payments_queue  0  0  1
```

## Modelo mental

```text
entrega da mensagem
↓
consumer processa
↓
ACK
↓
broker pode considerar concluída
```

Se o consumer morrer antes do ACK:

```text
mensagem entregue
↓
sem ACK
↓
conexão fecha / processo morre
↓
RabbitMQ requeue/redelivery
↓
mesma mensagem pode chegar novamente
```

## Descoberta principal

Entrega não significa processamento concluído.

Com ACK manual, o consumer escolhe quando assumir que terminou. Se o consumer morrer antes de confirmar, RabbitMQ pode entregar novamente.

Isso caracteriza o comportamento típico de **at-least-once delivery**: o sistema prefere possível duplicidade a possível perda.

Consequência: consumers com efeitos colaterais devem ser idempotentes.

## Próximo problema

Uma mensagem que falha sempre pode entrar em loop de requeue/redelivery. Próximo experimento: `nack`, poison message e DLQ.
