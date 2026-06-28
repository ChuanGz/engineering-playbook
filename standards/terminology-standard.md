# Terminology Standard

## Purpose

Use language that preserves responsibility and decision meaning across domains without manufacturing consensus around ambiguous jargon.

## Selection rules

- Prefer terms that name responsibility, behavior, state, or authority.
- Use one canonical term for one concept within a document set.
- Define terms whose common technical meanings could change the decision.
- Preserve domain language when it represents a real business distinction.
- Match established external contract terminology when compatibility requires it.
- Distinguish business concepts from similarly named implementation models.

## Classification rules

- A **principle** is a durable heuristic with boundaries and trade-offs.
- A **standard** is an enforceable requirement with acceptance evidence.
- A **recommendation** is a contextual default with exceptions.
- A **pattern** is a reusable solution shape, not a mandatory architecture.
- A **decision** selects among credible alternatives under explicit constraints.
- An **example** illustrates reasoning; it is not evidence unless it comes from the stated context.

## Resolve terminology conflict

1. Identify the decision or behavior affected by competing terms.
2. Prefer the term used by the authoritative domain or contract owner.
3. Record aliases only when readers must map existing language.
4. Update related indexes and links in the same change.
5. Avoid global renaming when local context legitimately differs.

## Reject or revise

- Responsibility-free labels such as manager, helper, engine, or common without a specific owned outcome.
- Trend terms used as quality claims.
- Multiple terms used interchangeably when they imply different authority or lifecycle.
- Definitions that merely repeat the term.

## Acceptance evidence

- [ ] Important terms identify distinct concepts or responsibilities.
- [ ] Overloaded terms are defined where readers encounter them.
- [ ] Contract and domain-owner language takes precedence over preference.
- [ ] Terminology changes preserve link and navigation consistency.

## Maintenance trigger

Review terminology when a domain model, public contract, ownership boundary, or authoritative external standard changes.
