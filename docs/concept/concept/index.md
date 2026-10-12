---
description: >-
  A reusable concept identifying the meaning of a data element or
  compound data construct, independently of its business or technical
  manifestations.
keywords:
  - data element concept
  - ISO/IEC 11179
  - concept
  - domain concept
  - business concept
  - semantic model
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Data Element Concept

<!--summary-start-->

_A reusable concept identifying the meaning of a data element or
compound data construct, independently of its particular business
or technical manifestations_

<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Concept?

    For every given [Use Case](../use-case/index.md), we want to start with
    capturing the concepts and manifestations that the user or
    "the business" uses or wants to use.

    A **Data Element Concept**, called a **Concept** for short,
    identifies a shared meaning. Reuse that Concept wherever the
    same meaning applies, across use cases, languages and systems.
    It can describe an individual data element, such as a customer
    identifier, or a compound construct, such as a whole customer
    record.

    Users and code encounter it through
    [Concept Manifestations](../term/index.md): business names,
    synonyms, abbreviations, API parameters, query variables,
    ontology terms, shapes and taxonomy entries. For example,
    "Customer identifier", `?customerId` in SPARQL and `customer_id`
    in Python can express the same Concept.

    A Concept is not inherently tied to one context. Separate
    Concepts can be created where needed, but reuse is the intended
    practice. Independently created Concepts may later be merged
    when their owners establish that they mean the same thing.

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

    The formal class is `ekg-concept:DataElementConcept` in the
    [EKGF Concept Ontology](https://github.com/EKGF/ekg-ontologies/blob/main/ekgf-concept.ttl).
    "Concept" is the everyday short form. `ConceptSet`,
    `ConceptManifestation` and properties such as `hasConcept` retain
    that short form.

    The Concept identifies the shared meaning. Its manifestations
    and graph relationships express and describe that meaning.
    Business terms, technical identifiers, ontology resources,
    SHACL shapes and taxonomy entries are represented through
    Concept Manifestations. A `ManifestationOccurrence` records a
    particular sighting of a manifestation in a source.

    ## Relationship to ISO/IEC 11179

    This class deliberately generalizes the data element concept in
    [ISO/IEC 11179-31:2023](https://www.iso.org/standard/78925.html),
    section 3.25. It follows the distinction between meaning and
    representation. The ISO model associates a data element concept
    with an object class and a property, such as Customer and
    Identifier.

    Our scope also includes compound data constructs, such as whole
    entity types and structured records. An entire OWL class or
    SHACL shape can be a manifestation of a Concept. This broader
    scope does not assert formal equivalence to the ISO model.

    A Data Element Concept has no `skos:Concept` superclass. SKOS
    resources can be linked through `SKOSConceptManifestation` or
    `SKOSConceptSchemeManifestation` resources.

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
        The Concept links to an OWL or SHACL manifestation; the
        manifestation points at the ontology resource or shape.
        Several use cases can reuse the same Concept while selecting
        the manifestations appropriate to their implementations.

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

    ## Shared meaning across manifestations

    Concepts connect Business Terms and Technical Manifestations
    across programs, apps, systems, statements, ontologies and data.

    !!! tip "Reuse across contexts"

        In the distributed EKG architecture, Stories can share a
        Concept while using different technical manifestations.
        Exploratory and production use cases can reuse the same
        meaning at different stages of implementation.

        See [Distributed EKG Architecture](../../article/distributed-ekg.md)
        for more on this approach.

    **Example:**

    A customer-identifier Concept can appear in different forms:

    - On forms as "Customer identifier" or "Customer ID"
    - In Python code as `customer_id`
    - In SPARQL statements as `?customerId`
    - In database schemas as `customer_id`
    - In API parameters as `customerId`

    These manifestations can link to the same Concept wherever that
    meaning is reused. Matching names alone do not establish that
    two manifestations express the same meaning.

    A Concept for the whole Customer construct can likewise have an
    OWL class and a SHACL shape as technical manifestations. Those
    manifestations link to the class or shape through
    `manifestationResource`.

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

    - **Reuse first** — Use an existing Concept wherever its meaning
      fits, even when a different name or technical form is needed
    - **Inheritance** — Lower-level use cases inherit concepts from
      parent use cases in the Use Case Tree
    - **Borrowing** — Use cases can reference concepts from related
      use cases
    - **New definitions** — Create a separate Concept when needed;
      a new context alone does not require one
    - **Reconciliation** — Owners can merge independently created
      Concepts when they establish that their meanings are the same

    This ensures that concepts are not duplicated unnecessarily and
    that the EKG maintains semantic consistency across the enterprise.

    ## Relationship to Other Concepts

    Concepts are fundamental building blocks that relate to:

    - **[Use Cases](../use-case/index.md)** — Each use case has a vocabulary
      of concepts
    - **[Personas](../persona/index.md)** — Personas interact with
      Stories using the business manifestations of their Concepts
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

    ### DataElementConcept

    The class IRI is `ekg-concept:DataElementConcept`, where the
    `ekg-concept` namespace is `https://ekgf.org/ontology/concept#`.
    "Concept" remains the short form throughout the Method.

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
        - Describe the shared meaning through business-facing
          manifestations and graph relationships.
        - The meaning can be reused across contexts.

    - **Zero or more manifestations**
        - A Concept can have zero or more
          `ConceptManifestation` resources.
        - Manifestations may include spellings, abbreviations,
          synonyms, variables, columns, ontology resources, shapes,
          and taxonomy entries.
        - Source sightings are `ManifestationOccurrence` resources
          linked to manifestations through `occurrenceOf`.
        - A Concept can be identified before its manifestations are
          discovered or curated.
        - Learn more in
          [Concept Manifestation](../term/index.md).

    - **Contained in a Concept Vocabulary**
        - A Concept Vocabulary is represented by `ConceptSet`.
        - `inConceptSet` links a Concept to a set. Membership does
          not make its meaning local to that vocabulary.
        - A Use Case can relate to Concept Vocabularies via relationship-objects:
            - it can **reference** an external vocabulary and/or
            - **own** a private vocabulary.

    - **Mapping to ontologies (optional)**
        - A Concept can link to OWL, SHACL, SKOS, SQL, and source
          artifacts through Technical Manifestations.
        - The manifestation carries the resource or literal value and
          its occurrences record source provenance.

    - **Used by Stories and Workflows**
        - Stories use Concepts as **input**, **output**, and
          **dependent** concepts.
        - Workflows use Concepts through the Stories they orchestrate
          and the vocabulary of the Use Case.

    ### Class IRI migration

    Replace references to the retired `ekg-concept:Concept` class
    with `ekg-concept:DataElementConcept` in RDF, queries, shapes and
    consumer code. There is no compatibility alias. The namespace,
    `ConceptSet`, `ConceptManifestation` and property names retain
    their short forms.
