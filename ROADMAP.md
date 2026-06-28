# Roadmap

The roadmap advances by evidence and quality, not file count or elapsed time. Each milestone represents roughly two months of focused work, but completion requires its exit criteria.

## Milestone 1 — Foundation and core engineering standards

### Outcome

Establish the minimum useful engineering handbook: substantive domain guidance, enforceable content standards, purpose-specific templates, contribution governance, and automated documentation hygiene.

### Scope

- Requirement analysis
- System design
- Software architecture
- Implementation
- Testing
- Code review
- Delivery
- Documentation
- Repository standards and document contract
- Engineering decision and review templates
- OSS governance and automated Markdown and link checks

### Exit criteria

M1 is complete only when all criteria are supported by repository evidence:

- [x] Each of the eight domains has an index and a minimum substantive guide set.
- [x] Domain guides support real decisions and include applicability, trade-offs, failure modes, and review evidence where relevant.
- [x] No domain is represented only by placeholders, generic advice, or empty taxonomy.
- [x] The document contract defines reader, problem, outcome, evidence, type, scope, and ownership.
- [x] Writing, content quality, terminology, decision-record, and contribution-review standards have enforceable acceptance criteria.
- [x] Every template has a distinct decision purpose, domain-specific evidence, ownership, and pass conditions.
- [x] Contribution, conduct, governance, security, changelog, license, and GitHub community files are present.
- [x] Root and domain navigation resolve to existing content.
- [x] Repository-wide Markdown lint and internal-link validation pass.
- [x] GitHub Actions validates Markdown successfully on the default branch.
- [x] A senior-quality audit finds no critical generic-content, duplication, or unsupported-standard gap.

### Non-goals

- Exhaustive coverage of every engineering specialty.
- Technology- or framework-specific implementation tutorials.
- Real-case examples without validated source context.
- Maturity claims based only on structure, formatting, or automation.

## Milestone 2 — High-value senior engineering practices

### Outcome

Deepen the decisions senior engineers make before and around implementation using evidence from real delivery contexts.

### Focus

- requirement clarification and ambiguity management;
- gap, impact, traceability, and change analysis;
- estimation and scope-reduction decisions;
- risk assessment and trade-off analysis;
- architecture and design reviews;
- engineering failure patterns and decision quality.

### Entry condition

M1 exit criteria remain satisfied and proposed content has real project evidence or an explicitly bounded framework.

## Milestone 3 — Maturity, feedback, and governance

### Outcome

Make the playbook measurably consistent, maintainable, and responsive to contribution and usage evidence.

### Focus

- cross-domain consistency and terminology audits;
- contribution feedback and quality-gate refinement;
- maturity assessment with observable evidence;
- governance and exception handling;
- ownership, maintenance triggers, and stale-content removal;
- stronger review and audit practices.

## Milestone 4 — Practical real-case playbooks

### Outcome

Demonstrate engineering judgment using sanitized, evidence-backed cases rather than fictional stories presented as experience.

### Focus

- requirement and estimation decisions;
- scope reduction and delivery-risk decisions;
- architecture and integration decisions;
- code review and incident learning;
- technical leadership and organizational change.

### Evidence requirement

Each case must state source context, constraints, decisions, consequences, anonymization boundaries, and lessons that transfer without inventing facts.
