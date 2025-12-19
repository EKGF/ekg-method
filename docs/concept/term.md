---
description: "A manifestation of a Concept: a business-facing or technical term (e.g., synonyms, abbreviations, variable names) that all mean the same thing in the Concept’s context. Learn how Terms work in the Use Case Tree Method."
keywords:
  - term
  - business term
  - technical term
  - concept term
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Term

<!--summary-start-->
_A manifestation of a Concept: the words (business-facing and technical) used to refer to the same underlying meaning_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Term?

    A **Term** is a word or phrase people use to refer to a [Concept](concept.md) in a given
    context.
    Concepts are about **meaning**; Terms are about **how that meaning shows up** in language.

    A Concept can have multiple Terms (synonyms, abbreviations, variations), but they all refer
    to the **same meaning** in the context of that Concept.

    ## Business Terms vs Technical Terms

    Terms come in two broad categories:

    - **Business Terms** — user-facing terminology used in conversations, documentation, UI, and
      policies (e.g., “Customer”, “Counterparty”, “Risk Position”)
    - **Technical Terms** — manifestations in code and data (e.g., variable names, column names,
      API parameters, query bindings)

    Treat both as Terms, because both are used by people, and both need to be linked back to the
    Concept so everyone stays aligned.

=== "Data & Tech Audience"

    ## Terms as Concept Manifestations

    A Term is a **manifestation** of a Concept.
    It can be:

    - a preferred business phrase
    - an abbreviation
    - a synonym
    - a technical symbol in code (e.g., `_customer`, `cust_id`, `?cust`, `/customers`)

    Terms allow the Knowledge Graph to connect human language and technical artifacts back to a
    consistent semantic core (the Concept).

    ## Discovering Technical Terms in code and data

    Technical Terms can often be **discovered automatically** by scanning the organization’s
    repositories and data artifacts:
    Python/Java code, SQL, configuration, CSV column headers, API specs, and more.

    Each detected manifestation becomes a **Technical Term** that links to:

    - the **Concept** it manifests, and optionally
    - the **Business Term** it corresponds to in that context.

    Example:
    If you detect the CSV header `P`, you can link that Technical Term to the Concept and also to
    the Business Term “Patient”.

    Technical Terms also include **semantic/validation artifacts** introduced later in the Use
    Case lifecycle (especially during the Build phase), such as:

    - OWL classes/properties/axioms in an ontology, and
    - SHACL shapes and constraints.

    In those cases, you link the Concept (and optionally a Business Term) to the ontology/shapes
    term via a **special mapping relationship** (e.g. “representsClass”, “representsProperty”,
    “constrainedByShape”), pointing at the ontology IRI.

    Example:
    If the Concept “patient” corresponds to the OWL class `hospital:Patient` in a Hospital
    ontology, create a Technical Term representing that ontology term and link it with something
    like **representsClass → `hospital:Patient`**.

    ## Preferred Term

    Concepts don’t need a traditional `rdfs:label` / `skos:prefLabel` label.
    Instead, a Concept can point to a **preferred Term** (a Term object) that represents the
    preferred expression in that context.

=== "Ontology"

    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-term.md"

    We're not (yet) prescribing a full OWL ontology here.
    But we can state a small set of **facts** that people can reliably use to build their own
    ontology / schema / graph model around a Term.

    ### Required facts about a Term

    - **Opaque universally unique identifier**
        - A Term should have an **opaque**, **universally unique** identifier.
        - Prefer a random identifier such as **UUIDv4**, represented as a URI:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **One or more forms (lexical variants)**
        - A Term must have **one or more textual forms** (the actual strings).
        - Business Terms often need multiple forms for different UI / communication contexts, for
          example:
            - **Singular**: “Patient”
            - **Plural**: “Patients”
            - **Abbreviation**: “Pat.”
            - **Short label**: “P”
        - These are variations of the **same Term** (think “sub-manifestations” of the Term).
          They should not be mixed with the forms of a different Term.

        Example:
        If “Patient” and “Client” are both used to mean the same thing in a given Use Case
        context, model them as **two separate Business Term objects**, each with their own
        lexical forms.
        Both Terms link to the same Concept, and the Concept defines the shared meaning.

    - **Term kind**
        - A Term should indicate whether it is a **Business Term** or a **Technical Term**.

    - **Owned by a Concept**
        - Terms are **owned** by a Concept (part-of): when the Concept is deleted, its Term
          objects are deleted as well.
        - A Concept must have **one or more Terms**.
        - All Terms for a Concept **mean the same thing** in that Concept’s context.

    ### Optional but useful facts

    - **Language**: natural language tag for business terms (e.g., `en`, `nl`)
    - **System / artifact**: where a technical term appears (e.g., codebase, dataset, API)
    - **Term subtype**: for technical terms (e.g., `VariableName`, `ColumnName`, `ApiFieldName`,
      `QueryBinding`)
    - **Provenance**: who introduced the term, when, and why

    ### Optional facts for Technical Terms (recommended)

    When a Term is discovered in code/data, capture **where it came from**:

    - **Repository URL** (e.g., GitHub repo)
    - **File path**
    - **Line range** (or equivalent location for non-text artifacts)
    - **Commit / tag / revision**
    - **Language / format** (e.g., Python, Java, SQL, CSV)
    - **Locator URL** (deep link to the exact source line / blob for traceability)

    When a Term represents an ontology or validation artifact, capture:

    - **Ontology / shape identifier** (IRI), e.g. `hospital:Patient`
    - **Mapping kind** (e.g., representsClass / representsProperty / constrainedByShape)

