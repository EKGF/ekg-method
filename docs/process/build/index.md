---
authors:
  - Jacobus Geluk
hide:
  - toc
---
# Build

!!! info inline end "no-code"

    In general, for most use cases, there is very little actual
    coding involved since the majority of use cases can be done
    in a ”low-code” or even ”no-code” manner by specifying all
    details of all functional requirements in the context of the
    UCT which then all ends up as ”executable models” in the 
    EKG itself.

<!--summary-build-start-->
_"Building" an EKG-based use case involves 
everything from detailed requirements gathering---structured 
around the Use Case Tree---all the way up to delivery of
components for your production EKG-platform._
<!--summary-build-end-->

??? info "Inputs"

    To set up for success, it is essential that the build phase starts with 
    the following artifacts and results that are created during the [plan phase](../plan)
    are input for the build phase:

    - **From [Envision](../plan/envision):** A shared vision and strategy, 
      an agreed overall scope and direction, all stakeholders are identified 
      and are supporting the strategy.
    - **From [Discover](../plan/discover):** The UCT, a broad-stroke overview
      of all use cases in the agreed scope with agreed names and
      "Business Outcomes" plus abstract business descriptions of functional
      requirements. (Details of the UCT to be determined during the build phase).
    - **From [Assess](../plan/assess):** A light assessment of the various 
      non-functional requirements and levels of maturity in the areas of 
      the organization that the EKG and the EKG team would depend on plus 
      a plan as to how to bridge gaps.
    - **From [Train](../plan/train):** Depending on the size of the 
      selected use cases and their scope, everyone involved should have
      gone through some light basic training where the various new concepts 
      around EKG have been explained, especially the members of the initial team.
    - **From [Chart](../plan/chart):** An agreed, supported and funded project 
      plan. With a well-defined _definition of done (DoD)_ or a definition 
      of what a successful delivery of the selected use cases means,
      ideally around agreed business outcomes.

??? info "Critical success factors"

     1. Creating an EKG can only be successful if it is done as part of the
        company’s strategy with solid top-down support and leadership.
     2. Bottom-up development of just one Knowledge Graph Use Case will only 
        lead to "yet another silo (YAS)" and cannot realistically compete
        with existing technology stacks, missing out on the actual benefits
        that EKG can provide.
     3. An EKG requires internal ownership and a team that understands
        the many new paradigms that are involved.
         - Creating a solid team---let's call it the [Center of Excellence (CoE)
           for the EKG](../../vocab/coe)---is essential.
     4. It is not the technology that holds us back---the technology works---it
        is the internal organization’s readiness and level of maturity in a
        number of areas that require focus. (See [assess](../plan/assess.md))
     5. A structured method is required that covers all areas, from strategy
        and idea inception to capturing the right business outcomes and
        requirements all the way to delivering a use case in production
        and supporting it during its life cycle.
     6. Any investment in a properly executed [plan phase](../plan) will 
        drastically increase the likelihood of successful delivery.

<div class="grid cards" markdown>

- :material-cached:{ .lg } __Allocate__

     {% include-markdown "allocate.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](allocate.md)

- :material-cached:{ .lg } __Design__

     {% include-markdown "design.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](design.md)

- :material-cached:{ .lg } __Implement__

     {% include-markdown "implement.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](implement.md)

- :material-cached:{ .lg } __Test__

     {% include-markdown "test.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](test.md)

- :material-cached:{ .lg } __Verify__

     {% include-markdown "verify.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](verify.md)

- :material-cached:{ .lg } __Deliver__

     {% include-markdown "deliver.md"
     start="<!--summary-start-->" end="<!--summary-end-->" %}
     [:octicons-arrow-right-24: Learn more](deliver.md)

</div>
