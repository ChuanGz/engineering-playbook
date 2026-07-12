# Architecture Principles

## Decision supported

Use durable reasoning to constrain structural choices without presenting preferences or named patterns as universally correct.

## When to use this

Use this when defining, reviewing, or retiring architecture principles that guide multiple designs or teams.

## Decision to make

Decide whether a statement is a real principle, a context-specific decision, or a technology preference being promoted without enough evidence.

## Principle test

Treat guidance as an architecture principle only when it:

- protects a named quality or reduces a recurring failure;
- applies across more than one implementation choice;
- states where it does not apply;
- exposes its cost and conflicting qualities;
- can be tested through design or runtime evidence.

For example, “keep authoritative business rules behind one ownership boundary” protects consistency and change control. “Use microservices” is a solution choice, not a principle.

## Applying a principle

1. Name the design pressure and evidence.
2. Identify the quality the principle protects.
3. Compare compliant options rather than jumping to one pattern.
4. Record exceptions where another quality has higher priority.
5. Define evidence that the resulting structure still serves the principle.

## Trade-offs

Principles increase consistency and review speed, but too many constrain local judgment and preserve obsolete assumptions. Keep the set small and retire principles whose protected risk no longer exists.

## Failure modes

- Renaming a preferred technology as a principle.
- Applying “loose coupling” without defining which change needs to be isolated.
- Keeping principles that conflict without priority or exception rules.
- Assessing compliance by diagram shape instead of change and runtime behavior.

## Example

Weak principle: "Use event-driven architecture." Better principle: "Do not let one boundary write another boundary's authoritative state; use events only after the owning boundary has made a durable decision."

## Evidence to keep

- [ ] Each principle names the failure or quality it protects.
- [ ] Applicability boundaries and costs are explicit.
- [ ] Multiple implementation options can satisfy it.
- [ ] Compliance can be observed or reviewed.
