# Coding Principles

## Decision supported

Choose implementation practices that preserve observable behavior, make business decisions visible, and reduce the risk of future change.

## When to use this

Use this while implementing or reviewing a code change whose behavior, failure handling, or future maintenance cost matters. It is especially useful when a change is correct in the happy path but hard to understand, diagnose, or safely extend.

## Decision to make

Decide whether the code makes the important behavior and failure modes explicit enough for the next developer to change safely.

## Principles

### Make correctness visible

Express invariants near the state they protect. Reject invalid transitions explicitly instead of relying on calling order, comments, or duplicated checks.

### Optimize for the next reader

Use names that describe responsibility and outcomes. Prefer direct control flow until abstraction removes proven duplication or protects a real variation point.

### Keep side effects at boundaries

Separate decisions from I/O where doing so makes behavior testable and failure handling explicit. Do not add layers merely to imitate an architecture diagram.

### Preserve operational truth

Implementation is incomplete when failures cannot be diagnosed, timeouts are unbounded, cancellation is ignored, or important state changes are invisible.

## How to apply

1. Put business rules and state transitions where the owning state or boundary can enforce them.
2. Use names and control flow that reveal responsibility before adding abstraction.
3. Keep I/O, external calls, and side effects at boundaries when that makes behavior easier to test.
4. Make important failure behavior observable through errors, logs, metrics, or state transitions.
5. Add abstraction only when it protects a current variation, dependency, or invariant.

## Example

Weak code hides a pricing rule inside a generic helper named `processData`, logs only "failed", and relies on callers to check state first. Better code names the pricing decision, validates the state transition at the owning boundary, and reports the failure reason without leaking sensitive data.

## Trade-offs

Explicit validation and boundaries add code, but reduce hidden coupling. Excessive indirection produces the opposite result: more navigation with no protected decision.

## Failure modes

- Applying “clean code” rules without considering runtime or domain behavior.
- Hiding meaningful decisions inside generic helpers.
- Using comments to compensate for misleading structure.
- Optimizing hot paths without measurements or regression evidence.

## Evidence to keep

- [ ] Business rules and state transitions have one clear location.
- [ ] Abstractions protect an identified variation, dependency, or invariant.
- [ ] Side effects, failure behavior, and operational signals are visible.
- [ ] Complexity is justified by current requirements.
