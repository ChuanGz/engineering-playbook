# Architecture Principles

## Decision supported

Use durable reasoning to constrain structural choices without presenting preferences or named patterns as universally correct.

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
- Applying “loose coupling” without defining which change must be isolated.
- Keeping principles that conflict without priority or exception rules.
- Assessing compliance by diagram shape instead of change and runtime behavior.

## Review evidence

- [ ] Each principle names the failure or quality it protects.
- [ ] Applicability boundaries and costs are explicit.
- [ ] Multiple implementation options can satisfy it.
- [ ] Compliance can be observed or reviewed.
