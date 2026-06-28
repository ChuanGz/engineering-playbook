# Decision Record Standard

## Purpose

Preserve consequential engineering choices and the evidence available when they were made without documenting every routine implementation detail.

## Creation criteria

Create a record when a decision:

- changes ownership, boundaries, data authority, or public contracts;
- materially affects reliability, security, cost, or operability;
- constrains multiple teams or future changes;
- accepts material risk or is expensive to reverse;
- repeatedly attracts debate because original context is missing.

Do not create one when code already explains a cheap, local, and easily reversible choice.

## Required fields

- status, date, scope, and accountable owner;
- context, constraints, evidence, and labeled assumptions;
- prioritized decision drivers and non-goals;
- credible alternatives under the same constraints;
- selected decision and boundary;
- positive and negative consequences;
- accepted risks, follow-up owners, validation, and reconsideration triggers.

## Lifecycle

- Use `Proposed`, `Accepted`, `Rejected`, or `Superseded` status.
- Preserve accepted records as historical evidence.
- Correct factual errors without rewriting original rationale.
- Create a new record when changed evidence produces a new decision.
- Link superseding and superseded records in both directions.

## Reject or revise

- Technology announcements without decision drivers or alternatives.
- Straw alternatives that were never credible.
- Benefits without negative consequences or ownership.
- Approval lists used as a substitute for accountable decision ownership.
- Records that cannot state what evidence would invalidate them.

## Acceptance evidence

- [ ] Recording criteria justify the maintenance cost.
- [ ] Alternatives are compared under the same constraints.
- [ ] Consequences, risks, and follow-up ownership are explicit.
- [ ] Validation and reconsideration rely on observable evidence.

## Maintenance trigger

Review status when a named assumption, constraint, validation result, or reconsideration trigger changes—not on an arbitrary documentation schedule.
