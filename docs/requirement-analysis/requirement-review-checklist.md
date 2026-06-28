# Requirement Review Checklist

## Purpose

Decide whether a requirement is clear enough to estimate, design, and validate without hiding material assumptions.

## Review sequence

1. State the user or business outcome in observable terms.
2. Identify the decision owner, affected stakeholders, and intended users.
3. Define included scope, excluded scope, constraints, and dependencies.
4. Replace subjective language with measurable acceptance conditions.
5. Record assumptions, unresolved questions, and their owners.
6. Identify delivery, operational, security, data, and compliance risks.
7. Confirm how the outcome will be validated after delivery.

## Decision guidance

- Mark the requirement **ready** only when unresolved items cannot materially change scope, design, or acceptance.
- Mark it **conditionally ready** when assumptions are explicit, owned, and safe to validate during delivery.
- Mark it **not ready** when the expected outcome, authority, boundary, or validation method remains unclear.

## Trade-offs

More review reduces expensive rework but delays learning if every minor uncertainty becomes a blocker. Apply review depth in proportion to reversibility, cost, and risk.

## Failure modes

- Treating a solution request as a validated problem.
- Using stakeholder agreement as evidence of user value.
- Accepting criteria that describe implementation rather than observable behavior.
- Leaving exclusions and operational constraints implicit.

## Exit checklist

- [ ] Outcome and success evidence are explicit.
- [ ] Scope boundaries and assumptions are recorded.
- [ ] Material dependencies and risks have owners.
- [ ] Acceptance conditions are testable.
- [ ] Readiness status and remaining actions are documented.
