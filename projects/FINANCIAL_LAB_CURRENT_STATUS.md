# Financial Lab — Current Status

_Last updated: 2026-10-01_

This file is the execution checkpoint for the Financial Lab. The canonical scope and gates remain in `projects/FINANCIAL_LAB_MASTER_PLAN.md`.

## Current learning strategy

The priority is to experience one complete vertical financial flow without over-practicing equivalent business rules or test syntax.

- New concept -> explain deeply.
- Already-understood concept -> use directly.
- Keep TDD, DDD and Clean Architecture active, but avoid repetitive drills.
- Work in small Visual Studio steps and wait for `go` before advancing.
- Finish a complete local flow, then return to the certification roadmap unless there is an explicit decision to continue immediately.

## PASS 1 — current checkpoint

Solution currently contains:

```text
FinancialLab
├── FinancialLab.Domain
├── FinancialLab.Application
└── FinancialLab.Tests
```

Completed / created so far:

- `FinancialLab.Domain`
- `FinancialLab.Tests`
- `FinancialLab.Application`
- `Tests -> Domain`
- `Tests -> Application`
- `Application -> Domain`
- `CreditRequest`
- invariant: credit amount must be greater than zero
- `CreditDecision`
- `CreditAnalyzer`
- rule: `score >= 700 -> Approved`, otherwise `Rejected`
- xUnit tests for valid/invalid request and score boundary
- initial `RequestCreditUseCase`
- `ICreditScoreProvider`

### Exact next step

Refactor `RequestCreditUseCase` to receive `ICreditScoreProvider` through constructor injection and change the use case from:

```text
Execute(amount, score)
```

to:

```text
Execute(amount)
        ↓
ICreditScoreProvider.GetScore()
        ↓
CreditAnalyzer
        ↓
CreditDecision
```

The test should use a small fake implementation of `ICreditScoreProvider`; do not introduce Moq/NSubstitute yet.

## PASS 1 target before returning to certifications

Complete one executable flow:

```text
Request credit
    ↓
Analyze credit
    ↓
Approve / reject
    ↓
Persist with EF Core + SQLite
    ↓
Create invoice for approved credit
    ↓
Register payment
    ↓
Prevent duplicate payment
    ↓
Run full local flow
```

Required engineering path includes Domain, Application, Infrastructure, Console, repositories, dependency inversion, DI/composition root, EF Core, SQLite, migrations, integration testing and a short ASP.NET Core API adapter pass.

## PASS 2 — confirmed distributed target

The second major pass is a primary learning objective, not optional stack decoration. It should evolve the same Financial Lab into microservices and distributed systems.

Required target characteristics:

- ASP.NET Core microservices
- .NET producer(s)
- at least one real NestJS consumer
- PostgreSQL per separated service where justified
- CQRS introduced from real command/query divergence
- RabbitMQ with explicit exchanges/queues/routing semantics
- manual ACK/NACK, prefetch and redelivery observation
- retry strategy and DLQ
- Transactional Outbox
- Inbox / idempotent consumer
- eventual consistency
- Saga / Process Manager only when the workflow justifies it
- concurrency experiments with multiple instances/replicas
- language-independent event contracts between .NET and NestJS
- contract versioning / compatibility and contract tests
- OpenTelemetry, structured logs, correlation/tracing and metrics
- Docker -> Docker Compose -> local Kubernetes with k3d
- Kubernetes Deployments, Services, ConfigMaps, Secrets, probes and scaling
- Terraform locally when it adds real value, preferably for infrastructure/Kubernetes/Helm resources
- CI with GitHub Actions
- later CD/GitOps with Argo CD after manual Kubernetes understanding

Conceptual target:

```text
Client
  ↓
Credit.Api (.NET)
  ↓
PostgreSQL + Transactional Outbox
  ↓
RabbitMQ
  ├──> Billing.Api (.NET)
  └──> Payments.Worker (NestJS)
```

Important distinctions to preserve while teaching:

```text
CQRS != MediatR
CQRS != microservices
CQRS != event sourcing

Outbox -> reliable publication
Inbox  -> duplicate-safe consumption

Terraform -> infrastructure provisioning
Kubernetes manifests / Helm -> application deployment definitions
GitOps / Argo CD -> continuous reconciliation
```

Do not introduce patterns or tools merely to inflate the stack. Each one must solve a concrete problem that has appeared in the evolving system.
