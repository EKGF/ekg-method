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

    ## What Is a Concept in the EKG Method?

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
    EKG Method:

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

