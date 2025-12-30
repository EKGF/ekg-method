---
description: >-
  Technical manifestations of a Concept in code, data, and metadata.
  Learn how Technical Terms bridge the gap between human language and
  machine-readable data.
keywords:
  - technical term
  - variable name
  - column header
  - API parameter
  - EKG method
---

# Technical Term

Technical Terms are manifestations of a [Concept](../concept.md) in
code and data.

## Purpose

Technical Terms allow the Knowledge Graph to connect technical
artifacts back to a consistent semantic core. This enables automated
discovery and traceability from business requirements down to the
exact line of code or database column.

## Categories of Technical Terms

### Code & Data Manifestations

- **Variable names** (e.g., `cust_id`, `?patient`)
- **Database column names** (e.g., `P_NAME`, `CLIENT_REF`)
- **API parameters and fields** (e.g., `/customers/{id}`)

### Semantic Artifacts

In the Build phase, Technical Terms include links to:

- **OWL classes and properties** (e.g., `hospital:Patient`)
- **SHACL shapes** for validation

## Automated Discovery

Technical Terms can often be **discovered automatically** by scanning
the organization’s repositories: Python/Java code, SQL, configuration,
CSV column headers, and API specs.
