# Content Accessibility and Durability Audit

## Audit result: PARTIAL

This audit covers all 61 Markdown files under `docs/` after the workflow-first navigation, visual senior-learning path, enterprise scaling guide, three pilot journeys, and practical writing contract were implemented. The repository structure, SDLC activity map, and adapted guide entry points are ready for reader validation. The result remains `PARTIAL` because no real technical, product, or leadership usability review is recorded.

Passing lint, links, or a structural checklist is not evidence that a reader can understand or apply the content.

## Classification rules

- **Keep:** currently has distinct decision value, a usable entry point, and a maintenance trigger or navigation purpose. Keep does not mean frozen.
- **Adapt:** substantive and technically useful, but needs a clearer reader entry, progressive depth, role consequence, or maintenance trigger.
- **Rewrite:** reasoning is too generic, unsupported, or misleading to preserve as the base.
- **Merge/Remove:** duplicates another authority or no longer serves a distinct reader decision.

## Complete inventory

| Area | Keep | Adapt | Rewrite | Merge/Remove |
| --- | --- | --- | --- | --- |
| Cross-domain index | `docs/README.md` | — | — | — |
| Ways of working | `README.md`, `delivery-flow.md`, `learning-from-outcomes.md`, `scaling-without-bureaucracy.md` | — | — | — |
| Requirement analysis | `ambiguity-detection.md`, `scope-breakdown.md`, `validation-before-implementation.md` | `README.md`, `common-failures.md`, `estimation-strategy.md`, `requirement-review-checklist.md` | — | — |
| System design | `design-review.md`, `problem-framing.md`, `trade-off-analysis.md` | `README.md`, `api-boundaries.md`, `capacity-estimation.md`, `data-flow.md` | — | — |
| Architecture | — | `README.md`, `architecture-decisions.md`, `architecture-evolution.md`, `architecture-principles.md`, `boundaries.md`, `integration-patterns.md`, `modularity.md` | — | — |
| Implementation | — | `README.md`, `api-design.md`, `code-organization.md`, `coding-principles.md`, `error-handling.md`, `maintainability.md`, `refactoring.md`, `technical-debt.md` | — | — |
| Testing | `test-strategy.md` | `README.md`, `contract-testing.md`, `integration-testing.md`, `test-automation.md`, `testing-principles.md`, `unit-testing.md` | — | — |
| Code review | — | `README.md`, `correctness-review.md`, `design-review.md`, `review-checklist.md`, `review-principles.md`, `review-scope.md`, `test-review.md` | — | — |
| Delivery | `delivery-risk.md`, `rollback-and-recovery.md` | `README.md`, `ci-cd-principles.md`, `git-workflow.md`, `quality-gates.md`, `release-readiness.md` | — | — |
| Documentation | — | `README.md`, `decision-records.md`, `diagrams.md`, `documentation-principles.md`, `documentation-review.md`, `readme-standard.md` | — | — |
| **Total** | **14** | **47** | **0** | **0** |

The audit found no guide that currently requires a full rewrite or removal. Existing guides have domain-specific decision value; most need adaptation to the newer accessibility and durability contract. A future evidence-based review may change these classifications.

## Practical writing adaptation evidence

The practical writing pass added role-flexible, developer-friendly entry points without changing repository ownership or claiming reader validation. The pass focused on:

- practical work-moment navigation and SDLC activity mapping;
- writing and content-quality standards that require situation, decision, consequence, action, example, and evidence to be discoverable without forcing identical headings;
- core daily-work guidance across ambiguity, scope, coding, testing, review, and release readiness;
- requirement, implementation, testing, review, delivery, architecture, and system-design guides that needed clearer when-to-use, decision, example, or evidence-to-keep sections.

The pass remains an implementation adaptation, not usability proof. Guides are better prepared for review, but `PASS` still requires observed reader evidence.

## Why the pilot guides are kept

The nine authoritative guides used by the first two journeys now lead with the affected readers, consequence, and smallest decision outcome, then preserve their deeper reasoning and review evidence. They also state a maintenance trigger:

- unclear idea journey: problem framing, ambiguity detection, validation before implementation, and scope breakdown;
- risky change journey: trade-off analysis, design review, test strategy, delivery risk, and rollback and recovery.

The learning journey uses the new ways-of-working guide plus the retrospective and incident review templates. Its repository implementation is complete, but organizational usefulness still requires observed use.

## Visual learning path evidence

The core senior path contains exactly ten editable Mermaid models. Each model states one question, stays within one abstraction level, and contains no more than eight primary nodes. Six simplified examples expose a bounded decision without pretending to be project evidence. Five original working maxims summarize adjacent reasoning without external attribution.

The visual path covers the decision-to-learning loop, three senior journeys, framework-neutral delivery, evidence-led learning, organizational scaling, maturity gates, problem framing, trade-off analysis, proportional delivery risk, and recovery choice. No raster assets, decorative icons, technology logos, or deeper navigation folders were added.

## Adaptation order

1. Use the practical writing contract as the review baseline for future guide changes.
2. Run usability reviews before claiming `PASS`. Record where readers fail to find the path, explain the consequence, identify the owner, or choose a next action.
3. Adapt remaining guide structure only when reader evidence, delivery evidence, or recurring confusion shows a specific gap.
4. Preserve stable paths. If evidence later requires a merge or replacement, leave a clear successor link at the old authority.
5. Separate time-sensitive examples from durable reasoning and label fictional scenarios.
6. Stop adapting when another change would add prose without improving a demonstrated reader task.

## Mandatory-language audit

The mandatory keyword remains only in:

- the content-quality requirement enforced through contribution review;
- the writing rule that defines when mandatory language is allowed;
- contributor guidance that points back to that rule.

Domain guidance expresses required outcomes and gate behavior directly instead of using unsupported policy language. Reviewers block new mandatory language when no safety, compliance, accepted contract, necessary condition, enforcement owner, or mechanism is visible.

## Usability review needed for PASS

Ask at least one technical reader, one product reader, and one leadership reader to begin from the root README without coaching. Give each reader a situation relevant to their role and observe whether they can, within two navigation choices:

1. find the applicable path;
2. explain the decision and why it matters;
3. identify the consequence and accountable owner;
4. choose the next guide, action, or template;
5. distinguish a recommendation or experiment from a mandatory rule.

For the senior path, use a 30-minute walkthrough and verify that the reader can explain the decision-to-learning loop, route the three pilot situations, distinguish principle from guardrail and local practice, and explain when shared control is justified.

Record navigation failures and misunderstood decisions, not opinions about visual polish. Correct material failures, rerun the tasks, and publish the evidence before changing this audit to `PASS`.

## Maintenance trigger

Repeat this audit after material navigation changes, reader evidence changes a classification, duplicated authority appears, or a guide loses its decision or maintenance owner.
