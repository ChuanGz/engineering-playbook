# Coding Principles

## Decision supported

Choose implementation practices that preserve observable behavior, make business decisions visible, and reduce the risk of future change.

## Principles

### Make correctness visible

Express invariants near the state they protect. Reject invalid transitions explicitly instead of relying on calling order, comments, or duplicated checks.

### Optimize for the next reader

Use names that describe responsibility and outcomes. Prefer direct control flow until abstraction removes proven duplication or protects a real variation point.

### Keep side effects at boundaries

Separate decisions from I/O where doing so makes behavior testable and failure handling explicit. Do not add layers merely to imitate an architecture diagram.

### Preserve operational truth

Implementation is incomplete when failures cannot be diagnosed, timeouts are unbounded, cancellation is ignored, or important state changes are invisible.

## Trade-offs

Explicit validation and boundaries add code, but reduce hidden coupling. Excessive indirection produces the opposite result: more navigation with no protected decision.

## Failure modes

- Applying “clean code” rules without considering runtime or domain behavior.
- Hiding meaningful decisions inside generic helpers.
- Using comments to compensate for misleading structure.
- Optimizing hot paths without measurements or regression evidence.

## Review evidence

- [ ] Business rules and state transitions have one clear location.
- [ ] Abstractions protect an identified variation, dependency, or invariant.
- [ ] Side effects, failure behavior, and operational signals are visible.
- [ ] Complexity is justified by current requirements.
