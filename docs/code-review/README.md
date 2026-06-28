# Code Review

## Purpose

Reduce change risk through focused review.

## Core guidance

Review correctness, design fit, tests, security, operability, and clarity while keeping feedback respectful.

Code review is a risk decision about a specific change. It is not a contest over personal style, a substitute for automated checks, or proof that the wider system is correct.

## Guides

- [Review principles](review-principles.md) — review for consequential risk and shared understanding.
- [Review scope](review-scope.md) — keep changes small enough to reason about without hiding necessary work.
- [Correctness review](correctness-review.md) — verify behavior, state, failure, and concurrency decisions.
- [Design review](design-review.md) — assess whether the change preserves intended boundaries and changeability.
- [Test review](test-review.md) — judge whether evidence matches the risks introduced.
- [Review checklist](review-checklist.md) — make the merge decision with explicit pass conditions.

## Review questions

- Does every blocking finding identify a concrete risk or unmet requirement?
- Are correctness, security, data, operational, and maintainability risks prioritized over style?
- Does the reviewed evidence cover the changed behavior and boundaries?
- Are approvals, follow-ups, accepted risks, and escalations explicitly disposed?
