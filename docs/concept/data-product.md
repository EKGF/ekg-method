---
description: >-
  A semantic data product that provides required information for a Use Case,
  selected based on semantic relevance and suitability. Learn how data products
  enable reuse in the Use Case Tree Method.
keywords:
  - data product
  - semantic data product
  - data asset
  - EKG method
  - enterprise knowledge graph
  - data reuse
schema_type: "Article"
---

# Data Product

<!--summary-start-->
_A semantic data product that provides required information for a Use
Case, selected based on semantic relevance and suitability to the
use case's requirements_
<!--summary-end-->

=== "Business & Management Audience"

    ## What Is a Data Product?

    A **Data Product** is a semantic data asset that provides the
    required information for a [Use Case](use-case.md).
    In later stages of the use case lifecycle, we can attach the use
    case to those semantic data products that already exist and can
    provide the required information.

    Data Products are reusable components that encapsulate data,
    along with its meaning (semantics), making it available for use
    across multiple use cases.

    ## The Data Economy

    Think of your entire data landscape or ecosystem as a **data
    economy** — like any economy, it has a supply side and a demand
    side.

    - **Supply side** — Data Products define what data is available,
      how it's packaged, and how it can be accessed.
      They represent the "supply" in the data economy.
    - **Demand side** — [Use Cases](use-case.md) define who needs
      data, what they need it for, and why.
      They represent the "demand" in the data economy.

    People often understand Data Products (the supply side), but
    struggle with "what's the demand?"
    Who uses these data products, and for what reasons?
    That's where Use Cases come in: a Use Case defines the demand
    side, specifying what data is needed and why.

    This economic model helps organizations understand the flow of
    data, identify gaps between supply and demand, and ensure that
    data products are created to meet actual business needs.

    ## Why Data Products Matter

    Data Products enable:

    - **Reuse** — Data can be packaged once and reused across
      multiple use cases
    - **Consistency** — The same data product ensures consistent
      meaning and structure across use cases
    - **Efficiency** — Avoids duplicating data preparation and
      transformation work
    - **Quality** — Data products are designed, tested, and
      maintained as reusable assets

    !!! tip "Semantic relevance matters"

        The choice of data products for a use case should be based
        on their semantic relevance and suitability to the use case's
        requirements, not just technical availability.

    ## When Are Data Products Used?

    Data Products are typically identified and attached to use cases
    in later stages of the lifecycle, once:

    - The use case requirements are well understood
    - The data needs are clearly defined
    - Existing data products can be evaluated for suitability

    This allows use cases to leverage existing, proven data products
    rather than creating new ones from scratch.

=== "Data & Tech Audience"

    ## What Is a Data Product in the Use Case Tree Method?

    A **Data Product** is a semantic data asset that provides
    required information for a [Use Case](use-case.md).
    It encapsulates data along with its semantic meaning (defined
    through [Ontologies](ontology.md)), making it a reusable
    component in the Enterprise Knowledge Graph.

    ## Semantic Data Products

    Data Products in the Use Case Tree Method are **semantic** — they include:

    - **Data** — The actual data values
    - **Semantics** — The meaning of the data, defined through
      ontologies
    - **Structure** — How the data is organized
    - **Metadata** — Information about the data product itself

    This semantic nature enables the EKG to understand what the data
    means, not just what it contains.

    ## Selection Criteria

    The choice of semantic data products to be used for a given use
    case should be made based on:

    - **Semantic relevance** — Does the data product contain
      concepts and terms that match the use case's vocabulary?
    - **Suitability** — Does the data product meet the use case's
      requirements?
    - **Quality** — Is the data product well-maintained and
      reliable?
    - **Availability** — Is the data product accessible and
      performant?

    !!! tip "Semantic matching"

        The most important criterion is semantic relevance — the
        data product should align with the use case's concepts and
        terminology, enabling semantic integration.

    ## Lifecycle Integration

    In later stages of the use case lifecycle, we can attach the use
    case to those semantic data products that already exist and can
    provide the required information.

    This approach:

    - **Promotes reuse** — Leverages existing data products rather
      than creating new ones
    - **Ensures consistency** — Multiple use cases can use the same
      data product, ensuring consistent data
    - **Reduces effort** — Avoids duplicating data preparation work
    - **Maintains quality** — Uses proven, tested data products

    ## Relationship to Other Concepts

    Data Products relate to other core concepts:

    - **[Use Cases](use-case.md)** — Use cases consume data
      products to fulfill their requirements
    - **[Ontologies](ontology.md)** — Data products use ontologies
      to define the semantic meaning of their data
    - **[Concepts](concept.md)** — Data products contain data about
      concepts that are relevant to use cases
    - **[Stories](story.md)** — Stories may require specific data
      products to fulfill their needs

    This integration ensures that data products are not isolated
    assets but part of a cohesive, semantic model of the enterprise.

    ## Reuse and Composition

    Data Products are designed for reuse across multiple use cases.
    This enables:

    - **Composition** — Use cases can combine multiple data products
      to meet their requirements
    - **Consistency** — The same data product ensures consistent
      meaning across use cases
    - **Efficiency** — Data preparation is done once and reused
      many times
    - **Maintainability** — Changes to a data product benefit all
      use cases that use it

    This reuse pattern aligns with the [composable
    business](../objective/composable-business.md) approach, where
    data products become reusable components in the Enterprise
    Knowledge Graph.

=== "DPROD Ontology"

    ## What Is DPROD?

    The **Data Product Ontology (DPROD)** is a specification developed
    by the Object Management Group (OMG) Enterprise Knowledge Graph Forum (EKGF) that provides
    a standardized way to describe Data Products using W3C Linked Data
    standards.
    DPROD is available at
    [https://ekgf.github.io/dprod/](https://ekgf.github.io/dprod/).

    DPROD builds on the W3C Data Catalog Vocabulary (DCAT) to enable
    publishers to describe Data Products and data services in a
    decentralized way.
    By using a standard model and ontology, DPROD facilitates the
    consumption and aggregation of metadata from multiple Data
    Marketplaces, increasing discoverability and enabling federated
    search.

    ## Why DPROD?

    As organizations increasingly recognize the value of data as an
    asset and adopt decentralized data architectures (such as Data
    Mesh), the need for standardized methods to describe and manage
    data products consistently across platforms has become critical.

    Without such a standard, organizations face:
    - Inconsistent metadata across diverse data products
    - Limited discoverability
    - Interoperability issues that hinder data integration
    - Difficulty scaling as data ecosystems grow
    - Increased vendor lock-in

    DPROD offers a solution by providing a clear schema for describing
    data products, ensuring they are discoverable, interoperable,
    and treated with the same level of accountability as traditional
    products.

    ## DPROD Principles

    DPROD follows two basic principles:

    - **Decentralize Data Ownership** — To make data integration
      more efficient, tasks should be shared among multiple teams.
      DCAT helps by offering a standard way to publish datasets in a
      decentralized manner.
    - **Harmonize Data Schemas** — Using shared schemas helps unify
      different data formats.
      DPROD provides a common set of rules for defining a Data
      Product, which users can extend as needed.

    ## DPROD Model

    The DPROD specification extends DCAT to connect Data Services to
    Data Products using input and output ports.
    These ports are used to publish and consume data from a Data
    Product.

    The model consists of:

    - **Data Product** (`dprod:DataProduct`) — A rational, managed,
      and governed collection of data, with purpose, value, and
      ownership, meeting consumer needs over a planned lifecycle
    - **Port** (`dcat:DataService`) — A digital interface that
      provides access to a Dataset (input or output port)
    - **Distribution** (`dcat:Distribution`) — A specific
      representation of a dataset (CSV, JSON, Parquet, etc.) which
      can conform to a physical model
    - **Dataset** (`dcat:Dataset`) — A collection of related data
      that can conform to a logical model

    Data Products can have:
    - **Input ports** — Services that collect source data and make
      it available for transformation
    - **Output ports** — Services that share generated data in a way
      that can be understood and trusted
    - **Lifecycle status** — Development status (e.g., Ideation,
      Design, Build, Deploy, Consume)
    - **Owner** — The agent accountable for the data product
    - **Domain** — The business or information area supported
    - **Purpose** — Objectives and intended usage

    ## Relationship to Use Case Tree Method

    DPROD provides a standardized way to describe Data Products that
    aligns with the Use Case Tree Method's approach:

    - **Semantic description** — DPROD uses ontologies to describe
      the semantic meaning of data products
    - **Reuse and composition** — DPROD enables data products to be
      discovered and composed
    - **Lifecycle management** — DPROD tracks the lifecycle status
      of data products
    - **Decentralized architecture** — DPROD supports decentralized
      data ownership and management

    When implementing Data Products in the Use Case Tree Method, DPROD can be
    used to provide standardized metadata that enables discovery,
    integration, and governance across the enterprise.

    ## Key Features

    DPROD enables:

    - **Unambiguous semantics** — Provides clear, sharable semantics
      to answer "What is a data product?"
    - **Simplicity and expressiveness** — Simple enough for anyone
      to use, but expressive enough to power large data marketplaces
    - **Reuse of existing infrastructure** — Allows organizations to
      reuse their existing data catalogues and dataset infrastructure
    - **Harmonization** — Shares common semantics across different
      Data Products, promoting consistency

    For more details, examples, and the complete specification, see
    the [DPROD documentation](https://ekgf.github.io/dprod/).

    !!! important "Data Products as Use Cases"

        A **Data Product is basically just another Use Case** — with
        its own stereotype.
        You can stereotype a use case as a "data-product" or as an
        "upstream data-source" or "downstream data-sink," or whatever
        categorization you prefer.
        But fundamentally, a data product can be seen as just another
        use case.

        This unified model means that:
        - Data Products follow the same lifecycle as Use Cases
        - They can be organized in the [Use Case
          Tree](use-case-tree.md)
        - They have the same components: Personas, Stories, Concepts,
          Outcomes
        - They enable the same composability and reuse patterns

        The stereotype simply indicates the primary purpose or role of
        that use case in the data economy.


