# Common Requirement Analysis Failures

## Purpose

Recognize recurring behaviors that create avoidable scope, design, and delivery problems.

## When to use this

Use this during refinement, estimation, requirement review, or delivery retrospectives when the team feels aligned but later discovers rework, hidden scope, or acceptance conflict.

## How to apply

1. Match the current symptom to one failure pattern.
2. Name the decision or evidence that was missing.
3. Apply the linked correction before adding process or more meetings.
4. Keep the correction small enough to change the next requirement decision.

## Failure patterns

### Solution before problem

A requested feature is accepted without confirming the outcome. Restate the problem, affected user, and success evidence before comparing solutions.

### Hidden decision authority

Feedback is collected from many stakeholders, but no one owns the final decision. Name the accountable decision owner and consultation boundary.

### Implicit scope

Teams agree on included behavior but not exclusions, error paths, migration, or operations. Record boundaries and non-goals beside acceptance conditions.

### False precision

Dates or estimates are committed while assumptions remain unresolved. Use ranges, confidence, and explicit re-estimation triggers.

### Validation after implementation

The first credible user or technical evidence arrives after most cost is incurred. Validate the highest-impact uncertainty before committing full implementation.

### Change without impact analysis

A small wording change alters data, integration, testing, or delivery work. Trace changes through affected requirements, decisions, dependencies, and acceptance evidence.

## Example

A team commits to "support bulk upload" and later discovers file size, duplicate handling, permission checks, and failure reporting were all assumed differently. The useful correction is not a longer template; it is an explicit scope boundary, owner for unresolved rules, and acceptance evidence for one upload scenario.

## Review checklist

- [ ] The stated problem is separate from the proposed solution.
- [ ] Decision ownership and scope boundaries are explicit.
- [ ] Estimates expose assumptions and uncertainty.
- [ ] Material changes trigger impact analysis.
- [ ] Validation occurs before irreversible cost.

## Evidence to keep

Keep the failure pattern observed, the missing decision or evidence, the correction applied, and the trigger that would show the same failure is returning.
