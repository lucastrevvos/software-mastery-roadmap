# KM One — Central Professional Engineering Path

Status: **canonical / main applied path**

Decision date: **2026-10-19**

## Core decision

KM One is the **main professional project** that connects the roadmap to real engineering practice.

The roadmap must no longer treat KM One as only a Node/Nest employability project. It starts there, but it evolves in controlled stages into the main environment for applying:

- JavaScript and TypeScript
- Node.js and NestJS
- C# and .NET
- PostgreSQL
- APIs and contracts
- modular architecture
- DDD and bounded contexts
- microservices when justified
- asynchronous messaging
- distributed-systems reliability
- observability
- containers and Kubernetes
- Azure
- CI/CD and platform engineering
- React/full-stack work when appropriate
- AI application engineering when appropriate
- SWEBOK senior-engineering knowledge
- iSAQB architecture knowledge

The central rule is:

> **Study provides capability; KM One provides professional evidence.**

## Architectural evolution

KM One should not begin as a distributed system merely to demonstrate microservices.

The canonical evolution is:

```text
JavaScript Certification
        ↓
TypeScript Guided Track
        ↓
Node.js / NestJS
        ↓
KM One modular monolith
        ↓
professional backend baseline
        ↓
bounded contexts become clear
        ↓
selective service extraction
        ↓
polyglot microservices
NestJS / TypeScript + .NET / C#
        ↓
messaging + distributed reliability
        ↓
observability + containers + platform
        ↓
AI-enabled services when justified
        ↓
architecture defense / professional portfolio
```

## Stage 1 — Professional NestJS foundation

Initial implementation:

- TypeScript
- Node.js
- NestJS
- PostgreSQL / Neon
- authentication and authorization
- DTOs and validation
- coherent API contracts
- migrations
- automated tests
- Docker
- logs and health checks
- CI/CD
- Azure deployment

Architecture at this stage: **modular monolith first**.

Reason: discover domain boundaries before paying the operational cost of distribution.

## Stage 2 — Domain and architecture discovery

Use the running product to identify genuine boundaries:

- modules with distinct business responsibility
- ownership of data and invariants
- different scaling characteristics
- different reliability needs
- different deployment cadence
- different security or compliance constraints
- integration boundaries

Apply:

- DDD where useful
- bounded contexts
- C4 diagrams
- ADRs
- quality attributes
- architecture scenarios
- SWEBOK concepts
- iSAQB concepts

Do not extract a service only because another language is available.

## Stage 3 — Selective polyglot microservices

When a boundary genuinely earns independent deployment, it may become a service.

KM One is intentionally allowed to become **polyglot**.

Preferred languages/stacks:

```text
NestJS / TypeScript
→ primary backend/product stack

.NET / C#
→ selected domain/service where its ecosystem or learning value is justified

Python
→ later, only where AI/data tooling creates a real advantage
```

Example shape:

```text
Frontend / Client
        ↓
API Gateway / BFF
        ↓
┌───────────────────────────────────────┐
│ KM One                                │
│                                       │
│ Workspace/Core      → NestJS          │
│ Identity/Access     → NestJS          │
│ Financial context  → .NET if justified│
│ Notifications      → NestJS           │
│ AI/Knowledge       → TS or Python     │
└───────────────────────────────────────┘
        ↓
language-independent contracts
        ↓
RabbitMQ / HTTP / other transport as justified
```

The domain boundary chooses the service. The service requirement chooses the technology.

Never create:

```text
".NET service because we want .NET"
"Python service because we want Python"
```

Instead:

```text
business/operational boundary
        ↓
independent service justified
        ↓
choose the best reasonable stack
```

## Stage 4 — Language-independent integration

A NestJS service and a .NET service must integrate through contracts that do not belong to either language.

Examples:

- versioned JSON event contracts
- OpenAPI where appropriate
- AsyncAPI/schema registry if justified later
- correlation IDs
- event IDs
- timestamps
- explicit versioning

Example event:

```json
{
  "eventId": "uuid",
  "eventType": "BillingAccountCreated",
  "occurredAt": "2026-10-19T12:00:00Z",
  "version": 1,
  "data": {
    "workspaceId": "uuid",
    "accountId": "uuid"
  }
}
```

Do not share TypeScript interfaces or C# classes across service boundaries as the distributed contract.

## Stage 5 — Distributed-systems reliability

When asynchronous integration appears, apply progressively:

- RabbitMQ semantics
- ACK / NACK
- redelivery
- prefetch
- retry
- dead-letter queues
- idempotent consumers
- Inbox
- Transactional Outbox
- eventual consistency
- Saga / Process Manager only when a workflow requires it
- compensation
- concurrency handling
- reconciliation where the domain requires it

These patterns must solve observed failure modes, not decorate the architecture.

## Stage 6 — Observability and platform

A distributed KM One should become observable end to end:

- OpenTelemetry
- structured logging
- metrics
- distributed tracing
- correlation IDs
- health/readiness checks
- performance profiling
- incident drills

Platform progression:

```text
Docker
→ Compose where useful
→ local Kubernetes/k3d
→ Azure deployment
→ Terraform where provisioning benefits
→ GitHub Actions
→ GitOps/Argo CD when the operational model justifies it
```

## Stage 7 — Full-stack evidence

React / TypeScript knowledge from Full Stack Open should be applied to real KM One user flows where practical.

KM One does not need every frontend framework in the roadmap.

The product should use one coherent frontend architecture; Angular/Next.js can remain separate specialization work unless a real product reason appears.

## Stage 8 — AI-enabled KM One

AI is added as engineering capability, not as a cosmetic chatbot.

Candidate capabilities:

- LLM APIs
- structured outputs
- tool calling
- embeddings
- retrieval / RAG
- agents/workflows where justified
- evaluations
- guardrails
- cost and latency controls
- AI observability
- secure data boundaries

TypeScript should be preferred when adequate. Python enters when its AI/data ecosystem provides concrete value.

## Relationship with Financial Lab

Financial Distributed Systems Lab remains a **focused training laboratory**.

Its role:

```text
Financial Lab
→ isolate and learn hard backend/distributed concepts
→ test them safely
→ transfer validated ideas into KM One when relevant
```

KM One is the professional product; Financial Lab is the engineering laboratory.

## Relationship with SWEBOK and iSAQB

SWEBOK and iSAQB should be applied against KM One whenever possible.

```text
SWEBOK
→ breadth of professional Software Engineering
→ KM One provides evidence

iSAQB
→ Software Architecture specialization
→ KM One provides architecture decisions and defenses
```

Examples:

- Requirements → real KM One requirements
- Design → modules and service boundaries
- Construction → code and APIs
- Testing → unit/integration/contract/E2E
- Operations → deployability and incidents
- Maintenance → change impact
- Security → threat-aware design
- Economics → build/buy and complexity trade-offs
- Architecture → drivers, quality attributes, ADRs and evolution

## Professional evidence target

KM One should eventually support claims such as:

- built and evolved a production-style NestJS backend
- designed a modular monolith before extracting services
- implemented polyglot services in NestJS/TypeScript and .NET/C#
- designed language-independent contracts
- implemented reliable asynchronous messaging
- handled idempotency and distributed failure modes
- instrumented end-to-end observability
- containerized and deployed services
- implemented CI/CD and cloud infrastructure
- integrated AI capabilities with evaluation and operational controls
- documented and defended architecture decisions

Every claim should be backed by code, tests, diagrams, ADRs, traces, deployment evidence, or demos.

## Guardrails

1. **No microservice without a boundary.**
2. **No new stack without a technical reason.**
3. **No pattern without a failure/problem it solves.**
4. **No architecture diagram without executable reality behind it.**
5. **No certificate without transferring the knowledge into KM One when relevant.**
6. **KM One remains coherent as a product; the roadmap serves the product, not the reverse.**

## Canonical sequence from current position

```text
freeCodeCamp JavaScript Certification
        ↓
TypeScript — Official Guided Track
        ↓
Node.js Core + NestJS Fundamentals
        ↓
KM One modular monolith / professional backend
        ↓
Full Stack Open / real frontend integration
        ↓
SWEBOK + architecture depth applied to KM One
        ↓
bounded-context discovery
        ↓
selective NestJS + .NET microservices
        ↓
RabbitMQ + reliability patterns
        ↓
OpenTelemetry + containers + Azure + CI/CD
        ↓
AI-enabled service(s)
        ↓
Senior Software Engineering + Software Architecture defenses
```
