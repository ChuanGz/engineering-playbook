# Code Organization

## Decision supported

Place code so a change to one responsibility can be understood, implemented, tested, and owned without searching unrelated technical layers.

## Organization drivers

Organize around:

- business capability and invariant ownership;
- code that changes for the same reason;
- dependency direction and public contracts;
- team ownership and release responsibility;
- runtime isolation only where it is operationally required.

Folder structure is an index, not architecture. Dependency behavior determines whether a boundary is real.

## Decision guide

1. Identify the decision or state the code owns.
2. Keep behavior, validation, and tests close enough to change together.
3. Expose a small contract; keep storage and framework details internal.
4. Separate shared code only when consumers share the same semantics and lifecycle.
5. Enforce important dependency rules automatically.

Prefer local duplication over a shared abstraction when similar code represents different business decisions or is likely to evolve independently.

## Trade-offs

Capability-oriented organization improves change locality but may duplicate technical setup. Layer-oriented organization centralizes technical concerns but spreads one outcome across many locations.

## Failure modes

- Creating `services`, `helpers`, or `common` folders with unrelated ownership.
- Extracting shared libraries from visual similarity alone.
- Allowing internal models to become cross-module contracts.
- Increasing project count without enforcing dependencies.

## Review evidence

- [ ] A typical change has a clear starting point and bounded impact.
- [ ] Shared code has shared semantics, ownership, and lifecycle.
- [ ] Internal details cannot be bypassed accidentally.
- [ ] Dependency direction is testable.
