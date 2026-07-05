# Enhancement Plan

## Purpose

Move the playbook from internally consistent guidance to externally demonstrated
reader value. This plan does not add new engineering domains until current
journeys have been tested with real readers.

## Current evidence and gap

The repository has eight decision domains, enforceable writing standards,
purpose-specific templates, validated navigation, and a transparent content
audit. Milestone 2 remains `PARTIAL`: there is no recorded proof that technical,
product, and leadership readers can find and apply the guidance independently.

## Enhancement sequence

### E1 — Run the reader usability review

- Recruit one technical, one product, and one leadership reader.
- Give them the existing ambiguous-request, risky-release, and poor-outcome
  journeys without maintainer coaching.
- Record navigation choices, elapsed time, misunderstood terms, resulting
  artifacts, and missing decisions in a sanitized evidence report.

**Exit evidence:** each reader reaches a relevant starting point within two
navigation choices and can identify the decision, consequence, owner, and next
action. Failures are published as findings rather than omitted.

### E2 — Correct observed journey failures

- Prioritize only issues demonstrated by E1.
- Update authoritative guides instead of creating parallel summaries.
- Re-run the failed tasks with a different reader and record the result.

**Exit evidence:** every material E1 failure is corrected, explicitly accepted,
or retained with a named constraint and review trigger.

### E3 — Adapt the audited content deliberately

- Process the 47 `Adapt` documents by reader journey and observed demand.
- Merge or retire guidance that duplicates an authoritative decision.
- Preserve stable links and point superseded pages to their successor.

**Exit evidence:** the content audit records a decision and evidence for every
changed document; adaptation is not counted as success without reader value.

### E4 — Publish practical cases and a stable release

- Add three sanitized cases covering input, constraints, decision, alternatives,
  outcome, and the guidance changed by the result.
- Include at least one failed or reversed decision.
- Publish a versioned release after navigation corrections are validated.

**Exit evidence:** cases are traceable to real evidence within their stated
anonymization boundary, and consumers have a stable version to cite.

## Measures

| Measure | Target |
|---|---|
| Readers reaching a start within two choices | 3 of 3 |
| Readers producing the expected decision artifact | 3 of 3 |
| Material usability findings with recorded disposition | 100% |
| Sanitized evidence-backed cases | At least 3 |

## Non-goals

- Adding new domains before current reader journeys work.
- Treating page count, CI status, or positive feedback as outcome evidence.
- Rewriting all audited documents without demonstrated reader need.

## Review trigger

Review this plan after each reader round and at every release. Change priorities
when observed reader failure or contribution evidence contradicts the sequence.
