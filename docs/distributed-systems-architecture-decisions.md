# Distributed Systems — Architecture Decisions

These rules guide the roadmap and should be preserved during the laboratory.

## Idempotency and concurrency
- Keep `UNIQUE(order_id)` as the final database invariant.
- Prefer atomic database operations such as `INSERT ... ON CONFLICT` over `SELECT` followed by `INSERT` when solving simple creation races.
- A duplicate message that represents work already completed successfully is normally acknowledged, not treated as a failure.
- Database idempotency does not automatically protect an external side effect performed before persistence.

## External side effects
- Introduce a simulated external service and deliberately reproduce duplicate external execution.
- Protect the external operation with an idempotency key where supported.
- Do not keep a PostgreSQL transaction open while waiting for a slow external HTTP call.
- Prefer a short database claim/commit, then the external call, then a second short state transition.

## Lock choice
- `UNIQUE` / `ON CONFLICT`: simple invariants and idempotent creation.
- Atomic `UPDATE ... WHERE ... RETURNING`: claim an existing unit of work.
- `SELECT ... FOR UPDATE`: serialize access to an existing row inside a short transaction.
- `pg_advisory_xact_lock`: logical mutex when there is no natural row to lock or coordination is keyed by a logical identifier.
- `FOR UPDATE SKIP LOCKED`: parallel workers selecting different rows, especially Outbox processing.
- Never choose a lock merely because concurrency exists; first ask whether a constraint or atomic state transition is enough.

## Messaging reliability
- Manual ACK means processing completed from the consumer's perspective.
- Redelivery is expected under at-least-once delivery; consumers must be idempotent.
- Immediate `NACK requeue=true` is temporary laboratory behavior, not the final retry strategy.
- Final retry strategy: delayed retries/backoff, persistent attempt history, and DLQ after the retry budget is exhausted.

## Event-driven architecture
- Independent subscribers that all need an event should have independent queues.
- Prefer events that describe facts, for example `order.created` and `payment.succeeded`.
- Notifications must react to the event that proves its prerequisite, not infer payment completion from `order.created`.
- Eventual consistency is expected; correlate related events with stable identifiers.

## Database + broker consistency
- Persisting business state and publishing to a broker are two different writes.
- Reproduce the failure where database commit succeeds but event publication does not.
- Solve this with Transactional Outbox: business change and Outbox record in the same database transaction.
- Scale Outbox workers with `FOR UPDATE SKIP LOCKED` after the single-worker version is proven.

## Learning discipline
Every mechanism must be learned by: build → break → observe → explain → fix → retest → compare trade-offs.
A concept is recorded as EXECUTED only after logs, broker state, database state, or automated tests prove it.