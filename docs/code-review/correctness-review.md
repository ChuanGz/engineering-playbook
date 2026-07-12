# Correctness Review

## Decision supported

Determine whether the implementation produces required outcomes across valid input, invalid input, state transitions, failures, and relevant concurrency.

## When to use this

Use this for changes that alter business behavior, state transitions, authorization, data writes, retries, concurrency, or error outcomes.

## Review method

1. Trace the requirement and acceptance condition into executable behavior.
2. Follow one success path and one consequential failure path through state and side effects.
3. Identify invariants, authority, and the point where changes become durable.
4. Check boundary values, missing state, duplicate requests, retries, cancellation, and concurrent updates where applicable.
5. Verify partial failure cannot report a false outcome or leave unrecoverable state.
6. Compare implementation evidence with the behavior actually required.

Use code, tests, contracts, and runtime behavior as evidence. A plausible reading of the happy path is insufficient.

## Trade-offs

Exhaustive reasoning is impossible for complex systems. Focus on high-impact states and transitions, then use types, invariants, tests, and runtime controls to cover remaining uncertainty.

## Failure modes

- Reviewing syntax while assuming domain behavior is correct.
- Checking validation but not authorization or state authority.
- Retrying non-idempotent work after an uncertain outcome.
- Returning success before required state is durable.
- Ignoring overflow, clock, locale, ordering, or null behavior that affects the domain.

## Example

Weak review checks that a submit button calls the expected endpoint. Stronger correctness review follows duplicate submit, expired permission, partial dependency failure, and whether success is returned only after the authoritative state is durable.

## Evidence to keep

- [ ] Acceptance conditions map to observable behavior.
- [ ] Invariants and invalid transitions are enforced at an authoritative boundary.
- [ ] Partial failure, retry, and concurrency behavior are intentional.
- [ ] Tests or equivalent evidence cover consequential branches.
