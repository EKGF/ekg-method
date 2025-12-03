---
title: "H: Avoid Disruption"
authors:
- Jacobus Geluk
hide:
- toc
description: "Make changes gradually with clear interdependencies to avoid disruption across use cases. Learn how the EKG Method enables safe, incremental change."
keywords:
  - change management
  - disruption avoidance
  - incremental change
  - EKG method
  - enterprise knowledge graph
  - use case dependencies
schema_type: "Article"
---
# H: Avoid Disruption

<!--summary-start-->
_Make changes gradually with clear interdependencies to avoid disruption across use cases._
<!--summary-end-->

[Capturing all knowledge in the organization](capture-knowledge.md)
as much as technically possible is not only useful to enable a whole
new league of use cases but is also a necessity since all of these 
use cases are served by one platform --- albeit distributed and federated.
Which means that there will be many stakeholders with different agendas
that would not care --- nor should they have to care --- about the wishes 
of the stakeholders in other use cases.

However, updates to one use case could potentially also
affect other use cases.

That's why:

- <u>all changes & updates have to be done gradually,
  no ”big bang” releases</u> and
- <u>all interdependencies need to be really clear and
  tested, in-full, automatically and continuously.</u>

So, for instance, when some sub-use case of a high-level use case is
also used in another high-level use case then a change that serves
the needs of one could potentially also affect the other and its
users.
That's why we need the [Use Case Tree](../concept/use-case-tree.md), to allow us to avoid any disruption
across the board.
