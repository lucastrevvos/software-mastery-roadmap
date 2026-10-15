# Senior Software Engineer — SWEBOK v4 Guided Track

Status: **planned / core**

## Why this track exists

The roadmap previously had strong stack, backend, cloud and architecture paths, but it did not explicitly use a profession-wide body of knowledge to define what a well-rounded Senior Software Engineer should know independent of language or framework.

This track corrects that gap.

Canonical reference: **SWEBOK Guide v4.0a — IEEE Computer Society**.

Official source:
https://www.computer.org/education/bodies-of-knowledge/software-engineering

## Role in the roadmap

This is not intended to become a long detour before employability.

It is the vendor-neutral spine for the Senior Software Engineer objective.

```text
JavaScript / TypeScript / Node / .NET practice
                ↓
real backend projects
                ↓
SWEBOK Guided Track
                ↓
Senior Software Engineering Mastery Gate
                ↓
optional IEEE Software Professional Level 2
                ↓
architecture specialization continues with iSAQB
```

SWEBOK and iSAQB serve different purposes:

```text
SWEBOK / IEEE
→ breadth of Software Engineering as a profession

iSAQB
→ specialization in Software Architecture
```

## Canonical Knowledge Areas

Use the current SWEBOK v4.0a organization as the source of truth, including:

1. Software Requirements
2. Software Architecture
3. Software Design
4. Software Construction
5. Software Testing
6. Software Engineering Operations
7. Software Maintenance
8. Software Configuration Management
9. Software Engineering Management
10. Software Engineering Process
11. Software Engineering Models and Methods
12. Software Quality
13. Software Security
14. Software Engineering Professional Practice
15. Software Engineering Economics
16. Computing Foundations
17. Mathematical Foundations
18. Engineering Foundations

## Teaching model

Do **not** read the guide linearly and call that mastery.

For each Knowledge Area:

```text
official concept
    ↓
what a senior engineer must be able to decide/explain
    ↓
connect to existing experience/project
    ↓
small diagnostic
    ↓
repair knowledge gaps
    ↓
applied scenario / code / design / review
    ↓
defense
    ↓
retest
```

Use AMS and reuse the user's real projects whenever possible.

Examples:

- Requirements → convert vague product requests into testable requirements and constraints.
- Architecture → Financial Lab and system-design defenses.
- Design / Construction → code structure, APIs, refactoring, error handling.
- Testing → unit, integration, contract, E2E and architecture tests.
- Operations → observability, deployment, incident reasoning.
- Maintenance → change impact and technical debt.
- Configuration Management → Git, CI/CD, release/version discipline.
- Management / Process → estimation, risk, metrics, delivery trade-offs.
- Quality → quality attributes and measurable acceptance.
- Security → threat-aware engineering and secure defaults.
- Economics → cost/benefit and build-vs-buy reasoning.
- Professional Practice → communication, ethics, uncertainty and stakeholder decisions.

## Relationship with certifications

The track itself is free-first and does not require buying an exam.

After the internal Mastery Gate, evaluate the **IEEE Certified Software Professional — Level 2** only if:

- the current exam remains available;
- the user is prepared to pass;
- the price/ROI is acceptable;
- it adds useful external validation.

Do not pursue the credential merely to collect another badge.

## Senior Software Engineering Mastery Gate

A pass requires the ability to handle a cross-functional engineering scenario without hiding behind one stack.

The user should be able to:

- clarify ambiguous requirements;
- identify functional and nonfunctional requirements;
- choose and defend a design;
- reason about quality attributes and trade-offs;
- define a testing strategy;
- review implementation quality;
- reason about deployability and operations;
- manage change and compatibility;
- identify security and reliability risks;
- reason about cost, complexity and delivery;
- communicate decisions through code, diagrams, ADRs or review comments;
- handle a changed constraint and adapt the solution.

The final gate should include both implementation-level and architecture/system-level decisions.
