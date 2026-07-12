# Release Readiness

## Decision supported

Choose whether to release, hold, or expose a change gradually using evidence about user value, technical risk, and recovery capability.

## When to use this

Use this before exposing a change to users, increasing rollout, or accepting a known gap. It is most useful when the change affects users, data, operations, commitments, security, compliance, or recovery capability.

## Decision to make

Decide whether to release, stage, hold, or accept a bounded risk, and name who has authority to pause, continue, or reverse the rollout.

## Readiness evidence

Assess:

- acceptance evidence for the intended outcome;
- unresolved defects and their user or operational impact;
- compatibility, schema, data migration, and dependency readiness;
- security, privacy, and compliance decisions;
- observability, support ownership, and operational runbooks;
- rollout controls, success thresholds, and recovery capability;
- timing constraints and affected stakeholder communication.

Absence of known defects is not evidence of readiness. Define required evidence from the ways the release can fail.

## Decision guide

- **Release:** material risks have accepted evidence and recovery fits the impact.
- **Stage:** uncertainty remains but exposure can be bounded and measured safely.
- **Hold:** a critical outcome, control, dependency, or recovery path is unproven.
- **Accept risk:** the accountable owner explicitly accepts a bounded gap with monitoring and expiry.

## How to apply

1. State the intended user or business outcome and release scope.
2. Identify the material ways the release can harm users, data, operations, or commitments.
3. Compare available evidence against those failure modes and known gaps.
4. Confirm rollout controls, success signals, stop thresholds, and recovery path.
5. Record the release decision, accountable owner, and expiry for accepted gaps.

## Common failure

A team treats green CI and no known defects as readiness. That can miss untested dependencies, weak observability, unsupported rollback, data reconciliation gaps, or no person with authority to stop rollout.

## Trade-offs

Waiting for more evidence lowers uncertainty but delays value and real feedback. Staged release improves learning but requires traffic control, segmentation, and trustworthy telemetry.

## Failure modes

- Using a checklist meeting as a substitute for evidence.
- Releasing because a date arrived while dependencies are not ready.
- Treating rollback availability as permission to skip validation.
- Lacking a person authorized to pause or reverse rollout.

## Evidence to keep

- [ ] Outcome, rollout, and stop thresholds are measurable.
- [ ] Material gaps have explicit acceptance and owner.
- [ ] Data, dependency, support, and operational readiness are verified.
- [ ] Recovery action can start within the required time.
