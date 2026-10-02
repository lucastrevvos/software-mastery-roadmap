# Financial Lab — Master Plan

## Purpose

Financial Lab is the integrator project for Lucas Amaral's active backend window. Its goal is not to repeat many isolated business rules, but to complete one realistic end-to-end financial flow and then evolve the same system into a distributed microservices lab.

The project is intentionally split into two passes so it can deliver a complete engineering experience without indefinitely delaying the certification roadmap.

---

## Teaching / execution rule

Use AMS, but optimize for a complete vertical flow.

- New concept: explain deeply and explicitly label C#, .NET, xUnit, EF Core, etc.
- Already-understood concept: use it directly without re-teaching it every time.
- Keep TDD, but do not multiply equivalent test cases just to practice syntax.
- Prefer one meaningful business rule that introduces each architectural concept.
- Code is primary. Diagrams are used only when they materially clarify a decision.
- Patterns and tools must emerge from concrete problems; do not add abstractions ceremonially.
- Work in small steps in Visual Studio and wait for `go` before advancing.

Canonical development rhythm when useful:

```text
architectural decision
        ↓
small diagram when useful
        ↓
failing test
        ↓
minimal implementation
        ↓
green test
        ↓
refactor
```

---

# PASS 1 — Complete .NET financial flow

## Goal

Build one working local financial flow that crosses all main layers before returning to certifications.

Target flow:

```text
User
  ↓
Console / later ASP.NET Core API
  ↓
Application use cases
  ↓
Domain
  ↓
Infrastructure
  ↓
EF Core + SQLite
```

Business flow:

```text
Request credit
    ↓
Analyze credit
    ↓
Approve / reject
    ↓
Create invoice for approved credit
    ↓
Register payment
    ↓
Prevent duplicate payment
    ↓
Persist everything
```

## Scope

### Architecture

```text
FinancialLab
├── FinancialLab.Domain
├── FinancialLab.Application
├── FinancialLab.Infrastructure
├── FinancialLab.Console
└── FinancialLab.Tests
```

Later in Pass 1, add ASP.NET Core Web API as a second presentation adapter without rewriting the core layers.

### Concepts / technologies to cover

- C# / .NET 10
- xUnit and TDD
- DDD fundamentals through the actual domain
- invariants
- entities and value objects only when justified
- Clean Architecture
- dependency inversion
- constructor dependency injection
- composition root / DI container
- use cases
- repository boundary
- EF Core
- SQLite
- migrations
- integration tests
- end-to-end local execution
- ASP.NET Core Web API as a short second presentation pass
- local idempotency through duplicate payment protection

### Business rule budget

Do not build dozens of credit rules. Use the smallest set that makes the architecture real.

Initial credit rule:

```text
score >= 700 -> APPROVED
score < 700  -> REJECTED
```

Main Pass 1 business behaviors:

1. A credit request must have a positive amount.
2. Credit analysis returns an explicit decision.
3. Only approved credit can produce an invoice.
4. A payment can be registered for an invoice.
5. The same external payment / transaction must not be processed twice.

## Pass 1 gate

Pass 1 is complete when the project demonstrates:

- [ ] Domain
- [ ] Application
- [ ] Infrastructure
- [ ] Console flow
- [ ] Tests
- [ ] TDD
- [ ] DDD fundamentals
- [ ] Clean Architecture
- [ ] dependency inversion
- [ ] dependency injection
- [ ] EF Core
- [ ] SQLite
- [ ] repository implementation
- [ ] migrations
- [ ] credit flow
- [ ] invoice / billing flow
- [ ] payment flow
- [ ] duplicate payment protection
- [ ] integration test
- [ ] complete local execution
- [ ] short ASP.NET Core Web API adapter pass

After this gate, resume the certification roadmap before deepening the distributed architecture unless there is a deliberate scheduling decision to continue immediately.

---

# PASS 2 — Distributed Financial Lab

## Goal

Evolve the same Financial Lab into a realistic distributed system using microservices, event-driven architecture, polyglot consumers, local Kubernetes, observability and infrastructure-as-code.

This pass is a major learning target, not optional decoration.

## Target services

Initial target topology:

```text
                    ┌────────────────┐
Client ────────────▶│   Credit.Api   │  .NET
                    └────────┬───────┘
                             │
                        PostgreSQL
                             │
                    Transactional Outbox
                             │
                             ▼
                         RabbitMQ
                    CreditApproved
                       /          \
                      /            \
                     ▼              ▼
          ┌────────────────┐   ┌──────────────────┐
          │  Billing.Api   │   │ Payments.Worker  │
          │     .NET       │   │     NestJS       │
          └───────┬────────┘   └────────┬─────────┘
                  │                     │
             PostgreSQL            PostgreSQL
```

Exact service boundaries may evolve as the domain becomes clearer, but the architecture must include at least one .NET producer and one NestJS event consumer.

## Required learning progression

### 1. Microservice extraction

Evolve the modular / monolithic Pass 1 system into independently deployable services, initially around:

- Credit
- Billing / Collections
- Payments

Prefer database-per-service when the services are actually separated.

### 2. CQRS

Introduce CQRS only after commands and queries create a real need for separation.

Candidate commands:

```text
RequestCredit
ApproveCredit / RejectCredit
CreateInvoice
RegisterPayment
```

Candidate queries:

```text
GetCreditRequest
GetInvoice
GetPaymentStatus
```

Important distinctions to teach explicitly:

```text
CQRS != MediatR
CQRS != microservices
CQRS != event sourcing
```

MediatR may be evaluated later if it solves a concrete coordination problem; it is not a prerequisite.

### 3. RabbitMQ and explicit messaging semantics

Use RabbitMQ directly enough to understand:

- exchanges / queues / routing
- producers and consumers
- manual ACK / NACK
- redelivery
- prefetch
- retry strategy
- dead-letter queues

Observe queue state and failures rather than treating messaging as a black box.

### 4. Cross-language contracts

At least one event must be produced by .NET and consumed by NestJS.

Example transport contract shape:

```json
{
  "eventId": "...",
  "eventType": "CreditApproved",
  "occurredAt": "...",
  "creditId": "...",
  "customerId": "...",
  "amount": 10000
}
```

Teach:

- event ownership
- language-independent contracts
- serialization
- versioning
- backward compatibility
- schema evolution

Do not share a `.NET Domain.dll` as an integration contract.

### 5. Transactional Outbox

Create the failure intentionally:

```text
database commit succeeds
        ↓
message publish fails
```

Then implement a transactional outbox so domain state and the pending integration event are committed atomically to the service database.

Use an outbox processor / publisher to deliver pending events to RabbitMQ.

### 6. Inbox / idempotent consumer

Assume at-least-once delivery.

Use event/message IDs to ensure a consumer can safely receive the same message multiple times without duplicating financial effects.

Teach the pairing explicitly:

```text
Outbox -> improve reliable publication
Inbox  -> prevent duplicate processing
```

### 7. Retry / DLQ / failure handling

Deliberately break a consumer and observe:

```text
failure
  ↓
NACK / retry
  ↓
redelivery
  ↓
retry exhaustion
  ↓
DLQ
```

### 8. Eventual consistency and process coordination

Use the actual credit -> billing -> payment flow to explain eventual consistency.

Introduce Saga / Process Manager / compensation only when a multi-step workflow creates the need.

### 9. Concurrency

Create real concurrent processing scenarios and address them with the appropriate mechanism, potentially including:

- optimistic concurrency
- unique constraints
- row locking where justified
- idempotency keys
- multiple consumer instances

### 10. Observability

Once multiple processes exist, introduce:

- structured logs
- CorrelationId
- TraceId
- distributed tracing
- metrics
- OpenTelemetry

The goal is to follow one financial operation across multiple services and RabbitMQ.

### 11. Containers and local Kubernetes

Progression:

```text
Docker
  ↓
Docker Compose
  ↓
k3d local Kubernetes
```

Target local Kubernetes namespace may include:

```text
financial-lab
├── credit-api
├── billing-api
├── payments-worker
├── rabbitmq
├── postgres-credit
├── postgres-billing
└── postgres-payments
```

Teach and use:

- Deployment
- Service
- ConfigMap
- Secret
- probes / health checks
- replicas
- scaling

Deliberately scale consumers / APIs to multiple replicas and verify correctness under concurrency.

### 12. Terraform locally

Terraform is desired in Pass 2 if it provides real value locally.

Preferred use:

- provision / configure Kubernetes infrastructure resources
- Kubernetes provider
- Helm provider / Helm releases where appropriate
- shared infrastructure configuration

Do not use Terraform merely to deploy application manifests if Helm / Kubernetes manifests are the clearer tool.

Teach the distinction:

```text
Terraform -> infrastructure provisioning
Kubernetes manifests / Helm -> application deployment definitions
GitOps / Argo CD -> continuous reconciliation
```

### 13. CI/CD and GitOps

Desired final evolution:

```text
GitHub Actions
   ↓
build + test + container image
   ↓
container registry
   ↓
Argo CD / GitOps
   ↓
Kubernetes
```

Introduce Argo CD only after the Kubernetes deployment model is understood manually.

## Pass 2 master gate

- [ ] ASP.NET Core microservices
- [ ] PostgreSQL per separated service where justified
- [ ] CQRS based on actual command/query divergence
- [ ] RabbitMQ
- [ ] .NET producer
- [ ] NestJS consumer
- [ ] explicit ACK / NACK
- [ ] prefetch / redelivery
- [ ] retry strategy
- [ ] DLQ
- [ ] Transactional Outbox
- [ ] Inbox / idempotent consumer
- [ ] eventual consistency
- [ ] Saga / Process Manager if justified
- [ ] concurrency controls
- [ ] structured logging
- [ ] OpenTelemetry / tracing / metrics
- [ ] Docker
- [ ] Docker Compose
- [ ] local Kubernetes with k3d
- [ ] replicas / scaling experiments
- [ ] Terraform locally where useful
- [ ] CI with GitHub Actions
- [ ] CD / GitOps / Argo CD after manual Kubernetes mastery

---

# Current state — 2026-10-01

Current solution work completed / in progress:

```text
FinancialLab
├── FinancialLab.Domain       ✅
├── FinancialLab.Application  ✅ created
└── FinancialLab.Tests        ✅
```

Existing domain work:

- `CreditRequest`
- invariant: `Amount > 0`
- `CreditDecision`
- `CreditAnalyzer`
- rule: `score >= 700` approves; below 700 rejects

Existing TDD work:

- invalid amount tests
- valid request test
- approval boundary test
- rejection boundary test

Existing application work:

- `RequestCreditUseCase` initial implementation
- `ICreditScoreProvider` created

Immediate next step:

```text
Make RequestCreditUseCase receive ICreditScoreProvider through constructor injection,
using the already-prepared test fake to drive the change.
```

Do not restart planning from zero in a future session. Continue from this exact step unless Lucas explicitly changes direction.
