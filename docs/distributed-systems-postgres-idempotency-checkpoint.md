# Distributed Systems Workshop — PostgreSQL Idempotency Checkpoint

## Goal
Move payment idempotency from in-memory state to PostgreSQL and share the same payment use case between synchronous HTTP and asynchronous RabbitMQ flows.

## Architecture after refactor

```text
HTTP POST /payments
        \
         -> PaymentService -> PostgreSQL
        /
RabbitMQ payment_requested
```

The transport changes, but the payment rule does not.

## Persistent storage
The `payments` table is persisted in PostgreSQL and has a unique business key:

```sql
CREATE TABLE IF NOT EXISTS payments (
    id UUID PRIMARY KEY,
    order_id UUID NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_payments_order_id UNIQUE (order_id)
);
```

The key invariant is `UNIQUE (order_id)`.

## Docker / networking
The Payments container received:

```text
DATABASE_URL=postgresql://app:app@postgres:5432/payments
```

Inside Docker Compose, `postgres` is the DNS name of the PostgreSQL service. Containers use the container port `5432`, independently of the host-mapped port.

## Refactor
A `PaymentService` now contains the payment/idempotency logic. Both the HTTP controller and RabbitMQ consumer call the same service.

This removed the duplicated `SELECT -> INSERT` payment logic from the transport layer.

## Successful synchronous test
Request:

```bash
curl -v -X POST http://localhost:3001/payments \
  -H "Content-Type: application/json" \
  -d '{
    "orderId":"11111111-1111-1111-1111-111111111111",
    "amount":100
  }'
```

Observed HTTP result:

```text
HTTP/1.1 201 Created
```

Observed body:

```json
{"id":"140d5f09-9507-47e7-9925-c8856f464342","order_id":"11111111-1111-1111-1111-111111111111","amount":100,"status":"APPROVED"}
```

Observed application logs:

```text
HTTP PAYMENT REQUEST: 11111111-1111-1111-1111-111111111111
PROCESS PAYMENT: 11111111-1111-1111-1111-111111111111
DB PAYMENT CREATED: 140d5f09-9507-47e7-9925-c8856f464342 11111111-1111-1111-1111-111111111111
```

## Debug endpoint confirmed persistence

```bash
curl -v http://localhost:3001/payments/debug
```

Observed persisted row:

```json
[{"id":"140d5f09-9507-47e7-9925-c8856f464342","order_id":"11111111-1111-1111-1111-111111111111","amount":"100.00","status":"APPROVED","created_at":"2026-09-15T03:19:23.303Z"}]
```

`NUMERIC` is returned by `pg` as a string by default to avoid accidental precision loss.

## Current status

```text
RabbitMQ durable          ✅
Manual ACK                ✅
Redelivery                ✅
DLQ                       ✅
PostgreSQL persistence    ✅
Shared PaymentService     ✅
Persistent idempotency    partially proven
Concurrent race handling  not yet proven
```

Next experiments:
1. Repeat the same HTTP request and verify `DB IDEMPOTENT HIT`.
2. Restart Payments and repeat the same order to prove idempotency survives process restart.
3. Force two concurrent requests through the `SELECT -> INSERT` window and observe the race.
4. Use the database `UNIQUE` constraint as the final invariant and then explore conflict handling / locking (`pg_advisory_xact_lock`).
