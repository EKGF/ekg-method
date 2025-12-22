---
title: >-
  K: Deliver Strategic Use Cases - Unique Business Capabilities
authors:
  - Jacobus Geluk
hide:
  - toc
date_published: "2022-01-01"
letter_prefix: "K"
description: >-
  Learn how to deliver strategic use cases that cannot realistically
  be done with other technologies. Discover how the Use Case Tree
  Method enables unique business capabilities.
keywords:
  - strategic use cases
  - unique capabilities
  - EKG advantages
  - EKG method
  - enterprise knowledge graph
  - competitive advantage
schema_type: "Article"
---

# The ability to deliver strategic use cases

<!--summary-start-->

_Deliver strategic use cases that cannot realistically be done with
other technologies._

<!--summary-end-->

## Objective

The primary justification for building an Enterprise Knowledge Graph
(EKG) is simple: **to deliver strategic use cases that cannot
realistically be implemented with other technologies**.

However, there is an important distinction between **lighthouse use
cases** and **strategic use cases**:

- **Lighthouse use cases** are the ultimate proof point that makes the
  case for EKG adoption, overcoming the enormous resistance to change
  that exists in large organizations. They are the use case that pulls
  everyone over the line—business stakeholders, technologists,
  security teams, and data professionals—convincing them that EKG is
  critically important to the organization.

- **Strategic use cases** are other strategically important or
  mission-critical use cases that can be done better (or only) by EKG.
  These are important capabilities that matter at the C-level, but
  they may not be the initial lighthouse that breaks through
  organizational resistance.

The Enterprise Knowledge Graph Forum (EKGF) claims that **only an EKG
can realistically implement these strategic use cases** at enterprise
scale.

## Lighthouse Use Cases: Making the Case for EKG

Large organizations have enormous, almost insurmountable resistance to
change. They've been doing things the same way for decades, and few
new paradigms are wholeheartedly embraced. Even when organizations
adopt Agile or DevOps, it's often in the lightest possible
way—basically just to "check the boxes."

EKG introduces many groundbreaking paradigms at once: semantic
technology, knowledge graphs, self-describing datasets, model-driven
development, and more. Convincing an organization and all its layers—
business people, technologists, security professionals, data
specialists—requires a compelling proof point.

**A lighthouse use case is that proof point.** It is the strategic use
case that:

- **Demonstrates undeniable value** that cannot be achieved with
  traditional approaches
- **Overcomes organizational resistance** by showing clear, measurable
  results
- **Convinces all stakeholders** across business, technology,
  security, and data domains
- **Justifies the investment** in EKG as a strategic platform, not
  just a one-off project
- **Creates momentum** for broader EKG adoption across the enterprise

The lighthouse use case is the one that makes everyone say: "We need
EKG. This is the future of how we operate."

## Strategic Use Cases: Mission-Critical Capabilities

Beyond the lighthouse use case, there are many other strategically
important or mission-critical use cases that can be done better (or
only) by EKG. These strategic use cases:

- **Deliver significant business value** at the executive level
- **Solve problems that other technologies cannot** realistically
  address
- **Create competitive advantage** through unique capabilities
- **Enable long-term transformation** rather than solving isolated
  problems
- **Build on the EKG foundation** established by the lighthouse use
  case

Strategic use cases may not be the initial proof point, but they are
essential capabilities that justify continued investment in EKG and
demonstrate its value across multiple domains.

### The GenAI Connection

A particularly relevant example today is **GenAI guardrailing**. As
organizations explore generative AI, there's a nightmare scenario:
letting GenAI agents loose on all legacy system endpoints using MCP
servers and similar approaches without proper guardrails.

**EKG provides the semantic foundation to guardrail GenAI**, enabling:

- **Controlled access** to enterprise data through semantic models
- **Governed interactions** with systems and data sources
- **Meaningful context** for AI agents through ontologies and
  relationships
- **Safe experimentation** without risking critical systems
- **Auditable AI operations** through the knowledge graph

Having GenAI guardrailed by EKG allows GenAI use cases to thrive
safely and effectively, rather than creating chaos by connecting AI
agents directly to legacy endpoints.

## Why EKG Enables Unique Capabilities

Traditional technology stacks face fundamental limitations when
addressing enterprise-wide strategic challenges:

### The Limitations of Traditional Approaches

- **Siloed data** — Information trapped in isolated systems cannot be
  easily connected or queried across domains
- **Rigid schemas** — Relational databases require predefined
  structures that break when business needs evolve
- **Point-to-point integration** — Connecting systems requires custom
  integrations for each connection, creating exponential complexity
- **Limited semantic understanding** — Systems cannot understand
  relationships and meaning across different domains
- **High maintenance costs** — Changes require extensive rework across
  multiple systems

### How EKG Overcomes These Limitations

Enterprise Knowledge Graphs enable strategic use cases through:

- **Semantic connectivity** — Data is connected by meaning, not just
  structure, enabling queries across any domain (see
  [Interoperability](interoperability.md))
- **Flexible schema** — Ontologies can evolve without breaking
  existing queries or applications
- **Universal integration** — One semantic layer connects all systems,
  reducing integration complexity (see
  [Interoperability](interoperability.md))
- **Relationship-first design** — The graph structure naturally
  represents complex relationships and dependencies
- **Incremental evolution** — New use cases can build on existing
  components without disrupting what's already working (see
  [Avoid Disruption](avoid-disruption.md))

### The Unique Power of Composable Components

When the [Use Case Tree Method](../process/index.md) is followed
completely, EKG enables a unique capability: **the delivery of robust,
heavily tested knowledge graph components** that function like highly
reusable lego bricks.

These components are:

- **Data as code** — Knowledge graph components are versioned,
  testable, and deployable like software code
- **Low-code or no-code** — Components can be composed into larger use
  cases with minimal custom development (see
  [Composable Business](composable-business.md))
- **Heavily tested** — Each component has comprehensive test coverage,
  ensuring reliability and quality (see
  [Increase Quality](increase-quality.md))
- **Highly reusable** — Small, focused components can be combined to
  build larger, more complex capabilities (see
  [Enable Reuse](enable-reuse.md))
- **Composable** — Components can be assembled like lego bricks to
  create enterprise-spanning solutions (see
  [Composable Business](composable-business.md) and
  [Modularity](modularity.md))

This composable architecture enables organizations to **scale up
drastically** in terms of both functionality and quality. As more
components are built and tested, the organization's capability to
deliver complex use cases accelerates exponentially.

## Examples of Lighthouse and Strategic Use Cases

Both lighthouse and strategic use cases typically appear at the top of
the [Use Case Tree](../concept/use-case-tree.md) and represent
enterprise-wide capabilities. The same use case might serve as a
lighthouse for one organization and a strategic use case for another,
depending on organizational context and priorities.

Common examples include:

### Client 360 / Customer 360

Create a unified, real-time view of every customer across all
touchpoints, products, and interactions. Traditional approaches
require massive data warehouses with complex ETL processes that are
expensive, slow to update, and break when new data sources are added.
EKG enables real-time, federated views that automatically connect
customer data from any source through semantic relationships (see
[Interoperability](interoperability.md)).

**Business Value:** Improved customer experience, reduced churn,
increased cross-selling, better personalization.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/client-360/)

### Enterprise Fraud Detection

Detect fraudulent patterns across all transactions, accounts, and
channels in real-time, even when patterns span multiple systems and
time periods. Fraud patterns often involve relationships between
entities (people, accounts, transactions, locations) that are not
visible in isolated systems. EKG's graph structure enables pattern
detection across the entire enterprise data landscape.

**Business Value:** Reduced fraud losses, regulatory compliance,
improved security posture.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/fraud-detection/)

### Enterprise Risk & Compliance Management

Monitor and manage risk and compliance across all regulatory
requirements, business units, and jurisdictions in real-time. Risk and
compliance require understanding relationships between regulations,
business processes, data lineage, and organizational structures. EKG
provides the semantic foundation to model and query these complex
relationships (see [Capture Knowledge](capture-knowledge.md)).

**Business Value:** Reduced regulatory fines, faster compliance
reporting, proactive risk management.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/risk-management/)

### Supply Chain Management

Optimize supply chains by understanding relationships between
suppliers, products, logistics, and demand across the entire
ecosystem. Supply chains involve complex, multi-level relationships
that span organizations, geographies, and time. EKG enables real-time
visibility and optimization across the entire supply network.

**Business Value:** Reduced costs, improved resilience, faster
response to disruptions.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/supply-chain-management/)

### Data Privacy & Governance

Track and manage personal data across all systems, ensuring compliance
with GDPR, CCPA, and other privacy regulations. Privacy regulations
require understanding data lineage, consent, sharing agreements, and
cross-system relationships. EKG provides the semantic foundation to
model and query these relationships automatically (see
[Capture Knowledge](capture-knowledge.md) and
[Interoperability](interoperability.md)).

**Business Value:** Reduced regulatory fines, improved customer trust,
automated compliance reporting.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/data-privacy-governance/)

### Recommendation Engine / Interest Graph

Provide personalized recommendations by understanding relationships
between users, content, products, and behaviors across the entire
platform. Effective recommendations require understanding complex,
multi-dimensional relationships that evolve over time. EKG's graph
structure naturally represents these relationships and enables
real-time recommendation generation.

**Business Value:** Increased engagement, higher conversion rates,
improved user experience.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/recommendation-engine/)

### Enterprise-Spanning Regulatory Reports

Deliver extremely complex regulatory reports that require full data
lineage and provenance discovery across all systems, complying with
regulatory requirements across multiple jurisdictions. Traditional
approaches cannot efficiently trace data lineage across siloed systems
or provide complete provenance for every data point. EKG's composable
component architecture enables organizations to build regulatory
reporting capabilities from reusable, tested components.

**Business Value:** Reduced compliance risk, faster regulatory
reporting, automated lineage tracking, reduced manual effort, ability
to respond to new regulations quickly.

This use case particularly demonstrates the power of composable
components—regulatory reporting capabilities can be built
incrementally from reusable components, enabling rapid adaptation to
changing regulatory requirements.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/regulatory-reports/)

### Digital Twin of Technology and Data Landscape

Build a complete, real-time representation of the entire technology
and data landscape to enable visibility, impact analysis,
optimization, and strategic planning. Traditional approaches cannot
effectively model the complex, multi-dimensional relationships between
systems, applications, data flows, business processes, and
dependencies. EKG's composable component architecture enables
organizations to build a digital twin by composing reusable
components.

**Business Value:** Reduced technology costs, improved risk
management, faster change impact analysis, better strategic planning,
optimized resource allocation.

The ability to build such comprehensive capabilities from reusable,
tested components is unique to EKG when following the Use Case Tree
Method completely.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/digital-twin/)

### Complex Construction Project Quotations

Create reliable, accurate quotations for complex construction projects
that typically take years from ideation to delivery. The quotation
process is extremely time-intensive, expensive, and involves
significant risk, heavily relying on experienced specialists and
subject matter experts (SMEs).

Complex construction projects depend on vast amounts of knowledge that
resides in the heads of experienced specialists, plus enormous volumes
of documentation (PDFs, diagrams, calculations). EKG captures
structured knowledge from SMEs, while GenAI extracts knowledge from
documents. EKG provides fact-checking guardrails to ensure GenAI
generated content is validated against structured knowledge, ensuring
reliability and accuracy.

**Business Value:** Dramatically reduced quotation time and cost,
improved accuracy and reliability, reduced risk, preserved
institutional knowledge, faster response to RFPs, competitive
advantage through quicker turnaround.

This use case demonstrates how **EKG and GenAI work together**—EKG
provides the structured, validated knowledge foundation, while GenAI
accelerates knowledge extraction and generation, with EKG serving as
the critical guardrail to ensure reliability.

[:octicons-arrow-right-24: Learn more on the EKG Catalog](https://catalog.ekgf.org/use-case/construction-project-quotations/)

## The Competitive Advantage

Both lighthouse and strategic use cases enabled by EKG create
sustainable competitive advantages because:

1. **They cannot be easily replicated** — Competitors using
   traditional technology stacks cannot match the capabilities without
   similar investment
2. **They compound over time** — Each new use case builds on previous
   ones, creating increasing returns
3. **They enable innovation** — The semantic foundation enables rapid
   experimentation and new capability development
4. **They reduce technical debt** — Unlike point solutions, EKG
   capabilities are reusable and composable
5. **They enable safe AI adoption** — EKG provides the guardrails
   needed for GenAI and other AI technologies to thrive in enterprise
   contexts

## How the Use Case Tree Method Enables Strategic Use Cases

The [Use Case Tree Method](../process/index.md) provides the structure
and discipline needed to deliver strategic use cases:

- **Strategic planning** — The Use Case Tree helps identify and
  prioritize strategic use cases at the top level (see
  [Align with Business Strategy](align-with-business-strategy.md))
- **Incremental delivery** — Strategic use cases are broken down into
  smaller, deliverable components that can be built incrementally (see
  [Avoid Boiling the Ocean](avoid-boiling-the-ocean.md) and
  [Avoid Disruption](avoid-disruption.md))
- **Reuse and composition** — Lower-level use cases become reusable
  components that accelerate delivery of strategic capabilities (see
  [Enable Reuse](enable-reuse.md) and
  [Composable Business](composable-business.md))
- **Business alignment** — The method ensures strategic use cases are
  defined in business terms and aligned with business outcomes (see
  [Know What the Business Wants](know-what-the-business-wants.md) and
  [Bridge the Gap](bridge-the-gap.md))
- **Risk management** — Dependencies and relationships are visible in
  the tree, enabling better risk assessment and mitigation

## Getting Started

To identify and deliver lighthouse and strategic use cases:

1. **Identify your lighthouse use case** — What use case will overcome
   organizational resistance and make the case for EKG? This should be
   a compelling proof point that demonstrates clear, measurable value.

2. **Identify strategic use cases** — What other strategically
   important or mission-critical use cases can be done better (or
   only) by EKG?

3. **Map to Use Case Tree** — Position lighthouse and strategic use
   cases at the top of your
   [Use Case Tree](../concept/use-case-tree.md)

4. **Break down into components** — Decompose use cases into smaller,
   deliverable components

5. **Start with the lighthouse** — Focus initial effort on the
   lighthouse use case to build momentum and overcome resistance

6. **Build foundational components** — Create reusable components that
   support both lighthouse and strategic use cases

7. **Measure business outcomes** — Track how use cases deliver on
   business objectives, especially for the lighthouse use case

## Related Content

### Concepts

- **[Use Case Tree](../concept/use-case-tree.md)** - The structure
  that organizes strategic use cases
- **[EKG](../vocab/ekg.md)** - The platform that enables strategic use
  cases

### Related Objectives

- **[Composable Business](composable-business.md)** - Strategic use
  cases enable composable business capabilities
- **[Enable Reuse](enable-reuse.md)** - Reusable components accelerate
  strategic use case delivery
- **[Modularity](modularity.md)** - Modular architecture supports
  composable components
- **[Interoperability](interoperability.md)** - Semantic connectivity
  enables strategic use cases across systems
- **[Increase Quality](increase-quality.md)** - Heavily tested
  components ensure reliability
- **[Align with Business Strategy](align-with-business-strategy.md)**
  - Strategic use cases align with business strategy
- **[Know What the Business Wants](know-what-the-business-wants.md)**
  - Understanding business needs drives strategic use cases
- **[Bridge the Gap](bridge-the-gap.md)** - Strategic use cases bridge
  business and technology
- **[Capture Knowledge](capture-knowledge.md)** - Knowledge graphs
  capture the semantic foundation for strategic use cases
- **[Avoid Boiling the Ocean](avoid-boiling-the-ocean.md)** -
  Incremental delivery of strategic use cases
- **[Avoid Disruption](avoid-disruption.md)** - Strategic use cases
  can be delivered incrementally without disruption

### Process

- **[Discover Process](../process/plan/discover.md)** - How to
  identify strategic use cases
