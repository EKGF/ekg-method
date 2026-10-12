---
description: >-
  A business or technical expression of a Data Element Concept, such
  as a business term, code identifier, query variable, schema
  resource or shape.
keywords:
  - concept manifestation
  - manifestation
  - business term
  - technical manifestation
  - concept term
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Concept manifestation

<!--summary-start-->

_A business or technical expression of a Data Element Concept in
language, code, data, metadata or schemas_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a concept manifestation?

    A **Concept Manifestation** is a visible form of a
    [Data Element Concept](../concept/index.md), or Concept for short.
    Concepts are about meaning. Manifestations are how that meaning
    shows up.

    A Concept can have many manifestations:

    - business names, synonyms, and abbreviations
    - labels used in documentation or user interfaces
    - report column names and spreadsheet headers
    - API field names and parameter names
    - ontology terms and validation shapes

    The same Concept can be reused across contexts. Its
    manifestations give that shared meaning observable forms in
    different languages and systems.

    ## Business terms and technical manifestations

    Manifestations come in two broad groups:

    - **[Business Terms](business-term.md)** are human-facing
      manifestations used in conversations, documentation, UI, and
      policies.
    - **[Technical Manifestations](technical-term.md)** are
      machine-facing manifestations in code, queries, schemas,
      ontologies, shapes, APIs, and source repositories.

    Treat both as manifestations because both need to be linked back
    to the Concept.

=== "Data & Tech Audience"

    ## Expressions of a shared meaning

    A manifestation expresses a Concept in a particular form.
    It can be:

    - a preferred business phrase
    - an abbreviation or synonym
    - a JavaScript, Python, SQL, SPARQL, or Cypher identifier
    - an API path parameter or query parameter
    - an OWL class, OWL property, or OWL axiom
    - a SHACL shape or property shape
    - a SKOS concept or concept scheme

    This lets the Knowledge Graph connect human language and technical
    artifacts back to the same Concept without putting schema-specific
    claims directly on the Concept.

    A `ManifestationOccurrence` records evidence that a manifestation
    appears at a particular source location. Several occurrences can
    refer to the same manifestation.

    ## Discovering manifestations

    Manifestations can be created manually, but many can be discovered
    by scanning repositories and data artifacts:

    - source code
    - SQL, SPARQL, Cypher, and GQL statements
    - RDF, OWL, SHACL, and SKOS files
    - API specifications
    - CSV files and database schemas

    Each detected occurrence can point at the manifestation it
    observed, including repository, file path, line, column, commit,
    and language or format.

    ## Preferred manifestation

    Concepts do not need to carry their own display labels. Instead,
    a Concept can point at a preferred Business Term. Technical roles
    can also have preferred manifestations, such as the preferred API
    parameter or preferred SPARQL placeholder.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-term.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ### ConceptManifestation

    - **Opaque universally unique identifier**
        - A manifestation should have an opaque, universally unique
          identifier.
        - Prefer a random identifier such as UUIDv4, represented as
          a URI:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **Belongs to a Concept**
        - A manifestation links to its `DataElementConcept` through
          `ekg-concept:concept`, the inverse of `hasManifestation`.
        - A Concept can have zero or more manifestations.
        - The same real-world token may appear as separate
          manifestations when two Concepts intentionally do not mean
          the same thing.

    - **Manifestation kind**
        - A manifestation should state its kind, such as
          `BusinessTerm`, `TechnicalManifestation`,
          `OWLClassManifestation`, `SHACLShapeManifestation`,
          `SQLColumnManifestation`, or
          `JavaScriptIdentifierManifestation`.

    ### Optional but useful facts

    - **Literal form**: exact string, label, slug, variable, or token.
    - **Resource form**: RDF IRI for an OWL, SHACL, SKOS, SQL, or
      other schema resource.
    - **Language**: natural language tag for business terms.
    - **System or artifact**: where the manifestation appears.
    - **Provenance**: who introduced it, when, and why.

    ### Optional source occurrence facts

    When a manifestation is discovered in code or data, record a
    `ManifestationOccurrence` linked through `occurrenceOf` and
    capture where it came from:

    - **Repository URL**
    - **File path**
    - **Line and column**
    - **Commit, tag, or revision**
    - **Language or format**
    - **Locator URL**
