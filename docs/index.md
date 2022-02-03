# Use Case Tree Method

Your enterprise embarked upon a strategic innovative journey towards 
establishing a full scale Enterprise Knowledge Graph (EKG) in order 
to be able to:

1. implement use cases that enable more foundational data quality 
   for your enterprise’s business processes,
2. be more easily compliant with regulations and
3. enable strategic use cases that create a competitive advantage.

The key _artifact_ in the development of an EKG is "the Use Case Tree":

- The Use Case Tree is the EKG's equivalent of a long term
  data strategy and business capability plan.

- The Use Case Tree is the high-level requirements overview, 
  scoping and dependency model.
  It gives a _mile wide, inch deep_ view of business capabilities.

Traditionally, data strategy, architecture and models i.e.
_specifications of business requirements_ on one side and technology
and software, i.e. _functionality_ on the other side, are separate.
They are concerns of different departments; different groups of
specialists think about these concepts in their own way and have their
own practices and models for it. 
For any given development of a business capability that is supported 
by technology, different groups of people, often across many departments, will get involved and they all
have their own way of looking at it.
There is no shared language, not one single artifact that they can 
all talk to and reason about.
The Use Case Tree is that single artifact. 
It provides one single construct, owned by _the business_, and 
primarily driven by business strategy, that every group of people, 
every specialist, can relate their way of thinking to. 
This includes not only data and technology specialists but also project
managers, financial managers, security and compliance officers,
operations engineers and so forth. 
All their models and different ways of looking at a given capability 
can be plugged into the Use Case Tree as different views.

Everything we ever do in a business, especially in the data and
technology pillars of that enterprise, should be related to a use
case in the Use Case Tree.

The Use Case Tree is a breakdown of strategic planned-for 
capabilities into smaller building blocks, all called use cases.
Strategic long term use cases such as _Enterprise Risk Management_ 
or _Client 360_ are broken down into smaller use cases that 
can (and should) be done first.

Each use case is a module --- an EKG-component so you will --- 
a building block with which other use cases can be constructed.

The Use Case Tree Method is a practice that has been developed and
used for many EKG use cases that are running in production.

The primary reasons for creating a Use Case Tree are:

1. **Know what the business wants**.<br/>
    Know exactly what the business --- i.e. the customer or product owner
    --- really needs, short-, mid- and long-term.

    1. <u>Plan phase: Discover the business opportunities & business needs</u><br/>
       One of the tasks during the planning phase of any new initiative
       --- or iteration --- is to "Discover" the business opportunities &
       needs:

         - In non-technical terms.

         - Without assuming anything about existing systems and "how
           things are done today".

         - Translate to "pure" functional requirements --- and "nice
           to haves".

         - Looking broad horizontally, thinking ahead. Mile wide, inch
           deep at this stage.

         - Let the business "dream a little" about "what could be"
           and "what should be", so that future needs can be
           identified and communicated --- without necessarily
           committing to them (yet).

         - Promote "thinking outside the box", encourage people to
           not make any assumptions about what is technically possible
           or not --- so often these assumptions unknowingly keep the
           bar lower than it could be.

    2. <u>Build phase: Translate requirements into an easy to 
       understand model i.e. the Use Case Tree</u><br/>
       "Contract with the business" i.e. the budget holder or
       product owner. 
       Every major change to any given use case in the 
       Use Case Tree will have to be signed off by the 
       appropriate product owner.

         - Capture it as "meta-data" that will be part of the
           EKG --- all the way to production.

         - Capture it in such a way that "everything that we ever do"
           is always directly or indirectly relatable to a use case
           in the Use Case Tree.

         - The business never loses sight on what happens with their
           budget and agreed deliverables.
           All reporting to the business occurs in the context of 
           the agreed , even after delivery.

2. **Bridge the traditional gap between Business & Technology**.

    - Engage with the business, the product owner and get continuous
      buy-in from the product owner during the life-cycle of the
      agreed use cases.

    - But not only with the product owner of the direct use case being
      developed but also show to the business what other future needs
      need to be considered.<br/>
      For instance, if one use case e.g. "Legal Entities" needs
      "workflows", would it make sense to invest a bit more effort
      to then create a reusable workflow component that can also 
      be used for many other use cases such as 
      "Shareholding disclosure"?

    - Yes, the customer is always right but the Use Case Tree 
      shows to the customer that there are many other customers
      (or future customers, in and outside the organization even)
      and why it makes sense to prioritize reuse and how that not 
      only could deliver more quality but also create more buy-in 
      from peer stakeholders across the firm or even across the 
      industry.

        * In other words, do not select one product owner to be the
          single stakeholder but also get other stakeholders of
          neighboring or higher level use cases in the room, their
          requirements may influence the reuse agenda and therefore
          the roadmap. It may sound paradoxal but investing in reuse
          will not slow things down but speed things up.

3. **Best form of "expectation management"**, creating an agreed and
    realistic strategic roadmap.

4. **Foundational mechanism to create an ecosystem of reusable
    components** for the EKG.

5. **Avoids "boiling the ocean"** because the Use Case Tree and its
    individual use cases define an agreed scope at the detail 
    level (without becoming technical).

    - Provides focus for the EKG Center of Excellence (CoE),
      "cranking out" use cases one by one

    - Ontology development will be focussed on delivering on the
      requirements (user stories and concepts) of the agreed use cases
      rather than ending up in philosophical exercise.

6. **Provides a "map" of all knowledge, data and functionality** that
    the EKG provides to the enterprise.
    Which is not only useful for users of the EKG but also a necessity 
    since all of these use cases are served by one platform -- albeit
    distributed and federated etc -- there will be many stakeholders
    with different agendas that would not care -- nor have to care --
    about the wishes of the stakeholders in other use cases.
    However, updates to one use case could potentially also
    affect other use cases.<br/>That's why:
    - <u>all changes & updates have to be done gradually, 
      no ”big bang” releases</u> and
    - <u>all inter-dependencies need to be really clear and
      tested in-full automatically and continuously.</u>
   
    So, for instance, when some sub-use case in a high-level use case is
    also used in another high-level use case then a change that serves
    the needs of one could potentially also affect the other and its
    users. That's why we need the , to allow us to avoid any disruption
    across the board.

9. **Foundational structure for quality** since it enforces, requires
    and enables 100% test coverage based on real business scenarios and
    requirements.

    - A use case has a life-cycle that starts with a name and a
      description and ends[^1] with a fully detailed model of all
      related concepts, personas, business outcomes, datasets,
      ontologies, user stories and dependencies.
      That model is all captured in the EKG itself which allows the
      EKG to not only fully and thoroughly test things during
      development time (build phase) but also in production
      (run phase).
      Which provides the level of quality that an EKG needs to
      have to become truly able to support enterprise level 
      strategic use cases.

[^1]: Obviously, use cases can also be decommissioned after their life
in producton so in fact there are more stages in the life-cycle of a
use case
