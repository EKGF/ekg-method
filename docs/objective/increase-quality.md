---
title: >-
  I: Increase Quality - Comprehensive Testing Methodology
authors:
  - Jacobus Geluk
hide:
  - toc
date_published: "2022-01-01"
letter_prefix: "I"
description: >-
  Learn how to enforce 100% test coverage based on real business
  scenarios and requirements. Discover how the Use Case Tree Method
  ensures quality through comprehensive testing.
keywords:
  - quality assurance
  - test coverage
  - business scenarios
  - EKG method
  - enterprise knowledge graph
  - testing methodology
schema_type: Article
---

# Increase Quality

<!--summary-start-->

_Enforce 100% test coverage based on real business scenarios and
requirements._

<!--summary-end-->

Quality in most organizations is an afterthought. Testing is something
developers do when they have time. Test coverage is a metric nobody
really believes. "It works on my machine" is still an acceptable answer
in too many places.

This doesn't work for an Enterprise Knowledge Graph. An EKG that serves
strategic use cases across the organization cannot afford "mostly works"
or "works in the demo." It has to work. Every time. For everyone.

## The Testing Problem

Traditional testing approaches fail for several reasons:

- **Tests are disconnected from requirements** - Developers write tests
  based on what they built, not what the business asked for
- **Coverage is meaningless** - 80% code coverage says nothing about
  whether the system does what users need
- **Tests rot** - Requirements change, tests don't, and nobody notices
  until production breaks
- **Testing happens too late** - Problems found in QA are expensive;
  problems found in production are disasters

## 100% Coverage That Actually Means Something

The [Use Case Tree](../concept/use-case-tree.md) enforces, requires, and
enables 100% test coverage—but coverage that's based on real business
scenarios and requirements, not arbitrary code metrics.

Every [story](../concept/story.md) in a use case defines what the system
must do, for whom, and why. Each story has explicit acceptance criteria.
Those criteria *are* the tests. If a story passes its criteria, it works.
If it doesn't, it doesn't ship.

No story without criteria. No criteria without tests. No deployment
without all tests passing.

## The Use Case as Living Specification

A use case starts with just a name and a description. Over its lifecycle,
it grows into a fully detailed model:

- [Concepts](../concept/concept/index.md) - What things are we talking about?
- [Personas](../concept/persona/index.md) - Who uses this?
- [Outcomes](../concept/outcome/index.md) - What value does it deliver?
- [Stories](../concept/story.md) - What must the system do?
- [Workflows](../concept/workflow.md) - How does work flow?
- Dependencies - What else does this need?

This model is captured in the EKG itself. The specification *is* the
system. When the model changes, the tests change. When the tests change,
you know immediately if something broke.

## Build Time and Run Time

Most testing happens during development. Ship it, and hope for the best.

The Use Case Tree approach tests continuously—not just during build, but
in production:

- **Build phase** - Every commit triggers full test suites
- **Run phase** - Production monitoring validates that the system
  continues to behave as specified

This is the quality level required for enterprise strategic use cases.
Anything less is hoping. Hope is not a strategy.

## See Also

- [Use Case Tree](../concept/use-case-tree.md)
- [Story](../concept/story.md)
- [Avoid Disruption](avoid-disruption.md)
