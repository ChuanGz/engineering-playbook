# Estimation Strategy

## Purpose

Support delivery decisions with an estimate whose scope, assumptions, uncertainty, and confidence are visible.

## Inputs

Estimate only after identifying the outcome, scope boundary, acceptance conditions, dependencies, implementation constraints, and major unknowns. An estimate without these inputs is a guess presented with unjustified precision.

## Decision guide

1. Break work into outcome-oriented slices and enabling work.
2. Separate known work, discovery work, external dependencies, and risk contingency.
3. Use ranges when uncertainty can materially change effort.
4. State assumptions and the evidence supporting them.
5. Assign a confidence level and explain what would change it.
6. Re-estimate when scope or a material assumption changes; preserve the previous estimate for learning.

Use relative estimation for prioritization among comparable work. Use time ranges for capacity and delivery commitments. Do not convert points mechanically into dates.

## Trade-offs

Detailed estimation improves shared understanding but has diminishing returns. Invest more when decisions are costly, commitments are external, or work is difficult to reverse.

## Failure modes

- Treating the estimate as a promise.
- Padding numbers instead of exposing uncertainty.
- Omitting review, testing, deployment, migration, and operational work.
- Reporting one number while material unknowns remain.

## Review checklist

- [ ] Scope and assumptions accompany the estimate.
- [ ] Unknowns and external dependencies are visible.
- [ ] Range and confidence match available evidence.
- [ ] Re-estimation triggers are defined.
