# Quality Gates

## Decision supported

Decide which automated or manual evidence blocks integration, promotion, or release because proceeding would exceed accepted risk.

## When to use this

Use this when adding, removing, promoting, bypassing, or reviewing a required check in development, CI, deployment, or release.

## Decision to make

Decide whether a check should block progress, warn, run on a schedule, or be removed because its signal no longer changes risk.

## Gate contract

For every required gate, state:

- the failure or policy it protects against;
- the evidence and objective pass condition;
- execution point and expected feedback time;
- accountable owner and correction path;
- bypass authority, required rationale, and expiry;
- review trigger for changing or removing the gate.

## Decision guide

Block early on deterministic issues that cannot be accepted: build failure, invalid artifacts, known vulnerable dependencies above policy threshold, failed critical behavior, or unauthorized configuration as applicable.

Use warnings or scheduled checks when evidence is informative but unreliable, slow, or unrelated to the current change. Promote a check to a gate only after its signal and ownership are proven.

## Trade-offs

Strong gates reduce known risk but extend feedback and can create unsafe bypass culture when noisy. Fewer gates improve flow but move detection into rollout and operations.

## Failure modes

- Setting arbitrary coverage or quality scores with no failure model.
- Keeping flaky checks as blockers.
- Allowing permanent bypasses without risk acceptance.
- Adding a gate after one incident without confirming recurrence or coverage.

## Example

Weak gate blocks release on an arbitrary coverage number while the critical migration path has no validation. Better gate blocks on migration compatibility and rollback evidence because those failures exceed accepted risk.

## Evidence to keep

- [ ] Each gate maps to a consequential failure or mandatory policy.
- [ ] Pass criteria are objective and reproducible.
- [ ] Failure has an owner and useful diagnostics.
- [ ] Bypass is bounded, traceable, and reviewed.
