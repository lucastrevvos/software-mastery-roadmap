# KM One — Node/Nest Backend Employability Gate

Status: **Decision accepted on 2026-09-21**

## Decision

Reconsider the KM One backend from **.NET** to **Node.js + TypeScript + NestJS**, while keeping **Azure** as the cloud platform.

KM One becomes the real-world project for **Node/Nest Backend Employability Project + Gate** in the roadmap.

This is not a rejection of .NET. The .NET ecosystem is deliberately postponed to the second major backend window, where the same architectural concepts will be reapplied in C# / ASP.NET Core / Azure.

## Why KM One

Using KM One avoids creating an artificial portfolio project only to satisfy the roadmap. It provides a real product in which backend decisions, persistence, authentication, testing, deployment, observability and future asynchronous processing can be demonstrated.

The employability goal is to reach a point where the project can support applications for:

- Node.js Backend
- TypeScript Backend
- NestJS Backend

without waiting for the later advanced architecture/cloud phases.

## Initial target stack

- **Runtime:** Node.js
- **Language:** TypeScript
- **Framework:** NestJS
- **Database:** PostgreSQL / Neon
- **Cloud:** Azure
- **Deployment candidates:** Azure Container Apps or Azure App Service
- **Secrets/configuration:** Azure Key Vault when required
- **Observability:** Application Insights
- **Storage:** Azure Storage when required
- **Delivery:** CI/CD

Azure remains an infrastructure decision; moving the application from .NET to NestJS does not require moving away from Azure.

## Delivery order

The first version should remain intentionally straightforward:

1. NestJS modules, controllers, services/providers and dependency injection
2. DTOs, validation and clear error contracts
3. PostgreSQL / Neon and migrations
4. Authentication and authorization
5. Automated tests
6. Docker
7. Logging and health checks
8. CI/CD
9. Azure deployment

Only after a real product need appears:

10. Cache / Redis
11. Background jobs or asynchronous processing
12. Messaging
13. Outbox / integration events
14. Distributed observability
15. DDD, CQRS or other advanced architecture patterns

The rule is: **do not front-load complexity to prove architecture knowledge**. Advanced patterns must solve an actual problem.

## Employability Gate

The Gate is passed when KM One has a backend that can be defended technically and demonstrated as a professional system, including:

- coherent API design
- persistence and migrations
- authentication / authorization
- validation and error handling
- automated tests
- containerization
- operational logging / health
- CI/CD
- deployed environment
- clear README and architecture notes

At that point, Node.js / TypeScript / NestJS job applications should begin even if advanced distributed systems, AWS/cloud architecture and AI phases are still pending.

## Relationship with Trevvos and .NET

Current architectural intent:

```text
KM One
→ Node.js + TypeScript + NestJS
→ PostgreSQL / Neon
→ Azure
→ primary Node/Nest employability project

Trevvos Platform Core
→ remains the candidate .NET system
→ future C# / ASP.NET Core / Azure window
```

This creates a useful future comparison: the same engineering ideas — dependency injection, middleware, persistence, background work, messaging, observability and architecture — can later be implemented in both NestJS and .NET.

## Long-term learning value

KM One is therefore both:

1. a real product; and
2. the practical proof that the Node/Nest learning window reached professional depth.

The later .NET window should not repeat architecture from zero. It should translate already-understood concepts into the .NET ecosystem.
