# Use Case Tree (UCT)

!!! warn

    Work in progress

Some notes as input for this article (to still be written):

- The Use Case Tree is a model at a higher level of abstraction than User Stories.
- It is a differentiator in the EKG/Method
- It enables consultative discussion that can identify options enterprises may otherwise not consider
- There is a need for something above User Stories to help define scope and priority
- The most critical and most important ”artifact” in the development of an Enterprise Knowledge Graph
  (EKG) is “the Use Case Tree” (UCT).
    - The Use Case Tree is the EKG’s equivalent of a long term data strategy and business capability plan.
      - The Use Case Tree is the EKG high level requirements overview, scoping and dependency model.
        In its initial stages, in the [Plan Phase](../process/plan/index.md), it gives a mile wide, inch deep view 
        of business capabilities.
- The Use Case Tree is a breakdown of strategic planned-for capabilities into smaller building blocks, all
  called ”use cases”. Strategic long term use cases such as
  ”[Enterprise Risk Management](https://catalog.ekgf.org/use-case/risk-management/)” or 
  ”[Client 360](https://catalog.ekgf.org/use-case/client-360/)” 
  are broken down into smaller use cases that can (and should) be done first.
- Each ”use case” is a module, an EKG component so you will, a building block with which other use cases
  can be constructed.
- Everything we ever do in a business, especially in the data and technology pillars of that enterprise, 
  should be related to ”a use case” in the Use Case Tree.
- The ”Use Case Tree” is a practice and is part of the Enterprise Knowledge Graph Method (EKG/Method).

## The primary reasons for creating a Use Case Tree are:

### 1. Know what the business wants.

Know exactly what the business---i.e. the customer or product owner---really needs, short-, mid-
and long-term.

#### (a) Plan phase: Discover the business opportunities & business needs

One of the tasks during the planning phase of any new initiative – or iteration – is to ”Discover”
the business opportunities & needs:

- In non-technical terms.
- Without assuming anything about existing systems and ”how things are done today”.
- Translate to ”pure” functional requirements – and ”nice to haves”.
- Looking broad horizontally, thinking ahead. Mile wide, inch deep at this stage.
- Let the business ”dream a little” about ”what could be” and ”what should be” so that future
  needs can be identified and communicated – without necessarily committing to them (yet).
- Promote ”thinking outside the box”, encourage people to not make any assumptions about
  what is technically possible or not – so often these assumptions unknowingly keep the bar
  lower than it could be.

#### (b) Build phase: Translate requirements into an easy to understand model i.e. the Use Case Tree

- ”Contract with the business” i.e. the budget holder or product owner., every major change
  to the Use Case Tree will have to be signed off by the product owner.
- Capture it as ”meta-data” that will be part of the EKG – all the way to production.
- Capture it in such a way that ”everything that we ever do” is always directly or indirectly
  relatable to ”a use case” in ”the Use Case Tree”.
- The business never loses sight on what happens with their budget and agreed deliverables.
  All reporting to the business occurs in the context of the agreed Use Case Tree, even after
  delivery.

### Bridge the traditional gap between Business & Technology.

- Engage with the business, the product owner and get continuous buy-in from the product
  owner during the life-cycle of the agreed use cases.
- But not only with the product owner of the direct use case being developed but also show to
  the business what other future needs need to be considered. For instance, if one use case
  e.g. ”Legal Entities” needs ”workflows”, would it make sense to invest a bit more effort to then
  create a reusable workflow component that can also be used for many other use cases such
  as ”Shareholding disclosure”?
- Yes, the customer is always right but the Use Case Tree shows to the customer that there are
  many other customers (or future customers, in and outside the organization even) and why it
  makes sense to prioritize reuse and how that not only could deliver more quality but also create
  more buy-in from peer stakeholders across the firm or even across the industry.
– In other words, do not select one product owner to be the single stakeholder but also get
  other stakeholders of neighboring or higher level use cases in the room, their requirements
  may influence the reuse agenda and therefore the roadmap. It may sound paradoxal but
  investing in reuse will not slow things down but speed things up.

### Managed Expectations

The Use Case Tree is the best form of ”expectation management”, creating an agreed and 
realistic strategic roadmap.

### Modularity Managed

The Use Case Tree is a foundational mechanism to create an ecosystem of reusable components
for the EKG.

### Avoids ”boiling the ocean”

Semantic Technology based projects often spend a lot of time "boiling the ocean", modeling
everything in a given domain. The Use Case Tree and its individual use cases define an agreed
scope at the detail level (without becoming technical).

- Provides focus for the Center of Excellence (CoE), ”cranking out” use cases one by one
- Ontology development will be focussed on delivering on the requirements (user stories and
  concepts) of the agreed use cases rather than ending up in philosophical exercise.

### Map of all Knowledge 

The Use Case Tree provides a ”map” of all knowledge, data and functionality (whether implemented
as running EKG use cases or not) of the enterprise.
Which is not only useful for users of the EKG but also a necessity since all of these use cases are
served by one platform – albeit distributed and federated etc – there will be many stakeholders with
different agendas that would not care – nor have to care – about the wishes of the stakeholders in
other use cases. However, updates to one use case could potentially also affect other use cases.

That’s why:

1. all changes & updates have to be done gradually, no ”big bang” releases and
2. all inter-dependencies need to be really clear and tested in-full automatically and continuously.

So, for instance, when some sub-use case in a high-level use case is also used in another high-level
use case then a change that serves the needs of one could potentially also affect the other and its
users. That’s why we need the Use Case Tree, to allow us to avoid any disruption across the board.

### Foundational structure for quality

The Use Case Tree is a foundational structure for quality since it enforces, requires and 
enables 100% test coverage based on real business scenarios and requirements.

- A use case has a life-cycle that starts with a name and a description and ends1 with a fully
  detailed model of all related concepts, personas, business outcomes, datasets, ontologies, user
  stories and dependencies. That model is all captured in the EKG itself which allows the EKG
  to not only fully and thoroughly test things during development time (build phase) but also
  in production (run phase). Which provides the level of quality that an EKG needs to have to
  become truly able to support enterprise level strategic use cases.
