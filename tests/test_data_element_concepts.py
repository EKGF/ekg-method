"""Keep the Method's definitions, examples and diagrams on the same concept model."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CONCEPT_DOCS = ROOT / "docs" / "concept" / "concept"
DIAGRAMS = ROOT / "docs" / "diagrams" / "src"


def test_concept_definition_explains_the_formal_name_and_broader_scope() -> None:
    text = (CONCEPT_DOCS / "index.md").read_text()
    assert "# Data Element Concept" in text
    assert "ekg-concept:DataElementConcept" in text
    assert "ISO/IEC 11179" in text
    assert "compound data construct" in text
    assert "OWL class" in text
    assert "SHACL shape" in text


@pytest.mark.parametrize("name", ["index.md", "concept-vocabulary.md"])
def test_concepts_are_not_defined_as_inherently_context_specific(name: str) -> None:
    text = " ".join((CONCEPT_DOCS / name).read_text().split()).lower()
    assert "context-specific linking pin" not in text
    assert "concepts are contextual" not in text
    assert "is specific to the use case's context" not in text


def test_vocabulary_example_uses_the_ekg_classes_and_membership() -> None:
    text = (CONCEPT_DOCS / "concept-vocabulary.md").read_text()
    examples = re.findall(r"```turtle\n(.*?)```", text, re.DOTALL)
    assert examples
    example = "\n".join(examples)
    assert re.search(r"\ba\s+ekg-concept:DataElementConcept\b", example)
    assert re.search(r"\ba\s+ekg-concept:ConceptSet\b", example)
    assert "ekg-concept:inConceptSet" in example
    assert "ekg-concept:preferredBusinessTerm" in example
    assert not re.search(r"\ba\s+skos:Concept(?:Scheme)?\b", example)
    assert "skos:inScheme" not in example


@pytest.mark.parametrize(
    "path",
    [path for path in sorted(DIAGRAMS.glob("*.puml")) if "/concept/concept/#" in path.read_text()],
    ids=lambda path: path.name,
)
def test_diagrams_use_the_formal_concept_class(path: Path) -> None:
    text = path.read_text()
    assert 'class "DataElementConcept" as DataElementConcept' in text
    statements = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("'"))
    assert not re.search(r"\bConcept\b", statements)


@pytest.mark.parametrize(
    "path",
    [
        path
        for path in sorted(DIAGRAMS.glob("*.puml"))
        if "/concept/concept/concept-vocabulary/#" in path.read_text()
    ],
    ids=lambda path: path.name,
)
def test_diagrams_use_concept_set_membership_instead_of_skos(path: Path) -> None:
    text = path.read_text()
    assert 'class "ConceptSet" as ConceptSet' in text
    membership = [
        line for line in text.splitlines() if "DataElementConcept" in line and "ConceptSet" in line
    ]
    assert membership
    assert all("ekg-concept:inConceptSet" in line for line in membership)
    assert "ConceptVocabulary" not in text
