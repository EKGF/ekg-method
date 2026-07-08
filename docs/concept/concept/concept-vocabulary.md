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

    - A **Concept** in our model is essentially just a unique
      identifier (a random UUID) that represents an idea or thing in
      your domain
    - This concept can have **multiple manifestations** associated
      with it, such as business words, abbreviations, API parameters,
      query variables, ontology classes, shapes, and source
      occurrences
    - This is a **one-to-many relationship**: one concept, potentially
      many manifestations

    ### Why multiple manifestations?

    In a given context, people often use different words for the same
    thing, and systems often use different identifiers for it:

    **Example: Hospital Context**

    > In a hospital use case, the concept of "a person receiving care"
    > might have multiple manifestations:
    >
    > - "Patient" — medical staff terminology
    > - "Client" — administrative perspective
    > - "Customer" — billing department
    > - "Visitor" — reception desk
    >
    > All these manifestations refer to the same underlying Concept in
    > this hospital context, so they are grouped under one Concept
    > identifier.

    ### Context Matters

    The same manifestation value might mean completely different things
    in other contexts:

    - "Patient" in a hospital means something different than "patient"
      in a legal context (someone waiting)
    - "Client" in a hospital is different from "client" in a law firm
    - Each use case defines its own concepts that make sense in its
      context

    The Concept (the UUID) ties together all the manifestations that
    mean the same thing **in your specific use case context**.

    !!! note "Manifestations can repeat, Concepts are contextual"

        The **manifestation values** themselves, such as "patient",
        "client", `?patient`, or `patient_id`, can appear in many
        vocabularies and systems. The **Concept** that groups them
        together is specific to the use case's context and meaning.

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
      resources, shapes, and source occurrences used in different
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
    - The Concept identifier represents the local linking pin
    - The Concept has a **one-to-many relationship** with
      **Concept Manifestations**
    - Manifestations are the observable forms: words, phrases, code
      identifiers, schema resources, shapes, and source occurrences
    - A Concept can have multiple manifestations, each representing a
      different way the same meaning appears in a given context

    **Why this matters:**

    In a given use case context, people often use multiple words for
    the same concept:

    ```
    Concept: urn:uuid:a1b2c3d4-... (hospital visitor concept)
    ├── BusinessTerm: "Patient" (medical staff usage)
    ├── BusinessTerm: "Client" (administrative usage)
    ├── URIParameterManifestation: "patient-id"
    └── OWLClassManifestation: hospital:Patient
    ```

    All these manifestations refer to the same underlying Concept
    **in this hospital use case's context**. In other contexts, these
    same values might mean different things and would not be grouped
    together.

    **Key insight:**

    - **Concepts** are context-specific linking pins
    - **Manifestation values** can recur across many contexts
    - The Concept binds together all manifestations that mean the same
      thing in your specific use case context

    This separation allows:

    - Different use cases to use the same values with different
      meanings
    - One use case to group multiple manifestations under one Concept
    - Clear traceability of which manifestations are considered
      equivalent in which contexts

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
- [Concept Manifestation](../term/index.md) — Observable forms of
  concepts within vocabularies
