# Modularity

## Decision supported

Contain the cost of change by making responsibilities cohesive and dependencies visible, directional, and enforceable.

## What to measure

Evaluate modularity through behavior rather than folder count:

- which modules change together for one outcome;
- whether callers bypass public contracts;
- whether cycles force coordinated changes;
- whether tests can exercise a responsibility without unrelated setup;
- whether ownership and dependency violations can be detected automatically.

## Decision guide

1. Group code around stable responsibilities and business decisions.
2. Expose a small contract that communicates outcomes, not internal storage.
3. Direct dependencies toward the module that owns the rule.
4. Remove cycles by relocating responsibility or introducing an explicit contract.
5. Enforce important boundaries with build, dependency, or architecture tests.
6. Split deployment only when independent operation provides measurable value.

Avoid adding interfaces between code that has no independent variation, ownership, or testing need. Indirection without a protected boundary adds navigation cost.

## Trade-offs

Isolation improves independent change and testing but introduces mapping, contracts, and duplicated representations. Excessive consolidation reduces ceremony but allows unrelated decisions to become coupled.

## Failure modes

- Calling a directory a module while every project references it directly.
- Creating one shared library for unrelated cross-cutting concerns.
- Measuring modularity by project count.
- Using events internally to conceal cyclic ownership.

## Review evidence

- [ ] Each module owns a coherent set of decisions and state.
- [ ] Public contracts are smaller and more stable than internals.
- [ ] Dependency direction is enforceable.
- [ ] Deployment boundaries are not required to obtain modularity.
