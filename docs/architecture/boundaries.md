# Boundaries

## Decision supported

Place responsibility, data authority, and change ownership so that one business change does not create uncontrolled coordination across the system.

## Boundary evidence

Use observed signals:

- business invariants that need to change together;
- language and rules owned by the same domain experts;
- data requiring one authoritative writer;
- changes that repeatedly touch the same components;
- security, compliance, or operational ownership;
- different scaling or availability requirements.

Do not create a boundary solely from organization charts, database tables, or current technical layers.

## Decision guide

1. Identify the responsibility and decisions the boundary owns.
2. Place state and invariants with that responsibility.
3. Define what consumers may know and which changes remain internal.
4. Test the boundary against recent or expected business changes.
5. Choose process and deployment boundaries separately; logical ownership does not require a network call.

Keep responsibilities together when separating them would require coordinated writes, chatty interaction, or shared release decisions without an offsetting ownership benefit.

## Trade-offs

Strong boundaries reduce propagation of change but duplicate models and require explicit integration. Broad boundaries simplify transactions but increase contention and accidental coupling.

## Failure modes

- Splitting by nouns while business rules span every boundary.
- Claiming ownership while allowing direct writes to another boundary’s data.
- Distributing modules before logical dependencies are controlled.
- Treating every team boundary as permanent architecture.

## Review evidence

- [ ] Responsibility and authoritative state have one owner.
- [ ] Invariants do not require routine cross-boundary transactions.
- [ ] Consumer contracts hide internal change where intended.
- [ ] Deployment separation has evidence beyond conceptual neatness.
