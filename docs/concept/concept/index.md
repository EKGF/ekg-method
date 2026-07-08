---
description: >-
  A thin linking pin for a context-specific meaning, connected to
  business terms, technical manifestations, ontology resources,
  shapes, taxonomies, code identifiers, and source occurrences.
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

_A thin linking pin for a context-specific meaning, connected to
business terms, technical manifestations, models, code, data, and
source occurrences_

<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Concept?

    For every given [Use Case](../use-case/index.md), we want to start with
    capturing the concepts and manifestations that the user or
    "the business" uses or wants to use.

    A **Concept** is a context-specific linking pin for a meaning.
    It is deliberately small: the Concept itself does not need to
    carry every label, ontology class, shape, data field, or code
    identifier.

    Instead, it links to
    [Concept Manifestations](../term/index.md): business names,
    synonyms, abbreviations, API parameters, query variables,
    ontology terms, shapes, taxonomy entries, and source occurrences.

    ## Why Concepts Matter

    Concepts ensure that:

    - **Business language is preserved** — We capture terms as the
      business uses them, not as some external standard defines them
    - **Semantic meaning is enabled** — Concepts link to technical
      manifestations that point at ontologies, shapes, taxonomies,
      code, and data
    - **Consistency is maintained** — The same concept can be reused
      across multiple use cases
    - **Interoperability is achieved** — Concepts can map to
      multiple ontologies, enabling integration across systems

    !!! tip "Start with business language"

        Don't worry about ontologies in the early stages.
        Focus on capturing what the business calls things and what
        those things mean in their context.

    ## Concept Vocabulary

    Concepts are organized into
    **[Concept Vocabularies](concept-vocabulary.md)**---collections of
    related concepts that share a common context or domain.

    Most concepts and manifestations will be pre-defined in all kinds
    of vocabularies. For brand-new use cases in a new domain,
    concepts and their manifestations may have to be created.

    Each Use Case can have its own vocabulary of concepts, but it can
    also inherit or borrow concepts from higher-level or related use
    cases in the [Use Case Tree](../use-case-tree.md).
    This enables reuse and consistency across the enterprise.

    For more information about how vocabularies are organized and
    managed, see [Concept Vocabulary](concept-vocabulary.md).

    ## Evolution and Refinement

    As the use case evolves and the understanding of the domain
    becomes clearer, it may be necessary to:

    - **Adjust concepts** — Better reflect the reality of the domain
    - **Map to ontologies** — Link concepts to more appropriate
      ontology terms, shapes, taxonomies, or other technical
      manifestations to ensure consistency and interoperability
      across the enterprise

    In either case, the important thing is to ensure that the
    captured concepts and manifestations accurately reflect the
    reality of the domain and the needs of the stakeholders.

=== "Data & Tech Audience"

    ## What Is a Concept in the Use Case Tree Method?

    A **Concept** is the linking pin between local business language,
    technical implementation, and formal semantic models.
    It stays deliberately thin. Business terms, technical identifiers,
    ontology resources, SHACL shapes, taxonomy entries, and source
    occurrences are modeled as Concept Manifestations.

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

    ### Mapping to ontologies and shapes

    Later in the use case's lifecycle, once the problem is well
    understood, the relevant ontologies, shapes, and taxonomies can be
    mapped to manifestations of the concepts captured earlier.
    This allows for better integration of the use case with the
    overall EKG ecosystem.

    !!! note "Implementation Detail"
        The mapping to OWL ontologies or SHACL shapes is primarily a
        technical implementation detail that is local to the specific
        use case. The Concept links to an OWL or SHACL manifestation;
        the manifestation points at the ontology resource or shape.

    ### Refinement and Evolution

    As the use case evolves and the understanding of the domain
    becomes clearer, it may be necessary to:

    - **Adjust captured concepts** — Better reflect the reality of
      the domain
    - **Map to appropriate ontologies** — Link to more appropriate
      ontology resources, shapes, taxonomies, or other technical
      manifestations to ensure consistency and interoperability
      across the enterprise

    ## Manifestation types

    Concepts do not need a class/property/shape subtype hierarchy.
    Their manifestations carry that detail:

    - **Business Terms** represent names, synonyms, and abbreviations.
    - **Technical Manifestations** represent API parameters, code
      identifiers, query variables, tables, and columns.
    - **OWL Manifestations** represent classes, properties,
      individuals, and axioms.
    - **SHACL Manifestations** represent node shapes and property
      shapes.
    - **SKOS Manifestations** represent concepts and concept schemes.

    ## Concepts as Linking Pins

    Concepts are the linking pin in many ways.
    They link Business Terms and Technical Manifestations as they are
    used in the context of the given use case, by the business and by
    programs, apps, systems, statements, ontologies, and data.

    !!! tip "Context-Specific Linking"

        In the distributed EKG architecture, Concepts provide the
        context-specific link between Stories and OWL ontology axioms.
        This allows use cases at various maturity levels to coexist—
        from early exploration to production-ready implementations.

        See [Distributed EKG Architecture](../../article/distributed-ekg.md)
        for more on this approach.

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
    of the same Concept and linked to it.
    Mappings to OWL axioms or SHACL shapes are Technical
    Manifestations, not direct properties of the Concept.

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

    - **[Use Cases](../use-case/index.md)** — Each use case has a vocabulary
      of concepts
    - **[Personas](../persona/index.md)** — Personas are Concepts, enabling
      semantic definition and reasoning
    - **[Stories](../story/index.md)** — Stories reference domain concepts
      that need to be understood and modeled
    - **[Ontologies](../ontology.md)** — Concepts link through
      manifestations to ontology classes, properties, axioms, and
      shapes

=== "Ontology"

    --8<-- "fragment/uctm-diagram-concept.md"

    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ### Concept

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

    - **Preferred Business Term**
        - A Concept does not need a traditional label such as
          `skos:prefLabel` or `rdfs:label`.
        - Instead, it can link to a preferred **BusinessTerm**.
        - Learn more in
          [Concept Manifestation](../term/index.md).

    - **Definition**
        - A Concept must have a business-focused definition explaining
          what it means in context.

    - **Zero or more manifestations**
        - A Concept can have zero or more
          `ConceptManifestation` resources.
        - Manifestations may include spellings, abbreviations,
          synonyms, variables, columns, ontology resources, shapes,
          taxonomy entries, and source occurrences.
        - A Concept can start empty and become meaningful as
          manifestations are discovered or curated.
        - Learn more in
          [Concept Manifestation](../term/index.md).

    - **Contained in a Concept Vocabulary**
        - A Concept is a member of a Concept Vocabulary (a “container” of Concepts).
        - A Use Case can relate to Concept Vocabularies via relationship-objects:
            - it can **reference** an external vocabulary and/or
            - **own** a private vocabulary.

    - **Mapping to ontologies (optional)**
        - A Concept can link to OWL, SHACL, SKOS, SQL, and source
          artifacts through Technical Manifestations.
        - The manifestation carries the resource or literal value and
          any provenance.

    - **Used by Stories and Workflows**
        - Stories use Concepts as **input**, **output**, and
          **dependent** concepts.
        - Workflows use Concepts through the Stories they orchestrate
          and the vocabulary of the Use Case.
