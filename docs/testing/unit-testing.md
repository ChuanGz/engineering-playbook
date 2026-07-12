# Unit Testing

## Decision supported

Protect deterministic rules and state transitions with fast evidence that remains stable when unrelated implementation details change.

## When to use this

Use this when the risk is inside deterministic behavior: rules, calculations, validation, state transitions, branching, or small policy decisions.

## Appropriate boundary

Use a unit test when the behavior can be evaluated without relying on real infrastructure, serialization, framework wiring, or network semantics. The unit may be a function, class, aggregate, or coherent module—not necessarily one method.

## Test design

1. Name the business rule or failure the test protects.
2. Arrange only state relevant to that decision.
3. Trigger behavior through a stable public boundary.
4. Assert the observable result, state transition, or emitted decision.
5. Cover meaningful boundaries and invalid transitions, not every code branch mechanically.
6. Use test doubles only for external effects or controllable decision inputs.

Avoid mocking internal collaborators merely to isolate classes. Such tests often preserve current structure instead of behavior.

## Trade-offs

Unit tests are fast and diagnostic but cannot validate configuration, persistence, serialization, or dependency contracts. Adding mocks can increase isolation while decreasing behavioral confidence.

## Failure modes

- One test per method without a protected rule.
- Asserting private calls, call order, or internal collections.
- Reproducing production calculations inside expected values.
- Making time, randomness, or concurrency implicit and flaky.

## Example

Weak unit test verifies that `calculate()` calls three helpers. Better unit test proves that an expired discount is rejected, boundary dates are handled, and the expected state transition is emitted.

## Evidence to keep

- [ ] The test name identifies behavior and relevant condition.
- [ ] Assertions remain valid after safe internal refactoring.
- [ ] Test doubles represent real controllable boundaries.
- [ ] Boundary cases come from domain behavior, not coverage gaps alone.
