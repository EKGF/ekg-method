import subprocess
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def site_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output_dir = tmp_path_factory.mktemp("mkdocs-homepage") / "site"
    subprocess.run(
        ["mkdocs", "build", "--strict", "--site-dir", str(output_dir)],
        check=True,
    )
    return output_dir


def test_homepage_uses_method_specific_redesign(site_dir: Path) -> None:
    html = (site_dir / "index.html").read_text(encoding="utf-8")

    assert "method-home" in html
    assert "Turn strategic EKG use cases into reusable" in html
    assert "Strategic Use Case" in html
    assert "Semantic Packages" in html
    assert "Running EKG" in html


def test_homepage_replaces_stock_photo_outcome_cards(site_dir: Path) -> None:
    html = (site_dir / "index.html").read_text(encoding="utf-8")

    assert "Built for Business Outcomes" not in html
    assert "ekgf-image-card" not in html
    assert "background-image:" not in html

    for heading in [
        "Lighthouse use cases",
        "Semantic package manager",
        "Executable knowledge",
        "Functional health",
    ]:
        assert heading in html


def test_homepage_exposes_plan_build_run_journey(site_dir: Path) -> None:
    html = (site_dir / "index.html").read_text(encoding="utf-8")

    assert "Plan → Build → Run" in html

    for step in [
        "Envision",
        "Discover",
        "Assess",
        "Train",
        "Chart",
        "Allocate",
        "Design",
        "Implement",
        "Test",
        "Verify",
        "Deliver",
        "Deploy",
        "Operate",
        "Measure",
        "Optimize",
    ]:
        assert step in html


def test_homepage_left_edge_aligns_with_header_logo_word(site_dir: Path) -> None:
    url = (site_dir / "index.html").resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1862, "height": 1280},
            device_scale_factor=1,
        )
        page.goto(url, wait_until="load")
        page.wait_for_selector(".method-home")

        logo_word = page.locator(".md-header__button.md-logo .ekgf-logo-text").bounding_box()
        homepage = page.locator(".method-home").bounding_box()
        browser.close()

    assert logo_word is not None
    assert homepage is not None
    assert abs(homepage["x"] - logo_word["x"]) <= 8


def test_homepage_uses_full_article_width(site_dir: Path) -> None:
    url = (site_dir / "index.html").resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1632, "height": 1536},
            device_scale_factor=1,
        )
        page.goto(url, wait_until="load")
        page.wait_for_selector(".method-home")

        article = page.locator(".md-content__inner").bounding_box()
        homepage = page.locator(".method-home").bounding_box()
        first_section = page.locator(".method-capabilities").bounding_box()
        browser.close()

    assert article is not None
    assert homepage is not None
    assert first_section is not None
    article_right = article["x"] + article["width"]
    homepage_right = homepage["x"] + homepage["width"]
    first_section_right = first_section["x"] + first_section["width"]
    assert abs(homepage_right - article_right) <= 8
    assert abs(first_section_right - article_right) <= 8


def test_homepage_diagram_package_labels_fit_without_word_splitting(
    site_dir: Path,
) -> None:
    url = (site_dir / "index.html").resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1862, "height": 1280},
            device_scale_factor=1,
        )
        page.goto(url, wait_until="load")
        page.wait_for_selector(".method-package-grid")

        package_grid = page.locator(".method-package-grid").evaluate(
            """
            (element) => ({
              overflow: element.scrollWidth - element.clientWidth,
            })
            """
        )
        labels = page.locator(".method-package-grid span").evaluate_all(
            """
            (elements) => elements.map((element) => {
              const range = document.createRange();
              range.selectNodeContents(element);
              const lines = Array.from(range.getClientRects())
                .filter((rect) => rect.width > 1 && rect.height > 1);
              range.detach();

              return {
                text: element.textContent.trim(),
                lineCount: lines.length,
                overflow: element.scrollWidth - element.clientWidth,
              };
            })
            """
        )
        browser.close()

    assert package_grid["overflow"] <= 1
    assert labels
    for label in labels:
        assert label["overflow"] <= 1, label
        assert label["lineCount"] == 1, label


def test_homepage_diagram_secondary_stage_labels_align_horizontally(
    site_dir: Path,
) -> None:
    url = (site_dir / "index.html").resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1862, "height": 1280},
            device_scale_factor=1,
        )
        page.goto(url, wait_until="load")
        page.wait_for_selector(".method-flow")

        stage_label_tops = page.locator(".method-flow__node strong").evaluate_all(
            """
            (elements) => elements.map((element) => element.getBoundingClientRect().top)
            """
        )
        browser.close()

    assert len(stage_label_tops) == 4
    assert max(stage_label_tops) - min(stage_label_tops) <= 2
