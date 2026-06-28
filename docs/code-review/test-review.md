# Test Review

## Decision supported

Determine whether the change includes credible evidence for the failures it can introduce, without preserving implementation details as tests.

## Review method

1. List the changed behaviors, boundaries, data, and failure paths.
2. Identify the most consequential regression for each.
3. Verify each material risk has evidence at the lowest sufficient test boundary.
4. Check assertions prove outcomes or durable state rather than calls and setup.
5. Confirm test data exposes boundary and invalid cases.
6. Identify risks that require integration, deployment, or production validation instead of unit tests.

No test change can be valid when behavior is demonstrably unchanged and existing evidence already protects the affected boundary. Require new tests because risk changed, not because every diff must increase test count.

## Trade-offs

More test cases can improve confidence but also increase suite cost and false failures. Favor a small set of diagnostic checks over broad scenarios with unclear ownership.

## Failure modes

- Accepting coverage increases without checking what behavior is asserted.
- Mocking the integration semantics under review.
- Rewriting tests to match internals while weakening outcome evidence.
- Ignoring migration, configuration, cancellation, or recovery behavior.

## Review evidence

- [ ] Tests map to changed risks and required outcomes.
- [ ] The test boundary includes the source of failure.
- [ ] Assertions survive safe implementation refactoring.
- [ ] Unverified residual risk and production checks are explicit.
