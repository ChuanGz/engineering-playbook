# Code Review Checklist

## Purpose

Make the merge decision using checks tied to observable correctness, risk, and maintainability rather than checklist completion alone.

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
