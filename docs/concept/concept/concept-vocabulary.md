---
title: Concept Vocabulary
description: >-
  A governed set of related data element concepts, enabling reuse
  and consistency across use cases in the Use Case Tree Method.
keywords:
  - concept vocabulary
  - vocabulary
  - concept set
  - data element concept
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

_A governed set of related data element concepts, enabling reuse and
consistency across use cases_

<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Concept Vocabulary?

    A **Concept Vocabulary** is a governed set of related
    [Data Element Concepts](index.md), called Concepts for short. Think
    of it as a dictionary or glossary specific to a particular area of
    your business. It groups together concepts and their
    manifestations that make sense to use together.

    Just as you might have a "Finance Vocabulary" or a "Product
    Management Vocabulary" in your organization, the Use Case Tree
    Method organizes concepts into vocabularies to keep things clear
    and reusable.

    ## How concepts work with manifestations

    An important characteristic of our Concept Vocabularies is how
    concepts relate to the actual words and technical forms people and
    systems use:

    - A **Concept** identifies a reusable meaning, independently of
      the names and technical forms used to express it
    - This concept can have **multiple manifestations** associated
      with it, such as business words, abbreviations, API parameters,
      query variables, ontology classes and shapes
    - This is a **one-to-many relationship**: one concept, potentially
      many manifestations

    ### Why multiple manifestations?

    In a given context, people often use different words for the same
    thing, and systems often use different identifiers for it:

    **Example: Customer identifier**

    > A shared customer-identifier Concept might have these
    > manifestations across sales, service and billing:
    >
    > - "Customer identifier" — the business term
    > - "Customer ID" — a shorter label on forms
    > - `?customerId` — a SPARQL variable
    > - `customer_id` — a Python variable
    >
    > These manifestations express the same meaning and link to
    > one Concept reused by those use cases.

    ### Context Matters

    The same word or token can have different meanings. For example,
    "bank" can denote a financial institution or the side of a river.
    Conversely, different names can express the same meaning.

    Check the meaning before reusing a Concept. A new use case or
    vocabulary does not by itself require a new Concept. A Concept
    can also belong to more than one vocabulary.

    !!! note "Reuse meaning across contexts"

        Reuse existing Concepts wherever their meanings apply.
        Separate Concepts may be created where needed and later
        merged when their owners establish that they mean the same
        thing. Matching manifestation values alone do not establish
        that identity.

    ## Why Use Concept Vocabularies?

    Concept Vocabularies serve several important purposes:

    1. **Organization** — Keeps related concepts together in meaningful
       groupings

    2. **Reuse** — Allows multiple use cases to share the same
       vocabulary without duplicating concepts

    3. **Consistency** — Ensures that the same manifestation values
       can be interpreted in the right context

    4. **Ownership** — Clarifies who is responsible for defining and
       maintaining concepts in each domain

    !!! tip "One vocabulary, many use cases"

        A well-defined vocabulary can serve multiple use cases. For
        example, a "Customer Vocabulary" might be used by Customer
        Service, Sales, Marketing, and Analytics use cases.

    ## Ownership and Inheritance

    Every Concept Vocabulary is **owned by exactly one Use Case**.
    However, vocabularies are automatically **inherited** by all
    descendant Use Cases in the
    [Use Case Tree](../use-case-tree.md):

    - **Own vocabularies** — Vocabularies owned by the
      current Use Case.
      The owning Use Case can add, modify, or remove
      Concepts in these vocabularies.
    - **Inherited vocabularies** — Vocabularies owned by
      ancestor Use Cases.
      These are available **read-only** to descendant
      Use Cases --- they can use the Concepts but cannot
      change them.

    This means broadly applicable vocabularies should be
    defined at higher levels of the Use Case Tree, where
    they benefit the most Use Cases.

    **Example:**

    > The top-level "Customer Management" Use Case owns a
    > "Customer Vocabulary."
    > All child Use Cases --- "Onboarding," "Service,"
    > "Billing" --- automatically inherit this vocabulary
    > and can reference its Concepts in their Stories.
    > The "KYC Verification" Use Case (a child of
    > Onboarding) also defines its own "KYC Vocabulary"
    > with specialized Concepts like "Beneficial Owner"
    > and "Sanctions List."

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

    Reuse existing Concepts while developing new vocabulary content:

    1. **Discover** — Find existing Concepts that express the needed
       meanings
    2. **Extend** — Add manifestations or create new Concepts for
       meanings that are not already covered
    3. **Refine** — Clarify definitions and reconcile duplicates
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
    In the EKGF Concept Ontology:

    - A Concept Vocabulary is an `ekg-concept:ConceptSet`
    - A Concept is an `ekg-concept:DataElementConcept`
    - `ekg-concept:inConceptSet` links a Concept to a vocabulary

    Membership organizes shared meanings without making each
    Concept local to a vocabulary. SKOS concepts and schemes can
    be linked through technical manifestations.

    ## Relationship to Use Cases

    Each Concept Vocabulary is **owned by exactly one**
    [Use Case](../use-case/index.md).
    A Use Case can own zero or more Concept Vocabularies.

    ### Inheritance through the Use Case Tree

    Concept Vocabularies are **inherited** down the
    [Use Case Tree](../use-case-tree.md).
    When a Story in a child Use Case needs to reference
    Concepts, it can draw from:

    - **Own vocabularies** — Concept Vocabularies owned by
      the Story's own Use Case (read-write)
    - **Ancestor vocabularies** — Concept Vocabularies
      owned by any ancestor Use Case in the tree
      (read-only)

    This inheritance mechanism means that broadly
    applicable vocabularies can be defined at higher
    levels of the Use Case Tree and reused by all
    descendant Use Cases without duplication.

    ### Practical example

    ```
    Enterprise Use Case Tree
    └── Customer Management          ← owns "Customer Vocabulary"
        ├── Customer Onboarding      ← inherits "Customer Vocabulary"
        │   └── KYC Verification     ← inherits "Customer Vocabulary"
        │       ← owns "KYC Vocabulary"
        └── Customer Service         ← inherits "Customer Vocabulary"
    ```

    In this example, "KYC Verification" can pick Concepts
    from both its own "KYC Vocabulary" and the inherited
    "Customer Vocabulary" from its ancestor.

    ## Relationship to Stories

    [Stories](../story/index.md) use Concepts from vocabularies
    through
    [Story/Concept Relationships](story-concept-relationship.md).
    When associating Concepts to a Story as **InputConcept**,
    **OutputConcept**, or **DependentConcept**, the available
    Concepts come from:

    - Concept Vocabularies **owned by** the Story's own
      Use Case
    - Concept Vocabularies **inherited from** any ancestor
      Use Case in the tree (read-only)

    A Story may reference Concepts from multiple
    vocabularies.

    ## Relationship to manifestations

    [Concept Manifestations](../term/index.md) are attached to
    concepts, which are part of vocabularies:

    - A Concept Vocabulary contains multiple Concepts
    - Each Concept can have zero or more manifestations
    - Manifestations provide the labels, names, variables, schema
      resources and shapes used in different contexts
    - `ManifestationOccurrence` records where a manifestation
      appears in a source

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

    ### Shared meanings and their manifestations

    `DataElementConcept` identifies the meaning of a data element or
    compound data construct. Its
    [relationship to ISO/IEC 11179](index.md#relationship-to-isoiec-11179)
    follows the separation of meaning and representation, with a
    broader scope that includes whole classes and shapes.

    A Concept can have many manifestations across different use
    cases and systems:

    ```text
    DataElementConcept: customer identifier
    ├── BusinessTerm: "Customer identifier"
    ├── BusinessTerm: "Customer ID"
    ├── URIParameterManifestation: "customerId"
    └── SPARQLVariableManifestation: "?customerId"
    ```

    The Concept identifies the shared meaning, while manifestations
    express it in particular forms. Reuse the Concept when a new
    use case needs that meaning. Create a separate Concept when
    needed, and reconcile independently created duplicates when
    their owners establish that they mean the same thing.

    A SKOS concept is one possible technical manifestation's
    resource. `DataElementConcept` has no `skos:Concept` superclass,
    and `ConceptSet` is not a `skos:ConceptScheme` subclass.

    ### Concept Vocabulary

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
        - A Concept Vocabulary is an `ekg-concept:ConceptSet`

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
        - `ekg-concept:inConceptSet` links a Concept to its set
        - Concepts can belong to multiple sets; shared membership
          reuses the same identity

    - **Owned by exactly one Use Case**
        - A Concept Vocabulary is owned by exactly **one** Use Case
        - The Use Case owns **zero or more** Concept Vocabularies
        - Cardinality: 1 vocabulary → 1 use case (ownership)
        - If the owning Use Case is deleted, its Concept
          Vocabularies are deleted as well

    - **Inherited by descendant Use Cases**
        - Descendant Use Cases in the tree inherit
          (read-only) access to ancestor Concept
          Vocabularies
        - This is not a stored relationship but derived
          from the `:isPartOf` hierarchy of Use Cases

    ### EKG ontology example

    These readable example identifiers illustrate a vocabulary,
    a Concept and its manifestations:

    ```turtle
    @prefix ex: <https://example.org/> .
    @prefix ekg-concept: <https://ekgf.org/ontology/concept#> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

    ex:CustomerVocabulary a ekg-concept:ConceptSet ;
        dcterms:title "Customer Vocabulary" ;
        dcterms:description "Concepts for customer management" .

    ex:CustomerIdentifier a ekg-concept:DataElementConcept ;
        ekg-concept:inConceptSet ex:CustomerVocabulary ;
        ekg-concept:preferredBusinessTerm ex:CustomerIdentifierTerm ;
        ekg-concept:hasManifestation ex:CustomerIdVariable .

    ex:CustomerIdentifierTerm a ekg-concept:BusinessTerm ;
        rdfs:label "Customer identifier"@en .

    ex:CustomerIdVariable a ekg-concept:SPARQLVariableManifestation ;
        ekg-concept:manifestationValue "?customerId" .
    ```

    ### Implementation Considerations

    - Use URIs for vocabulary identifiers to enable linking
    - Consider using standard vocabulary management systems
    - Implement version control for vocabularies
    - Link SKOS representations through technical manifestations
    - Support vocabulary import/export for reuse

## See Also

- [Concept](index.md) — The base concept that vocabularies contain
- [Story/Concept Relationship](story-concept-relationship.md) — How
  stories use concepts
- [Use Case](../use-case/index.md) — How use cases relate to
  vocabularies
- [Concept Manifestation](../term/index.md) — Observable forms of
  concepts within vocabularies
