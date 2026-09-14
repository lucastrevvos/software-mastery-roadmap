# Messaging checkpoint

RabbitMQ lab completed through manual acknowledgements, message redelivery, retry behavior, routing policies, and a separate failure queue. The final observed state was:

```text
payments_queue       0  0  1
payments_dead_queue  1  0  0
```

Important debugging result: the exchange and policy existed, but the explicit binding to `payments_dead_queue` was initially missing. After creating the binding with routing key `payments.dead`, the failed message reached the separate failure queue.

Useful inspection commands learned: `rabbitmqctl list_queues`, `list_exchanges`, `list_bindings`, and `list_policies`.

Architecture note: the asynchronous Orders-to-Payments flow is event/message driven, while the overall application remains hybrid because synchronous HTTP endpoints still exist. `payment_requested` behaves more like an asynchronous command than a pure domain event; `OrderCreated` would be a more canonical event for multiple independent consumers.