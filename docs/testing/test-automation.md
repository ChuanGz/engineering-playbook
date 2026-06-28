# Test Automation

## Decision supported

Automate a check when repeated, trustworthy evidence is worth its execution, maintenance, and diagnostic cost.

## Automation criteria

Automate when the check:

- protects consequential behavior or a recurring regression;
- has an objective pass condition;
- can control inputs and observe outputs reliably;
- runs often enough to recover implementation cost;
- produces a clear owner and corrective action when it fails.

Keep exploratory, usability, or novel-risk investigation manual when human observation provides the evidence automation would miss.

## Pipeline placement

1. Run fast deterministic checks close to the change.
2. Run expensive integration and compatibility evidence when relevant artifacts exist.
3. Separate release-blocking checks from scheduled diagnostics.
4. Quarantine only with owner, reason, and expiration; never silently ignore.
5. Track failure cause, duration, flakiness, and escaped defects to refine the suite.

## Trade-offs

Automation increases repeatability and feedback frequency but codifies assumptions and requires maintenance. A large suite with weak signal can slow delivery more than it reduces risk.

## Failure modes

- Automating a visually appealing scenario with no release decision.
- Adding retries until intermittent product defects appear green.
- Keeping tests after their protected behavior or consumer is removed.
- Treating environment instability as an unavoidable test characteristic.

## Review evidence

- [ ] Each automated check influences a named engineering decision.
- [ ] Pass criteria and failure ownership are objective.
- [ ] Flaky or quarantined checks have bounded remediation.
- [ ] Suite cost and escaped defects are reviewed over time.
