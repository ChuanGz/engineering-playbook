# Refactoring

## Decision supported

Improve internal structure while preserving required behavior and controlling the delivery risk of the change.

## Entry criteria

Refactor when evidence shows:

- repeated changes cross the same accidental boundary;
- a defect is likely because rules are duplicated or hidden;
- tests cannot isolate an important behavior;
- dependency direction prevents a planned change;
- operational diagnosis is blocked by current structure.

Do not refactor solely because another pattern appears cleaner.

## Method

1. State the change problem and expected improvement.
2. Establish behavior evidence through tests, telemetry, or controlled comparison.
3. Choose the smallest structural move that addresses the problem.
4. Separate behavior change from structural change when review risk would otherwise increase.
5. Keep commits reversible and validate after each meaningful step.
6. Remove superseded paths and measure the original pain after delivery.

## Trade-offs

Incremental refactoring limits risk and preserves feedback but may temporarily increase duplication. Large rewrites remove constraints faster but combine behavioral, migration, and operational uncertainty.

## Failure modes

- Refactoring without a named change or risk problem.
- Rewriting tests to match new internals while losing behavior coverage.
- Introducing generic abstractions before two real variations exist.
- Leaving old and new paths indefinitely.

## Exit evidence

- [ ] Required behavior is protected independently from implementation shape.
- [ ] The original change, defect, or diagnostic problem is reduced.
- [ ] Migration and rollback risk are bounded.
- [ ] Obsolete structure and temporary compatibility code are removed or owned.
