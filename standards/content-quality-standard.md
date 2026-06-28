# Content Quality Standard

## Purpose

Prevent generic, unsupported, or professionally worded filler from being accepted as engineering guidance.

## Evidence requirement

Ground material claims in the strongest available source:

1. Current repository, system, workflow, or production behavior.
2. Actual measurements, incidents, experiments, reviews, or delivery outcomes.
3. Accepted requirements, constraints, and decisions.
4. Authoritative primary references or established standards.
5. Transferable reasoning with assumptions explicitly labeled.

Do not invent project detail when stronger evidence is unavailable. Publish a bounded framework or identify the evidence gap instead.

## Decision-value requirement

Every document must enable at least one of these outcomes:

- complete a real engineering task;
- make or review a consequential decision;
- apply or verify a contract;
- prevent, detect, or recover from a named failure;
- understand a system behavior necessary for safe change.

## Required reasoning

Include applicability, non-applicability, alternatives, negative consequences, failure modes, and validation when they can change the decision. Do not force identical headings when a document type does not need them.

## Reject or revise

- Advice that can be copied unchanged into nearly any repository.
- Pattern or framework summaries without a problem and credible alternative.
- Personal preference presented as principle or standard.
- Checklists without observable pass conditions.
- Repeated skeletons whose sections contain no domain-specific judgment.
- Claims of maturity based only on file count, format, lint, or tooling.

## Acceptance evidence

- [ ] The problem and affected reader are concrete.
- [ ] Material claims trace to evidence or labeled assumptions.
- [ ] Guidance changes a task, decision, or risk response.
- [ ] Trade-offs include meaningful negative consequences.
- [ ] Remaining domain or senior-review gaps are visible.

## Maintenance trigger

Review content when its evidence, system behavior, ownership, accepted decision, or intended reader changes.
