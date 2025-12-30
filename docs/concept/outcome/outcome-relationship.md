---
description: >-
  A relationship object that connects a Use Case to a specific
  Outcome,  supporting inheritance and contribution mapping.
keywords:
  - outcome relationship
  - contribution mapping
  - outcome inheritance
  - EKG method
schema_type: "Article"
---

# Outcome Relationship

<!--summary-start-->

_Connects a Use Case to an Outcome, supporting inheritance and
contribution mapping_

<!--summary-end-->

=== "Business & Management Audience"

    ## What is an Outcome Relationship?
    An **Outcome Relationship** defines the link between a [Use
    Case](../use-case.md) and a desired [Outcome](index.md).

    It's more than just a link; it captures *how* a use case
    contributes to an outcome. For example, a sub-use case might
    inherit an outcome from its parent and specify its own specific
    contribution to that goal.

    ## Why it Matters
    - **Traceability**: Shows exactly which use cases are responsible
      for delivering which business results.
    - **Inheritance**: Allows goals defined at a high level
      (strategic) to flow down to specific delivery components.
    - **Impact Analysis**: Helps understand which business goals are
      at risk if a particular use case is delayed.

=== "Data & Tech Audience"

    ## Inheritance and Contribution
    The Outcome Relationship is a first-class object in the Knowledge
    Graph that enables:

    - **Ownership**: The relationship where a Use Case "owns" an
      Outcome.
    - **Inheritance**: A child Use Case referencing an Outcome defined
      on a parent Use Case.
    - **Contribution mapping**: Capturing metadata about *how* the
      child contributes to that desired Outcome (e.g., confidence
      scores or specific metrics).

=== "Ontology"

    <span id="ontology"></span>
    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-outcome-relationship.md"

    ### Required facts about an Outcome Relationship
    - **Opaque universally unique identifier**: A UUID representing
      this relationship instance.
    - **Source Use Case**: A reference to the [Use
      Case](../use-case.md) involved.
    - **Target Outcome**: A reference to the [Outcome](index.md) being
      achieved.

    ### Optional but Recommended
    - **Contribution description**: Textual description of how the use
      case helps achieve the outcome.
    - **Confidence / Priority**: Metadata indicating the strength or
      importance of this relationship.
