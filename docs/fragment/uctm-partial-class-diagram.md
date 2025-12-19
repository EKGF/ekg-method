<!-- markdownlint-disable MD041 MD012 -->

```mermaid
classDiagram
  direction LR
  hide members

  class UseCase

  class UseCaseStereotype

  class Story

  class WorkflowDefinition

  class Outcome

  class OutcomeRelationship

  class Concept

  class ConceptVocabulary
  class Term
  class Persona

  %% Ownership / composition (part-of)
  UseCase "1" *-- "0..*" Story : owns
  UseCase "1" *-- "0..*" WorkflowDefinition : owns
  Concept "1" *-- "1..*" Term : owns

  %% Relationships
  UseCase "0..1" --> "1" UseCaseStereotype : hasStereotype
  UseCase "0..*" --> "0..*" OutcomeRelationship : outcomeLink
  OutcomeRelationship --> Outcome : targetOutcome
  UseCase "0..*" --> "0..*" ConceptVocabulary : references/owns
  ConceptVocabulary "1" o-- "0..*" Concept : contains

  %% Usage
  Story --> Persona : story:playedBy
  Story --> Outcome : story:contributesTo
  Story --> StoryConceptRelationship : story∶relatedConcept
  StoryConceptRelationship --> Concept: story∶concept
  WorkflowDefinition --> Story : workflow:firstStep
```

