# Use Case


=== "Business & Management Audience"

    A Use Case specifies a distinct set of business requirements --- ideally
    but not necessarily captured as an "executable model" --- resulting in
    a specific business outcome.

    It starts with ideas for use cases that could come from any person in 
    the organization at any point in time.
    We want to capture all these ideas (and as much of the knowledge behind
    those ideas) and create one data structure for it that
    we call "the [Use Case Tree](/concept/use-case-tree)" because it looks like an inverted tree: it's
    something that starts on a whiteboard, showing a break-down of a
    component of the business into smaller components.
  
    Anyone should be able to contribute ideas that may or may not 
    end up as fully implemented use cases to end up in the organization's 
    [Use Case Tree](/concept/use-case-tree), whether they are viable or not.
    If an idea for a given use case is rejected then show the rationale
    for that to everyone so that everyone can learn, and we're not wasting
    anyones time on that idea again. 
    Let people contribute. 
    All knowledge workers, all specialist users, data architects, 
    technical architects, ontologists, end users, business executives, 
    literally anyone should be allowed to understand:

    * What's our 
      [business identity](https://maturity.ekgf.org/pillar/business/background-and-intro/#business-identity)?
      Our [mission and strategy](https://maturity.ekgf.org/pillar/business/capability-area/strategy-actuation/)?
      What do we all this for (besides being profitable), what are the long term
      objectives that we are going to achieve?
    * How does that map to our current and future data and technology landscape?
        * (without becoming too technical or detailed, we want everyone to be able to chip in)
    * [Assess](../process/plan/assess.md) all our organization's capabalities,
      as specified in the 
      [Maturity Model for the Enterprise Knowledge Graph (EKG/Maturity)](https://maturity.ekgf.org) 
      related to our own EKG and how they match with our ambitions to implement our 
      strategic use cases?
    * How does our "technical debt" fit in? (identify the functionality of our 
      technical debt as use cases in the tree as well)
        * How are we going to "rationalize" our current siloed landscape (and technical debt)?
    * What are the short and long term priorities?
    * What are the milestones and the roadmap? (see ["Chart"](../process/plan/chart.md))
    * Which ideas (for use cases) have been proposed, considered approved or rejected and why?

=== "Data & Tech Audience"

    The term "use case" means something specific to a technical audience who
    usually assume that the term use case means what the Object Management Group (OMG)
    defines what it is in their Unified Modeling Language (UML) and
    its ["use case diagrams"](https://en.wikipedia.org/wiki/Use_case_diagram).

    Although there are many similarities and overlap --- which is why we are repurposing
    the term --- it is not exactly the same, in our Use Case Tree Method:

    - use cases often are used a much broader and more abstract container concept ---
      compared to a UML Use Case --- that can be put in a "tree structure" where at the
      highest levels of these trees a use case can represent a capability domain or 
      a "strategic use case" --- or basically anything that fits well with the business.
    - at the lowest levels in this tree we would end up with use cases that are much more
      like turn-key components for the EKG, 100% reusable delivering "no code"-functionality[^2].

=== "Key components"

    For every Use Case we specify:

    - A name and a description
    - The desired or expected business outcome(s) and how they can be measured
    - The ["personas"](persona.md) of all the people and systems that are involved
      in the domain or scope represented by the Use Case
    - The concepts and their terms as they're used in the context of the Use Case

    At a later stage in the life-cycle of the Use Case we add:

    - The stories, see [Story](story.md)
    - The [datasets](dataset) and their ontologies
    - The workflows

    Specialists of various disciplines in the organization can add their details
    such as:

    - detailed business rationale, tied to the before-mentioned business outcomes
    - milestones, versions, projects, timelines, roadmaps, budgets
    - issues, tickets
    - environment topologies, deployments and configurations
    - detailed information about the various types of dependencies

=== "Life cycle"

    Each individual Use Case itself goes through a life-cycle of continuous improvement like:[^1]

    ![Context](../diagrams/out/use-case-life-cycle.svg#darkable)

=== "Plan/Build/Run"

    The EKG/Method defines a process that consists of three phases where each phase has 
    well-defined "steps":
    [Plan](../process/plan/index.md), 
    [Build](../process/build/index.md) and 
    [Run](../process/run/index.md).
    The common artifact across each of these phases---and most of their steps---is the Use Case Tree
    where certain information is relevant to that phase for each of its Use Cases:

    <div class="grid cards" markdown>
    
    - :material-floor-plan:{ .lg } __Plan Phase__

        -----    

        1. Name + Business Description
        2. Desired Business Outcomes
            - Definition of Success
        3. [Personas](../concept/persona.md), [Concepts & Terms](../concept/concept.md)
            - Add examples i.e. input for test scenarios
        4. [Stories](../concept/story.md) & [Workflows](../concept/workflow.md)
            - High level but agreed, metrics based estimates
        5. Tree Structure
            - Break-down into---existing or non-existing---sub-use cases
              (some of which are reusable and some of which are specific to the parent use case)
            - Priority is to look up in the tree, not down, and define the longer term “strategic use cases” as well

        [:octicons-arrow-right-24: Learn more about the _Discover Step_](../../process/plan/discover/)
       
    - :construction_site:{ .lg } __Build Phase__

        -----

        6. Datasets
            - identify existing datasets or develop new
              [_Self-describing datasets_ (SDDs)](https://principles.ekgf.org/vocab/sdd)
        7. Ontologies
            - map the given [Concepts](../concept/concept.md) to the right Ontologies
        8. Test scenarios
            - define test-datasets and test-scenarios for each [Story](../concept/story.md)
            - provision continuous integration pipelines for continuous automated testing
            - ensure 100% test coverage across all stories
        9. Story-implementation details
            - all optional -- e.g. SPARQL, SHACL, SQL, workflow, audit,
              history, provenance, entitlements, caching policies, etc
        10. Metrics
            - function point or story point-like metrics
            - lead / cycle time metrics
            - predict cost & delivery
            - based on metrics of previous use cases

        [:octicons-arrow-right-24: Learn more](../process/build/index.md)

    - :material-run:{ .lg } __Run Phase__

        -----

        Additional detail added after deployment.

        [:octicons-arrow-right-24: Learn more](../process/run/index.md)
    
    </div>
    



=== "Similar Concepts"

     * Packaged Business Capabilities
        * [WalkMe - Packaged Business Capabilities (PBCs)](https://www.walkme.com/glossary/packaged-business-capabilities/)
        * [ElasticPath - What Are Packaged Business Capabilities (PBCs)?](https://www.elasticpath.com/blog/what-are-packaged-business-capablities)

[^1]: the life-cycle diagram shown is obviously a simplification
[^2]: [No-code](https://en.wikipedia.org/wiki/No-code_development_platform) or 
      [Low-code](https://en.wikipedia.org/wiki/Low-code_development_platform) development
      allows non-programmers to create applications without
      hard-wiring business logic with a programming language




