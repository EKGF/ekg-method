---
description: >-
  A domain term or idea that links business language to semantic models,
  enabling the Enterprise Knowledge Graph to understand and reason about
  business concepts. Learn how concepts bridge business and technical domains
  in the Use Case Tree Method.
keywords:
  - concept
  - domain concept
  - business concept
  - semantic model
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Concept

<!--summary-start-->
_A domain term or idea that links business language to semantic models,
enabling the Enterprise Knowledge Graph to understand and reason about
business concepts_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Concept?

    For every given [Use Case](use-case.md), we want to start with
    capturing the concepts and terms that the user or "the business"
    uses or wants to use.

    A **Concept** is a way to represent a business idea or term in a
    way that both humans and machines can understand.
    It serves as a bridge between the language your organization uses
    and the formal semantic models (ontologies) that enable the
    Enterprise Knowledge Graph to reason about your business.

    ## Why Concepts Matter

    Concepts ensure that:

    - **Business language is preserved** — We capture terms as the
      business uses them, not as some external standard defines them
    - **Semantic meaning is enabled** — Concepts link to ontologies
      that give them machine-readable meaning
    - **Consistency is maintained** — The same concept can be reused
      across multiple use cases
    - **Interoperability is achieved** — Concepts can map to
      multiple ontologies, enabling integration across systems

    !!! tip "Start with business language"

        Don't worry about ontologies in the early stages.
        Focus on capturing what the business calls things and what
        those things mean in their context.

    ## Concept Vocabulary

    Most concepts and their terms will be pre-defined in all kinds of
    vocabularies, but for brand-new use cases in a new domain,
    concepts and their terms will have to be created.

    Each Use Case can have its own vocabulary of concepts, but it can
    also inherit or borrow concepts from higher-level or related use
    cases in the [Use Case Tree](use-case-tree.md).
    This enables reuse and consistency across the enterprise.

    ## Evolution and Refinement

    As the use case evolves and the understanding of the domain
    becomes clearer, it may be necessary to:

    - **Adjust concepts** — Better reflect the reality of the domain
    - **Map to ontologies** — Link concepts to more appropriate
      terms in specific ontologies or vocabularies to ensure
      consistency and interoperability across the enterprise

    In either case, the important thing is to ensure that the
    captured concepts and terms accurately reflect the reality of the
    domain and the needs of the stakeholders.

=== "Data & Tech Audience"

    ## What Is a Concept in the Use Case Tree Method?

    A **Concept** is the linking pin between local business language
    and formal semantic models (ontologies).
    It enables the EKG to understand business terminology while
    maintaining connections to standardized vocabularies and enabling
    automated reasoning.

    ## The Concept Lifecycle

    ### Initial Capture

    At the initial stages of a use case, the focus should be on
    capturing the language of the users in their domain, which may not
    necessarily involve discussing ontologies.
    The main goal is to gather requirements and understand the
    problem context, as well as the terms and concepts used by the
    users.

    !!! tip "Business-first approach"

        Start with what the business calls things, not what some
        ontology says they should be called.
        The business owns its use cases and should recognize them
        throughout their lifecycle.

    ### Mapping to Ontologies

    Later in the use case's lifecycle, once the problem is well
    understood, the relevant ontologies can be mapped to the terms and
    concepts captured earlier.
    This allows for better integration of the use case with the
    overall EKG ecosystem.

    !!! note "Implementation Detail"
        The mapping to OWL ontologies or SHACL shapes is primarily a
        technical implementation detail that is local to the specific
        use case. Different use cases may map to the same ontology in
        completely different ways, reflecting their unique business
        contexts and requirements. This flexibility ensures that
        ontology mappings serve the use case rather than constraining it.

    ### Refinement and Evolution

    As the use case evolves and the understanding of the domain
    becomes clearer, it may be necessary to:

    - **Adjust captured concepts** — Better reflect the reality of
      the domain
    - **Map to appropriate ontologies** — Link to more appropriate
      terms in specific ontologies or vocabularies to ensure
      consistency and interoperability across the enterprise

    ## Concept Types

    Concepts can represent different types of semantic elements:

    - **Class Concepts** — Represent types or categories (e.g.,
      "Person", "Account", "Transaction")
    - **Property Concepts** — Represent relationships or attributes
      (e.g., "hasOwner", "isLocatedIn", "hasValue")
    - **Shape Concepts** — Represent validation constraints or data
      shapes

    ## Concepts as Linking Pins

    Concepts are the linking pin in many ways.
    They link "business terms" and "technical terms" as they are
    used in the context of the given use case, by the business and
    by various programs, apps, and systems, in all their variations
    and manifestations.

    **Example:**
    The official term for Customer could be "Customer," but it
    appears in different forms:
    - On forms in apps as "Cust."
    - In Python code as `_customer`
    - In SPARQL statements as `?cust`
    - In database schemas as `cust_id` or `customer_id`
    - In API endpoints as `/customers` or `/api/cust`
    - In OWL ontologies as specific axioms (e.g., `owl:Class` or
      `rdfs:subClassOf` relationships)
    - In SHACL shapes as validation constraints (e.g., `sh:property`
      or `sh:minCount`)

    All these symbols, terms, axioms, and shapes are manifestations
    of the same concept and linked to it.
    Even the mapping to certain axioms in an OWL ontology or
    certain shapes in a SHACL shape would be seen as "technical
    terms" — just yet some other manifestations of a given concept.

    This enables the EKG to understand that these different
    representations all refer to the same business concept, enabling
    semantic integration across diverse systems and technologies.

    ## Relationship to Ontologies

    Concepts serve as a bridge between:

    - **Local business terminology** — The language used within a
      specific use case or domain
    - **Technical manifestations** — How concepts appear in code,
      databases, APIs, forms, and other systems
    - **Standard ontologies** — Formal semantic models that enable
      interoperability and reasoning

    This multi-faceted nature allows the EKG to:
    - Address "the business" with their language
    - Integrate with technical systems using their terminology
    - Keep backend EKG models generic and linked to appropriate
      ontologies
    - Model semantic conundrums (e.g., different terms for the same
      concept, same term for different concepts)

    ## Reuse and Inheritance

    Concepts follow the same reuse patterns as other elements in the
    Use Case Tree Method:

    - **Local definition** — Each use case can define concepts
      specific to its domain
    - **Inheritance** — Lower-level use cases inherit concepts from
      parent use cases in the Use Case Tree
    - **Borrowing** — Use cases can reference concepts from related
      use cases
    - **Consistency** — Common concepts are defined once and reused

    This ensures that concepts are not duplicated unnecessarily and
    that the EKG maintains semantic consistency across the enterprise.

    ## Relationship to Other Concepts

    Concepts are fundamental building blocks that relate to:

    - **[Use Cases](use-case.md)** — Each use case has a vocabulary
      of concepts
    - **[Personas](persona.md)** — Personas are Concepts, enabling
      semantic definition and reasoning
    - **[Stories](story.md)** — Stories reference domain concepts
      that need to be understood and modeled
    - **[Ontologies](ontology.md)** — Concepts link to ontology
      classes, properties, and shapes

=== "Ontology"

    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-concept.md"

    We're not (yet) prescribing a full OWL ontology here.
    But we can state a small set of **facts** that people can reliably use to build their own
    ontology / schema / graph model around a Concept.

    ### Required facts about a Concept

    - **Opaque universally unique identifier**
        - A Concept must have an **opaque**, **universally unique** identifier.
        - Prefer a random identifier such as **UUIDv4**.
        - Represent it as a URI, for example:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **Slug**
        - A Concept should have a kebab-cased slug.
        - Slug uniqueness cannot be guaranteed, but it can be used as a convenient alternative
          identifier next to the real identifier (with lookup/search).
        - Do **not** use the slug as a foreign key in the Knowledge Graph itself; use the real
          identifier for references.

    - **Label Term (instead of a traditional label)**
        - A Concept does not have a traditional label such as `skos:prefLabel` or `rdfs:label`.
        - Instead, it has a **labelTerm** link to one of its **BusinessTerm** objects (a resource
          in the Knowledge Graph).
        - Learn more in [Term](term.md).

    - **Definition**
        - A Concept must have a business-focused definition explaining what it means in context.

    - **One or more Terms (required)**
        - A Concept must have **one or more Terms** (`Term`), which can be either a
          **BusinessTerm** or a **TechnicalTerm**.
        - A Concept without a Term has no reason to exist.
        - All Terms of a Concept **mean the same thing** in the context of that Concept.
        - Terms may include alternative spellings, abbreviations, synonyms, and technical
          manifestations.
        - Terms are **owned** by the Concept (part-of): when the Concept is deleted, its Term
          objects are deleted as well.
        - Learn more in [Term](term.md).

    - **Contained in a Concept Vocabulary**
        - A Concept is a member of a Concept Vocabulary (a “container” of Concepts).
        - A Use Case can relate to Concept Vocabularies via relationship-objects:
            - it can **reference** an external vocabulary and/or
            - **own** a private vocabulary.

    - **Mapping to ontologies (optional)**
        - A Concept can be mapped/aligned to terms in one or more ontologies (classes,
          properties, shapes).
        - Model this via mapping/alignment relationships so you can capture confidence, rationale,
          and provenance.

    - **Used by Stories and Workflows**
        - Stories use Concepts as **input**, **output**, and **dependent** concepts.
        - Workflows use Concepts through the Stories they orchestrate and the vocabulary of the
          Use Case.

