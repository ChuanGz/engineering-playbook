# Engineering Domains

Use [Ways of Working](ways-of-working/README.md) if you want to start from a role, delivery moment, or practical journey. Use this index when you already know the engineering decision you need to make or review.

Leaders applying the playbook across teams can start with [Scaling Without Bureaucracy](ways-of-working/scaling-without-bureaucracy.md).

These domains are the authoritative sources. Scrum, Kanban, continuous flow, hybrid delivery paths, and role-based paths link here rather than copying the guidance.

## Domain focus

This playbook focuses on durable decision domains, not technology-specific recipes. A topic belongs here when it helps a reader make or review a consequential engineering decision across more than one stack, project, or delivery framework.

| In scope | Out of scope |
| --- | --- |
| Outcome, scope, trade-off, boundary, evidence, risk, release, documentation, and learning decisions. | Framework tutorials, tool setup, package defaults, generated project structure, and runtime-specific implementation contracts. |
| Guidance that names the decision, consequence, owner, evidence, and review questions. | Generic best-practice lists, pattern catalogs without context, and personal preference presented as policy. |
| Examples that make a decision easier to understand and are clearly bounded. | Fictional examples presented as real evidence or broad claims without source context. |

## How to use the domains

Start with the domain that owns the current decision. Use the guide to answer four questions before moving elsewhere:

1. What decision is being made?
2. What consequence or failure risk makes it matter?
3. Who owns the decision or accepts the residual risk?
4. What evidence would make the decision reviewable?

## SDLC activity map

The map below is not a mandatory process. It shows where the same engineering decisions tend to appear across Scrum, Kanban, continuous flow, or hybrid delivery.

| SDLC activity | Practical decision | Likely readers | Authoritative source | Evidence to keep |
| --- | --- | --- | --- | --- |
| Frame | Is the problem worth investigating, and what outcome matters? | Product, engineering, leadership, business | [Problem framing](system-design/problem-framing.md) | Outcome, affected people, constraints, assumptions, decision owner |
| Clarify | Can reasonable readers agree on success, failure, and boundaries? | Product, developers, reviewers | [Requirement analysis](requirement-analysis/README.md) | Examples, acceptance evidence, exclusions, open questions |
| Slice | What is the smallest end-to-end result that can produce value or learning? | Product, developers, delivery leads | [Scope breakdown](requirement-analysis/scope-breakdown.md) | Included outcome, excluded work, dependencies, validation signal |
| Decide | Which design option fits the constraints and accepted consequences? | Developers, architects, leaders, business owners | [System design](system-design/README.md) and [architecture](architecture/README.md) | Drivers, alternatives, trade-offs, owner, reconsideration trigger |
| Build | What code behavior, boundary, and failure handling need to stay clear? | Developers, reviewers | [Implementation](implementation/README.md) | Tests, code organization, failure behavior, accepted technical debt |
| Review | Is the change safe and understandable enough to merge? | Developers, reviewers, maintainers | [Code review](code-review/README.md) | Review findings, test evidence, unresolved risk disposition |
| Test | Which failure risks need credible evidence? | Developers, QA, reviewers, delivery leads | [Testing](testing/README.md) | Risk-to-test mapping, automation evidence, known gaps |
| Release | How will exposure be limited, observed, and accepted? | Developers, delivery leads, operations, business owners | [Delivery](delivery/README.md) | Release decision, rollout plan, quality gates, owner |
| Recover | How will harmful change be stopped, reversed, repaired, or reconciled? | Developers, operations, leaders, business owners | [Rollback and recovery](delivery/rollback-and-recovery.md) | Recovery path, signals, authority, data reconciliation plan |
| Learn | What condition should change after the outcome is observed? | Team, leaders, product, operations | [Learning from outcomes](ways-of-working/learning-from-outcomes.md) | Observed outcome, system condition, experiment, owner, review date |

| Domain | Decision focus |
| --- | --- |
| [Capability foundations](foundations/capability.md) | Understand how knowledge, skills, experience, mindset, and practice combine into capability and measurable impact. |
| [Requirement analysis](requirement-analysis/README.md) | Clarify outcomes, scope, evidence, estimates, and readiness before implementation. |
| [System design](system-design/README.md) | Translate constraints and quality scenarios into testable system decisions. |
| [Software architecture](architecture/README.md) | Control structural ownership, dependency direction, integration, and evolution. |
| [Implementation](implementation/README.md) | Preserve correctness, failure behavior, and safe change in production code. |
| [Testing](testing/README.md) | Map consequential failure risks to credible evidence. |
| [Code review](code-review/README.md) | Decide whether a specific change is safe and understandable enough to merge. |
| [Delivery](delivery/README.md) | Release traceable artifacts with explicit risk, rollout, and recovery controls. |
| [Documentation](documentation/README.md) | Preserve the tasks, contracts, decisions, and recovery knowledge worth maintaining. |
| [Ways of working](ways-of-working/README.md) | Connect these decisions across real delivery situations and learning loops. |

Start with the domain that owns the current decision. Follow cross-domain links only when the change introduces those concerns; the playbook is not a mandatory sequential process.
