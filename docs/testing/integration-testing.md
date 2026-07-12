# Integration Testing

## Decision supported

Verify behavior that depends on real collaboration across storage, framework, process, protocol, or managed-service boundaries.

## When to use this

Use this when confidence depends on real configuration, persistence, serialization, routing, authentication, messaging, transactions, or dependency failure behavior.

## Select the boundary

Use an integration test when confidence depends on:

- schema mappings, constraints, transactions, or query behavior;
- serialization, routing, authentication, or middleware configuration;
- message publication, consumption, idempotency, or ordering;
- filesystem, cache, queue, or external-service protocol behavior;
- dependency failure, timeout, or recovery semantics.

Include only the real components needed to expose the risk. A full deployed environment is not automatically more valuable.

## Test design

1. State the integration contract and failure being tested.
2. Use production-equivalent versions and configuration where they affect behavior.
3. Control test data ownership and cleanup.
4. Exercise the public boundary and assert durable outcome or external effect.
5. Test one credible dependency failure and recovery path.
6. Capture enough diagnostics to distinguish product failure from environment failure.

## Trade-offs

Real dependencies reveal configuration and protocol defects but increase execution cost and environmental variability. Substitutes improve control but may diverge from production semantics.

## Failure modes

- Replacing the database or broker with an in-memory implementation that behaves differently.
- Sharing mutable test data across parallel runs.
- Asserting only an HTTP status while state is incorrect.
- Retrying flaky tests without identifying environmental or product cause.

## Example

Weak integration test asserts `200 OK` after saving an order. Better integration test verifies persisted state, transaction behavior, authorization boundary, emitted message, and diagnostics for the expected dependency failure.

## Evidence to keep

- [ ] Every real dependency is present because it exposes a named risk.
- [ ] Versions and configuration match relevant production behavior.
- [ ] Data isolation and cleanup are deterministic.
- [ ] Failures produce actionable boundary diagnostics.
