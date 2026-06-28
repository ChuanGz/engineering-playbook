# Implementation

## Purpose

Build maintainable production software.

## Core guidance

Keep code cohesive, interfaces purposeful, errors explicit, dependencies controlled, and refactoring tied to value.

Implementation guidance applies after outcomes and boundaries are understood. It focuses on preserving correctness and changeability in production code, not enforcing one language, framework, or visual coding style.

## Guides

- [Coding principles](coding-principles.md) — turn engineering intent into reviewable code decisions.
- [Code organization](code-organization.md) — organize code around ownership and change behavior.
- [API design](api-design.md) — implement stable contracts with explicit semantics.
- [Error handling](error-handling.md) — preserve failure meaning and recovery responsibility.
- [Maintainability](maintainability.md) — assess whether future changes remain safe and understandable.
- [Refactoring](refactoring.md) — improve structure through bounded, evidence-driven change.
- [Technical debt](technical-debt.md) — manage known engineering liabilities as explicit risk decisions.

## Review questions

- Are business invariants and state transitions enforced at their owning boundary?
- Does each abstraction protect a current variation, dependency, or failure risk?
- Are error, cancellation, concurrency, observability, and recovery behaviors explicit where relevant?
- Can behavior evidence survive safe internal refactoring?
