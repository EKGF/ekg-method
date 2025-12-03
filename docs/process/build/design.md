---
authors:
  - Jacobus Geluk
hide:
  - toc
description: "Design the EKG Platform architecture and use case specifications. Learn how to architect both the technical platform and business-focused use case designs in the Design phase."
keywords:
  - design
  - EKG architecture
  - platform design
  - use case design
  - EKG method
  - enterprise knowledge graph architecture
schema_type: "HowTo"
---
# Design

<!--summary-start-->
TODO
<!--summary-end-->

Of course, no one can just start building use cases on a technology platform that does not exist yet. Things
have to be architected and designed. Architecture, design and having a plan for those is important. And
there are many types of architecture involved. But generally we can split it up into two rather independent
streams of work as mentioned above: the platform and the use cases it supports. The platform
is primarily a technical concern whereas the design of the use cases is primarily about understanding the
business.

## Approach

Once the business case has been approved, as it comes out of the [Chart phase](../plan/chart.md)
an initial team can be created, the scope is clearly defined, and we know what the first
use case is to start with. 
First thing to do then is to organize design sessions with that team and go through all the various
types of architecture and devise a project plan of milestones and clearly defined deliverables.
Avoid doing it the waterfall-way, do it Agile but Agile does not preclude you from 
first having a good plan.

## Outputs

1. A well-informed team, prepared to successfully implement your use cases.
2. More detailed use case tree, including datasets, data sources, ontologies, 
   personas, business outcomes and user stories, all delivered within the
   context of the UCT, as a model.
3. Then the translation of that to:
    * Ontology Architecture
    * Technical Architecture
        - [EKG/Platform](../../vocab/ekg-platform.md), identification and 
          functional description and requirements of all the various 
          platform services needed.
        - A design and architecture for the ”DataOps Environment” 
          which connects the upstream data providers and downstream 
          data consumers to the EKG/Platform.
        - A design and architecture for the user experience (either 
          bespoke or generic model-driven UI).
    * A clear sequence of deliverable artifacts as input to the project plan.
4. A realistic roadmap that can be explained satisfactorily to stakeholders
