# Scope Breakdown

## When to use this

Product owners and delivery teams use this guide to turn a broad outcome into smaller results that can be accepted, learned from, or released. Leaders can use the resulting slices to see what value is included now, what is deferred, and which dependency truly blocks progress.

Use this when an outcome is too large to estimate confidently, validate quickly, or release with clear acceptance evidence.

## Decision to make

Decide which slice should be built or validated next, what it includes, what it excludes, and which dependency genuinely blocks it.

## Why it matters

Poor slicing hides risk. A team may finish database, API, and UI tasks but still have no user-visible result, no acceptance decision, and no evidence that the core outcome works.

## How to apply

1. Start from the outcome and end-to-end user journey, not system components.
2. Separate mandatory behavior from policy variations and convenience features.
3. Identify business rules, data transitions, integrations, and operational needs.
4. Slice vertically so each increment produces observable value or learning.
5. Record dependencies and sequence only where one slice genuinely blocks another.
6. Define exclusions to prevent implied scope from returning during delivery.

## Decision guidance

Prefer a slice when it has one testable outcome, a clear owner, bounded dependencies, and an independent acceptance decision. Split again when estimation is dominated by unrelated uncertainties.

Do not split solely by technical layer. A database-only or API-only task may track implementation work, but it does not replace an outcome-oriented scope slice.

## Common failure

The team calls component work a slice: "database story", "API story", and "screen story". That can help task tracking, but it does not create an independently reviewable outcome.

## Example

“Database, service, and screen” are implementation tasks, not three useful delivery slices. A first vertical slice could let an authorized user view one known shipment status end to end. Later slices can add search, history, and exception handling with their own observable outcomes.

## Trade-offs

Smaller slices improve feedback and predictability but create coordination and release overhead. Keep slices large enough to produce meaningful evidence.

## Failure modes

- Renaming a component task as a user story.
- Hiding non-functional and operational work outside scope.
- Creating mandatory dependencies for work that could be validated independently.
- Removing difficult behavior without recording the resulting limitation.

## Review checklist

- [ ] Each slice has an observable outcome.
- [ ] Included and excluded behavior are explicit.
- [ ] Dependencies have technical or business justification.
- [ ] Cross-cutting security, data, and operational work is visible.

## Evidence to keep

Keep the selected next slice, its acceptance evidence, explicit exclusions, dependency decisions, and the signal that would justify expanding or changing scope.

## Maintenance trigger

Review this guide when slices repeatedly complete technical activity without producing an observable outcome, or when hidden dependencies return during delivery.
