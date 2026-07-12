# Test Strategy

## When to use this

Developers, testers, reviewers, and release owners use this guide to decide what evidence is worth paying for. Start from credible harmful outcomes and changed boundaries, then choose the cheapest evidence that can detect them. Test count and framework coverage are not the goal.

Use this before implementation starts for risky work, during review when evidence looks mismatched, and before release when residual risk needs explicit acceptance.

## Decision supported

Allocate validation effort and release evidence according to the ways a change can fail and the consequence of those failures.

## Strategy inputs

- critical user and operational workflows;
- business invariants and irreversible state changes;
- changed boundaries, dependencies, schemas, and configuration;
- security, privacy, reliability, and recovery requirements;
- historical defects and production incidents;
- release reversibility and detection time.

When project evidence is missing, label the strategy as provisional and identify what production or domain review needs to confirm.

## How to apply

1. List credible failure modes and rank impact, likelihood, and detectability.
2. Map each material risk to the cheapest credible evidence source.
3. Assign test level, environment, data, owner, and execution frequency.
4. Define entry, exit, and acceptable residual-risk criteria.
5. Separate release-blocking evidence from informational checks.
6. Review escaped defects and remove checks that no longer influence decisions.

Do not copy a standard test pyramid when risk is concentrated at contracts, migration, concurrency, or operations.

## Common failure

A team adds many tests around easy paths while the real risk sits in migration, authorization, compatibility, concurrency, or rollback. The test suite grows, but the release decision is still weak.

## Example

For a schema migration, unit tests may prove transformation helpers, but they do not prove production data can migrate, old and new code can coexist, or rollback is safe. The strategy should include representative data, compatibility checks, rollout signals, and a recovery decision owner.

## Trade-offs

Broader validation lowers residual uncertainty but increases feedback time and maintenance. Fast pipelines improve delivery flow but may move necessary evidence into staged rollout and production controls.

## Failure modes

- Listing test types without connecting them to failure modes.
- Requiring every check on every commit regardless of cost or signal.
- Omitting migration, rollback, observability, and recovery validation.
- Accepting known gaps without owner or compensating control.

## Evidence to keep

- [ ] Material risks map to explicit evidence and owners.
- [ ] Required environments and data are available and controlled.
- [ ] Release gates have objective pass conditions.
- [ ] Residual risk and production validation are accepted explicitly.

## Maintenance trigger

Review this guide when escaped failures reveal an uncovered risk, or when tests consume time without influencing a release, design, or recovery decision.
