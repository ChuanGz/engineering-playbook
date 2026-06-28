# Data Flow

## Decision supported

Make the origin, transformation, storage, movement, and failure behavior of important data explicit enough to review correctness and recovery.

## Model the flow

For each business-critical flow, record:

- initiating actor or event;
- system of record and data owner;
- synchronous calls, asynchronous messages, and state transitions;
- validation and authorization points;
- identifiers, ordering, duplication, and idempotency behavior;
- retained sensitive data and trust-boundary crossings;
- failure visibility, retry, reconciliation, and recovery owner.

Model the success path and at least one partial-failure path. A component diagram alone does not describe what happens to data.

## Decision guidance

Use synchronous flow when the caller needs an immediate authoritative result and dependencies can meet the availability budget. Use asynchronous flow when work can be accepted before completion, bursts need buffering, or temporal decoupling is worth added state and operational complexity.

Do not combine both styles without defining which state is authoritative and how conflicting outcomes are reconciled.

## Trade-offs

Synchronous flows simplify outcome visibility but couple latency and availability. Asynchronous flows absorb variation and isolate timing but add duplicate delivery, delayed failure, ordering, and reconciliation concerns.

## Failure modes

- Showing message movement without ownership of resulting state.
- Assuming exactly-once behavior instead of designing idempotency.
- Retrying non-idempotent operations without a stable operation identity.
- Omitting dead-letter, reconciliation, or manual recovery paths.

## Review evidence

- [ ] Every critical state has an authoritative owner.
- [ ] Partial failure and recovery are visible in the flow.
- [ ] Duplicate, ordering, retry, and idempotency behavior are defined where relevant.
- [ ] Sensitive-data movement and retention have been reviewed.
