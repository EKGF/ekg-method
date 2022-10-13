---
authors:
  - Jacobus Geluk
hide:
  - toc
---
# Operate

<!--summary-start-->
_Operating production-level, distributed and federated [EKG/Platform](/vocab/ekg-platform/) that serves
any wildly different use cases across the enterprise, guaranteeing business continuity._
<!--summary-end-->

What’s new for most organizations is to have one platform supporting many wildly different and
potentially complex transactional use cases used across many parts of the business. 
This is different from managing a siloed landscape of more or less independent systems.
Operating a production-level, distributed and federated [EKG/Platform](/vocab/ekg-platform/) that serves many 
wildly different use cases across the enterprise where stakeholders do not necessarily 
even know each other---let alone have their priorities aligned---is not something that 
most organizations are used to. 
There are obviously some parallels with existing "horizontal" services but those services
are usually all focussed on delivering ^^one^^ use case, not many.

It requires new operating models and enhanced capability.

An EKG evolves continuously---continuous deployment being a critical concept at a
certain level of maturity. 
It serves many use cases, and it deals with many completely different back-end
systems---upstream source systems or downstream consumers---each of which evolves 
over time as well. 
Upstream and downstream partners all need to move forward where the CoE needs to be
able to respond in a timely manner.
Furthermore, there are all kinds of operational requirements such as
Disaster Recovery (DR) processes, Security / Vulnerability checks and so forth.

Your CoE will (have to) support your operational teams to ensure the highest levels
of quality, resilience and security for your EKG. 
Your CoE makes sure that your teams are able to provide continual service
levels to support your mission-critical use cases.

## Audience

TODO

## Approach

The CoE works in collaboration with your Production Department to establish new
operating models and practices needed for distributed EKG deployment.

## Outputs

- An [EKG/Platform](/vocab/ekg-platform/) that complies with agreed levels of service and support
- Disaster recovery and business continuity testing for the EKG 
- Operational Processes for fast and effective issue resolution

## Topics

- The impact of concepts like DevOps, DataOps, Infrastructure as Code (IaC), 
  Continuous Improvement, Continuous Integration, Continuous Delivery and
  Continuous Deployment on operations.
- How to deal with serving many different agendas with one platform.
- How to reach full test coverage in an EKG and test model-driven and 
  data-driven applications / use cases.
- DR in an EKG context with many different upstream and downstream partners
