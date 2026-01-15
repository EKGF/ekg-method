---
description: >-
  A formal, machine-readable specification of concepts and their
  relationships that bridges the gap between demand (Use Cases) and
  supply (Data Products). Learn how ontologies enable semantic
  interoperability in the Use Case Tree Method.
keywords:
  - ontology
  - semantic model
  - knowledge representation
  - EKG method
  - enterprise knowledge graph
  - data modeling
schema_type: "Article"
---

# Ontology

<!--summary-start-->

_A formal, machine-readable specification of concepts and their
relationships that bridges the gap between demand (Use Cases) and
supply (Data Products) in the data economy_

<!--summary-end-->

=== "Business & Management Audience"

    ## What Is an Ontology?

    An **Ontology** is a formal specification of concepts and their
    relationships that provides a common language for describing
    business knowledge.
    In the context of the Enterprise Knowledge Graph, ontologies act
    as a crucial intermediary between the demand and supply sides of
    the information economy.

    ## The Role of Ontologies in the Data Economy

    Think of the data economy as having two sides:

    - **Demand side** — [Use Cases](use-case/index.md) represent the
      demands for information from various stakeholders.
      They define what data is needed and why.
    - **Supply side** — [Data Products](data-product.md) represent
      the supply of information.
      They define what data is available and how it can be accessed.

    **Ontologies bridge the gap** between these two sides by
    providing a common language that can be used to describe the
    [Concepts](concept/index.md) and relationships relevant to both the
    demand and supply sides.

    !!! tip "Common language"

        Ontologies enable use cases and data products to "speak the
        same language," making it possible to match what's needed with
        what's available.

    ## Why Ontologies Matter

    Ontologies enable:

    - **Semantic integration** — Different systems can understand
      each other's data because they share the same semantic model
    - **Reuse** — Concepts defined once in an ontology can be reused
      across multiple use cases and data products
    - **Consistency** — Ensures that the same concept means the same
      thing everywhere
    - **Automated reasoning** — Machines can understand and reason
      about business concepts
    - **Interoperability** — Enables integration across diverse
      systems and technologies

    This enables a more efficient and effective exchange of
    information, allowing organizations to better leverage their data
    assets and achieve their business objectives.

=== "Data & Tech Audience"

    ## What Is an Ontology in the Use Case Tree Method?

    An **Ontology** is a formal, machine-readable specification of
    concepts and their relationships, typically expressed using
    standards like OWL (Web Ontology Language) or SHACL (Shapes
    Constraint Language).

    In the Use Case Tree Method, ontologies serve as the semantic foundation
    that enables the Enterprise Knowledge Graph to understand and
    reason about business concepts.

    ## Ontologies as Intermediaries

    Ontologies act as a crucial intermediary between the demand and
    supply sides of the information economy:

    - **Demand side** — [Use Cases](use-case/index.md) represent the
      demands for information from various stakeholders.
      They define what data is needed and why.
    - **Supply side** — [Data Products](data-product.md) represent
      the supply of information.
      They define what data is available and how it can be accessed.

    The ontologies help bridge the gap between these two sides by
    providing a common language that can be used to describe the
    concepts and relationships relevant to both the demand and supply
    sides.

    ## How Ontologies Bridge the Gap

    Ontologies enable semantic matching between use cases and data
    products:

    1. **Use Cases define concepts** — Each use case has a
       vocabulary of [Concepts](concept/index.md) that represent the
       domain knowledge it needs
    2. **Concepts link to ontologies** — Concepts are linked to
       ontology classes, properties, and shapes that define their
       semantic meaning
    3. **Data Products conform to ontologies** — Data products
       specify which ontologies their datasets conform to
    4. **Semantic matching** — The EKG can match use cases to data
       products based on shared ontology concepts

    This semantic matching enables the EKG to automatically discover
    which data products can fulfill the requirements of a given use
    case.

    ## Ontology Standards

    Ontologies in the Use Case Tree Method typically use:

    - **OWL (Web Ontology Language)** — For defining classes,
      properties, and relationships with rich logical expressivity
    - **SHACL (Shapes Constraint Language)** — For defining
      validation constraints and data shapes
    - **RDFS (RDF Schema)** — For basic class and property
      hierarchies

    These standards enable:

    - **Machine readability** — Ontologies can be processed by
      automated systems
    - **Reasoning** — Automated reasoners can infer new knowledge
      from ontology definitions
    - **Validation** — Data can be validated against ontology
      constraints
    - **Interoperability** — Different systems can share and reuse
      ontology definitions

    ## Relationship to Concepts

    [Concepts](concept/index.md) serve as the linking pin between business
    language and ontologies:

    - **Business language** — Concepts capture the terms and ideas
      that the business uses
    - **Ontology mapping** — Concepts link to ontology classes,
      properties, and shapes that define their semantic meaning
    - **Multiple mappings** — A single concept can map to multiple
      ontologies, enabling integration across different standards

    This dual nature allows the EKG to address "the business" with
    their language while maintaining formal semantic models that
    enable automated reasoning and integration.

    ## Reuse and Standardization

    Ontologies enable reuse and standardization:

    - **Standard ontologies** — Organizations can use existing
      standard ontologies (e.g., FIBO, CDM, schema.org) rather than
      creating everything from scratch
    - **Domain ontologies** — Domain-specific ontologies can be
      created and reused across use cases in the same domain
    - **Extension** — Standard ontologies can be extended to meet
      specific organizational needs
    - **Composition** — Multiple ontologies can be combined to
      create comprehensive semantic models

    This reuse ensures consistency across the enterprise and enables
    interoperability with external systems and standards.

    ## Relationship to Other Concepts

    Ontologies relate to other core concepts:

    - **[Concepts](concept/index.md)** — Concepts link to ontology
      classes, properties, and shapes to define their semantic
      meaning
    - **[Use Cases](use-case/index.md)** — Use cases have vocabularies of
      concepts that link to ontologies
    - **[Data Products](data-product.md)** — Data products specify
      which ontologies their datasets conform to
    - **[Personas](persona/index.md)** — Personas are Concepts that link
      to ontology classes, enabling semantic definition

    This integration ensures that ontologies are not isolated
    specifications but part of a cohesive, semantic model of the
    enterprise.

    ## Ontologies in the EKG

    !!! tip "Distributed Architecture"

        Unlike traditional knowledge graph projects that load a single
        copy of each ontology into one monolithic graph, an EKG can
        consist of many knowledge graphs—each with their own versions
        of ontologies. This distributed, context-specific approach is
        fundamental to how the Use Case Tree Method works.

        See [Distributed EKG Architecture](../article/distributed-ekg.md)
        for a detailed explanation.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-ontology.md"

    ## Facts

    !!! abstract "Why this tab is different"

        This page is a bit "meta" — we're using ontological concepts
        to describe the concept of Ontology itself. On other pages in
        this method, we show minimal facts about business concepts
        like Use Case, Persona, or Outcome. Here, we're documenting
        what an OWL Ontology technically consists of.

        The terminology below (Classes, Properties, Individuals,
        Axioms) comes from the OWL 2 Web Ontology Language standard.
        Don't worry if it feels abstract — this is reference material
        for those building formal ontologies.

    ### Ontology

    Based on the OWL 2 Web Ontology Language, an Ontology consists of:

    - **Ontology IRI**
        - An Ontology must have an **IRI** (Internationalized Resource
          Identifier) that uniquely identifies it.
        - Example: `https://example.org/ontologies/my-ontology`

    - **Version IRI (optional)**
        - An Ontology may have a **version IRI** that identifies a
          specific version.
        - This enables versioning and evolution of ontologies over time.

    - **Imports**
        - An Ontology can **import** zero or more other ontologies
          via `owl:imports`.
        - Imported ontologies become part of the importing ontology's
          knowledge base.

    ### Classes

    - **Class** (`owl:Class`)
        - Represents a category or type of thing.
        - Classes can be organized in hierarchies using `rdfs:subClassOf`.
        - Example: `Person`, `Organization`, `LegalEntity`

    ### Properties

    Properties define relationships and have three subtypes:

    - **Object Property** (`owl:ObjectProperty`)
        - Relates individuals to other individuals.
        - Has a domain (subject type) and range (object type).
        - Example: `worksFor` relates a `Person` to an `Organization`

    - **Data Property** (`owl:DatatypeProperty`)
        - Relates individuals to literal data values.
        - Has a domain (subject type) and range (datatype).
        - Example: `birthDate` relates a `Person` to an `xsd:date`

    - **Annotation Property** (`owl:AnnotationProperty`)
        - Provides metadata about ontology elements.
        - Does not affect reasoning.
        - Example: `rdfs:label`, `rdfs:comment`, `skos:definition`

    ### Individuals

    !!! note "Terminology note"

        In ontology terminology, "Individual" does not mean a person.
        It's ontologist-speak for a specific object or instance in
        the graph — any concrete thing that belongs to a class.

    - **Named Individual** (`owl:NamedIndividual`)
        - Represents a specific instance of a class.
        - Has an IRI that uniquely identifies it.
        - Example: A specific person, organization, or any other
          concrete entity in your knowledge graph

    ### Axioms

    Axioms are statements that define the semantics:

    - **Class Axioms**
        - Subclass relationships (`rdfs:subClassOf`)
        - Equivalence (`owl:equivalentClass`)
        - Disjointness (`owl:disjointWith`)

    - **Property Axioms**
        - Domain and range declarations
        - Property characteristics (transitive, symmetric, functional)
        - Sub-property relationships

    - **Individual Axioms**
        - Class assertions (typing)
        - Property assertions (relationships between individuals)
        - Same/different individual declarations

    ### Relationship to SHACL

    While OWL defines the ontological structure, **SHACL** (Shapes
    Constraint Language) complements it by defining:

    - **Shapes** — Validation constraints on data
    - **Property constraints** — Cardinality, value types, patterns
    - **Node constraints** — Requirements for specific nodes

    Together, OWL and SHACL provide a complete semantic and validation
    framework for the Enterprise Knowledge Graph.
