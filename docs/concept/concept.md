# Concept

For every given Use Case we want to start with capturing the concepts and
terms that the user or "the business" uses or wants to use.

Most of these concepts and their terms will be pre-defined in all kinds of
vocabularies but for brand-new use cases in a new domain concepts and their
terms will have to be created.

```mermaid
classDiagram
    direction RL
    class Concept {
        - type : ConceptType
    }
    class UseCase {
        - vocabulary: Vocabulary
        - stories: Story[]
    }
    UseCase --> UseCase : requires
    Vocabulary "*" --> "*" Concept
    Vocabulary "*" --> "*" Term
    Story --> "*" Concept : input
    Story --> "*" Concept : output
    Term --> "1..*" Concept
    %% Concept --> OntologyAxiom
    Vocabulary <--> Concept
    UseCase --> "1..*" Story
    Persona --|> Concept
    Concept --> Concept : broader
    Concept --> Term : preferred
    UseCase --> "1" Vocabulary : use case vocabulary
    Persona "1" --o "0..*" Story
    link UseCase "../use-case/"
    link Story "../story/"
    link Concept "../concept/"
    link Persona "../persona/"
```
