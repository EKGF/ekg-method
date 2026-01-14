---
title: >-
  H: Avoid Disruption - Incremental Change Management
authors:
  - Jacobus Geluk
hide:
  - toc
date_published: "2022-01-01"
letter_prefix: "H"
description: >-
  Learn how to make changes gradually with clear interdependencies to
  avoid disruption. Discover how the Use Case Tree Method enables
  safe, incremental change across use cases.
keywords:
  - change management
  - disruption avoidance
  - incremental change
  - EKG method
  - enterprise knowledge graph
  - use case dependencies
schema_type: Article
---

# Avoid Disruption

<!--summary-start-->

_Make changes gradually with clear interdependencies to avoid
disruption across use cases._

<!--summary-end-->

An Enterprise Knowledge Graph serves many use cases on one platform—albeit
a distributed, federated platform not controlled by any single party.
Like the web itself, many parties have a say. Different stakeholders,
different agendas, different priorities—all sharing the same foundation.
They don't care about each other's use cases. Nor should they have to.

But here's the problem: a change to one use case can break another.

## The Scaling Wall

What traditionally happens with enterprise systems is predictable and
depressing. A system starts with ambitions to serve the whole enterprise.
It grows. More teams depend on it. More integrations. More data flows.

Then it hits the wall.

Not a technology wall—the technology could scale further. A *political*
wall. Nobody dares change anything anymore because nobody can oversee
the impact. Too many parties might be disrupted. Too many stakeholders
to consult. Too many approval processes.

The system fossilizes. It becomes "legacy" not because the technology
is old, but because the organization lost the ability to evolve it safely.
New requirements get bolted on as workarounds. Shadow systems spring up.
The original vision of enterprise-wide coverage dies quietly in committee
meetings.

This is not a technology problem. It's a visibility and governance problem.

## The Shared Foundation Risk

When use cases share components—ontologies, datasets, services—a change
that helps one team can blindside another:

- Updated ontology breaks a downstream query
- New validation rule rejects previously valid data
- Performance optimization slows down a different workflow
- "Improved" API response breaks an integration nobody told you about

This happens to every large system. Every knowledge graph project. Every
enterprise platform. It *always* goes like this.

Unless you organize it properly.

## Two Non-Negotiables

**1. No big bang releases**

Changes happen gradually. Small increments. Continuous delivery. If
something breaks, you know exactly what caused it and can roll back fast.

Big bang releases are how organizations burn millions and deliver chaos.
You test for months, release on a Friday night, and spend the weekend
firefighting. Nobody learns anything except that they hate release
weekends.

**2. Clear, tested interdependencies**

Every connection between use cases must be explicit, documented, and
automatically tested. Continuously. Not "we'll test it before release."
Continuously.

If use case A depends on use case B, and someone changes B, the tests
for A must run immediately. Not tomorrow. Not next sprint. Now.

## The Use Case Tree Makes This Possible

The [Use Case Tree](../concept/use-case-tree.md) is specifically designed
to solve this problem. It maps out precisely:

- Which use cases share which components
- Who depends on whom
- What the impact of any change will be
- What the cost of that change will be

Every use case, every story, every detail is rigorously tested in a
continuous deployment setup. No surprises in production. When you change
something, you know immediately what breaks—and you know before it reaches
anyone.

This isn't just technical scalability. It's *organizational* scalability.
The Use Case Tree method is designed for infinite scale—not by ignoring
the political and governance challenges, but by making them visible and
manageable.

## Reuse Without Fear

The goal of [modularity](modularity.md) is reuse. But reuse creates
dependencies. Dependencies create risk.

The Use Case Tree method doesn't pretend this risk doesn't exist. It
makes the risk visible and manageable. Build reusable components, share
them across use cases, but know exactly what you're sharing with whom—and
test it relentlessly.

## See Also

- [Use Case Tree](../concept/use-case-tree.md)
- [Modularity](modularity.md)
- [Capture Knowledge](capture-knowledge.md)
