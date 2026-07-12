# API Design

## Decision supported

Implement a contract whose behavior, authority, failure semantics, and evolution can be understood independently from provider internals.

## When to use this

Use this when adding or changing an API, event, command, query, or internal service contract that another caller depends on. Apply more rigor when consumers deploy independently or when failures affect data, money, security, or operations.

## Decision to make

Decide what outcome the contract owns, what information callers must provide, which failures are part of the public contract, and how the contract can evolve without breaking consumers.

## Contract evidence

Define before implementation:

- caller outcome and authorization context;
- operation semantics and authoritative owner;
- request, response, validation, and error behavior;
- idempotency, concurrency, timeout, and cancellation expectations;
- compatibility, versioning, and retirement policy;
- observability needed by callers and operators.

## Decision guide

1. Name operations after outcomes rather than persistence actions.
2. Require only information the provider needs to make its decision.
3. Return stable domain outcomes; do not leak framework exceptions or storage models.
4. Distinguish invalid input, rejected business action, unavailable dependency, and unexpected failure.
5. Make retries safe through explicit idempotency where duplicate execution has consequences.
6. Evolve additively when possible and measure consumer usage before removal.

Do not add versioning machinery without a real independent consumer or compatibility requirement.

## Trade-offs

Rich contracts can reduce caller round trips but increase coupling and compatibility cost. Narrow contracts preserve provider freedom but may require more interactions.

## Failure modes

- Designing endpoints directly from database tables.
- Returning success before durable acceptance is known.
- Treating every failure as the same status or exception.
- Publishing internal enum values as permanent contracts.

## Example

Weak API: `POST /orders/update` accepts the full storage model and returns raw provider errors. Better API: `POST /orders/{id}/confirm-payment` accepts only the payment decision inputs, returns stable accepted/rejected/conflict outcomes, and states retry and idempotency behavior.

## Evidence to keep

- [ ] Outcomes, authority, and error semantics are explicit.
- [ ] Retry, idempotency, timeout, and cancellation behavior match failure risk.
- [ ] Internal models and implementation failures remain private.
- [ ] Compatibility rules match actual consumer independence.
