---
authors:
  - Jacobus Geluk
hide:
  - toc
description: "Discover all use cases in the given scope and create a Use Case Tree that shows a viable pathway towards strategic goals. Learn how to identify business outcomes and select the shortest path to value in the Discover phase."
keywords:
  - discover
  - use case discovery
  - use case tree creation
  - EKG method
  - enterprise knowledge graph
  - business outcomes
schema_type: "HowTo"
---
# Discover

<!--summary-start-->

- strategic [use cases](../../concept/use-case.md) & desired [business outcomes](../../concept/outcome.md)
- initial [Use Case Tree](../../concept/use-case-tree.md) and primary branch
- shared business language & knowledge
- aligned priorities and reuse opportunities

<!--summary-end-->

Discover all strategic [use cases](../../concept/use-case.md) in the given scope that support the agreed vision
and strategy. Create the initial [Use Case Tree (UCT)](../../concept/use-case-tree.md) for the organization.
Identify desired mid and long term [business outcomes](../../concept/outcome.md).
Select the primary branch in the Use Case Tree to focus on, break that part
of the Use Case Tree down into deeper levels, identify the shortest pathway to real business
value.

The Discover phase translates organizational and business priorities into 
strategic use cases. 
In this step, priorities are converted into data requirements devoid of any technical considerations. 
The output aligns all stakeholders on intermediate deliverables and emphasizes those with 
the greatest reuse potential. 
This helps refine the business case and plan implementation as a series of 
steppingstones toward more strategic goals.

## Approach

The team works with business experts and change managers in a series of interactive
workshops to define requirements. 
The team adopts the business language in the selected context to capture goals, 
data requirements, [stories](../../concept/story.md) and [workflows](../../concept/workflow.md). 
These are aligned as a set of visual roadmaps to be used to create onward business
cases. 
The team leverages the [knowledge graph maturity model](../../vocab/maturity-model.md) 
to help frame each deliverable in terms of staged business capabilities.

## Audience

* Business Audience, “the customer”, product owners, business experts, change managers, SMEs
* EKG Champion(s)

## Outputs 

All outputs below describe the properties of what a [Use Case Tree](../../concept/use-case-tree.md) is:

* Identification of strategic [use cases](../../concept/use-case.md), priorities and desired [business outcomes](../../concept/outcome.md)
* Initial scope in the form of one priority strategic [use case](../../concept/use-case.md), 
  one branch of the [Use Case Tree](../../concept/use-case-tree.md) to focus on
* Evaluation criteria from both a business process and data perspective to ensure 
  EKG synchronization with defined requirements
* Conversion of strategic priorities into a staged [Use Case Tree](../../concept/use-case-tree.md) specifying 
  business functionality and data requirements
* A shared understanding of the requirements for success including the investments 
  needed to deliver against expected functionality
* Well managed and agreed expectations with "the business"
    * A "Contract" with the business in plain English, devoid of any technology assumptions
    * One-to-one and end-to-end linkage between a plain english business user story and the
      evidence that this user story has been delivered, works and stays working[^testing]
* **A permanent artifact, a shared model, continuously being improved, that all stakeholders across
  the enterprise can talk to for the whole life-cycle of any given [use case](../../concept/use-case.md) (even in production)**
* Living data structure that becomes part of the [Enterprise Knowledge Graph](../../vocab/ekg.md) itself for its whole life-cycle
* Modular structure of components that allows for an ecosystem of internal and external reusable
  components compliant with standards set by the EKGF.

[^testing]: this relates to all the further detail that will be added to each use case and its
stories in all subsequent phases allowing the business to get insights to any level of depth
and exactly trace cost, risk, timelines etc.

## Topics

### The Use Case Tree practice

Explanation of the key principles of how an EKG and its development can be structured in an organization
and what leads to successful and modular implementations.

### What is a "strategic use case"

A **strategic use case** is more than just a good first candidate to implement.
It is a lighthouse use case that is of **strategic importance to the business**:
it visibly saves money, increases profit, improves quality, reduces risk, or boosts efficiency
in a way that matters at the C‑level.

Strategic use cases are the scenarios that convince executive leadership to **invest in EKG strategically**,
not just as a one‑off project.
They demonstrate that an EKG‑based approach can unlock long‑term competitive advantage, not merely solve a local problem.

### Examples of Strategic Use Cases

Discuss some “standard” strategic use cases (at this helicopter-level these “use cases” are more like
“domains”) such as Enterprise Fraud Detection, Enterprise Compliance Management, Connected Inventory 
and Customer 360.

* Reg problems. Lineage. CCAR esp. threat of Fines.
* Data privacy. Sharing agreements. Cataloging PII data. GDPR and CCPA. The threat of fines.
* Reducing data estate/sprawl. Cost.
* Move data to the cloud. Cost & capability
* Improving Data Quality generally. Risk
* Supporting the digitalization / Transform / Innovation agenda, capability play

### Identify your Strategic Use Cases & Business Outcomes

Identify the organization's own “strategic use cases” and formulate their expected business outcomes.
Think outside the box, “dream a little”, think long term, set long term goals so that a reuse strategy
can be derived. Rough sketch areas where the organization could (and should) possibly go if
innovations, technology and organization could deliver.

### Select a Strategic Use Case & Identify Stakeholders

After step 3, select one area to dive into, with the agreement of all key stakeholders for that
area.

### What is "the right use case" (to start with)

One of the key outcomes of the Discover phase is the identification and definition of the **first** [use case](../../concept/use-case.md) to start with.
Ideally, this is a **lighthouse use case**: a concrete example that shows everyone why building use cases in an Enterprise Knowledge Graph context is worth the effort in the first place.

Expectations around this first use case are often sky-high — it can become a go/no‑go decision point for further EKG investment — so **expectation management is critical**.
Stakeholders need to understand that the first use case may actually take **longer** to implement than building something similar on the existing "bread and butter" technology stack:
teams know those tools, they have done it many times before, and can “crank out” another solution quickly.
Doing the same thing with a **new technology stack** and several **new paradigms** (graph, semantics, EKG, GenAI, etc.) almost always takes more time at first.
The real payoff is that **every subsequent use case will go faster and faster**, because:

- you are building everything with **reuse** in mind (components, models, workflows, test assets)
- you rapidly build up a catalog of reusable EKG components
- GenAI can increasingly help you discover, combine, and implement those components faster

When choosing the lighthouse use case:

- pick a use case that is **not “typical”** — something that is genuinely **hard to do with existing technology**, for example because it combines complex data from multiple sources or domains
- pick a use case that sits **in the middle of the designated scope**, with **high reuse potential** into neighboring areas of the [Use Case Tree](../../concept/use-case-tree.md)

The goal is not to “win” on raw delivery speed for the first use case, but to **prove the point**:
that an EKG‑based, reuse‑driven approach will make each subsequent use case cheaper, faster, and more robust than the last.

### Deep-dive Strategic Use Case & Business Outcomes

Develop the details of the “use case tree” of the selected top-level strategic use case.

### Work out Use Case Roadmap

Practical roadmap (short and long term) of use cases, reusable EKG components that can be
delivered in a logical sequence. 
All stakeholders have realistic expectations and know exactly what is going to be delivered, 
why, and in which order.

