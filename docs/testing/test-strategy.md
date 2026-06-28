# Test Strategy

## Decision supported

Allocate validation effort and release evidence according to the ways a change can fail and the consequence of those failures.

## Strategy inputs

- critical user and operational workflows;
- business invariants and irreversible state changes;
- changed boundaries, dependencies, schemas, and configuration;
- security, privacy, reliability, and recovery requirements;
- historical defects and production incidents;
- release reversibility and detection time.

When project evidence is missing, label the strategy as provisional and identify what production or domain review must confirm.

## Method

1. List credible failure modes and rank impact, likelihood, and detectability.
2. Map each material risk to the cheapest credible evidence source.
3. Assign test level, environment, data, owner, and execution frequency.
4. Define entry, exit, and acceptable residual-risk criteria.
5. Separate release-blocking evidence from informational checks.
6. Review escaped defects and remove checks that no longer influence decisions.

Do not copy a standard test pyramid when risk is concentrated at contracts, migration, concurrency, or operations.

## Trade-offs

Broader validation lowers residual uncertainty but increases feedback time and maintenance. Fast pipelines improve delivery flow but may move necessary evidence into staged rollout and production controls.

## Failure modes

- Listing test types without connecting them to failure modes.
- Requiring every check on every commit regardless of cost or signal.
- Omitting migration, rollback, observability, and recovery validation.
- Accepting known gaps without owner or compensating control.

## Exit evidence

- [ ] Material risks map to explicit evidence and owners.
- [ ] Required environments and data are available and controlled.
- [ ] Release gates have objective pass conditions.
- [ ] Residual risk and production validation are accepted explicitly.
