# Validation Before Implementation

## When to use this

Product, engineering, and business decision owners use this guide before committing heavily to an uncertain outcome or solution. Validate the assumption that combines high consequence with weak evidence, using the cheapest credible method that can change the decision.

Use this before implementation when the team has weak evidence for user value, workflow fit, data availability, integration behavior, operational feasibility, or acceptance conditions.

## Decision to make

Decide which assumption must be tested before commitment, which evidence is credible enough, and how the result will change scope, acceptance, design, or priority.

## What to validate

- The problem exists and is important enough to solve.
- The intended users and decision owners agree on the outcome.
- Proposed behavior satisfies real workflow constraints.
- Required data, permissions, integrations, and operational capabilities exist.
- Acceptance conditions distinguish success from completion.

## How to apply

Rank assumptions by impact and uncertainty. Validate high-impact, low-confidence assumptions first using interviews, existing data, workflow observation, prototypes, technical spikes, or contract tests as appropriate.

Proceed when evidence is strong enough for the reversibility and cost of the decision. Do not demand production-level proof for a reversible experiment, and do not accept informal confidence for an irreversible migration.

Choose the validation method by the question:

- Use user interviews or workflow observation for problem importance and workflow fit.
- Use existing data or operational reports for frequency, volume, or business impact.
- Use prototypes for interaction uncertainty, not production readiness.
- Use technical spikes or contract tests for integration, data, performance, or feasibility uncertainty.

## Trade-offs

Validation costs time and can delay delivery; skipping it transfers that cost to rework and production risk. Time-box discovery and define the decision it needs to enable.

## Failure modes

- Using stakeholder preference as user validation.
- Building a polished prototype when a workflow sketch would answer the question.
- Running a technical spike without explicit learning criteria.
- Collecting evidence but not changing the requirement when it is disproved.

## Example

Before building an approval dashboard, the riskiest assumption may not be UI layout. It may be whether approvers can trust the underlying status data. A short data audit or workflow observation can change the decision faster than a polished prototype.

## Evidence to keep

- [ ] Critical assumptions are ranked by impact and uncertainty.
- [ ] Each validation activity has a decision and success threshold.
- [ ] Evidence and remaining uncertainty are recorded.
- [ ] Scope and acceptance conditions reflect the findings.

## Maintenance trigger

Review this guide when validation work repeatedly produces no decision, arrives after commitment, or fails to change scope when evidence disproves an assumption.
