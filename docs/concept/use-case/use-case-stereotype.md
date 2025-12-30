---
title: Use Case Stereotype
summary: >
  Organization-defined categorizations of use cases that make them
  recognizable in local language while maintaining the underlying Use
  Case Tree Method model.
authors:
  - Jacobus Geluk
date: 2024-12-30
---

# Use Case Stereotype

## Overview

A **Use Case Stereotype** is an organization-defined categorization of
a [Use Case](index.md) that makes it recognizable in the local
language without changing the underlying model. While the Use Case
Tree Method treats everything as a "Use Case", stereotypes allow
organizations to use their own familiar terminology (like "Business
Capability", "Data Domain", "Application", etc.) while maintaining the
structural consistency of the method.

By default, the stereotype is simply "Use Case". However, many
organizations use different type names for scopes that are effectively
the same concept in the Use Case Tree Method.

## Purpose

Use Case Stereotypes serve several important purposes:

1. **Local Language Recognition** — Organizations can use terminology
   that resonates with their culture and existing frameworks (e.g.,
   "Business Capability Area", "Data Domain", "Technical Component")

2. **Structural Guidance** — Stereotypes can define rules about how
   use cases relate to each other, including constraints like "allowed
   parent stereotypes" and "allowed child stereotypes"

3. **Domain Boundaries** — Stereotypes help clarify the scope and
   level of abstraction for different parts of the Use Case Tree

4. **Governance** — Stereotypes provide a mechanism for enforcing
   organizational standards and patterns in the Use Case Tree
   structure

## Key Characteristics

### Organization-Defined

Unlike [Outcome Stereotypes](../outcome/outcome-stereotype.md) which
have common industry patterns (Goals, KPIs, etc.), Use Case
Stereotypes are **entirely organization-defined**. Each organization
creates the stereotypes that make sense for their context,
terminology, and governance needs.

### Arbitrary Number

Organizations can define **any number** of stereotypes. There's no
prescribed set—create as many or as few as needed to support your
organizational structure and communication needs.

### Relationship Constraints

Stereotypes can define constraints about how use cases with different
stereotypes can relate to each other:

- **Allowed parent stereotypes** — What type of use case can be the
  parent of this type?
- **Allowed child stereotypes** — What types of use cases can be
  children of this type?

These constraints help maintain consistency and prevent structural
errors in the Use Case Tree.

## Common Stereotype Examples

While each organization defines its own stereotypes, here are some
common patterns:

### Business Capability Hierarchy

Many organizations use stereotypes to represent levels in their
business capability model:

#### Business Capability Area

The highest level of business capability organization.

**Constraints:**

- **Allowed children:** Business Capability Domain only
- **Allowed parents:** None (typically a root use case)

**Example:**

> "Customer Management", "Product Development", "Supply Chain"

#### Business Capability Domain

A domain within a capability area.

**Constraints:**

- **Allowed parent:** Business Capability Area
- **Allowed children:** Business Capability

**Example:**

> "Customer Onboarding", "Customer Support", "Customer Analytics"
> (within Customer Management area)

#### Business Capability

A specific business capability that delivers business outcomes.

**Constraints:**

- **Allowed parent:** Business Capability Domain
- **Allowed children:** Any (can contain more specific capabilities,
  services, components, etc.)

**Example:**

> "Process Customer Application", "Verify Customer Identity", "Open
> Customer Account"

### Data Architecture Stereotypes

#### Data Domain

A bounded area of data responsibility and governance.

**Example:**

> "Customer Data Domain", "Product Data Domain", "Financial Data
> Domain"

#### Data Product

A specific data product within a data domain (could also be modeled as
a regular Use Case with a stereotype).

**Example:**

> "Customer 360 View", "Product Catalog", "Transaction History"

### Technical Architecture Stereotypes

#### Technical Capability

A technical capability that supports business capabilities.

**Example:**

> "Identity & Access Management", "API Gateway", "Event Streaming"

#### Architecture Component

A structural component in the enterprise architecture.

**Example:**

> "Authentication Service", "Authorization Service", "Audit Service"

#### Module

A deployable module or package of functionality.

**Example:**

> "Customer UI Module", "Payment Processing Module", "Reporting
> Module"

#### API Service

A service exposed via API.

**Example:**

> "Customer API", "Product API", "Order API"

#### Application

A complete application or system.

**Example:**

> "Customer Portal", "Mobile Banking App", "Admin Dashboard"

## Defining Your Stereotypes

When defining Use Case Stereotypes for your organization, consider:

### 1. Align with Existing Frameworks

If your organization already uses frameworks like:

- **Business Capability Models** — Use stereotypes that match your
  capability hierarchy levels
- **Data Mesh** — Use stereotypes like "Data Domain", "Data Product"
- **Enterprise Architecture Frameworks** (TOGAF, Zachman, etc.) — Use
  stereotypes that align with your architecture views
- **Microservices Architecture** — Use stereotypes like "Service",
  "API", "Component"

### 2. Define Clear Hierarchies

Establish clear rules about:

- Which stereotypes can be parents of which other stereotypes
- Which stereotypes can be children of which other stereotypes
- Which stereotypes must be at the root level
- Which stereotypes must be leaf nodes

### 3. Keep It Simple Initially

Start with a small set of stereotypes:

- Don't try to define every possible stereotype upfront
- Begin with 3-5 key stereotypes that address your most important
  organizational needs
- Add more stereotypes as patterns emerge and needs become clear
- Refine constraints based on actual usage patterns

### 4. Document the Purpose

For each stereotype, document:

- **Purpose** — Why does this stereotype exist?
- **Scope** — What level of abstraction does it represent?
- **Constraints** — What parent/child relationships are allowed?
- **Examples** — What are typical use cases with this stereotype?
- **Guidance** — When should teams use this stereotype?

## Relationship to Use Case Tree Structure

Use Case Stereotypes work within the fundamental structure of the Use
Case Tree:

### is-part-of (Ownership)

Stereotypes don't change the ownership relationship. A child use case
is still **owned** by its parent, regardless of their stereotypes. The
stereotypes simply add validation rules about what types of ownership
relationships are valid.

**Example:**

> A "Business Capability" (child) can only be part of a "Business
> Capability Domain" (parent). This constraint is enforced by the
> stereotypes, but the underlying relationship is still `is-part-of`.

### is-used-in (Reuse)

Stereotypes can define constraints on reuse relationships as well. For
example, you might specify that a "Data Domain" can be used in any use
case, but a "Business Capability" can only be used in other "Business
Capability" use cases.

### Tree Flexibility

Even with stereotype constraints, the Use Case Tree remains flexible:

- Constraints guide structure but don't overly restrict it
- You can evolve stereotypes as your organization learns
- You can relax constraints when needed for valid use cases
- The underlying "everything is a Use Case" model remains intact

## Stereotypes vs. Other Categorizations

### Use Case Stereotype vs. Outcome Stereotype

- **[Outcome Stereotypes](../outcome/outcome-stereotype.md)** —
  Categorize the "why" (Goals, KPIs, Success Criteria)
- **Use Case Stereotypes** — Categorize the "what" (Capabilities,
  Domains, Components)

Both types of stereotypes can be used together. A "Business Capability
Area" (Use Case Stereotype) might have "Goals" and "KPIs" (Outcome
Stereotypes) associated with it.

### Use Case Stereotype vs. Persona Type

[Persona Taxonomy](../persona/persona-taxonomy.md) categorizes "who"
interacts with use cases. Use Case Stereotypes categorize the use
cases themselves. These are complementary categorizations:

- A "Customer Portal" (Use Case Stereotype: Application) might be used
  by "End User" (Persona Type: Human)
- A "Data Domain" (Use Case Stereotype) might be accessed by "System"
  (Persona Type: Non-Human)

## Best Practices

1. **Start with business language** — Use terminology that business
   stakeholders already understand and use

2. **Align with existing models** — If you have a business capability
   model or enterprise architecture framework, align stereotypes with
   those structures

3. **Define constraints thoughtfully** — Constraints should guide good
   structure, not create bureaucratic overhead

4. **Document and communicate** — Make sure everyone understands what
   each stereotype means and when to use it

5. **Evolve based on usage** — Monitor how teams use stereotypes and
   refine them based on actual patterns and needs

6. **Don't over-engineer** — Remember that stereotypes are just labels
   that add semantic meaning. The underlying Use Case concept remains
   the same.

7. **Enforce programmatically** — If you define constraints, implement
   them in your tooling to prevent invalid structures

## Implementation Considerations

### Validation

Implement validation rules to enforce stereotype constraints:

```python
def validate_parent_child_stereotypes(parent, child):
    """
    Validate that a child use case stereotype is allowed
    under a parent use case stereotype.
    """
    allowed_children = STEREOTYPE_RULES[parent.stereotype]['allowed_children']

    if child.stereotype not in allowed_children:
        raise ValidationError(
            f"A '{child.stereotype}' cannot be a child of '{parent.stereotype}'"
        )
```

### Migration

When introducing or changing stereotypes:

- **Grandfather existing structure** — Don't break existing use cases
- **Provide migration guidance** — Help teams update to new
  stereotypes
- **Support transitions** — Allow time for gradual adoption
- **Version your rules** — Track changes to stereotype definitions
  over time

### Tooling Support

Ensure your Use Case Tree management tools support:

- **Stereotype selection** — Easy UI for choosing stereotypes
- **Constraint validation** — Real-time feedback on valid/invalid
  relationships
- **Stereotype filtering** — Ability to view the tree filtered by
  stereotype
- **Reporting** — Analytics on stereotype usage and distribution

## See Also

- [Use Case](index.md) — The base concept
- [Use Case Tree](../use-case-tree.md) — How use cases are organized
- [Outcome Stereotype](../outcome/outcome-stereotype.md) —
  Categorizing outcomes
- [Persona Taxonomy](../persona/persona-taxonomy.md) — Categorizing
  personas
