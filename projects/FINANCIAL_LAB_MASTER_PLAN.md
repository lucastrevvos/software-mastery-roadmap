# Financial Lab — Master Plan

## Purpose

Financial Lab is the integrator project for Lucas Amaral's active backend window. Its goal is not to repeat many isolated business rules, but to complete one realistic end-to-end financial flow and then evolve the same system into a production-style backend and distributed microservices lab.

The project is intentionally split into three passes so it can deliver a complete engineering experience without indefinitely delaying the certification roadmap.

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
- The system should evolve from one working vertical flow rather than from many isolated exercises.

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
- basic API input validation
- basic authentication / authorization concepts at the API boundary when the API pass begins
- configuration and secrets kept outside source code

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
- [ ] basic API validation / auth boundary concepts
- [ ] secrets / configuration outside code

After this gate, the normal plan is to resume the certification roadmap unless there is a deliberate scheduling decision to continue immediately into Pass 1.5.

---

# PASS 1.5 — Production backend hardening

## Goal

Before splitting the system into microservices, make the same application look and behave more like a production backend. This pass is intentionally compact: it exists to prevent an artificial jump from a local SQLite application directly to distributed infrastructure.

## Required topics

### 1. PostgreSQL transition

Move persistence from SQLite to PostgreSQL and observe the practical differences that matter for a backend service.

Cover:

- provider configuration
- migrations
- connection configuration
- data inspection
- constraints
- indexes when justified

### 2. Modular monolith and bounded contexts

Before extracting services, identify domain/module boundaries inside the monolith.

Candidate contexts:

- Credit
- Billing / Collections
- Payments

Teach explicitly:

```text
module boundary first
        ↓
independent deployability later
```

Do not create microservices merely because the system has multiple folders.

### 3. Architecture documentation

Use lightweight documentation for important decisions:

- small C4-style views when useful
- ADRs for meaningful architectural decisions
- record the reason, alternatives and trade-offs, not just the final choice

### 4. API security and configuration

Cover the backend concerns a financial API cannot ignore, without turning the lab into a security specialization:

- authentication and authorization
- JWT / OAuth concepts at the appropriate depth
- authorization policies where justified
- input validation
- rate limiting
- secrets outside source code
- environment-specific configuration

### 5. HTTP resilience

Cover failure handling outside RabbitMQ:

- timeout
- cancellation
- `CancellationToken`
- retry only where semantically safe
- circuit breaker
- resilience pipelines

Do not add retries blindly to non-idempotent operations.

### 6. Testing strategy

Expand the testing pyramid / portfolio beyond unit tests:

```text
unit
  ↓
integration
  ↓
contract
  ↓
end-to-end
  ↓
architecture tests
```

Use Testcontainers where it provides realistic PostgreSQL / RabbitMQ integration without requiring permanently installed shared infrastructure.

Architecture tests should protect important dependency rules such as Domain not depending on Infrastructure.

### 7. Performance and profiling

Create at least one measurable performance exercise rather than discussing performance only in theory.

Observe and reason about:

- latency
- throughput
- CPU / memory where relevant
- connection pool behavior
- slow queries
- indexes
- concurrency
- before / after measurements

Use profiling / diagnostic tools only when they make a real bottleneck observable.

### 8. Financial correctness: audit, ledger and reconciliation

Add a compact but meaningful financial-correctness pass so the project is more than a generic CRUD with financial naming.

Cover at a practical level:

- audit trail
- immutable / append-oriented financial records where appropriate
- ledger concepts
- reconciliation
- detecting mismatches rather than silently overwriting them

Do not attempt to build a full banking core or full accounting engine.

## Pass 1.5 gate

- [ ] PostgreSQL
- [ ] modular monolith view
- [ ] bounded contexts identified
- [ ] ADRs for meaningful decisions
- [ ] lightweight architecture diagram / C4 view where useful
- [ ] authentication / authorization basics
- [ ] configuration / secrets discipline
- [ ] validation / rate limiting
- [ ] HTTP timeout / cancellation
- [ ] retry / circuit breaker where justified
- [ ] unit + integration + contract + E2E strategy
- [ ] architecture tests
- [ ] Testcontainers where useful
- [ ] performance / profiling exercise
- [ ] audit trail
- [ ] ledger concepts
- [ ] reconciliation exercise

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

Extract services from the modular monolith only after the boundaries are understood.

Initial candidates:

- Credit
- Billing / Collections
- Payments

Prefer database-per-service when the services are actually separated.

The learning question is not only "how to create a microservice?" but also:

> Why should this boundary be independently deployable?

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
- contract testing across .NET and NestJS

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
- [ ] language-independent event contracts
- [ ] contract testing across services
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

# MASTER GATE — Architecture Defense

The Financial Lab is not considered truly complete merely because the code runs.

At the end, Lucas must be able to defend the architecture without relying on the code being open in front of him.

Practice scenarios should include questions such as:

- What happens if RabbitMQ is unavailable after the database commits?
- What happens if the same event is delivered twice?
- What happens if a consumer dies before ACK?
- What happens if three replicas process work concurrently?
- What happens if a downstream HTTP dependency is slow?
- How do you trace one request across services?
- How do you evolve an event contract without breaking NestJS consumers?
- Why is a given boundary a microservice instead of a module?
- Where is strong consistency required and where is eventual consistency acceptable?
- What would be rolled back or compensated after a partial failure?
- How would the system be deployed and recovered?
- How would a financial mismatch be reconciled?
- What would you measure before claiming a performance improvement?

Final evidence should include architecture reasoning, trade-offs, failure handling, operations and testing strategy — not only source code.

---

# Explicitly out of scope unless a concrete need appears

These technologies / patterns must not be added just to inflate the stack:

```text
Event Sourcing  -> no, unless a real requirement justifies it
Kafka           -> no; RabbitMQ is sufficient for the planned learning goals
Redis / cache   -> only if a measured performance / read problem justifies it
GraphQL         -> no planned value for this lab
Service Mesh    -> not in the current scope
Cloud hosting   -> not required; local Kubernetes / Terraform comes first
MediatR         -> only if it solves a concrete coordination problem
AutoMapper      -> only if it removes a real mapping burden
extra business rules -> no repetition just to make the domain look larger
```

New technologies do not enter the plan automatically. A tool must close a concrete learning or engineering gap.

---

# Final learning progression

```text
PASS 1 — Software Engineering
C# / .NET 10
TDD
DDD fundamentals
Clean Architecture
EF Core
SQLite
Console
ASP.NET Core
DI
Repository
integration
local idempotency
basic API security / configuration
complete financial flow

        ↓

PASS 1.5 — Production Backend
PostgreSQL
modular monolith
bounded contexts
ADRs / architecture docs
API security
HTTP resilience
Testcontainers
contract / architecture tests
performance / profiling
audit trail
ledger concepts
reconciliation

        ↓

PASS 2 — Distributed Systems
Microservices
CQRS
RabbitMQ
.NET producer
NestJS consumer
Outbox
Inbox
at-least-once delivery
ACK / NACK
retry / DLQ
eventual consistency
Saga when justified
concurrency
cross-language contract testing
OpenTelemetry
Docker
Kubernetes / k3d
Terraform
CI / CD
GitOps / Argo CD

        ↓

MASTER GATE
Architecture Defense
```

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
