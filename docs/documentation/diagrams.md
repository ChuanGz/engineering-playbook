# Diagrams

## Decision supported

Choose and maintain a visual model when spatial, structural, or sequential relationships are materially harder to understand in prose or a table.

A diagram is a decision aid, not decoration. Remove it when a short paragraph or table communicates the same relationship with less effort.

## Select the visual

- Use a context diagram for external actors, systems, and trust boundaries.
- Use a container or component view for ownership and dependencies at one declared level.
- Use a sequence diagram for time-ordered interaction and failure behavior.
- Use a state diagram for valid transitions and rejected events.
- Use a data-flow view for authority, transformation, storage, and sensitive-data movement.

Do not combine several abstraction levels in one diagram. State the question the visual answers and what it intentionally omits.

For concise playbook models:

- answer one explicit question;
- use no more than eight primary nodes, where a primary node represents an actor, state, decision, or responsibility in the model;
- label relationships with their meaning instead of using unexplained arrows;
- avoid decorative icons, emojis, technology logos, and color used only for emotion;
- do not rely on color alone to communicate meaning;
- prefer editable, versioned Mermaid source over generated image assets.

## Construction method

1. Define audience, decision, and abstraction level.
2. Include only elements required for that decision.
3. Label responsibilities and interaction meaning, not only technology names.
4. Show boundaries, direction, and authoritative state where relevant.
5. Model at least one important failure or alternate flow when runtime behavior matters.
6. Keep source editable, versioned, and reviewable with the affected system.
7. Confirm that a reader can explain the model without reading unrelated sections.

## Trade-offs

Diagrams compress relationships and improve shared review, but abstraction can hide runtime detail and become stale. Pair visuals with concise constraints and authoritative links.

## Failure modes

- Drawing a target architecture with no relation to current state or migration.
- Using arrows without interaction or ownership semantics.
- Presenting a framework-generated dependency graph as an architecture explanation.
- Updating prose while leaving the visual contradictory.
- Using a large model to display knowledge instead of clarifying one decision.
- Repeating the surrounding prose node by node without adding a relationship.

## Review evidence

- [ ] The diagram answers one explicit question at one abstraction level.
- [ ] The model contains no more than eight primary nodes.
- [ ] Boundaries, direction, and ownership are unambiguous.
- [ ] Omitted detail and assumptions are stated.
- [ ] The source and maintenance trigger are known.
