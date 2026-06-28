# API Boundaries

## Decision supported

Place a service or module contract where ownership, business responsibility, and change can be controlled without creating unnecessary distribution.

## Boundary drivers

Evaluate:

- business capability and invariant ownership;
- data authority and consistency requirements;
- caller needs and expected change patterns;
- team ownership and operational responsibility;
- security and trust boundaries;
- latency, availability, and failure coupling.

A boundary is justified by responsibility and change control. Reusing an entity name or creating an interface is not sufficient evidence.

## Contract design

1. Express operations in domain outcomes, not internal table operations.
2. Define request, response, error, idempotency, authorization, and compatibility behavior.
3. Keep the authoritative state and its invariants behind one ownership boundary.
4. Expose only information callers need to make their own decision.
5. Record versioning and retirement expectations before independent consumers depend on the contract.

Keep the boundary in-process when independent deployment, scaling, trust, or ownership does not justify network and operational cost.

## Trade-offs

Stronger boundaries reduce accidental coupling but duplicate some models and mapping. Shared models reduce short-term effort but allow provider changes to propagate into consumers.

## Failure modes

- Splitting services by database table or technical layer.
- Creating chatty contracts that require callers to reconstruct provider rules.
- Returning internal exceptions or persistence models.
- Claiming independence while sharing schema ownership or coordinated releases.

## Review evidence

- [ ] The boundary has one accountable business and operational owner.
- [ ] State authority and consistency expectations are explicit.
- [ ] Failure, idempotency, compatibility, and authorization behavior are defined.
- [ ] Distribution cost is justified against an in-process alternative.
