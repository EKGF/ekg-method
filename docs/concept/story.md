# Story

<!--summary-start-->
_A structured business requirement expressed in plain language that
defines what a Persona needs to accomplish within a Use Case_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Story?

    A **Story** — in the context of a [Use Case](use-case.md) in the
    [Use Case Tree](use-case-tree.md) — defines a business
    requirement.
    It captures what someone needs to accomplish, expressed in their
    own language.

    ## Story Structure

    Stories follow a simple, structured format that captures three
    essential elements:

    - **Who** — The [Persona](persona.md) who needs this capability
      (e.g., "As the Chief Risk Officer...")
    - **What** — What they need to do or know (e.g., "...I need to
      know our current Risk Position...")
    - **Why** — The business [Outcome](outcome.md) or purpose (e.g.,
      "...so that I can Assess the Risk")

    !!! tip "Start simple"

        In the early phases of a use case, we only ask for these
        three elements.
        Don't worry about how it will be implemented — that comes
        later.

    ## Examples

    A business user could specify requirements as follows:

    - _As the Chief Risk Officer, I need to know our current Risk
      Position against party B, so that I can Assess the Risk_
    - _As an Auditor, I need to get a list of all current board
      members of legal entity X, so that I can Verify Stakeholders_
    - _As an Employee, I need to get a list of all my colleagues in
      my unit, so that I Know my Colleagues_
    - _As a customer, I need to get a list of all products, so that
      I can make a product selection_

    And so forth.
    That's all we ask in the early phases of a given use case.

    ## Why Stories Matter

    Stories provide a bridge between business needs and technical
    implementation.
    They ensure that:

    - **Business language is preserved** — Requirements are captured
      in terms the business understands
    - **Focus stays on outcomes** — We understand the "why" behind
      each requirement
    - **Everyone is aligned** — Business, data, and technology
      teams share a common understanding of what needs to be
      delivered


=== "Data & Tech Audience"

    ## What Is a Story in the EKG Method?

    "User Stories" start out as plain English sentences that, as the
    name suggests, come from the user.
    In other words, "the Business" or "the Customer" — the end user
    of a system or application — is responsible for explaining to
    the people who need to deliver that system what the system is
    supposed to do.

    Makes sense, right?
    Unfortunately, it's usually not that simple.
    All kinds of other factors come into play that have nothing to
    do with specifying what the user _really_ wants, such as design,
    architecture, existing systems, budgets, time, regulations,
    policies, and technical capabilities.

    ## The Challenge

    However, it is a good thing to at least capture the "real"
    wishes of the user without having to consider all of those other
    aspects.
    The challenge is to ask the user to step out of their normal
    day-to-day practices and comfort zone and to think ahead in a
    way that is not restricted by all the daily hurdles and
    practicalities.

    ## Structured Business User Stories

    This method proposes to use "Structured Business User Stories"
    to achieve many things:

    ### Strategic Focus

    Have a more strategic view on which functionality is **really**
    required.
    By focusing on business outcomes rather than implementation
    details, we can identify what truly matters.

    ### Gap Analysis

    Allow seeing "the disconnect" or "the gap" between what's
    required and what is currently available, delivered, and
    deliverable.
    This helps prioritize work and identify areas where new
    capabilities are needed.

    ### Avoid Tunnel Thinking

    Avoid "tunnel thinking" where everyone, especially "the business"
    itself, makes all kinds of assumptions that may or may not be true
    and could severely diminish creativity.
    Stories encourage thinking beyond current constraints.

    ### Separation of Concerns

    Create a clear separation of concerns: the business specifies what
    they need but leaves it to the data and technology people to
    work out how they can deliver it.
    So no more "screen designs" (that comes later) or "schemas" that
    are used as "functional specification".
    We need to be able to go deeper, to the core questions about
    **"what do you really need?"** (and forget about the "How" for a
    minute).

    ### Testable Specifications

    Have clear testable specifications of required functionality for
    the whole lifecycle of a given user story.
    As long as people need a given story to be implemented, it will
    continuously be tested "end-to-end," from inception all the way
    to production, not only before deployment into production but
    actually also in production itself.

    ## Continuous Testing and Functional Health

    The EKG knows about "its Stories" and continuously tests them.
    It therefore knows about its own "functional health" and can
    detect whenever something changes (code, ontologies, ETL, new
    policies) whether it can still deliver all functionality.

    This means that Stories are not just requirements documents —
    they are **living, executable specifications** that the EKG
    monitors and validates throughout their entire lifecycle.

    ## Relationship to Workflows

    Stories are executed as steps within [Workflows](workflow.md).
    For each Story, we always know in which Workflows it participates
    as a Step.

    This bidirectional relationship enables:

    - **Story reuse** — Stories can be reused across multiple
      workflows, enabling composition and consistency
    - **Workflow discovery** — Understanding which workflows use a
      given story helps discover related business processes
    - **Impact analysis** — Knowing what workflows are affected when
      a story changes enables better change management
    - **Process understanding** — Seeing how stories are composed
      into workflows provides insight into business processes

    Stories define the "what" (the capability), while Workflows
    define the "how" (the sequence and order of execution).

    ## Relationship to Other Concepts

    Stories link to other data structures in the Knowledge Graph:

    - **[Personas](persona.md)** — Each Story specifies which
      Persona needs the capability
    - **[Use Cases](use-case.md)** — Stories are organized within
      Use Cases, defining the functional requirements
    - **[Outcomes](outcome.md)** — The "why" part of a Story links
      to business outcomes
    - **[Concepts](concept.md)** — Stories reference domain concepts
      that need to be understood and modeled
    - **[Workflows](workflow.md)** — Stories are executed as steps
      within workflows

    This integration ensures that Stories are not isolated
    requirements but part of a cohesive, semantic model of the
    enterprise.
