# CI/CD Principles

## Decision supported

Design a pipeline that produces repeatable evidence and promotes the same immutable artifact through controlled delivery stages.

## Principles

### Build once, promote deliberately

Create an immutable artifact from a traceable revision. Do not rebuild per environment when that can change what was tested.

### Fail on actionable evidence

For each required check, identify a responsible owner and corrective action. Unreliable gates train teams to ignore red status.

### Keep configuration differences explicit

Separate deployable artifact from environment configuration while validating both together before exposure.

### Limit delivery authority

Use least privilege, protected environments, auditable approvals, and short-lived credentials where supported. Pipeline access is production access.

## Decision guide

1. Map pipeline stages to evidence and release decisions.
2. Run deterministic, fast checks early; defer expensive evidence only when risk permits.
3. Sign or otherwise verify artifact provenance when supply-chain risk requires it.
4. Make promotion, rollout, pause, and recovery observable.
5. Measure pipeline duration, failure cause, flaky checks, and rollback outcomes.

## Trade-offs

More automation improves consistency but can accelerate incorrect decisions. Manual approval adds judgment only when the approver receives relevant evidence and owns the risk.

## Failure modes

- Treating pipeline completion as proof of production correctness.
- Rebuilding artifacts after validation.
- Storing long-lived production credentials in workflow configuration.
- Adding approval steps whose reviewers lack context or authority.

## Review evidence

- [ ] Every stage produces evidence used by a named decision.
- [ ] Artifact identity remains stable through promotion.
- [ ] Environment configuration and permissions are validated.
- [ ] Pipeline failure and bypass paths are owned and auditable.
