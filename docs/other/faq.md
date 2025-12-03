---
title: FAQ
author:
  - Jacobus Geluk
description: "Frequently asked questions about the Use Case Tree Method and Use Case Tree. Get answers about use cases, stories, personas, data products, and the Enterprise Knowledge Graph methodology."
keywords:
  - FAQ
  - frequently asked questions
  - EKG method FAQ
  - use case tree FAQ
  - enterprise knowledge graph questions
schema_type: "FAQPage"
--- 
# Frequently Asked Questions

## What is a Use Case?

A [Use Case](../concept/use-case.md) is an aggregation of user (or data-) [stories](../concept/story.md) on a common theme.

They are the modules---or components, so you will---of an [EKG](../vocab/ekg.md).
A business-focused packaging of stories, concepts, personas, logical [self-describing](https://principles.ekgf.org/vocab/sdd/)
datasets (or data products), ontologies, workflows, user interface models and functionality.

## What’s the relationship to user stories?

A user story can be seen as a black-box function with inputs and outputs.
We model these inputs and outputs initially just as simple "[Concepts](../concept/concept.md)"
(and the terms that are being used for those concepts).
By adding more and more detail to these stories, they eventually become runnable or 
executable and can be invoked as an HTTP API, in response to a Kafka message, 
or via any other technology.
Stories can be "implemented" using SPARQL, SQL, Gremlin, or calls to external APIs 
of any sort since they're seen as a "black box," it really doesn't matter, although usually, 
the easiest way to implement them is, of course, SPARQL since an EKG is primarily an 
RDF-based world.

A story is (by precedent) linked to only one use case.

## How do EKG use cases compare to UML use cases?

Not focused on a single system; not linked to technical software components.

EKG use cases can be "higher level," more generic, and more abstract than a UML use case
and are, therefore, more suitable for the EKG scale and have much higher reuse potential.

The UML notion of single-user interaction is closer to an EKG story.

## What are the relationships between the use cases?

A use case can be a `componentOf` of other use cases and therefore form a hierarchy that
more or less resembles a tree structure that can be easily visualized on a whiteboard hence
the term [Use Case Tree](../concept/use-case-tree.md/).

## Are use case trees actually trees (hierarchies)?

No, they are [DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (one use case 
can support, and be supported by, many others) but we obviously didn't want to call it 
"Use Case DAG" :-)

## What is the detail needed behind each use case? - Narrative? Happy case? Exceptions

Here's a [template](../concept/use-case.md#plan-build-run) for the kind of information that we need
to collect for any given use case during the various phases in their life cycle.

## How are use cases named?

- traditionally: verb phrase including noun, e.g., _Maintain customer accounts_
- actual: noun phrase for a data subject area, which may be singular or plural, 
  for instance, _Customer Accounts_.

With just using nouns, any given use case tree starts to look like one of three things
or some sort of combination of it, especially at the higher levels in the tree:

- Domain Taxonomy
- Business Capability Map
- Organization Structure

This may be a bit confusing because it's none of those three things, but there is a close relationship
between these four concepts (domains, capabilities, organizational units, and Use Case Trees).
And that's precisely how it should be; your EKG's modular structure should look like 
_your_ enterprise structure.

However:

- `<usecase> improves <business-capability> .` (zero or more)
- `<usecase> isOwnedBy <organizational-unit> .` (1)
- `<usecase> covers <subject-matter-domain> .` (zero or more)

## What are the diagrams?

They show only use cases and their relationships, with supporting use cases below the ones they support.

Stories are not depicted.

## What about Actors/Personas?

We use the term [_Personas_](../concept/persona.md) rather than _Actors_ or _Roles_ to avoid confusion because
they are slightly different concepts. Like in the real world, you could have a `Person` who is an `Actor` playing
a `Role` as a certain `Persona.`

- `<persona> isUsedIn <usecase> .`
- `<story> hasPersona <persona> .`

## Does this imply that Personas are always human?

No, other systems can invoke the stories of a given use case that act like a persona.
At run-time, stories are invoked (through a given technology stack) in the context of an authenticated
session (except for the persona `Anonymous`). For each authenticated user---or system---account
there can be one or more current Personas in a given session.

- `<user-or-system-account> hasPersona <persona>` (1 or more)

## Do personas have inheritance?

Yes, through `isSubPersonaOf`:

- `<persona-A> isSubPersonaOf <persona-B>` (0 or more)

Inheritance works bottom-up, `<persona-A>` is a sub-persona of `<persona-B>,` which means that
a user that has been associated (through a computation) with `<persona-A>` will, therefore, also be
associated with `<persona-B>.`

## What is the relationship to ontologies?

Any given use case has business terms and concepts associated with it.

We initially capture what the business explains to us and capture "business requirements" in their
own context-specific language.

We want the business to "own" its use cases and always recognize them throughout their whole
life cycle, from initiation to production and beyond.

Changing terms simply because some external ontology has a "better" name for the same concept is
not helping.
The whole point of using semantic technology is that we can easily model all "semantic conundrums" 
and make sure that we always address "the business" (i.e., the customer) with their language
while keeping the backend EKG models "generic" and linked to any number of appropriate ontologies.

A "concept" in the Use Case Tree Method is, therefore, "the linking pin," linking local business language to
any other appropriate concepts in any number of other ontologies.

- `<usecase> usesConcept <concept> .`
- `<concept> is a Concept|ClassConcept|PropertyConcept|ShapeConcept .`
- `<concept> predicate <owl-defined predicate> .` (optional)
- `<concept> datatype <xsd datatype> .` (optional)
- `<concept> ....` (all kinds of mapping information)
- `<concept> term <term>` (where term can be a multilingual context-specific name for the concept or
   a technology-stack specific name)
- `<concept> isInputFor <story>`
- `<concept> isOutputFor <story>`
- `<concept> isUsedInUseCase <usecase>` (derived from the stories of the use case)

## What is the relationship to Business Processes?

Every use case can be enriched with all kinds of additional models, such as:

- Project Model
- Time Registration
- Funding Model
- Maturity Requirements (linkage to EKG Maturity Model)
- Issue Management (JIRA, GitHub Issues, production issues, etc.)
- Implementation Details (SPARQL, SQL, anything)
- Deployment Details (Kubernetes cluster, required services, etc.)
- Organizational Model (ownership and the like)
- Life Cycle Model
- User Interface Models (for model-driven UI)
- Workflows and Business Processes

We believe that business processes can be modeled as a collection of workflows in the context
of this method, spanning across the workflows of many use cases.

## What is the relationship to Strategy?

The Use Case Tree of an organization has everything to do with Strategy;
overall [Business Strategy](https://maturity.ekgf.org/pillar/business/capability-area/strategy-actuation/),
[Data Strategy](https://maturity.ekgf.org/pillar/data/capability-area/data-strategy/), 
[Organizational Strategy](https://maturity.ekgf.org/pillar/organization/capability-area/executive-leadership/capability/organizational-strategy/)
and [Technology Strategy](https://maturity.ekgf.org/pillar/technology/capability-area/technology-strategy/).

These are the topics that we discuss in the EKGF Maturity Model at [https://maturity.ekgf.org](https://maturity.ekgf.org).

In general:

- `<usecase> improves <business-capability> .` (zero or more)

Via an intermediate object called "Business Outcome", so it actually looks more like:

- `<usecase> delivers <business-outcome> .`
- `<business-outcome> improves <business-capability> .`
- `<business-outcome> isPartOf <business-strategy> .`

## What is the relationship to Business Capability?

See above.

## What is the relationship to organizations?

Any EKG enterprise will have their own [use case tree (UCT)](../concept/use-case-tree.md) but
not all use cases are owned by that enterprise since many use cases may have been
provided by external parties such as the EKGF community as "reusable components".

Any use case itself "lives" in the EKG as a graph of detailed facts, the more detail there
is, the more those details can be executed by general services, ultimately providing
whole "applications".

All those additional details are modeled with their own ontologies, including
the organization details e.g. who "owns" the use case, who is responsible for it, which
deployments do we have across the enterprise, who was involved and which department
and so forth.

## What is the relationship to technology?

Use Cases can be implemented in many different ways. In fact, a Use Case does not even
_have_ to be implemented as a "model-driven application" inside the EKG, it could also
just stand for some external "legacy" system. For instance if your organization has
an old mainframe running "Billing" for 40 years, built with COBOL, then we can add
that as a Use Case, a black box really, to the Use Case Tree.

The implementation of a use case can be anything. Implementation details will be 
added by engineers using their own models.

Point is: everyone can talk to the Use Case Tree; business people, any stakeholder,
end users, ontologists, data modelers, knowledge graph engineers or other data scientists,
COBOL programmers, devops people, they're all talking about the same deliverables that 
the business ultimately pays for.

## How, if at all, is a UCT specific to Knowledge Graphs?

See previous question as well. No, the Use Case Tree is not specific to Knowledge Graphs,
it can in fact capture the whole data and technology landscape in one model.

It is just another way to model all knowledge, data and functionality in an enterprise
and provide a relatively simple language for all specialists to talk to, reducing
confusion, communication disconnects, the gap between "business & technology" etc.

## How is a use case associated with EKG maturity?

Certain use cases may require a certain level of EKG maturity.

## How to know which use cases to create?

Selecting the "right" first use cases is a bit of an art.

Some rules of thumb:

- Define use cases with a minimum number of "dependencies"
   - dependencies come in many forms, ontologies, datasets, people, maturity requirements,
     departments and so forth.
- Start with "reference data" (so that we have something to link to)
- Build upon standard use cases (downloadable from EKGF and others, or other internal departments)
- Select the shortest path in the tree
    - should lead quickly to the delivery of a "lighthouse use case" or a "strategic use case", 
      delivering real value to the business, ideally value that no other technology stack can currently 
      (realistically) provide.
- Deliver straight to production, from the first tiny use case onwards
    - Implement full test-driven development with 100% test-coverage
    - Implement full end-to-end [continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) 
      or [GitOps](https://www.gitops.tech/).
    - Get through all red-tape and learning curve with the technology first so that delivery
      of all subsequent use cases is not held back and it can be proven that price and time-to-market
      will be reduced drastically with each subsequent use case delivery.
 
## What is reusable?

Most Use Cases can be developed as "reusable components" (if you do it right).
If all datasets that a given use case works with are so called "self-describing datasets" (SDDs)
or "self-describing data products" then there is already a high-level of "decoupling" from
the nitty-gritty details of all the various siloed systems providing or consuming that data.

Which makes each use case already drastically more reusable than a comparable bespoke application
built with common technology stacks like Java or Python since they generally do not have that
level of decoupling.

Besides that, most use cases are pretty generic in the first place, managing legal entities
or contracts is primarily driven by law and there's barely any "secret sauce" associated with
those use cases that would make a business more competitive. So these general use cases can
be acquired from the community of other companies building these use cases, vendors or even
competitors.

Every successful technology stack has a central place where the community publishes their
reusable components, for JavaScript that is [https://npmjs.org](https://npmjs.org), for
Java we have [Maven Central](https://mvnrepository.com/repos/central) (and others), Python has
[https://pypi.org](https://pypi.org) and for the EKG we have the EKGF Catalog 
(under development, it's in its very early stages still) at 
[https://catalog.ekgf.org](https://catalog.ekgf.org).

## How are Use Cases "plug and play?"

Any given use case can be "enriched" with more and more detail during its development.
This eventually leads to it becoming "executable", which in effect turns it into the 
EKG equivalent of an "application".
Use Cases at this level of sophistication are then "plug and play" and can be re-deployed
in other EKGs.

## How do you work - top down or bottom up?

Think big, start small, rinse, repeat, accelerate. See [Process](../process/plan/index.md).

### Think Big

Creating your overall enterprise use case tree is "thinking big".
It provides a strategic roadmap for all use cases to be built (and it also
serves as a "parking lot for all good ideas").
So that's a top-down approach.

### Start Small

Then once a business case has been created and approved (see [Chart](../process/plan/chart.md)),
the build-phase can start with a use case at the bottom of the tree, building all
lego bricks to then build higher level use cases.
That's the start small (and bottom up) approach.

### Rinse, Repeat, Accelerate

Optimize the development process, learn from mistakes, gain experience, perform
analysis on real production usage, and rerun the cycle.

## When is a use case “done”?

A use case is "done" when the business says so.
Ideally, the initial use case in its early plan stage of its life cycle serves
as a "contract with the business" that includes agreed test scenarios so that
a it can be [verified](../process/build/verify.md) and validated with the business
that a given use case is "done".

After deployment to production, business metrics could be [collected](../process/run/measure.md)
to check whether the use case actually delivers on the agreed business outcome.

## How to measure the design and the implementation?

## How can a use case drive a UI?

In two ways:

### Bespoke UI

A use case can be "served" (or "executed") by a service or "engine" that reads
all the metadata of the use case and translates that into action, without the
need to generate any code. For instance, most low-level stories of the use case
can be translated directly into HTTP APIs, for instance the URL
`https://yourcompany.com/legal-entity-management/get-dissolved-parties`
would, when called, invoke the story "Get Dissolved Parties" and return the results.
This can be used by any UI-frontend technology such as React and JavaScript to
build any imaginable user interface.

### Model-driven UI

In a more sophisticated setup you could have some frontend-logic that first queries
the EKG for the relevant user interface model, translating that to a user interface
that can be as advanced as a bespoke user interface.
The advantage of that is scalability. An EKG will usually deal with hundreds if not
thousands of different types of objects and hundreds if not thousands of use cases
around those objects. At higher levels of maturity you do not want to be forced to
develop hundreds of bespoke user interfaces. Each use case can come pre-packaged
with its user interface models that allow your organization to not have to build
any UI for it, showing it fully integrated with all other use cases with your
corporate styling etc.

## How can you drive (data) modeling?

One major "lesson learned" is that semantic technology and knowledge graphs easily
allow people to "[boil the ocean](../objective/avoid-boiling-the-ocean.md)" and 
"model the whole world" using generic abstract ontologies, sometimes even up to 
philosophical levels of abstraction.

One of the key objectives of the Use Case Tree Method is to [avoid boiling the ocean](../objective/avoid-boiling-the-ocean.md)
by creating a laser sharp description of what the business needs and pays for.
And make that description testable and therefore verifiable.

This then also provides focus for ontologists and data modelers to only focus
on delivering the use case at hand. Obviously, a good ontology is "use case independent"
so that's a bit of a paradox, on one hand you want to keep the ontology generic,
abstract, and use case independent, and on the other hand you do not want to waste time
and make it too beautiful from the start. Finding that balance is a key objective
for the ontologist, the use case's automated tests being the overall judge.

## What sort of system is it suitable for?

Theoretically there is no limitation to this technology, basically any system or application
can be built as an EKG use case.

Practically, there will always be many other systems that are specialised in what they're
doing. Source of record systems, PeopleSoft, Salesforce, spreadsheets, trading systems,
blockchains and the like. The EKG can serve as a layer on top of all those other systems, 
connecting the dots across the enterprise or ecosystem.

## Not suitable for?

EKG as a general concept is not tied to specific types of databases although standard
semantic graph database products (aka "triple stores") are the de-facto choice to underpin
the EKG. However, many other technologies can be used as well, with a bit more work,
such as time series databases, Kafka, relational databases and labeled property graph (LPG)
databases.

