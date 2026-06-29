# Ambiguity Detection

## At a glance

Product owners, developers, reviewers, and affected business owners use this guide when one statement could lead to different outcomes. The smallest useful action is to show two plausible interpretations, name who can decide, and record the observable behavior that distinguishes them.

## Purpose

Find statements that reasonable readers can interpret differently before those differences become design or delivery failures.

## Signals

Look for subjective terms such as *fast*, *simple*, *secure*, *real time*, *user friendly*, *large*, or *as needed*. Also challenge missing actors, undefined states, hidden time boundaries, broad quantifiers, and unclear ownership.

## Decision guide

For each ambiguous statement:

1. Ask which observable behavior would prove it true.
2. Provide two plausible interpretations to expose the decision.
3. Quantify thresholds, time windows, volumes, and error tolerance where they affect design.
4. Name the actor authorized to resolve the ambiguity.
5. Record the chosen interpretation and rejected alternatives.

Do not force precision that has no effect on implementation, risk, or acceptance. Record low-impact uncertainty instead.

## Simplified example

“Update status in real time” may mean within one second without refresh or visible on the next normal refresh. Replace the phrase with the affected user action, an observable delay range, operating conditions, and the owner who can accept that behavior. Label an unmeasured threshold as an assumption.

## Trade-offs

Precision improves alignment but can create false certainty when evidence is weak. Prefer bounded assumptions and planned validation over invented numbers.

## Failure modes

- Replacing one vague term with another.
- Assuming familiar domain language has one shared meaning.
- Resolving ambiguity privately without updating the source requirement.
- Treating every unanswered question as an implementation blocker.

## Review checklist

- [ ] Actors, states, triggers, and expected outcomes are named.
- [ ] Quality expectations use observable thresholds.
- [ ] Material interpretations have an explicit decision owner.
- [ ] Remaining uncertainty is visible and intentionally accepted.

## Maintenance trigger

Review this guide when requirement reviews repeatedly miss a class of ambiguity that later causes rework, acceptance conflict, or delivery failure.
