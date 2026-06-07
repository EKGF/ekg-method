import re

from mkdocs.structure.nav import _add_parent_links, _add_previous_and_next_links
from mkdocs.structure.pages import Page

OBJECTIVES_SECTION_TITLE = "Objectives"
PLURAL_OBJECTIVES_INDEX = "objectives/index.md"
SINGULAR_OBJECTIVE_INDEX = "objective/index.md"


def _nav_item_src_uri(item):
    file = getattr(item, "file", None)
    return getattr(file, "src_uri", None)


def define_env(env):
    "Hook function"

    @env.macro
    def test123(page):
        list = []
        while page.next_page:
            list.append(page.next_page)
            page = page.next_page
        return list


def on_nav(nav, config, files):
    """Use /objectives/ as the Objective section index."""
    objectives_file = files.get_file_from_path(PLURAL_OBJECTIVES_INDEX)
    if objectives_file is None:
        return nav

    objective_section = next(
        (
            item
            for item in nav.items
            if getattr(item, "is_section", False) and item.title == OBJECTIVES_SECTION_TITLE
        ),
        None,
    )
    if objective_section is None:
        return nav

    objectives_page = objectives_file.page or Page("Objectives", objectives_file, config)
    objectives_page.title = OBJECTIVES_SECTION_TITLE

    hidden_section_indexes = {PLURAL_OBJECTIVES_INDEX, SINGULAR_OBJECTIVE_INDEX}
    objective_section.children = [
        child
        for child in objective_section.children
        if _nav_item_src_uri(child) not in hidden_section_indexes
    ]
    nav.pages = [
        page
        for page in nav.pages
        if page is not objectives_page and _nav_item_src_uri(page) != SINGULAR_OBJECTIVE_INDEX
    ]

    objective_section.children.insert(0, objectives_page)
    nav.pages.insert(1, objectives_page)

    _add_previous_and_next_links(nav.pages)
    _add_parent_links(nav.items)

    return nav


def on_page_content(html, page, config, files):
    """
    Inject objective letter badge before the first H1 heading.
    This runs after markdown is converted to HTML.
    """
    # Check if page has letter_prefix in frontmatter
    if not hasattr(page, "meta") or "letter_prefix" not in page.meta:
        return html

    letter_prefix = page.meta["letter_prefix"]
    if not letter_prefix or not isinstance(letter_prefix, str):
        return html

    # Find the first H1 tag and wrap it with the badge
    # Pattern: <h1 ... > ... </h1>
    h1_pattern = r"(<h1[^>]*>)(.*?)(</h1>)"

    def replace_first_h1(match):
        opening_tag = match.group(1)
        h1_content = match.group(2)
        closing_tag = match.group(3)

        # Create the badge wrapper HTML
        badge_html = f"""<div class="objective-header-with-badge">
<span class="objective-badge-standalone" data-letter="{letter_prefix}"></span>

{opening_tag}{h1_content}{closing_tag}

</div>"""
        return badge_html

    # Replace only the first H1
    modified_html = re.sub(
        h1_pattern,
        replace_first_h1,
        html,
        count=1,
        flags=re.DOTALL,
    )

    return modified_html
