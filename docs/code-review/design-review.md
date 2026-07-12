# Design Review in Code Changes

## Decision supported

Determine whether a change fits the accepted architecture and keeps future changes local without adding speculative abstraction.

## When to use this

Use this when a code change moves responsibilities, adds abstractions, touches ownership boundaries, introduces shared models, or changes dependency direction.

## Review method

1. Identify the responsibility and boundary being changed.
2. Check whether state, rules, and dependency direction remain with their owner.
3. Look for new coupling through shared models, direct data access, events, helpers, or configuration.
4. Test abstractions against a real variation, invariant, dependency, or ownership need.
5. Compare the implementation with a simpler option under the same requirements.
6. Escalate only structural decisions that affect multiple changes, teams, or operational qualities.

Do not redesign the wider system inside a review unless the current change exposes a material architecture risk. Record broader improvement separately with evidence.

## Trade-offs

Local consistency lowers comprehension cost, but preserving a weak pattern can compound debt. Deviation is justified when the existing approach cannot satisfy a named requirement and migration impact is controlled.

## Failure modes

- Requiring a pattern because it exists elsewhere without verifying context.
- Adding an interface for every class without independent variation.
- Moving logic into generic helpers that erase ownership.
- Blocking a bounded change on hypothetical future scale.

## Example

Weak review says "use the same pattern as the other module." Stronger review asks whether the same ownership, change pressure, dependency direction, and operational constraints actually apply to this change.

## Evidence to keep

- [ ] Responsibility, state authority, and dependency direction remain explicit.
- [ ] New abstractions protect a current decision or variation.
- [ ] Cross-boundary contracts expose outcomes rather than internals.
- [ ] Any architecture deviation includes rationale and migration impact.
