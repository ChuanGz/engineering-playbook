# Code Review Checklist

## Purpose

Make the merge decision using checks tied to observable correctness, risk, and maintainability rather than checklist completion alone.

## When to use this

Use this when reviewing a pull request, pairing on a risky change, or deciding whether unresolved findings can safely move after merge.

## Decision to make

Decide whether the change is safe and understandable enough to merge, whether it needs changes, or whether the decision needs another owner or specialist.

## How to review

1. Confirm the intended outcome, non-goals, and acceptance evidence.
2. Review the highest-consequence behavior and failure paths before style or preference.
3. Check whether implementation, tests, migration, documentation, and rollout evidence match the changed risk.
4. Separate blockers from non-blocking follow-up work.
5. Record who accepts any residual risk.

## Context and scope

- [ ] The change states one primary outcome, acceptance evidence, and non-goals.
- [ ] The diff contains the implementation, migration, tests, and operational changes required to deliver that outcome safely.
- [ ] Deferred work does not hide a release-critical gap.

## Correctness and safety

- [ ] Required behavior and business invariants are enforced at the owning boundary.
- [ ] Invalid input, authorization, partial failure, retry, cancellation, and concurrency are handled where relevant.
- [ ] Sensitive data, secrets, trust boundaries, and destructive operations received explicit review.

## Design and maintenance

- [ ] Responsibilities, data authority, and dependency direction remain clear.
- [ ] Added abstraction or complexity protects a current requirement or known variation.
- [ ] Logs, metrics, errors, and ownership support diagnosis and recovery.

## Evidence and delivery

- [ ] Tests or equivalent evidence cover the material risks introduced.
- [ ] Compatibility, migration, rollout, and rollback are defined where needed.
- [ ] Documentation and decision records change when behavior or accepted constraints change.

## Merge decision

- **Approve:** all material risks have accepted evidence.
- **Approve with follow-up:** remaining work is non-blocking, bounded, and owned.
- **Request changes:** a named correctness, security, data, operational, or maintainability risk remains unresolved.
- **Escalate:** the change requires authority or domain evidence unavailable to the review participants.

Comments about personal style, unsupported preference, or unrelated redesign are not merge blockers.

## Common failure

A review blocks on naming or formatting while missing a data migration, authorization gap, partial failure path, or rollback problem. Preference comments may still be useful, but they should not crowd out the merge decision.

## Evidence to keep

Keep blocking findings, accepted residual risks, required follow-ups with owners, and the evidence used to approve or hold the change.
