---
title: Continuous testing
description: >-
  How the Enterprise Knowledge Graph continuously tests
  stories and monitors its own functional health.
---

# Continuous testing and functional health

The EKG knows about "its Stories" and continuously tests
them.
It therefore knows about its own "functional health" and can
detect whenever something changes (code, ontologies, ETL,
new policies) whether it can still deliver all
functionality.

This means that Stories are not just requirements
documents — they are **living, executable specifications**
that the EKG monitors and validates throughout their entire
lifecycle.

## How it works

Every story has one or more
[test scenarios](test-scenarios.md) — concrete
Given-When-Then checks that verify the story delivers
what it promises.
The EKG runs these test scenarios continuously, not
just before deployment but also in production.

When a test scenario fails, the EKG knows exactly
which story is affected, which
[use case](../use-case/index.md) it belongs to, and
which [personas](../persona/index.md) are impacted.
This turns a technical failure into a business-level
signal.

## Functional health

**Functional health** is the degree to which the EKG
is delivering on its promises.
It is measured by the ratio of passing test scenarios
to total test scenarios across all stories.

Because the EKG tracks this continuously, stakeholders
can answer questions like:

- Are all stories still delivering after last night's
  data load?
- Which use cases are affected by the ontology change
  we just deployed?
- What is the overall health of the EKG right now?

## Coverage as a first-class metric

Stories without [test scenarios](test-scenarios.md) are
immediately visible as gaps.
The goal is 100% story coverage — every story should
have at least one test scenario verifying its behavior.

This makes testing a **structural property** of the
EKG, not an afterthought.
