# Release Readiness

## Decision supported

Choose whether to release, hold, or expose a change gradually using evidence about user value, technical risk, and recovery capability.

## Readiness evidence

Assess:

- acceptance evidence for the intended outcome;
- unresolved defects and their user or operational impact;
- compatibility, schema, data migration, and dependency readiness;
- security, privacy, and compliance decisions;
- observability, support ownership, and operational runbooks;
- rollout controls, success thresholds, and recovery capability;
- timing constraints and affected stakeholder communication.

Absence of known defects is not evidence of readiness. Required evidence must reflect how the release can fail.

## Decision guide

- **Release:** material risks have accepted evidence and recovery fits the impact.
- **Stage:** uncertainty remains but exposure can be bounded and measured safely.
- **Hold:** a critical outcome, control, dependency, or recovery path is unproven.
- **Accept risk:** the accountable owner explicitly accepts a bounded gap with monitoring and expiry.

## Trade-offs

Waiting for more evidence lowers uncertainty but delays value and real feedback. Staged release improves learning but requires traffic control, segmentation, and trustworthy telemetry.

## Failure modes

- Using a checklist meeting as a substitute for evidence.
- Releasing because a date arrived while dependencies are not ready.
- Treating rollback availability as permission to skip validation.
- Lacking a person authorized to pause or reverse rollout.

## Exit evidence

- [ ] Outcome, rollout, and stop thresholds are measurable.
- [ ] Material gaps have explicit acceptance and owner.
- [ ] Data, dependency, support, and operational readiness are verified.
- [ ] Recovery action can start within the required time.
