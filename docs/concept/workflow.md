---
description: "A logical sequence of steps that defines the order of execution for Stories within a Use Case to achieve desired business Outcomes. Learn how workflows structure business processes in the Use Case Tree Method."
keywords:
  - workflow
  - business process
  - process flow
  - EKG method
  - enterprise knowledge graph
  - business automation
schema_type: "Article"
---

# Workflow

<!--summary-start-->
_A logical sequence of steps that defines the order of execution for
Stories within a Use Case to achieve desired business Outcomes_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Workflow?

    A **Workflow** defines the logical order of steps needed to
    accomplish a business process within a [Use Case](use-case.md).
    Every Use Case has one or more Workflows that describe how
    business activities should be performed.

    Workflows provide a structured way to organize and sequence the
    work that needs to be done, ensuring that tasks are performed in
    the right order and that dependencies are respected.

    ## Why Workflows Matter

    Workflows enable:

    - **Clarity** — Everyone understands the sequence of activities
      needed to accomplish a goal
    - **Consistency** — The same process is followed every time,
      reducing errors and variability
    - **Efficiency** — Workflows optimize the order of operations
    - **Automation** — Well-defined workflows can be automated,
      reducing manual effort
    - **Governance** — Workflows ensure that business rules and
      policies are followed

    !!! tip "Start with business logic"

        Workflows should reflect how the business actually works, not
        how systems are currently implemented.
        Focus on the logical order of business activities.

    ## Workflow Structure

    Workflows consist of a sequence of steps, where each step
    corresponds to executing a [Story](story.md) in the use case.
    The steps are organized to achieve the desired business
    [Outcome](outcome.md).

    The concepts and terms used in the workflow are based on the
    context-specific vocabulary identified during the requirements
    gathering phase — the same [Concepts](concept.md) that define
    the use case's domain.

    ## When Are Workflows Defined?

    Workflows are typically defined in later stages of the use case
    lifecycle, once:

    - The use case requirements are well understood
    - The Stories are clearly defined
    - The logical order of activities is known
    - Dependencies between activities are identified

    This allows workflows to be designed based on a solid
    understanding of what needs to be accomplished and how.

=== "Data & Tech Audience"

    ## What Is a Workflow in the Use Case Tree Method?

    A **Workflow** is a logical sequence of steps that defines the
    order of execution for [Stories](story.md) within a [Use
    Case](use-case.md).
    Every Use Case has one or more Workflows that describe how
    business processes should be executed.

    Workflows depend on the [Concepts](concept.md) captured during
    the requirements gathering phase and are executed to achieve the
    desired business [Outcome](outcome.md).

    ## Workflow Components

    Workflows consist of:

    - **Steps** — Each step corresponds to executing a Story in the
      use case
    - **Sequence** — The logical order in which steps should be
      executed
    - **Dependencies** — Relationships between steps that determine
      execution order
    - **Concepts** — The domain concepts and terms used throughout
      the workflow

    The concepts and terms used in the workflow are based on the
    context-specific vocabulary identified during the requirements
    gathering phase — the same Concepts that define the use case's
    domain.

    ## Relationship to Stories

    Each step in a workflow corresponds to executing a Story in the
    use case.
    This means:

    - **Stories define what** — Each Story specifies what needs to
      be accomplished (the capability)
    - **Workflows define how** — Workflows specify the order and
      sequence in which Stories are executed
    - **Together they define the process** — Stories + Workflows =
      Complete business process definition

    This separation allows Stories to be reusable across different
    workflows, while workflows can compose Stories in different ways
    to achieve different outcomes.

    **Bidirectional relationship:**
    For each Story, we always know in which Workflows it participates
    as a Step.
    This bidirectional relationship enables:

    - **Story reuse analysis** — Understanding which workflows use a
      given story
    - **Impact analysis** — Knowing what workflows are affected when
      a story changes
    - **Discovery** — Finding workflows that accomplish similar
      outcomes by examining their constituent stories

    ## Workflow Execution

    Workflows can be executed in different ways:

    - **Manual execution** — Steps are performed by people following
      the workflow definition
    - **Automated execution** — Steps are performed by systems that
      interpret and execute the workflow
    - **Hybrid execution** — Some steps are automated, others are
      manual

    The EKG can track workflow execution, monitor progress, and
    ensure that business rules and policies are followed throughout
    the process.

    ## Persistent Stateful Workflows

    It is expected that workflows have **persistent stateful**
    execution capabilities.
    This means that workflows can maintain their state across
    execution sessions, enabling them to handle processes of varying
    durations and complexity.

    **Short-duration workflows:**
    Some workflows can be done quickly in real-time and in-memory,
    where one [Story's](story.md) output can be directly used as the
    next Story's input.
    These workflows execute entirely within a single session and
    complete in seconds or minutes.

    **Long-duration workflows:**
    Some workflows may take hours, weeks, or even months to complete.
    These workflows require persistent state management because:

    - **Human involvement** — Steps may require human review,
      approval, or input, which can take significant time
    - **Agentic steps** — Steps may involve autonomous agents that
      need time to complete their tasks
    - **External dependencies** — Steps may depend on external
      systems or events that occur over extended periods
    - **Complex processes** — Business processes may naturally span
      long timeframes (e.g., procurement, project management,
      regulatory approvals)

    Persistent stateful workflows enable the EKG to:

    - **Resume execution** — Workflows can pause and resume from
      their last state
    - **Track progress** — Long-running workflows maintain their
      state and can report progress at any time
    - **Handle interruptions** — Workflows can handle system
      restarts, failures, or pauses without losing their state
    - **Support human-in-the-loop** — Workflows can wait for human
      input and resume when that input is provided

    This capability is essential for modeling real-world business
    processes that don't complete instantly but unfold over time.

    ## Workflows as First-Class EKG Objects

    Ideally, workflows are persisted as part of the overall EKG as
    **first-class citizen objects**.
    This means that workflows, their steps, and their states can be
    inspected, queried, and reasoned about like any other object in
    the     Enterprise Knowledge Graph.

    **Workflow lifecycle:**

    - **Workflows are initiated by Stories** — A Story can trigger
      the execution of a workflow
    - **Each step is a call to a Story** — Each step in a workflow
      corresponds to executing a Story, maintaining the connection
      between the workflow definition and the business requirements
    - **State is persisted** — Workflow state is stored in the EKG,
      enabling inspection, monitoring, and reasoning about workflow
      execution

    **Benefits of first-class persistence:**

    - **Inspectability** — Workflow steps and states can be queried
      and analyzed like any other EKG data
    - **Observability** — Workflow execution can be monitored and
      traced through the EKG
    - **Reasoning** — The EKG can reason about workflow state,
      dependencies, and execution paths
    - **Integration** — Workflows are integrated with other EKG
      concepts (Use Cases, Stories, Concepts, Personas)

    **Implementation:**
    Conceptually, workflows are similar to
    [AWS Step Functions](https://aws.amazon.com/step-functions/),
    which could be one of the technologies used to implement these
    workflows.
    However, the key difference is that in the Use Case Tree Method, workflows
    are not just execution engines but semantic objects that are part
    of the knowledge graph itself, enabling deeper integration and
    reasoning capabilities.

    !!! info "Provenance"

        When your EKG Service Layer fully supports the Use Case Tree Method and
        you have a Story Service that can execute Stories, then
        ideally you want it to automatically maintain the provenance
        chain of activities.

        Like the [PROV-O](https://www.w3.org/TR/prov-o/) (Provenance
        Ontology) describes, provenance has three main classes:
        **Activity**, **Agent**, and **Entity**.

        The ultimate form of provenance implementation is to be able
        to link an Activity to the execution of a particular Story in
        the context of a particular instance of a Workflow.
        Then you have everything to provide full explainability.

        This provenance chain enables:

        - **Traceability** — Understanding what happened and why
        - **Explainability** — Explaining how results were produced
        - **Auditability** — Tracking who did what and when
        - **Debugging** — Understanding execution paths and failures

    !!! tip "Observability"

        In modern-day architectures, you have fully instrumented code
        producing traces that are collected by
        [OpenTelemetry](https://opentelemetry.io/) (OTEL)-compliant
        collectors.

        The concept of a so-called **"span"** (in
        [OTLP](https://opentelemetry.io/docs/specs/otlp/) / OTEL
        jargon) perfectly aligns with a
        [PROV-O](https://www.w3.org/TR/prov-o/) Activity and with a
        Workflow-step execution.

        This alignment enables:

        - **Unified observability** — Workflow execution traces can
          be integrated with application traces
        - **End-to-end visibility** — From business process
          (Workflow) to technical implementation (code spans)
        - **Semantic enrichment** — OTEL spans can be enriched with
          EKG semantic metadata (Story, Workflow, Persona, etc.)
        - **Cross-system correlation** — Linking business activities
          with technical execution across distributed systems

    ## Workflow Patterns

    Common workflow patterns include:

    - **Sequential** — Steps execute one after another in a fixed
      order
    - **Parallel** — Multiple steps execute simultaneously
    - **Conditional** — Different steps execute based on conditions
    - **Iterative** — Steps repeat until a condition is met
    - **Event-driven** — Steps execute in response to events

    These patterns can be combined to create complex workflows that
    model real-world business processes.

    ## Relationship to Other Concepts

    Workflows relate to other core concepts:

    - **[Use Cases](use-case.md)** — Every use case has one or more
      workflows
    - **[Stories](story.md)** — Each workflow step corresponds to
      executing a story
    - **[Concepts](concept.md)** — Workflows use concepts from the
      use case's vocabulary
    - **[Outcomes](outcome.md)** — Workflows are executed to achieve
      desired business outcomes
    - **[Personas](persona.md)** — Workflows specify which personas
      are involved in each step

    This integration ensures that workflows are not isolated process
    definitions but part of a cohesive, semantic model of the
    enterprise.

=== "Ontology"

    ## Ontology (minimal facts we can state today)

    --8<-- "fragment/uctm-diagram-workflow.md"

    We're not (yet) prescribing a full OWL ontology here.
    But we can state a small set of **facts** that people can reliably use to build their own
    ontology / schema / graph model around a Workflow.

    !!! note "WorkflowDefinition"

        When we say “Workflow” here, we primarily mean the **definition** of a workflow
        (a **WorkflowDefinition**), not a specific runtime execution instance.

    ### Required facts about a WorkflowDefinition

    - **Opaque universally unique identifier**
        - A WorkflowDefinition should have an **opaque**, **universally unique** identifier.
        - Prefer a random identifier such as **UUIDv4**, represented as a URI:
          `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

    - **Business-friendly name**
        - A WorkflowDefinition should have a human-readable name.

    - **Slug**
        - A WorkflowDefinition should have a kebab-cased slug that is unique at least within the
          organization.
        - Example: `onboard-supplier`, `assess-counterparty-risk`

    - **Definition**
        - A WorkflowDefinition should have a definition describing the business process it models.

    - **Owned by a Use Case**
        - A WorkflowDefinition is **part-of** a Use Case: the Use Case **owns** it.
        - If the owning Use Case is deleted, its workflow definitions are deleted as well.

    - **Steps that reference Stories (relationship-object)**
        - A WorkflowDefinition has **zero or more Steps**.
        - Each Step references a Story.
        - Model Steps as relationship-objects so you can capture ordering and execution semantics
          (sequence, branching/conditions, parallelism, retries, etc.).

    - **Outcomes and concepts**
        - Workflows are executed to achieve Outcomes (directly or via the Stories they orchestrate).
        - Workflows use Concepts through the Use Case’s Concept Vocabularies and the Stories in
          their steps.
