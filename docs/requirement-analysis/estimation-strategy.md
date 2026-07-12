# Estimation Strategy

## Purpose

Support delivery decisions with an estimate whose scope, assumptions, uncertainty, and confidence are visible.

## When to use this

Use this when an estimate will influence prioritization, staffing, sequencing, budget, external commitment, or release planning. Do not spend estimation effort when no decision will change.

## Decision to make

Decide what level of effort, range, confidence, and uncertainty is honest enough for the decision being made.

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

## Example

Weak estimate: "This is five days." Better estimate: "Three to seven days if the existing API contract holds; add two to four days if the provider cannot support partial updates. Confidence is medium until contract behavior is verified." The better estimate helps a delivery decision because it exposes the assumption and re-estimation trigger.

## Evidence to keep

- [ ] Scope and assumptions accompany the estimate.
- [ ] Unknowns and external dependencies are visible.
- [ ] Range and confidence match available evidence.
- [ ] Re-estimation triggers are defined.

## Maintenance trigger

Review this guide when estimates repeatedly miss because scope, assumptions, external dependencies, or confidence were hidden.
