# Architecture Evolution

## Decision supported

Change system structure when observed delivery or runtime pressure exceeds the cost and risk of migration—not because a future pattern appears more mature.

## Evolution signals

Use evidence such as:

- recurring changes crossing the same boundaries;
- ownership conflict or release coordination delaying outcomes;
- measured reliability, latency, scaling, or recovery limits;
- security or regulatory boundaries the current structure cannot enforce;
- operational load caused by unclear authority or integration behavior;
- migration cost that is increasing faster than the protected value.

One difficult feature or isolated incident is a signal to investigate, not automatic proof of structural failure.

## Evolution method

1. Describe the current constraint using delivery or runtime evidence.
2. Identify the smallest boundary or dependency change that addresses it.
3. Compare improvement of the current structure with introducing a new one.
4. Define coexistence, data migration, rollback, and ownership transition.
5. Move one observable capability or flow and measure the expected effect.
6. Continue only when evidence supports the next migration step.

Prefer reversible, incremental changes. A target diagram is not a migration strategy.

## Trade-offs

Evolution preserves learning and limits migration risk but temporarily supports old and new structures. Large replacement may remove legacy constraints faster but concentrates risk and delays feedback.

## Failure modes

- Starting a rewrite without a measured current constraint.
- Distributing a system while retaining shared data and coordinated releases.
- Counting migrated components instead of improved outcomes.
- Removing rollback before behavior and operations are proven.

## Review evidence

- [ ] The current constraint is observable and consequential.
- [ ] The proposed change is smaller than credible alternatives.
- [ ] Coexistence, migration, rollback, and ownership are defined.
- [ ] Success and stop conditions measure the original pressure.
