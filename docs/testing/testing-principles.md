# Testing Principles

## Decision supported

Choose evidence that can reveal a consequential failure before users or operators must discover it.

## Principles

### Test behavior and risk

Start from the incorrect outcome, violated invariant, unsafe transition, or integration failure. A test exists to detect that risk, not to increase a metric.

### Use the lowest sufficient boundary

Prefer the smallest test that includes every component capable of causing the failure. Move outward only when confidence depends on real serialization, storage, networking, configuration, or deployment behavior.

### Make failures diagnostic

A failing test should identify the broken behavior and relevant evidence. Broad scenarios that can fail for unrelated reasons slow correction and become ignored.

### Keep production feedback in the strategy

Some qualities require telemetry, canaries, synthetic checks, or recovery exercises. Pre-release tests cannot prove every production property.

## Trade-offs

More realistic tests increase confidence in integration behavior but cost more to run, diagnose, and maintain. Narrow tests provide fast feedback but cannot expose boundary failures they exclude.

## Failure modes

- Testing implementation calls instead of required outcomes.
- Treating coverage targets as risk coverage.
- Mocking the dependency behavior the test is meant to verify.
- Keeping flaky tests in a required gate until failures lose meaning.

## Review evidence

- [ ] Each test protects a named behavior or failure risk.
- [ ] The selected boundary includes the source of that risk.
- [ ] Failure output supports a specific corrective action.
- [ ] Unverified production assumptions remain visible.
