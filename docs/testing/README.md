# Testing

## Purpose

Choose evidence proportionate to risk.

## Core guidance

Define test intent, select the lowest effective test level, control data, automate repeatable checks, and monitor flaky results.

Testing provides evidence about a named risk. Test count, coverage percentage, and pyramid shape are signals—not proof that a system is correct or safe to release.

## Guides

- [Testing principles](testing-principles.md) — connect every test to behavior, risk, and useful failure evidence.
- [Test strategy](test-strategy.md) — allocate validation effort from change and production risk.
- [Unit testing](unit-testing.md) — protect deterministic rules with fast, focused feedback.
- [Integration testing](integration-testing.md) — verify behavior across real technical boundaries.
- [Contract testing](contract-testing.md) — detect incompatible provider and consumer evolution.
- [Test automation](test-automation.md) — automate checks only when their signal remains trustworthy.

## Review questions

- Which consequential failure does each test or control detect?
- Does the selected test boundary include every component capable of causing that failure?
- Will a failure provide diagnostic evidence and an accountable next action?
- Which residual risks require staged rollout or production validation?
