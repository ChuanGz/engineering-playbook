# Integration Patterns

## Decision supported

Select interaction semantics that satisfy consistency, latency, availability, ownership, and recovery requirements with acceptable operational cost.

## Start from semantics

Before selecting HTTP, messaging, events, queues, or streams, define:

- which boundary owns the decision and resulting state;
- whether the caller needs an immediate authoritative outcome;
- acceptable delay, duplication, ordering, and data loss;
- failure visibility and recovery owner;
- compatibility and consumer lifecycle requirements;
- sensitive-data and trust-boundary constraints.

## Decision guide

- Prefer a synchronous request when the caller cannot proceed without the result and the dependency fits its latency and availability budget.
- Prefer an asynchronous command when work may complete later and acceptance can be separated from outcome.
- Publish an event for a fact already decided by its owner; do not use events to avoid assigning decision authority.
- Share data only when ownership and update semantics remain explicit. A replicated read model is not a second authority.

Use the least complex mechanism that satisfies failure and consistency behavior. Technology choice follows semantics.

## Trade-offs

Synchronous integration simplifies immediate outcomes but propagates latency and failure. Asynchronous integration isolates timing and absorbs bursts but adds delayed failure, idempotency, ordering, reconciliation, and observability work.

## Failure modes

- Choosing events because they appear loosely coupled while schemas and release timing remain coupled.
- Implementing dual writes without atomicity or reconciliation.
- Retrying operations without stable identity and idempotency.
- Publishing internal state changes as permanent public contracts.

## Review evidence

- [ ] Consistency and completion semantics are explicit.
- [ ] Duplicate, ordering, retry, and recovery behavior has an owner.
- [ ] Consumers can evolve without reading provider internals.
- [ ] Operational complexity is justified against a simpler interaction.
