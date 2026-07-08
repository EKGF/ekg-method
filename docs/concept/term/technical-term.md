---
description: >-
  A machine-facing Concept Manifestation in code, data, metadata,
  queries, ontologies, shapes, taxonomies, APIs, or source
  repositories.
keywords:
  - technical manifestation
  - technical term
  - variable name
  - column header
  - API parameter
  - EKG method
schema_type: "Article"
---

# Technical manifestation

<!--summary-start-->

<!-- markdownlint-disable MD036 -->
_A machine-facing Concept Manifestation in code, data, metadata,
queries, ontologies, shapes, taxonomies, APIs, or source repositories_
<!-- markdownlint-enable MD036 -->

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a technical manifestation?

    A **Technical Manifestation** is how a
    [Concept](../concept/index.md) appears in the digital landscape:
    code, databases, APIs, statements, ontologies, shapes, and source
    repositories.

    Business Terms focus on how people talk. Technical Manifestations
    focus on how systems speak. Linking both to the same Concept gives
    traceability from business language to concrete implementation
    details.

    ## Why it matters

    - **Automated discovery**: repositories can be scanned for where
      Concepts appear.
    - **Impact analysis**: a Concept change can be traced to affected
      code, queries, columns, shapes, and ontology terms.
    - **Transparency**: business meaning is linked to the exact
      technical surfaces that implement it.

=== "Data & Tech Audience"

    ## Technical manifestations in code and data

    Technical Manifestations include symbols and resources such as:

    - variable names, for example `_customer` or `cust_id`
    - SPARQL variables, for example `?customer`
    - SQL columns and tables
    - Cypher labels, relationship types, and properties
    - API parameters and JSON field names
    - OWL classes, properties, individuals, and axioms
    - SHACL node shapes and property shapes
    - SKOS concepts and concept schemes

    ## Automated discovery

    Technical Manifestations can often be discovered automatically by
    scanning repositories and data artifacts. Each detected occurrence
    can become a `ManifestationOccurrence` linked to a stable
    Technical Manifestation.

    ## Semantic and validation artifacts

    OWL and SHACL bindings are Technical Manifestations too. A Concept
    should not directly say that it represents `hospital:Patient`.
    Instead, it links to an `OWLClassManifestation` whose
    `manifestationResource` is `hospital:Patient`.

    This keeps the Concept thin and lets one Concept have multiple
    ontology, shape, taxonomy, query, and code manifestations.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-technical-term.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ### TechnicalManifestation

    - **Subclass of ConceptManifestation**
        - All manifestation facts apply here.
    - **Literal value**
        - Use the exact token for variables, columns, identifiers,
          placeholders, and API parameters.
    - **Resource value**
        - Use an IRI for OWL, SHACL, SKOS, SQL, RDF, or other schema
          resources.
    - **Source occurrence**
        - Use an occurrence object for repository, file, line, column,
          commit, and language details.

    ### Recommended subtypes

    - `URIParameterManifestation`
    - `SPARQLVariableManifestation`
    - `SPARQLResultColumnManifestation`
    - `OWLClassManifestation`
    - `OWLPropertyManifestation`
    - `OWLAxiomManifestation`
    - `SHACLShapeManifestation`
    - `SKOSConceptManifestation`
    - `SQLTableManifestation`
    - `SQLColumnManifestation`
    - `CypherIdentifierManifestation`
    - `JavaScriptIdentifierManifestation`
    - `JSONFieldManifestation`
