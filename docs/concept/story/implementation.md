---
title: Story Implementation
description: >-
  The concrete technical realization of a Story, bridging the
  gap between a business requirement and its executable
  delivery in the Enterprise Knowledge Graph.
keywords:
  - story implementation
  - technical implementation
  - business requirement
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Story Implementation

<!--summary-start-->

_The concrete technical realization of a Story, bridging the
gap between a business requirement and its executable delivery
in the Enterprise Knowledge Graph_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a Story Implementation?

    A **Story Implementation** is the concrete technical
    realization of a [Story](index.md).
    While a Story captures _what_ a
    [Persona](../persona/index.md) needs to accomplish in
    business language, a Story Implementation captures _how_
    that requirement is actually delivered.

    Think of it this way: the Story is the business
    requirement, and the Story Implementation is the
    solution that fulfills it.

    ## Why separate Story from Implementation?

    Separating the _what_ from the _how_ provides several
    key benefits:

    - **Multiple implementations** — A single Story can
      have more than one implementation, for example when
      different platforms or technologies deliver the same
      business capability
    - **Independent evolution** — The business requirement
      (Story) can remain stable while the implementation
      changes underneath
    - **Traceability** — There is a clear, auditable link
      from business need to technical delivery
    - **Gap analysis** — Stories without implementations
      are immediately visible, highlighting unmet business
      requirements

    ## How does this affect business stakeholders?

    As a business stakeholder, you typically do not need to
    worry about Story Implementations directly.
    However, knowing they exist helps you understand:

    - Whether your requirements have been addressed
    - When multiple solutions exist for the same need
    - How changes to requirements might affect existing
      implementations

=== "Data & Tech Audience"

    ## What is a Story Implementation?

    A **Story Implementation** is the technical artifact
    that realizes a [Story](index.md).
    Where a Story is a logical, business-level description
    of a unit of work, the Story Implementation is the
    concrete, executable component that delivers on that
    requirement.

    Every Story Implementation has an **implementation type**
    that specifies what form it takes.
    Common implementation types include:

    - **Query** — A query or set of queries in any query
      language (SPARQL, SQL, Cypher, GQL, etc.)
    - **API** — An API endpoint or service
    - **Pipeline** — An ETL pipeline or data transformation
    - **UI** — A user interface component

    ## Relationship to Story

    A single Story can have **multiple** Story
    Implementations.
    This is common in scenarios such as:

    - **Platform variants** — The same business requirement
      delivered on different platforms (web, mobile, API)
    - **Technology migration** — A new implementation
      replaces an older one while both coexist during
      transition
    - **Performance optimization** — A specialized
      implementation for high-volume scenarios alongside a
      general-purpose one

    Each Story Implementation belongs to exactly **one**
    Story.

    ## Lifecycle

    Story Implementations follow their own lifecycle,
    independent of the Story they implement:

    1. **Development** — The implementation is being built
       and tested
    2. **Active** — The implementation is in production and
       delivering the Story's requirements
    3. **Deprecated** — The implementation is being phased
       out in favor of a newer one
    4. **Retired** — The implementation is no longer in use

    ## Continuous Testing

    Because the EKG knows about both Stories and their
    Implementations, it can continuously verify that each
    Implementation still correctly delivers the
    requirements defined by its Story.
    When code, ontologies, or data pipelines change, the
    EKG can detect whether existing Implementations are
    still functioning as expected.

    ## Relationship to Other Concepts

    Story Implementations connect to several other concepts
    in the model:

    - **[Story](index.md)** — Each Implementation realizes
      exactly one Story
    - **[Workflow](../workflow.md)** — Implementations are
      invoked as part of workflow execution
    - **[Concepts](../concept/index.md)** — Implementations
      operate on the same domain concepts referenced by
      their Story

=== "Ontology"

    --8<-- "fragment/uctm-diagram-story.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here.
        These are minimal facts you can use to build your
        own ontology, schema, or graph model.

    ### Story Implementation

    - **Opaque universally unique identifier**
        - A Story Implementation must have an **opaque**,
          **universally unique** identifier.
        - Prefer a random identifier such as **UUIDv4**.

    - **Implements exactly one Story**
        - A Story Implementation must reference exactly one
          [Story](index.md) via an `:implements`
          relationship.
        - A Story can have **0..\*** Story Implementations.

    - **Name**
        - A Story Implementation should have a
          human-readable name or label.

    - **Description**
        - A Story Implementation should have a description
          of how the Story is realized.

    - **Implementation type (enumeration)**
        - A Story Implementation must specify its
          **implementation type**.
        - This is an enumerated value, for example:
            - **Query** — a query or set of queries
              (SPARQL, SQL, Cypher, GQL, etc.)
            - **API** — an API endpoint or service
            - **Pipeline** — an ETL pipeline or data
              transformation
            - **UI** — a user interface component
        - Organizations may extend this enumeration with
          additional types as needed.

    ### Cardinality

    - A Story can have **0..\*** Story Implementations
    - A Story Implementation belongs to exactly **1** Story

## See also

- [Story](index.md) — The business requirement that a
  Story Implementation realizes
- [Workflow](../workflow.md) — How stories are executed
  as steps in workflows
- [Concept](../concept/index.md) — Domain concepts
  referenced by stories
