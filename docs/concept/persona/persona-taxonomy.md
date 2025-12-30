---
description: >-
  A structured collection of Personas organized as a SKOS Concept
  Scheme within a Use Case. Learn how Persona Taxonomies enable
  semantic organization of actors and roles.
keywords:
  - persona taxonomy
  - SKOS scheme
  - persona organization
  - EKG method
schema_type: "Article"
---

# Persona Taxonomy

<!--summary-start-->

_A structured collection of Personas organized as a SKOS Concept
Scheme within a Use Case_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a Persona Taxonomy?
    A **Persona Taxonomy** is an organized collection of all the [Personas](index.md) relevant to a specific [Use Case](../use-case/index.md).

    Think of it as the "cast of characters" for a use case—everyone and everything that interacts with the system or business capability.

    ## Why it Matters
    - **Completeness**: Ensures you don't miss important actors or roles.
    - **Organization**: Groups related personas together (e.g., all customer types, all regulatory entities).
    - **Reusability**: Once defined, the taxonomy can be inherited by child use cases.

=== "Data & Tech Audience"

    ## Persona Taxonomy as SKOS Scheme
    From a technical perspective, a Persona Taxonomy is a `skos:ConceptScheme` that groups Personas (which are `skos:Concept` instances).

    Each Persona is a member of exactly one PersonaTaxonomy via the `skos:inScheme` relationship.

    ## Ownership
    - **Owned by Use Case**: A PersonaTaxonomy is owned by a specific Use Case (zero or one cardinality).
    - **Personas belong to Taxonomy**: All Personas in the Use Case are members of the taxonomy.

    ## Inheritance
    Lower-level use cases can inherit personas from parent use cases, enabling reuse and consistency.

=== "Ontology"

    <span id="ontology"></span>
    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-persona-taxonomy.md"

    ### Required facts about a Persona Taxonomy
    - **Opaque universally unique identifier**: A UUID representing this taxonomy.
    - **SKOS Concept Scheme**: Modeled as `skos:ConceptScheme`.
    - **Owned by Use Case**: A reference to the [Use Case](../use-case/index.md) that owns it (zero or one cardinality).

    ### Relationship to Personas
    - **Contains Personas**: Personas reference the taxonomy via `skos:inScheme`.
