---
title: Distributed EKG Architecture
description: >-
  How an Enterprise Knowledge Graph differs from traditional knowledge
  graph projects in its distributed, context-specific approach to
  ontologies and data integration.
keywords:
  - distributed EKG
  - enterprise knowledge graph
  - knowledge graph architecture
  - ontology versioning
  - context-specific ontology
  - use case context
  - heterogeneous data
  - LPG
  - semantic web
  - EKG method
schema_type: Article
---

# Distributed EKG Architecture

## Traditional Knowledge Graphs vs EKG

Most knowledge graph projects to date follow a **monolithic pattern**:
a single (often giant) knowledge graph where only one copy of any
given ontology is loaded. While the OWL specification technically
supports loading multiple versions of an ontology (via the version
IRI mechanism), this is rarely done in practice—especially when
reasoners or inference engines are involved.

An **Enterprise Knowledge Graph (EKG)** takes a fundamentally
different approach.

## The EKG Difference

### [Distributed by Design](https://principles.ekgf.org/principle/03-distributed/)

An EKG is not a single monolithic graph. It can consist of **many
knowledge graphs**, each of which can have their own versions of
ontologies loaded. This distributed architecture reflects the reality
of large enterprises where:

- Different business units have different data needs
- Systems evolve at different rates
- Legacy and modern systems must coexist
- Regional or regulatory requirements vary

### Heterogeneous Components

Not all components of an EKG need to be semantic knowledge graphs.
The EKG can integrate:

- **Semantic Knowledge Graphs** — RDF/OWL-based triple stores
- **Labeled Property Graphs (LPGs)** — Graph databases using the
  property graph model
- **Hybrid Graph Databases** — Systems that support both semantic
  (RDF) and property graph models
- **Relational Databases** — SQL databases with structured data
- **Document Stores** — NoSQL databases storing JSON or similar
  formats
- **Data Lakes** — Large-scale storage systems
- **APIs and Services** — External data sources

The EKG provides a **semantic layer** that enables these diverse
components to be understood and queried as if they were part of a
unified knowledge graph.

## Context-Specific Ontology Linking

When we link [Use Cases](../concept/use-case/index.md) to
[Ontology](../concept/ontology.md) axioms, we do so in a way that is
always **context-specific**. The context is primarily defined by the
given Use Case.

### The Linking Chain

The Use Case Tree Method establishes a clear chain from business
requirements to formal ontology axioms:

```text
Use Case
    └── Story
        └── Concept
            └── Technical Term
                └── Ontology Axiom
```

Each level in this chain serves a purpose:

1. **[Use Case](../concept/use-case/index.md)** — Defines the business
   context and requirements
2. **[Story](../concept/story.md)** — Captures specific scenarios and
   user needs
3. **[Concept](../concept/concept/index.md)** — The linking pin between
   business language and technical implementation
4. **[Technical Term](../concept/term/technical-term.md)** — The
   manifestation in code, data, and metadata
5. **Ontology Axiom** — The formal semantic definition in OWL or SHACL

### Why Context Matters

Different use cases may map to the **same ontology** in completely
different ways. A "Customer" concept in a sales use case may have
different attributes, constraints, and relationships than "Customer"
in a compliance use case—even if both ultimately link to the same
OWL class.

This flexibility ensures that:

- **Ontology mappings serve the use case**, not the other way around
- **Business language is preserved** throughout the lifecycle
- **Technical implementation details** remain local to the use case

## Use Cases at Various Maturity Levels

The [Use Case Tree](../concept/use-case-tree.md) does not necessarily
consist only of production-ready use cases with perfect mappings to
OWL ontologies. The tree may contain:

- **Exploratory use cases** — Early ideas being validated
- **Partially defined use cases** — Requirements still being gathered
- **Well-defined use cases** — Clear requirements, not yet mapped
- **Mapped use cases** — Linked to ontologies but not implemented
- **Production use cases** — Fully implemented and operational

This is one of the key reasons why the Use Case Tree Method
introduces the idea of **[Concepts](../concept/concept/index.md) of
the Use Case**.

## Concepts as the Linking Pin

[Concepts](../concept/concept/index.md) form the linking pin—in the
context of the given use case—between the
[Stories](../concept/story.md) and the OWL ontology axioms.

### Why Concepts, Not Direct Ontology Mapping?

If use cases mapped directly to ontology axioms, we would face
several problems:

1. **Premature commitment** — Use cases would need ontology mappings
   before requirements are fully understood
2. **Brittleness** — Changes to ontologies would ripple through all
   use cases
3. **Loss of business language** — Technical terminology would
   dominate
4. **Integration complexity** — Different systems couldn't speak
   their own language

By introducing Concepts as an intermediate layer:

- **Business language is preserved** — Stakeholders recognize their
  terminology
- **Mapping can be deferred** — Ontology integration happens when
  appropriate
- **Context is maintained** — Each use case has its own semantic
  context
- **Evolution is supported** — Concepts can be refined as
  understanding grows

### The Mapping

Concepts provide the information needed to do **"the mapping"** of
all data that goes in and out of the EKG:

- **Inbound mapping** — Transform data from source systems into EKG
  representations
- **Outbound mapping** — Transform EKG data into formats required by
  consuming systems
- **Semantic alignment** — Ensure that different representations of
  the same concept are understood as equivalent

This mapping is always context-specific, defined by the use case that
needs the data.

## Implications for Architecture

### No Single Source of Truth

Unlike traditional data architectures that seek a "single source of
truth," the EKG embraces the reality that:

- Truth is context-dependent
- Multiple valid representations exist
- Reconciliation happens at query time, not load time

### Federated Reasoning

Reasoning in a distributed EKG is different from reasoning in a
monolithic graph:

- Reasoners may operate on subsets of the overall graph
- Different use cases may apply different reasoning profiles
- Context determines which axioms and rules apply

### Evolutionary Architecture

The distributed, context-specific approach enables:

- **Incremental adoption** — Start with one use case, expand over
  time
- **Parallel development** — Different teams can work on different
  use cases
- **Graceful evolution** — Ontologies can evolve without breaking
  existing use cases

## See Also

- [Enterprise Knowledge Graph](ekg.md) — What an EKG is
- [Ontology](../concept/ontology.md) — Formal specification of
  concepts
- [Concept](../concept/concept/index.md) — The linking pin between
  business and technical
- [Use Case](../concept/use-case/index.md) — Business capabilities in
  the EKG
- [Use Case Tree](../concept/use-case-tree.md) — Organizing use cases
