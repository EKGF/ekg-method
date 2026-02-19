---
title: Test scenarios
description: >-
  How stories are tested using BDD-style test scenarios
  with Given-When-Then, making them executable
  specifications that verify the EKG delivers what it
  promises.
keywords:
  - story test scenario
  - given-when-then
  - BDD
  - test coverage
  - functional health
  - EKG method
  - enterprise knowledge graph
schema_type: "Article"
---

# Test scenarios

<!--summary-start-->

_A concrete verification of a Story, following a
Given-When-Then pattern that defines an initial state,
input values, and the expected result_

<!--summary-end-->

=== "Business & Management Audience"

    ## Stories are testable

    Stories are not just documentation — they are
    **testable, executable specifications**.
    Each story has one or more test scenarios that verify
    the story delivers what it promises.

    This is what separates the Use Case Tree Method from
    traditional requirements management: every story can
    be automatically checked, not just reviewed by a
    human.

    ## How testing works

    Each test scenario follows a simple three-step
    pattern:

    1. **Set up the situation** — Define the data that
       should already exist before the story runs
    2. **Run the story** — Provide the inputs the story
       needs
    3. **Check the result** — Verify that the output
       matches what was expected

    This pattern is repeated for each scenario, covering
    different situations the story might encounter:
    normal cases, edge cases, and error conditions.

    ## Why this matters

    Because every story has test scenarios, the EKG can
    continuously verify that all stories still deliver
    what was promised.
    When anything changes — code, ontologies, data
    pipelines, policies — the EKG can immediately detect
    whether all stories still work.

    This is how you achieve **functional health** of
    the EKG: the system knows whether it is delivering
    on its promises, at all times.

    Stories without test scenarios are immediately
    visible as gaps, making it clear where coverage
    needs to improve.
    The goal is 100% story coverage.

    See [Continuous testing](continuous-testing.md) for
    more on how the EKG monitors its own health.

=== "Data & Tech Audience"

    ## Given-When-Then

    Each story has one or more **test scenarios** that
    follow the
    [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development)-style
    Given-When-Then pattern:

    - **Given** — An input graph: a dataset that sets up
      the initial state (the world as it exists before
      the story runs)
    - **When** — Invoke the story with input values for
      each input [concept](../concept/index.md) (the
      parameters the story needs)
    - **Then** — The expected result, which takes one of
      two forms depending on the story type:
        - For **query stories**: output data matching
          the defined output concepts
        - For **update stories / transform rules**: an
          expected output graph representing the new
          state

    ## Example

    Consider a story _"As the Chief Risk Officer, I need
    to know our current Risk Position against party B."_

    A test scenario might look like:

    - **Given** — A graph containing party B, its
      contracts, and known exposures
    - **When** — Invoke the story with `party = B`
    - **Then** — The result contains the aggregated risk
      position matching the expected output

    Multiple scenarios cover different situations: a
    party with no exposures, a party with multiple
    contract types, missing data, and so on.

    ## Living specifications

    This is what makes stories **living specifications**
    rather than throwaway tasks.
    Every story is continuously tested across its entire
    lifecycle.
    When anything changes — code, ontologies, data
    pipelines, policies — the EKG can immediately detect
    whether all stories still deliver.

    Because the EKG knows about both
    [Stories](index.md) and their
    [Implementations](implementation.md), it can run
    test scenarios against each implementation and
    report on which stories are passing, failing, or
    untested.

    ## Test coverage

    The goal is **100% story coverage**: every story
    should have at least one test scenario.
    Stories without test scenarios are immediately
    visible as gaps in the system's coverage report.

    This visibility is deliberate — it turns testing
    from an afterthought into a first-class concern
    that is tracked alongside the stories themselves.

    See [Continuous testing](continuous-testing.md) for
    how test scenarios fit into the EKG's ongoing
    health monitoring.

=== "Ontology"

    --8<-- "fragment/uctm-diagram-story-test-scenario.md"

    <span id="ontology"></span>
    ## Facts

    !!! info "About these facts"

        We're not prescribing a full OWL ontology here.
        These are minimal facts you can use to build your
        own ontology, schema, or graph model.

    ### StoryTestScenario

    - **Opaque universally unique identifier**
        - A StoryTestScenario must have an **opaque**,
          **universally unique** identifier.
        - Prefer a random identifier such as
          **UUIDv4**.

    - **Belongs to exactly one Story**
        - A StoryTestScenario must reference exactly one
          [Story](index.md) via a `:testScenario`
          relationship.
        - A Story can have **0..\*** StoryTestScenarios.

    - **Description**
        - A StoryTestScenario should have a
          human-readable description of the situation
          it verifies.

    - **Given (initial state)**
        - A StoryTestScenario must reference a
          **State** — a set of datasets that define the
          initial graph before the story runs.

    - **When (input values)**
        - A StoryTestScenario must specify input values
          for each input
          [Concept](../concept/index.md) that the
          Story requires.

    - **Then (expected result)**
        - A StoryTestScenario must reference an
          **Expectation**, which takes one of two
          forms:
            - **State** — an expected output graph
              (for update stories / transform rules)
            - **StoryOutputs** — expected output
              values matching the defined output
              concepts (for query stories)

    ### State

    - A **State** is a set of named datasets (graphs)
      representing a snapshot of the world.
    - Used as both the **given** (initial state) and,
      for update stories, as the **then** (expected
      output state).

    ### Expectation

    - **Expectation** is the base type for the expected
      result of a test scenario.
    - It has two specializations:
        - **State** — the expected output graph
        - **StoryOutputs** — the expected output values

    ### Cardinality

    - A Story can have **0..\*** StoryTestScenarios
    - A StoryTestScenario belongs to exactly **1** Story

## See also

- [Story](index.md) — The business requirement that
  test scenarios verify
- [Story Implementation](implementation.md) — The
  technical realization tested by scenarios
- [Continuous testing](continuous-testing.md) — How
  test scenarios fit into ongoing health monitoring
