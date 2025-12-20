---
title: >-
  M: Enable Reuse - Knowledge Reuse Across Enterprise
authors:
- Jacobus Geluk
hide:
- toc
date_published: "2022-01-01"
description: >-
  Learn how to build composable, scalable enterprise knowledge through reuse.
  Discover how the Use Case Tree Method enables safe reuse of knowledge assets
  across teams and domains.
keywords:
  - reuse
  - knowledge reuse
  - reusable components
  - EKG method
  - enterprise knowledge graph
  - composability
schema_type: "Article"
---
# M: Enable Reuse

<!--summary-start-->
_Building the foundation for composable, scalable enterprise knowledge_
<!--summary-end-->

## Objective

**Reuse Enablement** is the discipline of designing, packaging, and
governing every knowledge asset — use case, ontology, data product, or
workflow — so that it can be safely reused across teams, domains, and
generations of technology.

It is the foundation of the Enterprise Knowledge Graph (EKG): without
reuse, there is no composability, no scalability, and no sustainable
intelligence.
The Use Case Tree Method defines reuse not as a technical afterthought but as a
*core architectural principle* — embedded in the way we plan, build,
and run every enterprise capability.

## Why It Matters

Enterprises waste enormous effort solving the same problems repeatedly —
integrating the same data, remodelling the same business rules,
recreating the same workflows.

Most of this duplication stems from one cause: **knowledge is not shared
as reusable components**.

When knowledge lives in silos — spreadsheets, slide decks, bespoke
systems — every project begins from zero.
By contrast, a reuse-enabled organisation captures its work as
semantically defined, governed components that can be discovered and
recomposed anywhere across the enterprise.

The result:

- Drastically reduced duplication and cost
- Higher quality and consistency through shared models
- Faster delivery and innovation
- Stronger alignment across business and technology

## Beyond Data: The Real Meaning of Reuse

Most "semantic technology" initiatives of the past two decades have been
driven from the **data perspective** — led by integration specialists and
ontology engineers.
They delivered powerful data harmonisation but rarely transformed how
the enterprise actually *works*.

That is where the **Enterprise Knowledge Graph (EKG)** and **Use Case
Tree (UCT)** shift the paradigm.
They treat **reuse not as a data exercise**, but as the foundation for
*application composition*.
In the Use Case Tree Method, reuse is not limited to triples or ontologies — it
extends to **behaviour**, expressed as *Stories* and *Workflows*.

Just as **object-oriented programming** in the 1980s combined data and
methods into a reusable "object,"
the **Use Case Tree (UCT)** combines data, logic, and process into a
reusable **semantic package**:
a use case that contains its meaning (ontology), its data products, and
its behaviour (stories, workflows, outcomes).

This is the crucial difference:

!!! tip "The Use Case Tree Method paradigm shift"

    Instead of describing data that *others must code against*, the Use Case
    Tree Method captures *the behaviour itself* — executable, governed, and
    reusable across domains — without necessarily writing code at all.

In this sense, a **Use Case** in the EKG is just as real and reusable as
a software package in the JavaScript or Python ecosystems.
Each can be discovered, installed, versioned, extended, and composed —
but the EKG package operates at the **semantic and business level**,
spanning data, logic, and meaning.

That's why **reuse** is not a side effect of the EKG.
It's the *reason the EKG exists.*

### From DIKW to EKGF: Making Knowledge Executable

The well-known **DIKW Model** (Data → Information → Knowledge → Wisdom)
has guided information management for decades.
But it assumes that *Wisdom naturally follows from Knowledge* — as if
understanding automatically produces action.
In practice, enterprises rarely reach that state because the bridge from
*knowing* to *doing* is missing.

The **Use Case Tree Method** extends this model by adding the **operational
dimension**:
knowledge becomes **behaviour**, behaviour becomes **reusable**, and
reuse powers **composability**.
This is the *Path to Executable Knowledge* — where understanding turns
into governed, shareable, and actionable intelligence.

The diagram below visualises this shift — showing how the Use Case Tree Method
transforms the classic DIKW hierarchy into a living model of executable,
reusable knowledge.

![DIKW Model Revised – Path to Executable Knowledge](../assets/dikw-revised.svg)

<sub>Traditional DIKW ends at understanding.
The Use Case Tree Method continues by modelling behaviour, packaging it as reusable
use cases, and feeding it back into a composable enterprise — closing the
loop between data, knowledge, and operational wisdom.</sub>

## The Role of the Use Case Tree (UCT)

In the Use Case Tree Method, the **Use Case Tree (UCT)** is the mechanism that
makes reuse practical and governed.

Each node in the UCT acts as a *semantic package* — a defined,
versioned, and discoverable unit of business capability.
Within a UCT package, teams can register:

- **Ontologies and shapes** defining meaning and validation
- **Stories** (tool functions or APIs) that implement reusable logic
- **Data products** describing and delivering reusable datasets
- **Workflows and policies** orchestrating repeatable patterns

Every successful technology ecosystem has a way to **share reusable
components** — the JavaScript world has [*npm*](https://www.npmjs.com)
with over 3.5 million packages, the Python world has
[*PyPI*](https://pypi.org) with over 600,000 packages, and so on — each
enabling developers to build upon a vast ecosystem of reusable
components.
The **Use Case Tree (UCT)** plays the same role for the **Enterprise
Knowledge Graph (EKG)**: it is the *semantic package manager* that makes
every business capability, dataset, and workflow discoverable, versioned,
and ready for reuse across the organisation.

## Reuse Enablement vs. Composable Business

### Two sides of the same semantic coin

While *Reuse Enablement* and *Composable Business* share the same
foundation, they operate at different levels of abstraction.
The table below summarises their relationship within the Use Case Tree Method.

| Aspect | Composable Business | Reuse Enablement |
|--------|---------------------|------------------|
| Focus / Orientation | _How business capabilities are composed, orchestrated, and evolved_ | _How knowledge assets and components are packaged and shared_ |
| Primary Question | "How do we assemble business capabilities from reusable parts to adapt to change?" | "How do we design those reusable parts so they can be assembled safely and meaningfully?" |
| Scope | Business and operational level — orchestrating Use Cases, Personas, and Stories into composable outcomes. | Technical and semantic level — creating and governing reusable artifacts: ontologies, datasets, shapes, workflows, data products, and Stories. |
| Key Mechanism | **Use Case Tree (UCT)** as _the orchestration layer_: composing and aligning modular business capabilities. | **Use Case Tree (UCT)** as _the packaging layer_: publishing reusable components and metadata to the Enterprise Knowledge Graph (EKG) for discovery and re-use. |
| Relationship to the EKG | The EKG provides the shared semantics and service interfaces that make cross-use-case orchestration possible. | The EKG provides the shared identifiers, ontologies, and provenance that make reuse safe and traceable. |
| Value Proposition | Agility and adaptability: the ability to reconfigure the enterprise dynamically in response to change. | Efficiency and consistency: the ability to reduce duplication and accelerate delivery through reusable, versioned components. |
| Primary Users | Business and solution architects; transformation leads. | Data and knowledge engineers; ontology and platform teams. |
| Outcome | Composable business capabilities and adaptive workflows. | Reusable semantic components and data products. |
| Relationship to Each Other | Composable business **depends on** reuse. Without reusable components, there is nothing to compose. | Reuse **finds purpose** in composability. Without higher-level composition, reuse is just technical hygiene. |

!!! tip "Two sides of the same semantic coin"

    **Reuse Enablement** creates the *building blocks*.

    **Composable Business** assembles them into *living systems*.

    Both rely on the **Use Case Tree (UCT)** as the semantic package
    manager of the Enterprise Knowledge Graph — governing how business,
    data, and technical artifacts are versioned, discoverable, and
    composable.

## How to Enable Reuse in Practice

1. **Model once, reuse everywhere:** design ontologies, shapes, and
   stories as modular assets stored and versioned in the EKG.

2. **Publish via the UCT:** register components as packages with clear
   ownership, metadata, and dependency relationships.

3. **Govern for trust:** validate with SHACL, record provenance, enforce
   entitlements and lifecycle policies.

4. **Discover and compose:** make all reusable artifacts searchable and
   connectable across domains and teams.

5. **Measure reuse:** track adoption, version dependencies, and impact
   metrics to sustain continuous improvement.

## Related Objectives

- [Composable Business](composable-business.md)
- [Manage Modularity](modularity.md)
- [Achieve Interoperability](interoperability.md)
- [Capture Knowledge](capture-knowledge.md)

## Summary

Reuse Enablement is how the EKG turns knowledge into infrastructure.
By packaging every use case, ontology, and data product as a governed,
discoverable component within the Use Case Tree, the enterprise builds a
foundation for **scalable intelligence and composable business**.

When reuse becomes second nature, innovation stops reinventing the wheel
— and starts accelerating on shared semantic ground.
