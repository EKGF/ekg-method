import subprocess
from html.parser import HTMLParser
from pathlib import Path

import pytest


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[tuple[str, str, str]] = []
        self._current_anchor: dict[str, str] | None = None
        self._current_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return

        self._current_anchor = {
            key: value or "" for key, value in attrs if key in {"class", "href"}
        }
        self._current_text = []

    def handle_data(self, data: str) -> None:
        if self._current_anchor is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or self._current_anchor is None:
            return

        text = " ".join("".join(self._current_text).split())
        self.anchors.append(
            (
                self._current_anchor.get("href", ""),
                self._current_anchor.get("class", ""),
                text,
            )
        )
        self._current_anchor = None
        self._current_text = []


@pytest.fixture(scope="module")
def site_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output_dir = tmp_path_factory.mktemp("mkdocs-site") / "site"
    subprocess.run(
        ["mkdocs", "build", "--strict", "--site-dir", str(output_dir)],
        check=True,
    )
    return output_dir


def test_top_navigation_objectives_tab_targets_plural_index(site_dir: Path) -> None:
    parser = AnchorParser()
    parser.feed((site_dir / "index.html").read_text(encoding="utf-8"))

    objectives_tab_hrefs = [
        href
        for href, class_name, text in parser.anchors
        if text == "Objectives" and "md-tabs__link" in class_name.split()
    ]

    assert objectives_tab_hrefs == ["objectives/"]


def test_plural_objectives_url_is_the_cards_page(site_dir: Path) -> None:
    objectives_index = site_dir / "objectives" / "index.html"

    assert objectives_index.exists()

    objectives_html = objectives_index.read_text(encoding="utf-8")

    assert '<h1 id="objectives">' in objectives_html
    assert "objective-badge" in objectives_html
    assert "../objective/interoperability/" in objectives_html


def test_plural_objectives_url_keeps_original_objective_sidebar(site_dir: Path) -> None:
    objectives_html = (site_dir / "objectives" / "index.html").read_text(encoding="utf-8")

    assert (
        '<li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">'
    ) in objectives_html
    assert (
        '<input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_2" checked>'
    ) in objectives_html
    assert 'aria-expanded="true"' in objectives_html
    assert '<a href="../objective/interoperability/" class="md-nav__link">' in (objectives_html)
    assert '<a href="../objective/" class="md-nav__link">' not in objectives_html
    assert "../objectives/interoperability/" not in objectives_html


def test_existing_singular_objective_urls_stay_unchanged(site_dir: Path) -> None:
    objective_index = site_dir / "objective" / "index.html"
    objective_detail = site_dir / "objective" / "interoperability" / "index.html"

    assert objective_index.exists()
    assert objective_detail.exists()

    objective_index_html = objective_index.read_text(encoding="utf-8")
    objective_detail_html = objective_detail.read_text(encoding="utf-8")

    assert "Redirecting..." not in objective_index_html
    assert "Redirecting..." not in objective_detail_html
    assert '<h1 id="objectives">' in objective_index_html
    assert '<h1 id="interoperability-achieved">' in objective_detail_html


def test_only_plural_objectives_index_is_added(site_dir: Path) -> None:
    plural_paths = [
        path.relative_to(site_dir / "objectives")
        for path in (site_dir / "objectives").rglob("*.html")
    ]

    assert plural_paths == [Path("index.html")]
