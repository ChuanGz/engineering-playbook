# README Standard

## Decision supported

Give a repository visitor enough verified context to decide whether the project is relevant and take the correct next action.

## Required outcomes

A repository README should enable the reader to identify:

- purpose, audience, and current maturity;
- supported and unsupported scope;
- primary content or system entry points;
- minimum verified usage, development, or navigation path;
- validation and operational expectations where applicable;
- contribution, governance, security, and license information.

Documentation-only repositories should prioritize navigation and reading paths. Application repositories should provide executable setup and verification. Do not invent commands to satisfy a standard outline.

## Structure guidance

1. Lead with the outcome and intended reader.
2. Show scope and boundaries before detailed features.
3. Provide the shortest verified path to useful content or a successful run.
4. Link to deeper references instead of duplicating them.
5. Expose project status, known limitations, and ownership.
6. Keep decorative badges and diagrams only when they communicate current evidence.

## Trade-offs

A concise README improves orientation but may hide essential constraints. A comprehensive README becomes stale and makes navigation harder. Keep the landing page stable and move volatile detail to owned documents.

## Failure modes

- Marketing language without verifiable capability.
- Setup steps never tested from a clean environment.
- A large index pointing to thin or empty documents.
- Badges implying quality or security not supported by the linked check.

## Review evidence

- [ ] Purpose, audience, maturity, and non-goals are clear above detailed navigation.
- [ ] Every command, link, badge, and diagram reflects current repository state.
- [ ] The next action for each primary reader is discoverable.
- [ ] Volatile detail has an accountable source outside the landing page.
