# Diagrams

## Decision supported

Choose and maintain a visual model when spatial, structural, or sequential relationships are materially harder to understand in prose or a table.

## Select the visual

- Use a context diagram for external actors, systems, and trust boundaries.
- Use a container or component view for ownership and dependencies at one declared level.
- Use a sequence diagram for time-ordered interaction and failure behavior.
- Use a state diagram for valid transitions and rejected events.
- Use a data-flow view for authority, transformation, storage, and sensitive-data movement.

Do not combine several abstraction levels in one diagram. State the question the visual answers and what it intentionally omits.

## Construction method

1. Define audience, decision, and abstraction level.
2. Include only elements required for that decision.
3. Label responsibilities and interaction meaning, not only technology names.
4. Show boundaries, direction, and authoritative state where relevant.
5. Model at least one important failure or alternate flow when runtime behavior matters.
6. Keep source editable, versioned, and reviewable with the affected system.

## Trade-offs

Diagrams compress relationships and improve shared review, but abstraction can hide runtime detail and become stale. Pair visuals with concise constraints and authoritative links.

## Failure modes

- Drawing a target architecture with no relation to current state or migration.
- Using arrows without interaction or ownership semantics.
- Presenting a framework-generated dependency graph as an architecture explanation.
- Updating prose while leaving the visual contradictory.

## Review evidence

- [ ] The diagram answers one explicit question at one abstraction level.
- [ ] Boundaries, direction, and ownership are unambiguous.
- [ ] Omitted detail and assumptions are stated.
- [ ] The source and maintenance trigger are known.
