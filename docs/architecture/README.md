# Software Architecture

## Purpose

Guide structural decisions over time.

## Core guidance

Optimize boundaries, modularity, integration, quality attributes, decision records, and evolutionary cost.

Architecture guidance applies when a structural choice affects multiple changes, teams, runtime qualities, or recovery options. It is not a catalog of patterns and does not replace system-specific evidence.

## Guides

- [Architecture principles](architecture-principles.md) — apply durable heuristics without turning them into universal rules.
- [Boundaries](boundaries.md) — place ownership and change boundaries around coherent responsibilities.
- [Modularity](modularity.md) — contain change and enforce dependencies before distributing a system.
- [Integration patterns](integration-patterns.md) — choose interaction semantics from consistency and failure needs.
- [Architecture decisions](architecture-decisions.md) — record consequential choices and their evidence.
- [Architecture evolution](architecture-evolution.md) — evolve structure from observed pressure rather than prediction.

## Review questions

- What recurring change or runtime pressure justifies a structural decision?
- Are responsibility, state authority, dependency direction, and operational ownership aligned?
- Was the simplest credible structure compared under the same constraints?
- Which observable change will trigger evolution or reconsideration?
