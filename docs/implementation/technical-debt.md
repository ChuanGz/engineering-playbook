# Technical Debt

## Decision supported

Choose when to accept, reduce, or retire an engineering liability based on its effect on delivery, reliability, security, and operating cost.

## When to use this

Use this when a known engineering liability affects delivery speed, defect risk, operational recovery, security exposure, or cost. Do not use it to prioritize disliked code without consequence evidence.

## Decision to make

Decide whether to remediate now, contain the risk, attach remediation to nearby work, accept the debt temporarily, or close it because the consequence no longer exists.

## Debt record

Record a debt item only when it contains:

- the constrained behavior or engineering decision;
- evidence of current or expected impact;
- affected changes, systems, or owners;
- risk of deferral and cost of remediation;
- trigger, priority, and accountable owner.

Outdated style, disliked code, and missing ideal abstractions are not debt without a consequential impact.

## Decision guide

1. Quantify impact using rework, incidents, lead time, exposure, or blocked outcomes.
2. Compare remediation with containment and deliberate acceptance.
3. Fix immediately when exposure is unacceptable or every nearby change compounds cost.
4. Attach bounded remediation to planned work when context and tests are already active.
5. Accept explicitly when remediation costs more than the remaining risk.
6. Close items whose impact no longer exists.

## Trade-offs

Dedicated remediation can restore structural capacity but delays visible outcomes. Opportunistic improvement lowers coordination cost but may never address cross-cutting debt.

## Failure modes

- Using “technical debt” to obtain priority without impact evidence.
- Maintaining a backlog with no owner or decision trigger.
- Rewriting a subsystem when containment would reduce the actual risk.
- Paying low-impact cleanup while high-impact operational debt remains.

## Example

Weak debt item: "Refactor old reporting code." Better debt item: "Monthly report changes require coordinated edits in four modules and caused two reconciliation defects; contain by adding contract tests now, then remove duplicated mapping when the next report change touches the area."

## Evidence to keep

- [ ] The item names a real consequence, not aesthetic discomfort.
- [ ] Remediation, containment, and acceptance were compared.
- [ ] Priority reflects impact and compounding cost.
- [ ] Ownership and closure conditions are explicit.
