---
description: >-
  A relationship object that defines how a Story uses a specific
  Concept (e.g., as input, output, or dependent). Learn how
  Story/Concept Relationships enable precise data traceability in the
  Use Case Tree Method.
keywords:
  - story concept relationship
  - concept usage
  - input concept
  - output concept
  - dependent concept
  - EKG method
schema_type: "Article"
---

# Story/Concept Relationship

<!--summary-start-->

_Defines how a Story uses a specific Concept (e.g., as input, output,
or dependent)_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a Story/Concept Relationship?
    A **Story/Concept Relationship** explains *how* a [Story](../story.md) interacts with a [Concept](index.md).

    It's not enough to say that a story "uses" a concept; we need to know if the concept is something the user *provides* (Input), something the system *returns* (Output), or something used behind the scenes to filter or calculate data (Dependent).

    ## Why it Matters
    - **Data Requirements**: Clearly identifies what data points are needed to fulfill a business requirement.
    - **Impact Analysis**: If a concept changes, we know exactly which stories (and therefore which business capabilities) are affected.
    - **Consistency**: Ensures that the same concept is used consistently across different stories and use cases.

=== "Data & Tech Audience"

    ## Concept Usage Types
    The relationship between a Story and a Concept is modeled via a relationship-object to capture the specific nature of the usage:

    - **Input Concept**: A required or optional input parameter for the story (e.g., a filter criteria or a value to be saved).
    - **Output Concept**: Defines the data returned by the story (often a complex object or "shape").
    - **Dependent Concept**: A concept referenced in the implementation (e.g., used in a `WHERE` clause or a join) but not directly exposed as input or output.

    ## Traceability
    By modeling these relationships explicitly, the EKG can automatically generate data lineage and requirement maps, showing exactly how business logic translates into data consumption and production.

=== "Ontology"

    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-story-concept-relationship.md"

    ### Required facts about a Story/Concept Relationship
    - **Opaque universally unique identifier**: A UUID representing this specific relationship instance.
    - **Source Story**: A reference to the [Story](../story.md) that owns this relationship.
    - **Target Concept**: A reference to the [Concept](index.md) being used.
    - **Usage Type**: One of `Input`, `Output`, or `Dependent`.

    ### Ownership
    - **Owned by Story**: A Story/Concept Relationship is part-of a Story. If the Story is deleted, the relationship object is deleted.
