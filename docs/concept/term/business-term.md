---
description: >-
  A human-facing Concept Manifestation used in conversations,
  documentation, user interfaces, policies, glossaries, and
  governance.
keywords:
  - business term
  - concept manifestation
  - glossary
  - vocabulary
  - EKG method
schema_type: "Article"
---

# Business term

<!--summary-start-->

_A human-facing Concept Manifestation used in conversations,
documentation, user interfaces, policies, and governance_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is a business term?

    A **Business Term** is a human-facing
    [Concept Manifestation](index.md). It is how people speak about a
    Concept in a specific context.

    Multiple Business Terms can point to one Concept when they mean the
    same thing in that context. For example, "Customer",
    "Counterparty", and "Client" may all be valid Business Terms for
    one Concept in one use case, while meaning different things in
    another use case.

    ## Key characteristics

    - **User-facing**: used in documentation, policies, UI, and
      conversation.
    - **Context-specific**: a term may mean different things in
      different contexts.
    - **Governable**: business owners can decide whether two terms
      really mean the same Concept.
    - **Mergeable**: Concepts can be merged later when owners agree
      that they mean the same thing.

    ## Examples

    - "Customer"
    - "Counterparty"
    - "Risk Position"
    - "Beneficial Owner"

=== "Data & Tech Audience"

    ## Business terms as manifestations

    A Business Term is a specialization of
    `concept:ConceptManifestation`.
    It carries human-readable lexical forms such as:

    - preferred label
    - synonym
    - abbreviation
    - singular form
    - plural form
    - short UI label

    The Concept itself stays thin. The preferred display label is a
    link from the Concept to a preferred Business Term.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-business-term.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here. These are
        minimal facts you can use to build your own ontology, schema,
        or graph model.

    ### BusinessTerm

    - **Subclass of ConceptManifestation**
        - All manifestation facts apply here.
    - **Language**
        - A natural language tag should be used when the form is
          language-specific.
    - **Lexical form**
        - Use a label or value for the exact business-facing text.
    - **Preferred role**
        - A Concept can mark one Business Term as its preferred
          business-facing manifestation in a given context.
