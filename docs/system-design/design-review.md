# Design Review

## Decision supported

Determine whether a proposed design has enough evidence and operational clarity to enter implementation, or whether a specific unresolved risk must be addressed first.

## Review inputs

- problem frame, scope, constraints, and quality scenarios;
- system context, boundaries, critical data flows, and dependencies;
- capacity assumptions and validation targets;
- alternatives considered and decision records;
- security, privacy, failure, recovery, migration, and operational model;
- open questions with impact, owner, and due decision.

## Review sequence

1. Confirm the problem and design drivers before discussing components.
2. Walk one critical success flow and one degraded or failure flow.
3. Challenge the highest-impact assumptions with evidence.
4. Verify ownership at boundaries, state transitions, and recovery points.
5. Compare the design with the simplest credible alternative.
6. Classify findings as blocking, follow-up, accepted risk, or preference.

Approve conditionally when remaining work has bounded impact and a named owner. Do not block implementation for formatting, stylistic preference, or hypothetical scale unrelated to stated constraints.

## Trade-offs

Review reduces blind spots and shared-risk decisions, but large review groups can dilute accountability. Include people who own affected constraints or can supply required evidence.

## Failure modes

- Reviewing diagrams without tracing runtime behavior.
- Introducing new requirements during the review without changing scope.
- Treating reviewer seniority as evidence.
- Recording comments without disposition, owner, or decision.

## Exit criteria

- [ ] Design drivers and accepted evidence are agreed.
- [ ] Critical flows, failures, and recovery have accountable owners.
- [ ] Blocking findings are resolved or explicitly accepted by the decision owner.
- [ ] Decisions, follow-ups, and reconsideration triggers are recorded.
