---
title: >-
  C: Know What the Business Wants - Capture Business Requirements
authors:
- Jacobus Geluk
hide:
- toc
date_published: "2022-01-01"
description: >-
  Learn how to capture what the business really needs—short, mid, and
  long-term. Discover how the Use Case Tree Method ensures you know what the
  business wants and why.
keywords:
  - business requirements
  - requirements capture
  - business needs
  - EKG method
  - enterprise knowledge graph
  - product owner
schema_type: "Article"
---
# C: Know what the business wants & why

<!--summary-start-->
_Know exactly what the business---the customer or
product owner---really needs, short-, mid- and long-term._
<!--summary-end-->

## [Plan Phase](../process/plan/index.md)

One of the tasks during the planning phase of any new
initiative---or iteration---is to ["Discover"](../process/plan/discover.md)
the business opportunities & needs:

* In non-technical terms. No screen designs, no data models, just plain English.

* Without assuming anything about existing systems and "how
  things are done today".

* Translate to "pure" functional requirements --- and "nice
  to haves".

* Looking broad horizontally, thinking ahead. Mile wide, inch
  deep at this stage.

* Let the business "dream a little" about "what could be"
  and "what should be", so that future needs can be
  identified and communicated --- without necessarily
  committing to them (yet).

* Promote "thinking outside the box", encourage people to
  not make any assumptions about what is technically possible
  or not --- so often these assumptions unknowingly keep the
  bar lower than it could be.

* Continuously improve, new insights occur all the time, have one
  "living" shared data structure --- the [Use Case Tree](../concept/use-case-tree.md) --- that gets
  continuously updated with the latest insights even while parts
  of that Use Case Tree are already running in production or still
  worked on.

* Business clearly decides which strategic use case(s) -- in the tree --- 
  has/have priority. Capture these priority settings and use them to
  derive the right implementation order of use cases, determine 
  --- with the business --- the shortest path to delivering on the
  specified business outcomes.

## [Build Phase](../process/build/index.md)

Once a roadmap has been agreed, which is "the contract with the business" 
i.e. the budget holder or product owner, implementation of the first use
case on the given roadmap can commence.

Implementation means, in the context of an EKG and from the viewpoint of
the business:

* Specialists are adding details to the use cases that are on the roadmap.
* All effort will be visible. Anything that anyone does to implement a use cases
  is directly or indirectly related to that use case and therefore trackable
  and traceable providing full transparency to the business around:
    * progress, blockers
    * cost, risk, raid log
* The business never loses sight on what happens with their
  budget and agreed deliverables.
  All reporting to the business occurs in the context of
  the agreed roadmap, even after delivery.

## [Run Phase](../process/run/index.md)

Ideally, at higher levels of operational maturity, changes get rolled out to
production continuously and as frequently as possible so that any given update
to production is as small and impact-free as possible.

* End users get to see results on a continuous basis and will be able to provide
  immediate feedback in the expectation that their feedback will be heard and possibly
  lead to improvements in the very short term (which keeps people much more engaged)
* There will never be any "big bang deployments" anymore. There's no need anymore
  to send whole departments to training because of a giant new release, everything
  goes gradually and people get used to it in a more natural way --- boiling the frog 
  in cold water, thereby reducing the resistance to change and enabling a much
  more engaged user community.
* End users will be able to relate their work directly to the appropriate use cases
  as they are defined in the [Use Case Tree](../concept/use-case-tree.md) because the 
  Use Case Tree is part of the EKG itself and advanced user interfaces can link to it. 
  It describes the user's domain in their own terms. Direct feedback loops to all 
  relevant stakeholders are therefore possible which yet again promotes collaboration, 
  end user satisfaction, reduces costs and avoids technologists building something 
  that's wrong or will never be used.

