# Error Handling

## Decision supported

Preserve enough failure meaning for the caller to respond correctly and for operators to diagnose and recover without exposing sensitive internals.

## Failure classification

Distinguish at least:

- invalid input the caller can correct;
- rejected business action with a stable reason;
- concurrency conflict requiring refresh or retry;
- dependency failure that may recover;
- cancellation or deadline expiration;
- unexpected defect requiring investigation.

Classification should change caller or operational behavior. Do not create categories that all receive the same response.

## Decision guide

1. Handle a failure only where context exists to recover, translate, or add useful evidence.
2. Preserve the original cause when translating across boundaries.
3. Retry only transient, idempotent work within a bounded deadline.
4. Log once at the accountable boundary with correlation and safe context.
5. Return stable public error contracts without stack traces, secrets, or provider details.
6. Define compensation or reconciliation for partial state changes.

## Trade-offs

Detailed error contracts improve caller decisions but increase compatibility surface. Generic errors reduce exposure but force callers and operators to guess.

## Failure modes

- Catching broad exceptions and continuing with invalid state.
- Logging the same failure at every layer.
- Retrying permanent validation or authorization failures.
- Converting cancellation into an unexpected server error.
- Returning raw dependency messages to consumers.

## Review evidence

- [ ] Each error category drives a distinct response.
- [ ] Retry has bounded time, transient criteria, and idempotency evidence.
- [ ] Partial failures have recovery ownership.
- [ ] Logs support diagnosis without exposing sensitive data.
