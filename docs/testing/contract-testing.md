# Contract Testing

## Decision supported

Detect whether independently evolving providers and consumers still agree on request, response, event, error, and compatibility semantics.

## When to use this

Use this when provider and consumer change independently and integration failure would otherwise appear late, especially across service, team, package, or external API boundaries.

## When contract tests add value

Use contract tests when consumers release independently, provider internals should remain private, and integration failures would otherwise appear late. Do not add them when producer and consumer share one release boundary and an integration test gives clearer evidence at lower cost.

## Contract scope

Validate only behavior consumers rely on:

- required fields and semantic constraints;
- response and error outcomes;
- compatibility of optional or additive changes;
- event meaning, identity, and ordering assumptions;
- authentication or protocol requirements that affect interaction.

Do not freeze entire payloads or provider models when consumers use only a subset.

## Decision guide

1. Assign provider and consumer ownership.
2. Capture expectations from real consumer behavior.
3. Verify contracts against the provider before deployment.
4. Publish and version contract evidence with traceable revisions.
5. Define deprecation, consumer verification, and removal policy.

## Trade-offs

Contract tests enable independent change but create governance and tooling overhead. Overly broad contracts reduce provider freedom and become another shared model.

## Failure modes

- Treating schema compatibility as semantic compatibility.
- Publishing expectations no production consumer actually uses.
- Allowing stale consumer contracts to block safe provider change.
- Ignoring error and authorization behavior.

## Example

Weak contract freezes the provider payload because it is easy to snapshot. Better contract records the fields, error outcomes, authorization behavior, and compatibility assumptions the active consumer actually uses.

## Evidence to keep

- [ ] Each expectation traces to an active consumer behavior.
- [ ] Provider verification runs before incompatible deployment.
- [ ] Contract scope excludes unused internal representation.
- [ ] Deprecation and stale-consumer ownership are explicit.
