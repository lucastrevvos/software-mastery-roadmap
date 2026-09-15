# Distributed Systems Roadmap

Official sequence for the distributed-workshop laboratory.

1. RabbitMQ retry with delay and backoff; remove in-memory retry counters and use broker metadata.
2. Multiple Payments consumers; observe competing consumers, prefetch and cross-process idempotency.
3. Simulated external service; reproduce duplicate side effects and add an idempotency key.
4. Compare concurrency tools: UNIQUE/ON CONFLICT, atomic claim, SELECT FOR UPDATE, pg_advisory_xact_lock, and FOR UPDATE SKIP LOCKED.
5. Add Notifications and domain events such as order.created and payment.succeeded; separate queues for independent subscribers.
6. Reproduce the database-plus-broker dual-write failure.
7. Implement Transactional Outbox.
8. Run multiple Outbox workers with FOR UPDATE SKIP LOCKED.
9. Add Saga and compensation.
10. Refactor NestJS toward adapters, application use cases, domain, ports and infrastructure; apply SOLID only where it solves a real problem.
11. Add structured logs, correlation IDs, metrics, tracing, readiness, liveness and graceful shutdown.
12. Automate unit, integration, concurrency, retry, DLQ, redelivery and Outbox tests.
13. Improve Docker dev/prod builds and configuration.
14. Move the same workloads to local Kubernetes and test scaling and recovery.
15. Map the architecture to GCP: GKE, Cloud Run, Pub/Sub, Cloud Functions and Artifact Registry.
16. Add CI/CD and deployment/rollback practices.
17. Build an interview FAQ from experiments actually executed.

Method for every step: build → break → observe → explain → fix → retest → compare trade-offs → record evidence.

Key rule: a step is marked EXECUTED only after we have concrete evidence from logs, broker state, database state or automated tests.