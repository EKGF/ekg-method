---
description: >-
  User-facing terminology used in conversations, documentation, UI,
  and policies. Learn how Business Terms link to Concepts in the Use
  Case Tree Method.
keywords:
  - business term
  - term
  - glossary
  - vocabulary
  - EKG method
schema_type: "Article"
---

# Business Term

<!--summary-start-->

_User-facing terminology used in conversations, documentation, UI, and
policies_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a Business Term?
    A **Business Term** is a human-readable label for a [Concept](../concept/index.md). It represents how business users speak about a specific meaning within a given context.

    By linking multiple Business Terms (synonyms) to a single Concept, the Enterprise Knowledge Graph ensures that everyone is talking about the same underlying meaning even if they use different words.

    ## Key Characteristics
    - **User-facing**: Used in documentation, policies, and user interfaces.
    - **Context-specific**: A term might mean different things in different contexts, but it always links to a specific Concept that defines its meaning in *this* context.
    - **Synonym support**: Multiple business terms can manifest the same Concept.

    ## Examples
    - “Customer”
    - “Counterparty”
    - “Risk Position”

=== "Data & Tech Audience"

    ## Business Terms as Concept Manifestations
    From a technical perspective, a Business Term is a specific type of [Term](index.md) that provides the human-readable "face" of a Concept.

    ## Lexical Variants
    A single Business Term often has multiple forms for different communication contexts:

    - **Singular**: “Patient”
    - **Plural**: “Patients”
    - **Abbreviation**: “Pat.”
    - **Short label**: “P”

    These are variations of the **same Business Term object**. If two different words are used (e.g., “Patient” and “Client”), they should be modeled as two separate Business Term objects linking to the same Concept.

=== "Ontology"

    ## Ontology (minimal facts we can state today) {: #ontology }

    --8<-- "fragment/uctm-diagram-business-term.md"

    ### Required facts about a Business Term
    - **Inherits from Term**: All facts required for a [Term](index.md#ontology) (UUID, lexical forms, ownership) apply here.
    - **Term Kind**: Must be identified as a "Business Term".
    - **Language**: Should include a natural language tag (e.g., `en`, `nl`).

    ### Relationship to Concept
    - **Owned by Concept**: A Business Term is a part-of a Concept. If the Concept is deleted, the Business Term is deleted.
