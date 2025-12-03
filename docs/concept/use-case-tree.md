---
description: "The foundational structure that organizes business capabilities into reusable, governed components within the Enterprise Knowledge Graph. Learn how the Use Case Tree drives EKG development."
keywords:
  - use case tree
  - UCT
  - business capabilities
  - EKG method
  - enterprise knowledge graph
  - strategic planning
schema_type: "Article"
---

# Use Case Tree (UCT)

<!--summary-start-->
_The foundational structure that organizes business capabilities into
reusable, governed components within the Enterprise Knowledge Graph_
<!--summary-end-->

## What Is the Use Case Tree?

The **Use Case Tree (UCT)** is the most critical artifact in the
development of an Enterprise Knowledge Graph (EKG).
It is the EKG's equivalent of a long-term data strategy and business
capability plan — a high-level requirements overview, scoping and
dependency model that organizes everything the enterprise does.

At its core, the Use Case Tree breaks down strategic business
capabilities into smaller, reusable building blocks called
**use cases**.
Strategic use cases such as
"[Enterprise Risk Management](https://catalog.ekgf.org/use-case/risk-management/)"
or "[Client 360](https://catalog.ekgf.org/use-case/client-360/)" are
decomposed into smaller use cases that can be implemented
incrementally.

Each use case in the tree acts as a **semantic package** — a module,
component, and building block that can be discovered, versioned, and
reused across the enterprise.
Everything done in a business, especially in data and technology,
should be traceable to a use case in the Use Case Tree.

!!! tip "Higher-level abstraction"

    The Use Case Tree operates at a higher level of abstraction than
    User Stories.
    It enables consultative discussions that identify options
    enterprises might otherwise overlook, and provides the structure
    needed to define scope and priority above the level of individual
    stories.

## Why the Use Case Tree Matters

The Use Case Tree serves as the organizing principle for the entire
Use Case Tree Method.
It bridges the gap between business vision and technical execution,
ensuring that every capability is designed for reuse and governed
throughout its lifecycle.

### Know What the Business Wants

The Use Case Tree captures exactly what the business — customers,
product owners, and stakeholders — really needs, short-, mid-, and
long-term.

#### During Planning: Discover Opportunities

During the [Plan Phase](../process/plan/index.md), the Use Case Tree
helps teams discover business opportunities and needs:

- **In non-technical terms** — accessible to all stakeholders
- **Without assumptions** about existing systems or "how things are
  done today"
- **As pure functional requirements** — distinguishing needs from
  "nice to haves"
- **With broad, forward-looking perspective** — mile wide, inch deep
  at this stage
- **Encouraging innovation** — letting the business "dream" about
  "what could be" without premature technical constraints

The goal is to think outside the box and avoid assumptions about
technical limitations that might unnecessarily constrain
possibilities.

#### During Building: Translate to Executable Model

In the [Build Phase](../process/build/index.md), the Use Case Tree
becomes the contract with the business:

- **Governed changes** — every major change requires product owner
  sign-off
- **Metadata in the EKG** — captured as part of the EKG itself,
  persisting all the way to production
- **Complete traceability** — everything done is directly or
  indirectly relatable to a use case in the tree
- **Ongoing visibility** — the business never loses sight of budget
  and deliverables, with all reporting occurring in the context of
  the agreed Use Case Tree

### Bridge Business and Technology

The Use Case Tree creates a shared language between business and
technology teams.
It enables continuous engagement with product owners and stakeholders
throughout the lifecycle of use cases.

!!! tip "Think beyond the immediate use case"

    When developing a use case like "Legal Entities" that needs
    workflows, the Use Case Tree helps identify opportunities for
    broader reuse.
    Should you invest more effort to create a reusable workflow
    component that can also serve "Shareholding Disclosure" and other
    use cases?

    The tree shows stakeholders that there are many customers — current
    and future, inside and outside the organization — and demonstrates
    why prioritizing reuse delivers both quality and broader buy-in
    across the firm or industry.

By engaging multiple stakeholders — not just the direct product
owner, but also stakeholders of neighboring or higher-level use cases
— teams can identify reuse opportunities that accelerate delivery
rather than slow it down.

### Manage Expectations

The Use Case Tree is the foundation of expectation management,
creating an agreed and realistic strategic roadmap.
It provides clarity on:

- What will be delivered and when
- How capabilities relate to business outcomes
- Dependencies between use cases
- Priorities and sequencing

### Enable Modularity and Reuse

The Use Case Tree is the foundational mechanism for creating an
ecosystem of reusable components for the EKG.
Each use case can be:

- **Designed** as a reusable building block
- **Versioned** and governed independently
- **Composed** with other use cases to create larger capabilities
- **Discovered** by teams across the enterprise

This aligns directly with the objectives of
[**Enable Reuse**](../objective/enable-reuse.md) and
[**Composable Business**](../objective/composable-business.md).

### Avoid "Boiling the Ocean"

Semantic technology projects often spend excessive time modeling
everything in a domain — "boiling the ocean."
The Use Case Tree and its individual use cases define an agreed
scope at the appropriate level of detail (without becoming overly
technical).

- **Provides focus** for the Center of Excellence (CoE), enabling
  teams to deliver use cases incrementally
- **Directs ontology development** toward delivering on the
  requirements of agreed use cases, rather than philosophical
  exercises

### Map All Knowledge

The Use Case Tree provides a comprehensive map of all knowledge,
data, and functionality — whether implemented as running EKG use
cases or planned for the future — across the enterprise.

This map is essential because:

- All use cases are served by one platform (albeit distributed and
  federated)
- Many stakeholders have different agendas and priorities
- Updates to one use case can affect others

That's why the Use Case Tree enforces:

1. **Gradual, incremental changes** — no "big bang" releases
2. **Clear inter-dependencies** — all dependencies are explicit and
   tested automatically and continuously

For example, when a sub-use case in one high-level use case is also
used in another, changes serving one stakeholder's needs could affect
others.
The Use Case Tree makes these relationships visible, enabling teams to
avoid disruption across the board.

### Foundational Structure for Quality

The Use Case Tree provides the foundational structure for quality by
enforcing, requiring, and enabling 100% test coverage based on real
business scenarios and requirements.

A use case has a lifecycle that starts with a name and description and
evolves into a fully detailed model including:

- Related concepts and personas
- Business outcomes and success criteria
- Datasets and ontologies
- User stories and workflows
- Dependencies and relationships

This model is captured entirely within the EKG itself, enabling:

- **Comprehensive testing during development** (Build phase)
- **Continuous validation in production** (Run phase)
- **Quality assurance** at the level required for enterprise-scale
  strategic use cases

## Relationship to Other Concepts

The Use Case Tree is closely related to several other concepts in the
EKGF Method:

- **[Use Case](use-case.md)** — Individual nodes in the tree
- **[Enable Reuse](../objective/enable-reuse.md)** — The Use Case
  Tree is the primary mechanism for enabling reuse
- **[Composable Business](../objective/composable-business.md)** —
  The tree organizes capabilities for composition
- **[Persona](persona.md)**, **[Story](story.md)**,
  **[Workflow](workflow.md)**, **[Data Product](data-product.md)**,
  **[Ontology](ontology.md)** — All registered within use cases in
  the tree

## Summary

The Use Case Tree is not just a planning tool — it is the living
structure that organizes, governs, and enables reuse of every
business capability in the Enterprise Knowledge Graph.
It bridges business and technology, manages expectations, enables
modularity, prevents scope creep, maps enterprise knowledge, and
provides the foundation for quality at scale.
