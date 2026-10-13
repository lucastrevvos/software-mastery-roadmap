# TypeScript — Official Guided Track

Status: **planned**

## Trigger

Start **immediately after completion of the freeCodeCamp JavaScript Certification** and before the Node.js / NestJS employability window.

This is intentionally not another external course. The teaching will be led by ChatGPT using the roadmap's AMS method, with the official TypeScript documentation as the canonical technical source.

## Canonical sources

1. TypeScript for JavaScript Programmers  
   https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

2. TypeScript for Java/C# Programmers  
   https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-oop.html

3. TypeScript Handbook  
   https://www.typescriptlang.org/docs/handbook/intro.html

Additional official TypeScript documentation may be used when the topic requires it.

## Position in the roadmap

```text
freeCodeCamp JavaScript Certification
        ↓
TypeScript — Official Guided Track
        ↓
Node.js / NestJS
        ↓
Full Stack Open
        ↓
Full Stack Open Part 9 — TypeScript reinforcement
```

The Full Stack Open TypeScript material remains valuable, but it becomes **applied reinforcement**, not the first contact with TypeScript.

## Teaching contract

Use AMS and the official terminology, but teach actively instead of asking Lucas to read documentation alone.

For each new concept:

```text
official concept
    ↓
mental model
    ↓
small example
    ↓
predict / trace
    ↓
build
    ↓
compiler feedback
    ↓
debug / repair
    ↓
transfer
```

Do not turn the track into passive documentation reading.

Already-mastered JavaScript concepts should not be re-taught unless TypeScript changes their behavior or mental model.

Because Lucas also works with C#, explicitly compare TypeScript with both **JavaScript** and **C#** when that contrast clarifies the concept.

## Planned curriculum

1. What TypeScript adds to JavaScript; static checking versus runtime behavior
2. Type inference and explicit annotations
3. Object types, interfaces and type aliases
4. Union types and narrowing
5. Function typing
6. Literal types, optional properties and readonly
7. Generics
8. `keyof`, `typeof`, indexed access and useful utility types
9. Structural typing and the Java/C# contrast
10. Classes only where TypeScript semantics differ from ordinary JavaScript
11. Modules and package boundaries
12. `tsconfig.json`, `strict` and important compiler options
13. `any`, `unknown`, `never`, nullability and safe boundary typing
14. Async code and typed errors/results
15. JavaScript → TypeScript migration exercise
16. Bridge to NestJS: decorators/metadata and typed DTO-oriented backend code when the framework window begins

The order may adapt to observed gaps, but official TypeScript concepts remain the source of truth.

## Credential policy

There is **no external TypeScript certificate required** for this step.

Completion evidence will be a Programming Mastery Lab gate, not a decorative certificate.

## Mastery Gate

The track is complete only when Lucas can, without a tutorial:

- explain what TypeScript can and cannot guarantee at runtime;
- distinguish inference from annotation;
- model data with object types, interfaces, aliases and unions;
- narrow a union safely;
- explain and use `any`, `unknown` and `never`;
- write and explain a generic abstraction;
- explain structural typing and contrast it with nominal expectations from C#/Java;
- use `strict` deliberately;
- migrate a small JavaScript module to TypeScript and repair compiler errors;
- model a small backend-oriented flow in TypeScript;
- defend when a type abstraction improves safety and when it only adds noise.

After this gate, begin the Node.js / NestJS window.
