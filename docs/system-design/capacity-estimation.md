# Capacity Estimation

## Decision supported

Choose safe initial limits and identify the first likely bottlenecks without pretending uncertain forecasts are production facts.

## When to use this

Use this before choosing capacity-sensitive design defaults, scaling strategy, load-test targets, storage plans, queue limits, or operational alerts.

## Decision to make

Decide which capacity assumption can shape the design now, which assumption needs measurement, and what trigger will reopen the estimate.

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

## Example

Weak estimate: "We need to handle many users." Better estimate: "Peak upload is expected at 200 files per minute for 30 minutes, payload p95 is 8 MB, and the first likely bottleneck is virus scanning concurrency; load test that path before increasing queue limits."

## Evidence to keep

- [ ] Inputs, sources, ranges, and time windows are recorded.
- [ ] Peak and degraded-mode assumptions are included.
- [ ] Safety margin has an explicit reason.
- [ ] Estimates produce test targets and re-evaluation triggers.
