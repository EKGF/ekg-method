---
description: >-
  A structured business requirement — who, what, why — that
  captures what a Persona needs to accomplish within the context
  of a Use Case and the Outcome it contributes to.
keywords:
  - story
  - user story
  - business requirement
  - persona story
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Story

<!--summary-start-->

_A structured business requirement — who, what, why — that
captures what a Persona needs to accomplish within the context
of a Use Case and the Outcome it contributes to_

<!--summary-end-->

=== "Business & Management Audience"

    A **Story** — in the context of a
    [Use Case](../use-case/index.md) in the
    [Use Case Tree](../use-case-tree.md) — defines a business
    requirement.
    It captures what someone needs to accomplish, expressed in
    their own language.

=== "Data & Tech Audience"

    "User Stories" start out as plain English sentences that,
    as the name suggests, come from the user.
    In other words, "the Business" or "the Customer" — the
    end user of a system or application — is responsible for
    explaining to the people who need to deliver that system
    what the system is supposed to do.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-story.md"

    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ### Story

    - **Opaque universally unique identifier**
        - A Story must have an **opaque**, **universally unique** identifier.
        - Prefer a random identifier such as **UUIDv4**.
        - Represent it as a URI, for example:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **Business-friendly name**
        - A Story should have a concise, human-readable name.

    - **Slug**
        - A Story should have a kebab-cased slug that is unique at least within the organization.
        - Example: `assess-risk-position`, `verify-stakeholders`

    - **Business-focused definition**
        - A Story must have a plain-language definition of what the user needs.

    - **Structured statement (who / what / why)**
        - A Story should capture:
            - **Who**: a reference to a Persona (or persona-like Concept)
            - **What**: the capability/action needed
            - **Why**: a reference to an Outcome (the intended business value)

    - **Owned by a Use Case**
        - A Story is **part-of** a Use Case: the Use Case **owns** the Story.
        - If the owning Use Case is deleted, its Stories are deleted as well.

    - **Concept usage (relationship-object)**
        - Model the relationship between a Story and a Concept as a **relationship-object**
          (not a direct link), because it carries meaning about *how* the Concept is used.
        - The relationship-object defines a usage type, for example:
            - **Input Concept** — required/mandatory input parameter (or optional)
            - **Output Concept** — definition of the output (often a shape/compound object)
            - **Dependent Concept** — referenced in filters/constraints (e.g., SQL/SPARQL `WHERE`)

    - **Workflow participation**
        - A Story can participate as a **Step** in one or more WorkflowDefinitions.
        - Model this via a relationship-object (e.g. a "WorkflowStep") so you can capture step
          order, conditions, and other execution semantics.
