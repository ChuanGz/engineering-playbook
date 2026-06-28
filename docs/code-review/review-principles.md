# Review Principles

## Decision supported

Decide whether a change is safe and understandable enough to merge, and identify the smallest action needed when it is not.

## Principles

### Review risk before style

Prioritize incorrect outcomes, data loss, security exposure, compatibility, recovery, and future change cost. Delegate deterministic formatting and simple conventions to automation.

### Require evidence proportional to consequence

A reversible internal cleanup needs less proof than a schema migration, authorization change, or irreversible state transition.

### Comment on the change, not the author

State the observed risk, why it matters, and what evidence or outcome would resolve it. Questions are useful when information is missing; they should not disguise a required correction.

### Keep decision ownership explicit

The author owns the change. Reviewers own the quality of their findings. The designated maintainer or accountable owner resolves material disagreement.

## Trade-offs

Deep review reduces escaped risk but increases lead time and context switching. Apply depth to high-consequence or hard-to-reverse changes rather than reviewing every line equally.

## Failure modes

- Approving because checks pass without inspecting what they cover.
- Blocking on personal preference with no named impact.
- Expanding scope through unrelated redesign requests.
- Leaving ambiguous comments such as “clean this up” without a pass condition.

## Review evidence

- [ ] Blocking comments identify a concrete risk or unmet requirement.
- [ ] Suggestions and preferences are not presented as mandatory standards.
- [ ] Automated evidence is interpreted, not merely present.
- [ ] The final disposition of material findings is visible.
