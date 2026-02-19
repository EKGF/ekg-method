---
title: Relationships
description: >-
  How stories relate to workflows, personas, use cases,
  outcomes, concepts, and other elements in the Use Case
  Tree Method.
---

# Relationships

## Relationship to workflows

Stories are executed as steps within
[Workflows](../workflow.md).
For each Story, we always know in which Workflows it
participates as a Step.

This bidirectional relationship enables:

- **Story reuse** — Stories can be reused across multiple
  workflows, enabling composition and consistency
- **Workflow discovery** — Understanding which workflows use
  a given story helps discover related business processes
- **Impact analysis** — Knowing what workflows are affected
  when a story changes enables better change management
- **Process understanding** — Seeing how stories are
  composed into workflows provides insight into business
  processes

Stories define the "what" (the capability), while Workflows
define the "how" (the sequence and order of execution).

## Relationship to other concepts

Stories link to other data structures in the Knowledge
Graph:

- **[Personas](../persona/index.md)** — Each Story specifies
  which Persona needs the capability
- **[Use Cases](../use-case/index.md)** — Stories are
  organized within Use Cases, defining the functional
  requirements
- **[Outcomes](../outcome/index.md)** — The "why" part of a
  Story links to business outcomes
- **[Concepts](../concept/index.md)** — Stories reference
  domain concepts that need to be understood and modeled
- **[Workflows](../workflow.md)** — Stories are executed as
  steps within workflows

This integration ensures that Stories are not isolated
requirements but part of a cohesive, semantic model of the
enterprise.
