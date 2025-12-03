---
description: "A representation of the different types of players — people, systems, or entities — involved in a Use Case, defined using business language. Understand how personas shape requirements in the Use Case Tree Method."
keywords:
  - persona
  - user persona
  - stakeholder
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Persona

<!--summary-start-->
_A representation of the different types of players — people, systems,
or entities — involved in a Use Case, defined using business language_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Persona?

    For any given [Use Case](use-case.md), we need to identify all
    the different types of players involved.
    In the initial stages of a use case's lifecycle, it matters less
    whether these players are called Stakeholders, Actors, Roles, User
    Types, or Systems.
    What matters is understanding what terms the actual users — the
    real customers of the use case — use for them in their daily
    practice.

    We call them **Personas**.

    ## Why Personas Matter

    Personas help us understand who interacts with a use case and
    what their needs are.
    They provide a common language that bridges business and
    technology, ensuring that everyone understands who is involved
    and what roles they play.

    !!! tip "Use business language"

        Start with the terms your organization already uses.
        Don't force technical terminology — let the business
        language guide you.

    ## Examples

    For example, in the use case "Legal Entity Management," you
    would have Personas like:

    - **Auditor** — Reviews and verifies legal entity information
    - **Data Owner** — Responsible for maintaining accurate data
    - **Shareholder** — Has ownership interest in the entity
    - **Director** — Member of the board of directors
    - **Signator** — Authorized to sign on behalf of the entity
      - Signator Power Pursuant to Commercial Register
    - **Board Member** — Serves on the entity's board
    - **Legal Council** — Provides legal guidance
    - **Liquidator** — Manages entity dissolution
    - ...

    ## Reuse Across Use Cases

    Many Personas are involved in multiple use cases and are
    grouped together in **persona taxonomies**.
    These taxonomies are defined in [ontologies](ontology.md) with
    "machine-readable meaning" that enables algorithms to understand
    the actual context and act upon it.

    This reuse ensures consistency across the enterprise and enables
    the [composable business](../objective/composable-business.md)
    approach, where Personas become reusable components in the
    Enterprise Knowledge Graph.

=== "Data & Tech Audience"

    ## Persona vs. Actor vs. Role

    In traditional use case modeling, the term **Actor** is commonly
    used rather than **Persona**.
    The term Actor is also used in the TOGAF Metamodel, where it is
    combined with the term **Role** — an actor assumes a role to
    perform a task.

    The Use Case Tree Method does not make that distinction, primarily to keep
    things simple when capturing requirements — primarily as
    [Stories](story.md) — but also because the term Persona combines
    both concepts into one unified model.

    ## Key Technical Characteristics

    ### Automated Role Assignment

    Actors assuming a Role is fully automated, context-dependent,
    and driven by models, rules, and policies.
    This means that the system determines which Persona applies
    based on the current context, rather than requiring manual
    assignment.

    ### Real-Time Persona Computation

    A proper EKG service layer is able to compute the set of
    Personas that the current user has **in real-time** and map
    them to lower-level roles and privileges local to the given
    technology stack.

    This dynamic computation enables:

    - **Contextual assignment** — Some Personas are assigned to a
      user temporarily, just in the context of a given use case or
      when working with a specific object
    - **Rule-based determination** — Personas can be computed
      based on business rules (e.g., you can be the "Account
      Owner" if the account is assigned to you, is in your region,
      etc.)
    - **Technology stack mapping** — The EKG service layer
      translates high-level Personas into the specific roles and
      privileges required by each technology stack (databases,
      APIs, applications)

    This approach ensures that authorization and access control are
    driven by business semantics (Personas) rather than
    technology-specific roles, while still respecting the
    constraints and capabilities of each underlying system.

    ### Ontology-Based Definition

    Technically (or ontologically), a **Persona is just another
    [Concept](concept.md)** — tied to ontology-defined classes that
    can inherit from other Persona types.
    This fundamental equivalence enables:

    - **Inheritance relationships** — Personas can be organized in
      hierarchies (e.g., "Signator Power Pursuant to Commercial
      Register" is a sub-persona of "Signator")
    - **Semantic meaning** — Personas have machine-readable
      definitions that enable automated reasoning
    - **Reuse** — Personas defined once can be used across multiple
      use cases

    ### Concept Vocabulary and Reuse

    Each [Use Case](use-case.md) can have its own vocabulary of
    concepts, including Personas.
    However, use cases also **inherit or borrow** concepts from
    higher-level or otherwise related use cases in the
    [Use Case Tree](use-case-tree.md) (UCT).

    This approach enables:

    - **Local vocabulary** — Use cases can define concepts
      (including Personas) specific to their domain
    - **Inheritance** — Lower-level use cases inherit concepts from
      their parent use cases in the UCT hierarchy
    - **Borrowing** — Use cases can reference and reuse concepts
      from related use cases, even if they're not direct ancestors
    - **Consistency** — Common concepts (like standard Personas) are
      defined once and reused, ensuring consistency across the
      enterprise

    Since Personas are Concepts, they follow the same reuse and
    inheritance patterns as any other concept in the Use Case Tree Method.

    ### Beyond Active Users

    Personas are not just the "users" (or systems) of the use case
    but also any other party in the related data models (or EKG
    models/ontologies).

    For instance, your user can have the Persona "Legal Entity
    Maintainer," but since the legal entity can have a Director as
    well, the Director is also a Persona, even when that Director
    might never be an active user of the system.

    This broader definition ensures that all entities involved in
    the domain are properly represented, whether they actively
    interact with the system or are simply part of the data model.

    ## Relationship to Stories

    [Stories](story.md) define what a Persona needs to accomplish.
    Each Story specifies:

    - **Who** — The Persona (e.g., "As an Auditor...")
    - **What** — The action or need (e.g., "...I need to get a
      list of all current board members...")
    - **Why** — The business outcome (e.g., "...so that I can
      Verify Stakeholders")

    This structure links Personas to business requirements in a
    clear, testable way.

    ## Persona Inheritance

    Personas support inheritance through the `isSubPersonaOf`
    relationship.
    This enables hierarchical organization where more specific
    Personas inherit characteristics from more general ones.

    **Example:**
    - `Signator Power Pursuant to Commercial Register` is a
      sub-persona of `Signator`
    - A user associated with the sub-persona automatically inherits
      the parent Persona's characteristics

    **How it works:**
    This inheritance works bottom-up: if a user is associated with
    `<persona-A>`, and `<persona-A>` is a sub-persona of
    `<persona-B>`, then the user is also associated with
    `<persona-B>`.


=== "Model"

    ## Overview

    The following diagram shows a subset of the Use Case Tree Method model as a
    UML Class Diagram, focusing on **Persona** and its relationships
    to other core concepts.

    ![Persona Class Diagram](../diagrams/out/persona-class-diagram.svg#darkable)

    ## Key Relationships

    The model shows how Personas relate to:

    - **[Use Cases](use-case.md)** — Personas are used in use
      cases to identify who interacts with the capability
    - **[Stories](story.md)** — Stories specify what a Persona
      needs to accomplish
    - **[Concepts](concept.md)** — Personas are Concepts, enabling
      semantic definition and reasoning
    - **Ontologies** — Personas are defined as ontology classes,
      supporting inheritance and reuse

    This model ensures that Personas are not just labels but
    integrated components of the Enterprise Knowledge Graph,
    enabling automated reasoning, policy enforcement, and
    composability.
