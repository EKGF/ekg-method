---
title: Concept Vocabulary
description: >-
  A collection of related concepts that share a common context or
  domain, enabling reuse and consistency across use cases in the Use
  Case Tree Method.
keywords:
  - concept vocabulary
  - vocabulary
  - SKOS concept scheme
  - domain vocabulary
  - EKG method
  - enterprise knowledge graph
authors:
  - Jacobus Geluk
date: 2024-12-30
schema_type: "Article"
---

# Concept Vocabulary

<!--summary-start-->

_A collection of related concepts that share a common context or
domain, enabling reuse and consistency across use cases_

<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Concept Vocabulary?

    A **Concept Vocabulary** is a collection of related
    [Concepts](index.md) that share a common context or domain. Think
    of it as a dictionary or glossary specific to a particular area of
    your business---it groups together all the concepts and their terms
    that make sense to use together.

    Just as you might have a "Finance Vocabulary" or a "Product
    Management Vocabulary" in your organization, the Use Case Tree
    Method organizes concepts into vocabularies to keep things clear
    and reusable.

    ## How Concepts Work with Terms

    An important characteristic of our Concept Vocabularies is how
    concepts relate to the actual words people use:

    - A **Concept** in our model is essentially just a unique
      identifier (a random UUID) that represents an idea or thing in
      your domain
    - This concept can have **multiple Terms** associated with it---the
      actual words or phrases people use to refer to that concept
    - This is a **one-to-many relationship**: one concept, potentially
      many terms

    ### Why Multiple Terms?

    In a given context, people often use different words for the same
    thing:

    **Example: Hospital Context**

    > In a hospital use case, the concept of "a person receiving care"
    > might have multiple terms:
    >
    > - "Patient" — medical staff terminology
    > - "Client" — administrative perspective
    > - "Customer" — billing department
    > - "Visitor" — reception desk
    >
    > All these terms refer to the same underlying concept in this
    > hospital context, so they're grouped under one Concept identifier.

    ### Context Matters

    The same terms might mean completely different things in other
    contexts:

    - "Patient" in a hospital means something different than "patient"
      in a legal context (someone waiting)
    - "Client" in a hospital is different from "client" in a law firm
    - Each use case defines its own concepts that make sense in its
      context

    The Concept (the UUID) ties together all the terms that mean the
    same thing **in your specific use case context**.

    !!! note "Terms are reusable, Concepts are context-specific"

        The **terms** themselves (like "patient", "client") can be
        reused across many vocabularies and use cases. But the
        **concept** that groups those terms together is specific to the
        use case's context and meaning.

    ## Why Use Concept Vocabularies?

    Concept Vocabularies serve several important purposes:

    1. **Organization** — Keeps related concepts together in meaningful
       groupings

    2. **Reuse** — Allows multiple use cases to share the same
       vocabulary without duplicating concepts

    3. **Consistency** — Ensures that the same terms mean the same
       things across different parts of the organization

    4. **Ownership** — Clarifies who is responsible for defining and
       maintaining concepts in each domain

    !!! tip "One vocabulary, many use cases"

        A well-defined vocabulary can serve multiple use cases. For
        example, a "Customer Vocabulary" might be used by Customer
        Service, Sales, Marketing, and Analytics use cases.

    ## Types of Vocabularies

    There are typically two types of Concept Vocabularies:

    ### External (Referenced) Vocabularies

    These are vocabularies defined elsewhere---either by other teams,
    other use cases, or industry standards---that your use case
    references and uses.

    **Characteristics:**

    - Not owned by your use case
    - Shared across multiple use cases
    - Changes are controlled by the vocabulary owner
    - Promotes consistency across the enterprise

    **Example:**

    > The "Customer Service Use Case" references the enterprise-wide
    > "Customer Vocabulary" maintained by the Customer Data team.

    ### Private (Owned) Vocabularies

    These are vocabularies created specifically for your use case,
    containing concepts unique to your domain or context.

    **Characteristics:**

    - Owned by your use case
    - Can be evolved as the use case evolves
    - May eventually become shared vocabularies if useful to others
    - Useful for novel or highly specific domains

    **Example:**

    > The "Fraud Detection Use Case" creates its own private vocabulary
    > containing fraud-specific concepts like "Suspicious Pattern",
    > "Alert Threshold", and "Investigation Status".

    ## When to Create a New Vocabulary

    Create a new Concept Vocabulary when:

    - **New domain** — You're working in a domain that doesn't have
      existing vocabularies
    - **Unique terminology** — Your use case needs concepts that don't
      exist elsewhere
    - **Evolution needed** — Existing vocabularies don't quite fit and
      you need flexibility to evolve
    - **Experimentation** — You're exploring new concepts before
      proposing them for wider use

    ## When to Reference an Existing Vocabulary

    Reference an existing Concept Vocabulary when:

    - **Standard concepts** — The concepts you need are already defined
    - **Consistency matters** — You want to ensure alignment with other
      use cases
    - **Proven vocabulary** — An established vocabulary meets your
      needs
    - **Integration** — You need to integrate with systems using that
      vocabulary

    ## Evolution Path

    Many vocabularies start as private and evolve to become shared:

    1. **Start private** — Create a vocabulary specific to your use
       case
    2. **Prove value** — Demonstrate that the concepts are useful and
       well-defined
    3. **Generalize** — Remove use case-specific details and make
       concepts more generally applicable
    4. **Share** — Publish the vocabulary for other use cases to
       reference
    5. **Maintain** — Establish governance for the shared vocabulary

=== "Vocabulary Management"

    ## Governance

    Each Concept Vocabulary should have clear governance:

    ### Ownership

    - **Owner** — Who is responsible for the vocabulary?
    - **Maintainers** — Who can make changes?
    - **Stakeholders** — Who should be consulted for major changes?

    ### Versioning

    - Vocabularies should be versioned
    - Changes should be tracked and communicated
    - Backward compatibility should be considered
    - Deprecation policies should be defined

    ### Documentation

    - Each vocabulary should have clear purpose and scope
    - Concepts should be well-defined
    - Examples should be provided
    - Usage guidelines should be documented

    ## Discovery and Reuse

    To maximize reuse, vocabularies should be:

    - **Discoverable** — Listed in a central catalog
    - **Searchable** — Easy to find by topic or term
    - **Well-described** — With clear purpose and scope
    - **Example-rich** — Showing real usage

    !!! note "Vocabulary Catalog"

        Organizations should maintain a catalog of available
        vocabularies to promote discovery and reuse. This can be as
        simple as a wiki page or as sophisticated as a dedicated
        vocabulary management system.

    ## Quality Criteria

    A good Concept Vocabulary:

    1. **Focused** — Has a clear, well-defined scope
    2. **Cohesive** — Contains related concepts that belong together
    3. **Complete** — Includes all concepts needed for its domain
    4. **Consistent** — Uses terminology consistently throughout
    5. **Clear** — Has unambiguous definitions
    6. **Useful** — Serves actual use case needs

    ## Antipatterns to Avoid

    ### The Mega-Vocabulary

    **Problem:** Trying to put all concepts in one massive vocabulary

    **Solution:** Break into focused, domain-specific vocabularies

    ### The Ghost Vocabulary

    **Problem:** Creating vocabularies that nobody actually uses

    **Solution:** Build vocabularies from real use case needs, not
    speculation

    ### The Orphan Vocabulary

    **Problem:** Vocabularies with no clear owner or maintainer

    **Solution:** Assign ownership and maintenance responsibilities

    ### The Frozen Vocabulary

    **Problem:** Vocabularies that can't evolve with changing needs

    **Solution:** Establish change management processes that balance
    stability with evolution

=== "Relationships"

    ## Relationship to Concepts

    [Concepts](index.md) are the members of a Concept Vocabulary.
    Using the SKOS (Simple Knowledge Organization System) standard:

    - A Concept Vocabulary is a `skos:ConceptScheme`
    - A Concept is a `skos:Concept`
    - Concepts belong to a vocabulary via `skos:inScheme`

    This follows established W3C standards for organizing concepts.

    ## Relationship to Use Cases

    [Use Cases](../use-case/index.md) relate to Concept Vocabularies in
    two ways:

    ### Reference Relationship

    - Use case **references** an external vocabulary
    - Use case reads and uses concepts from the vocabulary
    - Use case does not own or control the vocabulary
    - Changes to the vocabulary affect the use case

    ### Ownership Relationship

    - Use case **owns** a private vocabulary
    - Use case defines and maintains the concepts
    - Use case can evolve the vocabulary as needed
    - Deleting the use case may delete the vocabulary

    A single use case can both reference some vocabularies and own
    others.

    ## Relationship to Stories

    [Stories](../story.md) use concepts from vocabularies through
    [Story/Concept Relationships](story-concept-relationship.md):

    - Stories reference concepts for inputs, outputs, and dependencies
    - Stories use the vocabulary of their parent use case
    - Stories may span multiple vocabularies if their use case
      references multiple vocabularies

    ## Relationship to Terms

    [Terms](../term/index.md) are part of concepts, which are part of
    vocabularies:

    - A Concept Vocabulary contains multiple Concepts
    - Each Concept has one or more Terms
    - Terms provide the actual labels and names used in different
      contexts

=== "Ontology"

    --8<-- "fragment/uctm-diagram-concept-vocabulary.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ## Technical Model

    A Concept Vocabulary is a container for related concepts:

    ### Extension of SKOS

    While a Concept Vocabulary is technically a `skos:ConceptScheme`
    following W3C SKOS standards, we extend the model in an important
    way:

    **Standard SKOS:**

    - A `skos:Concept` has labels directly attached
      (`skos:prefLabel`, `skos:altLabel`)
    - Labels are properties of the concept itself

    **Use Case Tree Method Extension:**

    - A **Concept** is essentially just a **universally unique
      identifier** (UUID)
    - The Concept identifier represents the abstract idea or thing
    - The Concept has a **one-to-many relationship** with **Terms**
    - Terms are the actual manifestations---the words and phrases
      people use
    - A Concept can have multiple Terms, each representing different
      ways people refer to the same thing in a given context

    **Why this matters:**

    In a given use case context, people often use multiple words for
    the same concept:

    ```
    Concept: urn:uuid:a1b2c3d4-... (hospital visitor concept)
    ├── Term: "Patient" (medical staff usage)
    ├── Term: "Client" (administrative usage)
    ├── Term: "Customer" (billing department usage)
    └── Term: "Visitor" (reception desk usage)
    ```

    All these terms refer to the same underlying concept **in this
    hospital use case's context**. In other contexts, these same terms
    might mean completely different things and wouldn't be grouped
    together.

    **Key insight:**

    - **Concepts** (the UUID identifier) are **context-specific** to
      the use case
    - **Terms** (the actual words) are **reusable** across many
      contexts
    - The Concept binds together all the terms that mean the same thing
      in your specific use case context

    This separation allows:

    - Different use cases to use the same terms with different meanings
    - One use case to group multiple terms under one concept
    - Clear traceability of which terms are considered equivalent in
      which contexts

    ### Required facts

    - **Identifier**
        - A Concept Vocabulary must have an **opaque**, **universally
          unique** identifier
        - Prefer a random identifier such as **UUIDv4**, represented as
          a URI:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **Name**
        - A Concept Vocabulary must have a **human-readable name**
        - Example: "Customer Vocabulary", "Product Vocabulary",
          "Financial Instruments Vocabulary"

    - **Type**
        - A Concept Vocabulary is a `skos:ConceptScheme` (following W3C
          SKOS standard)

    ### Optional facts

    - **Description**
        - A Concept Vocabulary should have a description explaining its
          purpose and scope

    - **Owner**
        - A Concept Vocabulary should have a designated owner (person,
          team, or organizational unit)

    - **Version**
        - A Concept Vocabulary should be versioned to track changes over
          time

    - **Status**
        - A Concept Vocabulary can have a status (e.g., "Draft",
          "Active", "Deprecated")

    ### Relationships

    - **Contains Concepts**
        - A Concept Vocabulary contains **zero or more** Concepts
        - Modeled using `skos:inScheme` relationship
        - Cardinality: 1 vocabulary → 0..* concepts

    - **Referenced by Use Cases**
        - A Concept Vocabulary can be referenced by **zero or more**
          Use Cases
        - Cardinality: 1 vocabulary → 0..* use cases (reference)

    - **Owned by Use Case**
        - A Concept Vocabulary can be owned by **zero or one** Use Case
        - If owned, the vocabulary is private to that use case
        - Cardinality: 1 vocabulary → 0..1 use case (ownership)

    ### SKOS Alignment

    Following W3C SKOS standards:

    ```turtle
    ex:CustomerVocabulary a skos:ConceptScheme ;
        dcterms:title "Customer Vocabulary" ;
        dcterms:description "Concepts related to customer management" ;
        dcterms:creator "Customer Data Team" ;
        dcterms:created "2024-01-15" ;
        dcterms:modified "2024-12-30" .

    ex:Customer a skos:Concept ;
        skos:inScheme ex:CustomerVocabulary ;
        skos:prefLabel "Customer"@en ;
        skos:definition "An organization or individual who purchases goods or services" .
    ```

    ### Implementation Considerations

    - Use URIs for vocabulary identifiers to enable linking
    - Consider using standard vocabulary management systems
    - Implement version control for vocabularies
    - Provide SKOS exports for interoperability
    - Support vocabulary import/export for reuse

## See Also

- [Concept](index.md) — The base concept that vocabularies contain
- [Story/Concept Relationship](story-concept-relationship.md) — How
  stories use concepts
- [Use Case](../use-case/index.md) — How use cases relate to
  vocabularies
- [Term](../term/index.md) — Components of concepts within
  vocabularies
