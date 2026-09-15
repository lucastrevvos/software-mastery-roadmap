# Distributed Systems Workshop — Persistent Idempotency Checkpoint

## What was proven

The payments flow was refactored so both synchronous HTTP requests and asynchronous RabbitMQ consumption use the same `PaymentService` use case.

### HTTP path

```text
POST /payments
→ AppController
→ PaymentService.processPayment()
→ PostgreSQL
```

### RabbitMQ path

```text
payment_requested
→ RabbitMQ consumer
→ PaymentService.processPayment()
→ PostgreSQL
→ ACK
```

## Persistent idempotency

The previous in-memory `Map` was replaced by PostgreSQL-backed idempotency. The `payments` table has:

```sql
CONSTRAINT uq_payments_order_id UNIQUE (order_id)
```

The current use case first queries by `order_id` and returns the existing payment when found.

Observed log after retry/restart:

```text
HTTP PAYMENT REQUEST: 11111111-1111-1111-1111-111111111111
PROCESS PAYMENT: 11111111-1111-1111-1111-111111111111
DB IDEMPOTENT HIT: 11111111-1111-1111-1111-111111111111
```

This proves that idempotency now survives a restart of `payments-service` because state lives in PostgreSQL instead of process memory.

## Current guarantee

```text
RabbitMQ durability         ✅
manual ACK                  ✅
redelivery                  ✅
DLQ                         ✅
persistent idempotency      ✅
UNIQUE(order_id)            ✅
```

## Important caveat — race condition still exists

The current logic is still conceptually:

```text
SELECT by order_id
if not found:
    INSERT
```

Two concurrent requests can both execute the `SELECT` before either `INSERT` commits:

```text
Request A → SELECT → not found
Request B → SELECT → not found
Request A → INSERT → success
Request B → INSERT → UNIQUE violation
```

The `UNIQUE` constraint is the final database invariant and prevents duplicate persisted rows, but the application still needs to handle the concurrent insert race correctly.

Next experiment: deliberately send concurrent requests with the same `orderId`, observe the unique-constraint failure, then compare strategies such as handling SQLSTATE `23505`, `INSERT ... ON CONFLICT`, and transaction-level logical locking with `pg_advisory_xact_lock`.
