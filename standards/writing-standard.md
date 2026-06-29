# Writing Standard

## Purpose

Make engineering guidance understandable to its intended reader without using polished language to hide weak reasoning.

## Required rules

- Write in concise, plain US English for a named audience and knowledge level.
- Lead sections with the outcome, decision, or question they support.
- Prefer responsibility and observable behavior over abstract labels.
- Define uncommon, overloaded, and domain-specific terms where readers first need them.
- State assumptions, uncertainty, and non-goals directly.
- Use active voice when ownership matters.
- Keep headings descriptive enough to support scanning and linking.
- Use code, tables, lists, and diagrams only when they improve the reader’s task.

## Examples and working maxims

- Label a fictional or compressed case as **Simplified example** and state the decision it illustrates.
- Keep the example shorter than the reasoning it supports. An example is not project evidence.
- Use at most one original working maxim on a page. Place it beside the reasoning it summarizes.
- Do not use a maxim as proof, invent an attribution, or add a quotation only for motivation.
- Remove examples and maxims that make a page more memorable but do not improve a decision or action.

## Progressive depth

When a document serves readers with different expertise, present information in this order:

1. **Understand:** explain the problem, why it matters, the consequence, and who owns the decision.
2. **Apply:** give the smallest useful action, input, output, or verification step.
3. **Deep dive:** provide technical reasoning, alternatives, trade-offs, and failure handling.

Do not repeat all three labels in every guide. Use the progression only when it helps readers stop at the depth they need.

Prefer a plain-language explanation before an acronym or framework term. Preserve a precise technical term when simplifying it would change the decision.

## Contextual rules

- Use `must` only for safety, compliance, an accepted contract, or another necessary condition with a visible enforcement owner or mechanism.
- Use `should` for a recommendation with strong default reasoning and state exceptions.
- Use `may` for a valid option, not to avoid making a decision.
- Describe a reversible improvement as an experiment when its value has not been validated in that context.
- Label fictional scenarios; never present them as project evidence.
- Preserve precise technical terms when simpler wording would change meaning.

## Reject or revise

- “Best practice” without applicability and evidence.
- Claims such as scalable, secure, simple, or production-ready without observable criteria.
- Readability scores used as a substitute for observing whether intended readers can find, explain, and apply the guidance.
- Introductory prose that repeats the title without adding context.
- Lists whose items mix different abstraction levels or ownership.
- Examples that are longer than the decision they clarify.
- Decorative quotations, slogans, emojis, icons, or technology logos.
- Buzzwords that do not name an observable behavior, responsibility, or consequence.

## Acceptance evidence

- [ ] The intended reader and next action are clear.
- [ ] A reader can find the relevant outcome without reading the document from beginning to end.
- [ ] Mandatory rules, recommendations, and options are distinguishable.
- [ ] Terms and claims have one unambiguous meaning in context.
- [ ] Examples and maxims expose judgment without pretending to be evidence.
- [ ] Removing decorative prose would not expose missing reasoning.

## Maintenance trigger

Review this standard when recurring contribution feedback reveals ambiguity, inaccessible language, or terminology conflict not covered here.
