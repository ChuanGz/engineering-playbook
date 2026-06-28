# Scope Breakdown

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
