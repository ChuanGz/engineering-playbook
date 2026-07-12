# Review Scope

## Decision supported

Shape a change so reviewers can reason about its behavior and risk without separating work that needs to be understood together.

## When to use this

Use this before opening or reviewing a large, mixed, or multi-step change. It helps decide whether to split, combine, or sequence the work.

## Scope signals

A review is probably too broad when it combines unrelated outcomes, mixes structural migration with new behavior, touches several ownership boundaries without one reason, or produces more findings than reviewers can prioritize.

A review is too narrow when it hides required schema, operational, security, migration, or test changes in later work while presenting the current change as complete.

## Decision guide

1. State one primary outcome and its acceptance evidence.
2. Separate mechanical preparation from behavioral change when either can be validated alone.
3. Keep dependent implementation, tests, migration, and observability together when splitting would hide risk.
4. Identify generated, vendored, or mechanical files so reviewers can focus attention.
5. Provide a safe sequence for multi-change migrations and define which intermediate states are deployable.

Do not optimize for a universal line limit. Change independence, conceptual load, and reversibility matter more than raw size.

## Trade-offs

Smaller reviews improve focus and feedback time but create sequencing overhead and temporary states. Larger reviews preserve end-to-end context but reduce defect-detection quality.

## Failure modes

- Splitting by file type so behavior and evidence land separately.
- Hiding refactoring inside a feature diff without explaining behavior preservation.
- Using a large generated diff to obscure meaningful changes.
- Treating follow-up issues as acceptable for release-critical omissions.

## Example

Weak split: migration in one PR, behavior in another, tests in a third, with no deployable intermediate state. Better split: first add compatible schema and tests, then change behavior behind a safe path, then remove old compatibility after rollout evidence.

## Evidence to keep

- [ ] The diff has one primary outcome and clear non-goals.
- [ ] Every included change is necessary for that outcome or safe migration.
- [ ] Deferred work does not invalidate current acceptance or safety.
- [ ] Reviewers can identify the high-risk portion quickly.
