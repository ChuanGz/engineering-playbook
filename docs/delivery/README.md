# Delivery

## Purpose

Move changes safely to users.

## Core guidance

Use traceable changes, quality gates, reproducible artifacts, readiness criteria, rollback plans, and risk controls.

Delivery guidance governs how accepted changes become observable user outcomes. It does not prescribe one branching model, deployment platform, or release frequency without product and operational context.

## Guides

- [Git workflow](git-workflow.md) — preserve reviewable intent and recoverable history.
- [CI/CD principles](ci-cd-principles.md) — build trustworthy delivery evidence and artifact flow.
- [Quality gates](quality-gates.md) — block releases only on checks tied to accepted risk.
- [Release readiness](release-readiness.md) — make an evidence-based go, hold, or staged-release decision.
- [Rollback and recovery](rollback-and-recovery.md) — restore safe service after harmful change.
- [Delivery risk](delivery-risk.md) — identify and control risks introduced by the release process.

## Review questions

- Does the release evidence cover the ways this change can harm users, data, or operations?
- Can the deployed artifact be traced to reviewed source and validated configuration?
- Are rollout, stop, containment, rollback, and reconciliation decisions executable?
- Who accepts residual risk and owns production outcome verification?
