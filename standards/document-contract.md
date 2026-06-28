# Document Contract

## Purpose

Prevent context-free, low-value, or unmaintainable documents from entering the playbook.

## Required contract

Before creating a document, identify:

- **Reader:** the role and knowledge level expected.
- **Problem:** the concrete task, decision, contract, or failure the document addresses.
- **Outcome:** what the reader can do or decide afterward.
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

Include when relevant:

- decision drivers and credible alternatives;
- applicability and non-applicability conditions;
- positive and negative consequences;
- failure modes and recovery ownership;
- validation evidence and reconsideration triggers.

Not every document needs identical headings. Structure follows reader outcome, not a universal skeleton.

## Acceptance evidence

- [ ] A named reader can demonstrate the intended task or decision.
- [ ] Material claims trace to evidence or labeled assumptions.
- [ ] Principles, recommendations, opinions, and mandatory rules are classified honestly.
- [ ] The document adds distinct value and has a maintenance trigger.
