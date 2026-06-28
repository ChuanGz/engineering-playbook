# Documentation Review

## Decision supported

Determine whether a document is accurate, useful, maintainable, and ready to influence engineering work.

## Review sequence

1. Identify the target reader and the task, decision, contract, or recovery action.
2. Verify claims against code, configuration, accepted decisions, production evidence, or primary references.
3. Check prerequisites, scope, non-goals, assumptions, and authority.
4. Execute commands and follow links where the document depends on them.
5. Challenge principles, recommendations, and mandatory rules for correct classification.
6. Verify checklists have observable pass conditions tied to real failures.
7. Compare with existing documents for contradiction and duplication.
8. Confirm ownership and events that require an update or deletion.

Formatting and lint are necessary hygiene, not evidence of correctness or usefulness.

## Review outcomes

- **Approve:** the document enables its stated outcome with verified evidence.
- **Approve with follow-up:** bounded non-critical gaps have owners and deadlines.
- **Request changes:** incorrect, unsupported, ambiguous, or unmaintainable guidance can affect decisions.
- **Reject or remove:** the document duplicates authoritative content or has no distinct reader value.
- **Escalate:** required domain, security, legal, or operational authority is unavailable.

## Failure modes

- Reviewing grammar while accepting unsupported engineering claims.
- Treating senior tone as proof of senior judgment.
- Adding sections to appear complete instead of resolving the reader’s need.
- Approving copied examples that were never verified in the target context.

## Review evidence

- [ ] The stated reader outcome can be demonstrated.
- [ ] Material claims trace to authoritative evidence or labeled assumptions.
- [ ] Rules, recommendations, opinions, and examples are classified honestly.
- [ ] Maintenance ownership and deletion criteria are explicit.
