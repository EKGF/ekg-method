<!-- markdownlint-disable MD041 MD012 -->

```mermaid
classDiagram
  direction LR
  hide members

  class Concept
  class Term
  class BusinessTerm
  class TechnicalTerm
  class ConceptVocabulary
  class UseCase
  class Story
  class StoryConceptRelationship

  %% Term specializations
  Term <|-- BusinessTerm
  Term <|-- TechnicalTerm

  %% Terms
  Concept "1" *-- "1..*" Term : ∶term
  Concept "0..1" --> "1" BusinessTerm : ∶labelTerm

  %% Vocabularies
  %% Mermaid classDiagram can't parse ASCII ':' inside labels; use ratio sign (∶) instead.
  ConceptVocabulary "1" o-- "0..*" Concept : skos∶inScheme
  ConceptVocabulary "0..*" --> "1" UseCase : ∶useCase

  %% Usage
  Story "0..*" --> "1" StoryConceptRelationship : ∶storyConcept
  StoryConceptRelationship --> Concept : ∶concept
```



