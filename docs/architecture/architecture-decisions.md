# Architecture Decisions

## Decision supported

Preserve why a consequential structural choice was made so future engineers can operate, challenge, or replace it using the original forces and new evidence.

## When to use this

Use this when a choice changes boundaries, data authority, integration semantics, quality attributes, operational responsibility, or future change cost.

## Decision to make

Decide whether the choice is consequential enough to record, and what evidence would let a future team keep, supersede, or reverse it.

## When to record

Create an architecture decision record when a choice:

- changes system boundaries, data authority, or integration semantics;
- materially affects reliability, security, cost, or operability;
- constrains multiple teams or future changes;
- is expensive to reverse;
- resolves a recurring disagreement that context alone cannot preserve.

Do not create an ADR for routine implementation details that are clear from code and cheap to change.

## Required decision content

1. Status and decision owner.
2. Context, constraints, and evidence available at decision time.
3. Prioritized decision drivers.
4. Credible alternatives, including the simplest current approach.
5. Decision and scope.
6. Positive and negative consequences.
7. Validation, follow-up actions, and reconsideration triggers.

Preserve superseded decisions. Link the replacement rather than rewriting historical context.

## Trade-offs

Decision records reduce repeated debate and context loss but become noise when every choice is documented. Record decisions in proportion to consequence and reversal cost.

## Failure modes

- Writing a technology announcement without alternatives or drivers.
- Recording only benefits of the selected option.
- Treating approval as permanent proof that assumptions remain true.
- Updating an old ADR until the original decision can no longer be understood.

## Example

Weak ADR: "Use Kafka." Better ADR: "Use asynchronous order events because checkout must continue when fulfillment is delayed; accept delayed failure and reconciliation cost; reconsider if fulfillment needs immediate authoritative response."

## Evidence to keep

- [ ] Alternatives were credible under the same constraints.
- [ ] Negative consequences and ownership are explicit.
- [ ] Validation and reconsideration use observable evidence.
- [ ] Status and replacement history are traceable.
