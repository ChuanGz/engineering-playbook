# Maintainability

## Decision supported

Determine whether the implementation can absorb expected changes safely without relying on undocumented knowledge or broad regression effort.

## Evidence of maintainability

Use observable signals:

- change locality for recent features and fixes;
- clarity of ownership and dependency direction;
- tests that detect behavior regressions without mirroring internals;
- time required to diagnose and recover failures;
- frequency of coordinated edits across unrelated modules;
- onboarding and review friction around the same code.

Line count, interface count, and pattern compliance are not maintainability evidence by themselves.

## Decision guide

1. Identify likely change axes from real roadmap or recent history.
2. Protect stable rules and volatile dependencies at the narrowest useful boundary.
3. Remove accidental complexity before introducing flexibility.
4. Keep operational behavior, ownership, and failure recovery discoverable.
5. Measure whether changes become safer or merely more indirect.

Avoid speculative extension points. A direct implementation is easier to replace than an incorrect abstraction used everywhere.

## Trade-offs

Preparing for evidenced change reduces future work but increases current surface area. Deferring structure preserves speed but may accumulate coordinated-change cost.

## Failure modes

- Equating abstraction with flexibility.
- Optimizing code for hypothetical reuse.
- Keeping obsolete compatibility paths without consumers.
- Measuring quality only through static-analysis scores.

## Review evidence

- [ ] Expected change axes come from real evidence.
- [ ] Complexity protects a named decision or dependency.
- [ ] Tests verify behavior at stable boundaries.
- [ ] Ownership and operational recovery are discoverable.
