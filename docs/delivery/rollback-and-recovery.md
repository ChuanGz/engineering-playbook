# Rollback and Recovery

## Decision supported

Select the fastest safe action to reduce harm after a release when software, data, contracts, or external effects may not be reversible together.

## Recovery options

- **Rollback:** restore a previous compatible artifact or configuration.
- **Roll forward:** deploy a corrective change when state or contracts cannot move backward safely.
- **Disable:** use a feature or operational control to stop the harmful path.
- **Contain:** limit traffic, tenants, operations, or integrations while preserving safe service.
- **Reconcile:** repair partial or inconsistent state after behavior is stabilized.

## Decision guide

1. Define failure signals and the person authorized to act.
2. Identify reversible and irreversible parts of the release.
3. Test artifact, configuration, schema, and data compatibility in both directions where rollback is claimed.
4. Prefer containment when diagnosis is incomplete and rollback may worsen state.
5. Preserve evidence while reducing impact; do not delay recovery for full root cause.
6. Verify service and data state after action, then reconcile affected work.

## Trade-offs

Backward-compatible migration preserves rollback but requires temporary dual support. Fast roll-forward avoids backward constraints but depends on diagnosis and deployment speed.

## Failure modes

- Calling artifact redeployment a rollback while schema or data is irreversible.
- Discovering missing permissions or runbooks during an incident.
- Repeated automated rollback causing oscillation.
- Restoring availability without checking data correctness.

## Review evidence

- [ ] Recovery choice accounts for code, configuration, contract, and data state.
- [ ] Trigger, authority, procedure, and verification are explicit.
- [ ] Irreversible effects have containment and reconciliation plans.
- [ ] Recovery capability has been exercised at realistic boundaries.
