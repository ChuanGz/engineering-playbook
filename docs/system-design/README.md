# System Design

## Purpose

Design systems from explicit constraints.

## Core guidance

Frame the problem, quantify demand, define boundaries and data flow, compare trade-offs, and review failure behavior.

The guides in this domain are decision frameworks. They do not prescribe a system shape without workload, reliability, security, cost, and team constraints.

## Guides

- [Problem framing](problem-framing.md) — establish the design decision before selecting components.
- [Capacity estimation](capacity-estimation.md) — translate workload evidence into design limits and validation targets.
- [API boundaries](api-boundaries.md) — define ownership and contracts around business capabilities.
- [Data flow](data-flow.md) — make data movement, state changes, and failure behavior reviewable.
- [Trade-off analysis](trade-off-analysis.md) — compare credible options against explicit decision drivers.
- [Design review](design-review.md) — determine whether a design is ready for implementation.

## Review questions

- Is the context and intended outcome explicit?
- Are alternatives and trade-offs recorded?
- Can the decision be validated and maintained?
