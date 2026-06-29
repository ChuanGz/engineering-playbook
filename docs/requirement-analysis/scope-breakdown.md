# Scope Breakdown

## At a glance

Product owners and delivery teams use this guide to turn a broad outcome into smaller results that can be accepted, learned from, or released. Leaders can use the resulting slices to see what value is included now, what is deferred, and which dependency truly blocks progress.

## Purpose

Turn a broad outcome into coherent delivery slices that can be estimated, validated, and released independently where practical.

## Breakdown method

1. Start from the outcome and end-to-end user journey, not system components.
2. Separate mandatory behavior from policy variations and convenience features.
3. Identify business rules, data transitions, integrations, and operational needs.
4. Slice vertically so each increment produces observable value or learning.
5. Record dependencies and sequence only where one slice genuinely blocks another.
6. Define exclusions to prevent implied scope from returning during delivery.

## Decision guidance

Prefer a slice when it has one testable outcome, a clear owner, bounded dependencies, and an independent acceptance decision. Split again when estimation is dominated by unrelated uncertainties.

Do not split solely by technical layer. A database-only or API-only task may track implementation work, but it does not replace an outcome-oriented scope slice.

## Simplified example

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

## Maintenance trigger

Review this guide when slices repeatedly complete technical activity without producing an observable outcome, or when hidden dependencies return during delivery.
