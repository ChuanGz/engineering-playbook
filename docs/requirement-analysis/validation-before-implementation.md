# Validation Before Implementation

## At a glance

Product, engineering, and business decision owners use this guide before committing heavily to an uncertain outcome or solution. Validate the assumption that combines high consequence with weak evidence, using the cheapest credible method that can change the decision.

## Purpose

Reduce avoidable implementation by testing the most consequential assumptions with the cheapest credible evidence.

## What to validate

- The problem exists and is important enough to solve.
- The intended users and decision owners agree on the outcome.
- Proposed behavior satisfies real workflow constraints.
- Required data, permissions, integrations, and operational capabilities exist.
- Acceptance conditions distinguish success from completion.

## Decision guide

Rank assumptions by impact and uncertainty. Validate high-impact, low-confidence assumptions first using interviews, existing data, workflow observation, prototypes, technical spikes, or contract tests as appropriate.

Proceed when evidence is strong enough for the reversibility and cost of the decision. Do not demand production-level proof for a reversible experiment, and do not accept informal confidence for an irreversible migration.

## Trade-offs

Validation costs time and can delay delivery; skipping it transfers that cost to rework and production risk. Time-box discovery and define the decision it needs to enable.

## Failure modes

- Using stakeholder preference as user validation.
- Building a polished prototype when a workflow sketch would answer the question.
- Running a technical spike without explicit learning criteria.
- Collecting evidence but not changing the requirement when it is disproved.

## Exit checklist

- [ ] Critical assumptions are ranked by impact and uncertainty.
- [ ] Each validation activity has a decision and success threshold.
- [ ] Evidence and remaining uncertainty are recorded.
- [ ] Scope and acceptance conditions reflect the findings.

## Maintenance trigger

Review this guide when validation work repeatedly produces no decision, arrives after commitment, or fails to change scope when evidence disproves an assumption.
