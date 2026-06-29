# Document Contract

## Purpose

Prevent context-free, low-value, or unmaintainable documents from entering the playbook.

## Required contract

Before creating a document, identify:

- **Primary reader:** the role, existing knowledge, and situation in which they will use the document.
- **Secondary reader:** any role that needs to understand the summary, consequence, or handoff without applying the technical detail.
- **Problem:** the concrete task, decision, contract, or failure the document addresses.
- **Outcome:** the action, decision, or observable explanation the primary reader can provide afterward.
- **Evidence:** repository behavior, production observation, accepted requirement, decision, or primary reference supporting the content.
- **Type:** tutorial, how-to guide, reference, or explanation.
- **Scope:** included concerns, non-goals, and known assumptions.
- **Ownership:** the maintainer or change event responsible for keeping it current.

If evidence is unavailable, label the content as a bounded framework or draft. Do not manufacture project context.

## Creation gate

A new file is justified only when it serves a reader need that an existing document cannot satisfy without mixing purposes or ownership.

Do not create:

- placeholder files or empty folders;
- generic best-practice summaries;
- duplicated indexes or copied source-of-truth data;
- pattern catalogs without a decision context;
- checklists whose items have no observable pass condition.

## Content contract

Classify material guidance honestly:

- A **durable principle** is a decision heuristic that remains useful across contexts. State its limit and cost.
- A **contextual recommendation** is preferred under named conditions. State when an alternative is more appropriate.
- An **enforceable rule** protects safety, compliance, an accepted contract, or another necessary condition with a visible enforcement owner or mechanism.
- An **example** illustrates judgment in a bounded context. It is not evidence that the same choice works elsewhere.
- An **experiment** is a reversible change with an expected signal and a review point. It is not policy.

Do not promote a recommendation, example, or experiment into a universal rule.

Use progressive depth when readers have different levels of expertise:

1. Explain the problem, value, consequence, and owner in plain language.
2. Give the smallest useful action or decision path.
3. Add alternatives, trade-offs, failure modes, and specialist detail.

The first layer should be understandable to a secondary reader who owns the outcome or risk. The deep-dive layer may assume the technical knowledge needed to apply it.

Include when relevant:

- decision drivers and credible alternatives;
- applicability and non-applicability conditions;
- positive and negative consequences;
- failure modes and recovery ownership;
- validation evidence and reconsideration triggers.
- stable links to authoritative guidance and any superseding decision.

Not every document needs identical headings. Structure follows reader outcome, not a universal skeleton.

## Acceptance evidence

- [ ] A named reader can demonstrate the intended task or decision.
- [ ] A secondary reader can identify the consequence and accountable owner without reading unnecessary implementation detail.
- [ ] Material claims trace to evidence or labeled assumptions.
- [ ] Principles, recommendations, opinions, and mandatory rules are classified honestly.
- [ ] The document adds distinct value and has a maintenance trigger.
