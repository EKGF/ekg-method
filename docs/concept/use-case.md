# Use Case

<!--summary-start-->
_An executable model of business requirements that delivers specific
business outcomes within the Use Case Tree_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Use Case?

    A **Use Case** specifies a distinct set of business requirements —
    ideally, but not necessarily, captured as an "executable model" —
    resulting in a specific business outcome.

    Use cases start as ideas that can come from anyone in the
    organization at any time.
    These ideas are captured in the
    [**Use Case Tree**](use-case-tree.md) — a data structure that
    organizes business capabilities into a hierarchical structure,
    starting on a whiteboard and showing how components of the business
    break down into smaller components.

    ## Open Contribution Model

    Anyone should be able to contribute ideas that may or may not end
    up as fully implemented use cases in the organization's
    [Use Case Tree](use-case-tree.md), whether they are viable or not.
    If an idea for a use case is rejected, the rationale should be
    shared with everyone so that everyone can learn and avoid wasting
    time on that idea again.

    Let people contribute.
    All knowledge workers, specialist users, data architects,
    technical architects, ontologists, end users, business executives
    — literally anyone — should be able to understand:

    ### Strategic Context

    - **Business identity and strategy**: What is our
      [business identity](https://maturity.ekgf.org/pillar/business/background-and-intro/#business-identity)?
      Our [mission and strategy](https://maturity.ekgf.org/pillar/business/capability-area/strategy-actuation/)?
      What do we do all this for (besides being profitable)? What are
      the long-term objectives we are going to achieve?

    - **Technology landscape**: How does that map to our current and
      future data and technology landscape? (Without becoming too
      technical or detailed — we want everyone to be able to
      contribute.)

    - **Capability assessment**: How do we
      [Assess](../process/plan/assess.md) all our organization's
      capabilities, as specified in the
      [Maturity Model for the Enterprise Knowledge Graph (EKG/Maturity)](https://maturity.ekgf.org),
      related to our own EKG and how they match with our ambitions to
      implement our strategic use cases?

    - **Technical debt**: How does our "technical debt" fit in?
      (Identify the functionality of our technical debt as use cases
      in the tree as well.)
      How are we going to "rationalize" our current siloed landscape
      (and technical debt)?

    - **Priorities and roadmap**: What are the short- and long-term
      priorities? What are the milestones and the roadmap? (See
      ["Chart"](../process/plan/chart.md).)

    - **Transparency**: Which ideas (for use cases) have been
      proposed, considered, approved, or rejected, and why?

=== "Data & Tech Audience"

    ## What Is a Use Case in the EKG Method?

    A **Use Case** in the EKG Method specifies a distinct set of
    business requirements — ideally captured as an "executable model"
    — resulting in a specific business outcome.
    Each use case is a node in the
    [**Use Case Tree**](use-case-tree.md), acting as a semantic
    package that can be discovered, versioned, and reused across the
    enterprise.

    ## Relationship to UML Use Cases

    The term "use case" has a specific meaning for technical audiences
    who typically assume it means what the Object Management Group (OMG)
    defines in their Unified Modeling Language (UML) and its
    ["use case diagrams"](https://en.wikipedia.org/wiki/Use_case_diagram).

    Although there are many similarities and overlap — which is why we
    are repurposing the term — it is not exactly the same in our Use
    Case Tree Method:

    ### Key Differences

    - **Broader abstraction**: Use cases in the EKG Method are often
      used as a much broader and more abstract container concept
      compared to a UML Use Case.
      They can be organized in a "tree structure" where, at the
      highest levels, a use case can represent a capability domain or
      a "strategic use case" — basically anything that fits well with
      the business.

    - **Reusable components**: At the lowest levels in this tree, we
      end up with use cases that are much more like turn-key
      components for the EKG — 100% reusable, delivering
      "no-code"-functionality[^2].

    - **Executable models**: Unlike UML use cases, which are primarily
      descriptive, EKG use cases can be captured as executable models
      that run directly in the Enterprise Knowledge Graph platform.

    - **Semantic packaging**: Each use case acts as a semantic package
      containing ontologies, stories, data products, workflows, and
      other reusable components — similar to how software packages
      contain code, dependencies, and metadata.

    ## Technical Implementation

    From a technical perspective, a Use Case in the EKG Method:

    - **Organizes related components**: Groups together personas,
      concepts, stories, workflows, datasets, and ontologies that
      belong to the same business capability

    - **Enables reuse**: Provides a mechanism for discovering and
      reusing business logic, data models, and workflows across
      different contexts

    - **Supports versioning**: Can be versioned and evolved over time
      while maintaining backward compatibility

    - **Facilitates testing**: Provides the structure for defining test
      scenarios and ensuring 100% test coverage based on real business
      requirements

    - **Enables composition**: Can be composed with other use cases to
      create larger business capabilities, supporting the goal of
      [Composable Business](../objective/composable-business.md)

=== "Key Components"

    ## Overview

    A Use Case in the EKG Method is composed of multiple components
    that evolve throughout its lifecycle.
    These components work together to create a complete, executable
    model of business requirements.

    ## Essential Elements

    Every Use Case starts with these fundamental components, defined
    during the [Plan Phase](../process/plan/index.md):

    - **Name and description** — Clear identification and purpose.
      This provides the foundation for all other components and
      enables discovery within the Use Case Tree.

    - **Business outcomes** — The desired or expected business
      outcome(s) and how they can be measured.
      These define success criteria and provide the "why" behind
      the use case.
      See [Outcome](outcome.md) for more details.

    - **Personas** — The [personas](persona.md) of all the people and
      systems involved in the domain or scope represented by the Use
      Case.
      Personas define who (or what) interacts with the use case and
      their needs.

    - **Concepts and terms** — The concepts and their terms as used
      in the context of the Use Case.
      These form the vocabulary of the domain and link to the
      semantic models (ontologies) that will be developed.
      See [Concept](concept.md) for more details.

    !!! tip "Start simple, evolve iteratively"

        These essential elements can be defined at a high level
        initially — "mile wide, inch deep" — and refined as the use
        case progresses through its lifecycle.

    ## Additional Elements (Later in Lifecycle)

    As the Use Case moves into the [Build Phase](../process/build/index.md),
    additional components are added:

    - **Stories** — The functional requirements and business logic
      that implement the use case.
      Stories define what the use case does and can be implemented
      as executable functions or APIs.
      See [Story](story.md) for more details.

    - **Datasets and ontologies** — The data structures and semantic
      models that support the use case.
      Datasets provide the data, while ontologies define the meaning
      and relationships.
      See [Data Product](data-product.md) and
      [Ontology](ontology.md) for more details.

    - **Workflows** — The process flows and orchestration that
      coordinate multiple stories and data flows.
      Workflows define how different components work together to
      deliver the business outcome.
      See [Workflow](workflow.md) for more details.

    ## Specialist Contributions

    Throughout the lifecycle, specialists from various disciplines
    in the organization contribute additional details:

    - **Business analysts** — Detailed business rationale, tied to
      the business outcomes, and requirements refinement

    - **Project managers** — Milestones, versions, projects,
      timelines, roadmaps, and budgets

    - **Development teams** — Issues, tickets, and implementation
      details

    - **Operations teams** — Environment topologies, deployments,
      and configurations

    - **Architects** — Detailed information about dependencies,
      integrations, and technical relationships

    ## Component Relationships

    These components are not independent — they form an integrated
    whole:

    - **Personas** interact with **Stories** to deliver **Business
      Outcomes**
    - **Stories** consume and produce **Data Products** using
      **Ontologies** for semantic meaning
    - **Workflows** orchestrate **Stories** to create end-to-end
      business processes
    - **Concepts** link to **Ontologies** that provide the semantic
      foundation
    - All components are versioned, tested, and governed together as
      part of the Use Case

    This integrated approach ensures that every component is
    traceable, reusable, and aligned with the business outcomes the
    use case is designed to deliver.

=== "Life Cycle"

    ## Continuous Improvement

    Each individual Use Case goes through a lifecycle of continuous
    improvement:[^1]
    This lifecycle spans the entire EKG Method process, from initial
    idea through planning, building, running, and ongoing optimization.

    ![Use Case Lifecycle](../diagrams/out/use-case-life-cycle.svg#darkable)

    ## Lifecycle Stages

    The Use Case lifecycle aligns with the three main phases of the
    EKG Method:

    ### Plan Phase

    During the [Plan Phase](../process/plan/index.md), the use case
    starts as an idea and evolves into a well-defined requirement:

    - **Ideation** — Initial concept or business need identified
    - **Discovery** — Business opportunities and needs explored
    - **Definition** — Essential elements defined (name, description,
      outcomes, personas, concepts)
    - **Scoping** — Boundaries and dependencies identified
    - **Prioritization** — Position in the Use Case Tree established

    At this stage, the use case is "mile wide, inch deep" — broad in
    scope but not yet detailed in implementation.

    ### Build Phase

    During the [Build Phase](../process/build/index.md), the use case
    becomes executable:

    - **Design** — Stories, workflows, and data models designed
    - **Development** — Components implemented (ontologies, data
      products, stories)
    - **Testing** — Test scenarios defined and executed, ensuring 100%
      test coverage
    - **Integration** — Components integrated and dependencies resolved
    - **Verification** — Business outcomes validated against success
      criteria

    The use case transitions from a requirement to an executable,
    testable capability.

    ### Run Phase

    During the [Run Phase](../process/run/index.md), the use case
    operates in production:

    - **Deployment** — Use case deployed to production environment
    - **Operation** — Monitoring, maintenance, and support
    - **Measurement** — Business outcomes measured and tracked
    - **Optimization** — Continuous improvement based on performance
      data and feedback
    - **Evolution** — Updates and enhancements based on changing
      business needs

    The use case becomes a living, evolving capability that delivers
    ongoing business value.

    ## Iterative Refinement

    The lifecycle is not linear — use cases continuously evolve:

    - **Feedback loops** — Learnings from Run phase inform future Plan
      and Build activities
    - **Incremental delivery** — Use cases can be delivered in
      increments, with each increment building on the previous
    - **Versioning** — Changes are versioned to maintain stability
      while enabling evolution
    - **Reuse** — Successful use cases become reusable components for
      future use cases

    !!! tip "Lifecycle as a learning cycle"

        The Use Case lifecycle is fundamentally a learning cycle.
        Each phase provides feedback that improves the next iteration,
        ensuring that the use case continuously aligns with business
        needs and delivers increasing value over time.

    ## Relationship to Use Case Tree

    The lifecycle of individual use cases is managed within the context
    of the [Use Case Tree](use-case-tree.md):

    - **Tree structure** — The tree shows relationships and
      dependencies between use cases
    - **Governance** — Changes to use cases are governed through the
      tree structure
    - **Reuse** — The tree enables discovery and reuse of use cases
      across the enterprise
    - **Evolution** — The tree evolves as use cases progress through
      their lifecycles

    This ensures that individual use case lifecycles are coordinated
    and aligned with the broader enterprise strategy.

=== "Plan/Build/Run"

    ## Use Cases Across the EKG Method Process

    The EKG Method defines a process consisting of three phases, each
    with well-defined steps:
    [Plan](../process/plan/index.md),
    [Build](../process/build/index.md), and
    [Run](../process/run/index.md).

    The **Use Case Tree** is the common artifact across each of these
    phases — and most of their steps.
    As a use case progresses through these phases, different types of
    information become relevant and are captured within the use case.

    !!! tip "Progressive elaboration"

        Use cases start simple in the Plan phase and progressively
        gain detail as they move through Build and Run.
        This approach ensures that investment is made incrementally,
        with each phase building on the previous one.

    ## Information by Phase

    The following shows what information is captured for each use case
    during each phase:

    <div class="grid cards" markdown>
    
    - :material-floor-plan:{ .lg } __Plan Phase__

        -----    

        1. **Name + Business Description**
        2. **Desired Business Outcomes**
            - Definition of Success
        3. **[Personas](../concept/persona.md), [Concepts & Terms](../concept/concept.md)**
            - Add examples i.e. input for test scenarios
        4. **[Stories](../concept/story.md) & [Workflows](../concept/workflow.md)**
            - High level but agreed, metrics-based estimates
        5. **Tree Structure**
            - Break-down into existing or non-existing sub-use cases
              (some reusable, some specific to the parent use case)
            - Priority is to look up in the tree, not down, and define
              the longer-term "strategic use cases" as well

        [:octicons-arrow-right-24: Learn more about the _Discover Step_](../process/plan/discover.md)
       
    - :construction_site:{ .lg } __Build Phase__

        -----

        6. **Datasets**
            - Identify existing datasets or develop new
              [_Self-describing datasets_ (SDDs)](https://principles.ekgf.org/vocab/sdd)
        7. **Ontologies**
            - Map the given [Concepts](../concept/concept.md) to the
              right Ontologies
        8. **Test Scenarios**
            - Define test-datasets and test-scenarios for each
              [Story](../concept/story.md)
            - Provision continuous integration pipelines for continuous
              automated testing
            - Ensure 100% test coverage across all stories
        9. **Story Implementation Details**
            - All optional — e.g. SPARQL, SHACL, SQL, workflow, audit,
              history, provenance, entitlements, caching policies, etc.
        10. **Metrics**
            - Function point or story point-like metrics
            - Lead / cycle time metrics
            - Predict cost & delivery
            - Based on metrics of previous use cases

        [:octicons-arrow-right-24: Learn more](../process/build/index.md)

    - :material-run:{ .lg } __Run Phase__

        -----

        11. **Operational Metrics**
            - Performance data and usage statistics
            - Business outcome measurements
            - Quality metrics and error rates
        12. **Production Configuration**
            - Environment details and deployment info
            - Monitoring and alerting setup
            - Backup and recovery procedures
        13. **Optimization Opportunities**
            - Performance improvements identified
            - User feedback and enhancement requests
            - Cost optimization insights
        14. **Evolution Planning**
            - Updates and enhancements planned
            - Version roadmap
            - Integration with new use cases

        [:octicons-arrow-right-24: Learn more](../process/run/index.md)
    
    </div>

    ## Phase Transitions

    Use cases transition between phases based on readiness criteria:

    - **Plan → Build**: When business outcomes are defined, personas
      identified, and high-level stories agreed upon
    - **Build → Run**: When components are implemented, tested (100%
      coverage), and verified against business outcomes
    - **Run → Plan/Build**: When optimization or evolution requires
      new planning or building activities

    These transitions are not always linear — use cases may iterate
    within phases or return to earlier phases based on feedback and
    changing requirements.

    ## Continuous Evolution

    Even after deployment, use cases continue to evolve:

    - **Measurement** drives understanding of what works and what
      doesn't
    - **Optimization** improves performance and reduces costs
    - **Evolution** adds new capabilities based on business needs
    - **Reuse** enables other use cases to leverage successful
      components

    This continuous evolution ensures that use cases remain aligned
    with business needs and continue to deliver value over time.

=== "Similar Concepts"

    ## Related Approaches

    The concept of Use Cases in the EKG Method shares similarities with
    several other approaches in enterprise architecture and software
    development.
    Understanding these relationships can help contextualize how Use
    Cases fit into broader industry practices.

    ### Packaged Business Capabilities (PBCs)

    **Packaged Business Capabilities (PBCs)** are a concept from
    composable commerce and enterprise architecture that emphasizes
    modular, reusable business components.

    **Similarities with EKG Use Cases:**

    - **Modular design** — Both PBCs and Use Cases represent
      self-contained business capabilities
    - **Reusability** — Both are designed to be reused across different
      contexts
    - **Composability** — Both can be composed to create larger
      capabilities
    - **Business focus** — Both emphasize business value over technical
      implementation

    **Key Differences:**

    - **Scope** — PBCs are typically focused on commerce and business
      applications, while Use Cases in the EKG Method span all
      enterprise capabilities
    - **Semantic foundation** — EKG Use Cases are built on semantic
      models (ontologies) that enable deeper integration and
      interoperability
    - **Executability** — EKG Use Cases can be captured as executable
      models that run directly in the Enterprise Knowledge Graph
    - **Tree structure** — Use Cases are organized in a hierarchical
      Use Case Tree that provides governance and dependency management

    **Learn More:**

    - [WalkMe - Packaged Business Capabilities (PBCs)](https://www.walkme.com/glossary/packaged-business-capabilities/)
    - [ElasticPath - What Are Packaged Business Capabilities (PBCs)?](https://www.elasticpath.com/blog/what-are-packaged-business-capablities)

    ### UML Use Cases

    As discussed in the [Data & Tech Audience](#data--tech-audience)
    tab, Use Cases in the EKG Method share terminology with UML Use
    Cases but operate at a different level of abstraction.

    **Key Distinctions:**

    - **Abstraction level** — EKG Use Cases can represent entire
      capability domains, not just individual interactions
    - **Executability** — EKG Use Cases can be implemented as
      executable models
    - **Semantic packaging** — EKG Use Cases contain ontologies, data
      products, and workflows, not just interaction descriptions
    - **Tree organization** — EKG Use Cases are organized in a
      hierarchical tree structure for governance and reuse

    ### Microservices

    **Microservices** architecture emphasizes building applications as
    collections of small, independent services.

    **Similarities:**

    - **Modularity** — Both emphasize breaking down capabilities into
      smaller, manageable components
    - **Independence** — Both can be developed and deployed
      independently
    - **Composability** — Both can be composed to create larger systems

    **Key Differences:**

    - **Abstraction** — Use Cases operate at a business capability level,
      while microservices operate at a technical service level
    - **Semantics** — Use Cases are built on semantic models that
      enable deeper integration
    - **Business focus** — Use Cases are defined by business outcomes,
      while microservices are defined by technical boundaries
    - **Reusability** — Use Cases emphasize reuse of business logic,
      data models, and workflows, not just code

    ### Domain-Driven Design (DDD) Bounded Contexts

    **Bounded Contexts** in Domain-Driven Design define the boundaries
    within which a domain model is valid.

    **Similarities:**

    - **Domain boundaries** — Both define boundaries for business
      concepts and logic
    - **Contextual models** — Both recognize that the same concept can
      have different meanings in different contexts
    - **Business alignment** — Both align technical implementation with
      business domains

    **Key Differences:**

    - **Scope** — Use Cases can span multiple bounded contexts or be
      contained within one
    - **Executability** — Use Cases can be captured as executable
      models
    - **Tree structure** — Use Cases are organized in a hierarchical
      tree for governance
    - **Reuse focus** — Use Cases emphasize reuse and composition across
      contexts

    ## Summary

    While Use Cases in the EKG Method share concepts with these related
    approaches, they are uniquely designed for the Enterprise Knowledge
    Graph context:

    - **Semantic foundation** enables deeper integration and
      interoperability
    - **Executable models** allow use cases to run directly in the EKG
    - **Tree structure** provides governance and dependency management
    - **Business-first approach** ensures alignment with business
      outcomes and value

[^1]: The lifecycle diagram shown is a simplification
[^2]: [No-code](https://en.wikipedia.org/wiki/No-code_development_platform) or
      [Low-code](https://en.wikipedia.org/wiki/Low-code_development_platform)
      development allows non-programmers to create applications without
      hard-wiring business logic with a programming language
