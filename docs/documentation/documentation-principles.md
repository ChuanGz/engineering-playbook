# Documentation Principles

## Decision supported

Decide whether documentation is needed, what form it should take, and how it will remain trustworthy after the initial change.

## Principles

### Start from reader action

Name the reader, their context, and the task or decision the document must enable. If no behavior changes after reading, challenge whether the document should exist.

### Keep truth near its owner

Store contracts, operational procedures, and decisions close to the system or team that changes them. Link to authoritative sources instead of copying volatile facts.

### Separate document purposes

Use tutorials for learning, how-to guides for tasks, reference for lookup, and explanation for understanding. Mixing purposes often hides prerequisites and makes maintenance ambiguous.

### Treat deletion as maintenance

Remove or supersede content when its decision, system, or audience no longer exists. More documentation is not automatically better coverage.

## Trade-offs

Detailed documentation reduces rediscovery but creates review and synchronization cost. Document stable decisions and dangerous procedures deeply; keep rapidly changing implementation discoverable from code and automation.

## Failure modes

- Writing generic guidance because project evidence is unavailable.
- Copying configuration values that already have an authoritative source.
- Creating one file per future topic with placeholder content.
- Publishing a document without ownership or update triggers.

## Review evidence

- [ ] A named reader can perform a task or make a decision from the document.
- [ ] Facts link to authoritative sources where practical.
- [ ] Scope, assumptions, and maintenance ownership are explicit.
- [ ] The content adds value not already provided elsewhere.
