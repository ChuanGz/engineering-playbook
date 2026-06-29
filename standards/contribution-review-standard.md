# Contribution Review Standard

## Purpose

Help contributors turn observations, decisions, and lessons into durable engineering value while preventing unsupported or duplicated guidance from becoming authoritative.

## Review order

1. **Scope:** Does the contribution solve a problem owned by this playbook?
2. **Document contract:** Are reader, problem, outcome, evidence, type, scope, and ownership clear?
3. **Engineering quality:** Are claims correct, contextual, and supported by meaningful trade-offs?
4. **Distinct value:** Does it improve an existing document or justify a new artifact?
5. **Operational truth:** Does it account for ownership, failure, maintenance, and feedback where relevant?
6. **Learning value:** If it reports an outcome or experiment, are system conditions, evidence, uncertainty, and the next learning decision visible?
7. **Editorial consistency:** Do structure, terminology, links, and Markdown meet standards?

Do not spend editorial effort polishing content that fails scope or engineering-quality gates.

## Finding classification

- **Blocking:** incorrect guidance, unsupported standard, duplicated authority, hidden material risk, or missing required evidence.
- **Follow-up:** bounded improvement that does not invalidate current guidance.
- **Suggestion:** optional clarity or usability improvement.
- **Preference:** personal choice with no demonstrated quality impact; never a merge blocker.

## Learning contributions

Accept a failed experiment or poor outcome when it:

- distinguishes intended and observed results;
- uses available evidence and labels hypotheses;
- describes system conditions instead of blaming an individual;
- protects confidential, personal, customer, security, and commercial information;
- records what should be kept, adapted, stopped, escalated, or tried next.

No-blame language does not remove accountability for material decisions, required reporting, or owned corrective work.

## Decline or redirect

Decline, redirect, or request revision when contributions:

- add noise, unsupported opinion, promotion, or unrelated debate;
- copy textbook or generated summaries without real decision value;
- increase structure or process without a concrete problem;
- duplicate guidance instead of improving its authoritative source;
- invent project experience or present assumptions as evidence;
- attack individuals or turn technical disagreement into personal conflict;
- remain unmaintainable after requested evidence and ownership are absent.

## Acceptance evidence

- [ ] The contribution satisfies the document contract.
- [ ] Review findings identify concrete risks and pass conditions.
- [ ] Mandatory changes derive from repository standards, not reviewer preference.
- [ ] New files have unique reader value and maintenance ownership.
- [ ] Learning contributions protect people while preserving decision accountability.
- [ ] Automated checks pass after substantive review succeeds.

## Maintenance trigger

Review this standard when recurring low-quality submissions bypass current gates or legitimate contributions are rejected for rules that no longer protect repository quality.
