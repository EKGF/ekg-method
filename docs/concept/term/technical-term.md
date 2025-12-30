---
description: >-
  Technical manifestations of a Concept in code, data, and metadata.
  Learn how Technical Terms bridge the gap between human language and
  machine-readable data.
keywords:
  - technical term
  - variable name
  - column header
  - API parameter
  - EKG method
schema_type: "Article"
---

# Technical Term

<!--summary-start-->

_Technical manifestations of a Concept in code, data, and metadata_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a Technical Term?
    A **Technical Term** is the manifestation of a [Concept](../concept.md) in the digital landscape—code, databases, and APIs.

    While Business Terms focus on how people talk, Technical Terms focus on how systems "speak." Linking these together in the Knowledge Graph provides 100% traceability from a high-level business requirement down to the exact database column or line of code.

    ## Why it Matters
    - **Automated Discovery**: We can scan codebases to find where business concepts are actually implemented.
    - **Impact Analysis**: See how a change in business logic affects specific technical components.
    - **Transparency**: Provides a clear map of how data flows through the enterprise.

=== "Data & Tech Audience"

    ## Technical Terms in Code and Data
    Technical Terms include any symbol or identifier used in technical artifacts:

    - **Variable names** (e.g., `_customer`, `cust_id`, `?cust`)
    - **Database columns** (e.g., `P_NAME`, `CLIENT_REF`)
    - **API parameters** (e.g., `/customers/{id}`)

    ## Automated Discovery
    Technical Terms are often discovered automatically by scanning repositories (Python, Java, SQL, CSV, etc.). Each detected manifestation becomes a Technical Term that links back to the Concept.

    ## Semantic & Validation Artifacts
    Later in the lifecycle (Build phase), Technical Terms also represent:

    - **OWL classes and properties** in an ontology.
    - **SHACL shapes** and constraints.

=== "Ontology"

    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-technical-term.md"

    ### Required facts about a Technical Term
    - **Inherits from Term**: All facts required for a [Term](index.md#ontology) apply.
    - **Term Kind**: Must be identified as a "Technical Term".
    - **Provenance (Source Location)**: Must capture where the term was found:
        - **Repository URL**
        - **File path & Line range**
        - **Commit / Revision**

    ### Optional but Recommended
    - **System / Artifact**: The specific system where the term resides.
    - **Mapping Kind**: For ontology terms (e.g., `representsClass`, `constrainedByShape`).
