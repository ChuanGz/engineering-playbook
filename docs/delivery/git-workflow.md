# Git Workflow

## Decision supported

Choose a change and integration workflow that preserves intent, enables effective review, and allows the team to recover without unnecessary branch ceremony.

## Workflow requirements

A reviewable workflow defines:

- the unit of review and accountable author;
- required evidence before integration;
- branch lifetime and synchronization expectations;
- merge authority and protected-branch rules;
- handling of urgent changes and failed integration;
- release traceability from source revision to deployed artifact.

## Decision guide

1. Prefer short-lived branches when integration is frequent and automated evidence is trustworthy.
2. Keep commits coherent enough to explain one decision or safe transition.
3. Use commit messages that state the engineering outcome, not tool taxonomy alone.
4. Protect the default branch with checks proportionate to release risk.
5. Preserve history required for audit and recovery; rewrite only unpublished work unless governance explicitly allows otherwise.
6. Tag releases or otherwise make deployed revisions traceable.

Do not add environment branches or complex branching models unless release coordination, support policy, or compliance creates a real need.

## Trade-offs

More workflow controls reduce unauthorized or weakly reviewed changes but increase lead time and bypass pressure. Minimal controls improve flow but require strong automation and ownership.

## Failure modes

- Long-lived branches hiding integration risk until release.
- Commits mixing unrelated behavior, formatting, and migration.
- Emergency paths that bypass traceability and never receive review.
- Merge policies that exist only as convention and cannot be enforced.

## Review evidence

- [ ] Each integrated change has an outcome, owner, and review evidence.
- [ ] Default-branch controls match actual delivery risk.
- [ ] Emergency and recovery paths remain traceable.
- [ ] A deployed artifact maps to an immutable source revision.
