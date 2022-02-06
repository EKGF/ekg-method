# Persona

=== "Business Audience"

    For any given Use Case we need to have a list of all the different types of players.
    In the initial stages of the life cycle of a use case it is less relevant whether these players
    are called Stakeholders, Actors, Roles, User Types or Systems, we simply need to know what terms the
    actual users, the real customer(s) of the use case, are using for them in their daily practice.

    We call them Personas.

    For example, in the use case "Legal Entity Management" you would have Personas like:

    - Auditor
    - Data Owner
    - Shareholder
    - Director
    - Signator
        - Signator Power Pursuent to Commercial Register
    - Board Member
    - Legal Council
    - Liquidator
    - ...

    Many of these Personas are involved in multiple use cases and are grouped together in _persona taxonomies_
    and defined in _ontologies_ with "machine readable meaning" that can be used to let algorithms "understand"
    the actual context and act upon it.

=== "Data & Tech Audience"

    In traditional use case modelling people use the term _Actor_ rather than _Persona_.
    The term _Actor_ is also used in a TOGAF Metamodel and combined with the term _Role_ whereby an actor 
    assumes a role to perform a task.

    The Use Case Tree Method does not make that distinction, primarily to keep things as simple as possible when
    capturing requirements --- primarily as [stories](story.md) --- but also because the term Persona combines both
    concepts into one whereby:

    - Actors assuming a Role is fully automated, context dependent, model-, rule- and policy-driven
    - Personas are [Concepts](concept.md) tied to Ontology-defined Classes that can inherit from other Persona types
    - Personas are not just the "users" (or systems) of the use case but also any other party in the related
      data-models (or EKG models/ontologies). For instance, your user can have the persona "Legal Entity Maintainer"
      but since the legal entity can have a Director as well, the Director is also a Persona, even when that
      Director might never be an active user of the system.


=== "Model"

A subset of the model, as a UML Class Diagram, around **Persona**.

![Context](../diagrams/out/persona-class-diagram.svg#darkable)
