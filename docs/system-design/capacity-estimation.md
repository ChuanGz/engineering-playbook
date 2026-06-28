# Capacity Estimation

## Decision supported

Choose safe initial limits and identify the first likely bottlenecks without pretending uncertain forecasts are production facts.

## Evidence model

Collect or label assumptions for:

- average and peak request or event rates;
- payload, record, and retained-data sizes;
- read-to-write mix and access distribution;
- concurrency, burst duration, and seasonal behavior;
- latency, recovery, and data-loss tolerances;
- expected growth horizon and measurement source.

Use units consistently and show the calculation. A result without inputs, time window, and safety margin is not reviewable.

## Estimation method

1. Model normal load, credible peak load, and one failure scenario.
2. Calculate throughput, storage growth, bandwidth, and concurrent work.
3. Identify which resource becomes constrained first.
4. Add margin based on uncertainty and scaling lead time, not a universal percentage.
5. Convert estimates into load-test targets, alerts, and capacity review triggers.

Prefer measurement from an existing workflow. When no measurement exists, use ranges and validate the widest design-changing uncertainty first.

## Trade-offs

Excess capacity buys resilience and response time but increases cost and can hide inefficient behavior. Tight capacity improves efficiency but requires reliable telemetry and fast scaling operations.

## Failure modes

- Designing only for averages while ignoring bursts and skew.
- Multiplying estimates without preserving units.
- Using business growth targets as observed demand.
- Estimating infrastructure capacity without dependency limits.

## Review evidence

- [ ] Inputs, sources, ranges, and time windows are recorded.
- [ ] Peak and degraded-mode assumptions are included.
- [ ] Safety margin has an explicit reason.
- [ ] Estimates produce test targets and re-evaluation triggers.
