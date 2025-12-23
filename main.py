import re

def define_env(env):
    "Hook function"

    @env.macro
    def test123(page):
        list = []
        while page.next_page:
            list.append(page.next_page)
            page = page.next_page
        return list


def on_page_content(html, page, config, files):
    """
    Inject objective letter badge before the first H1 heading.
    This runs after markdown is converted to HTML.
    """
    # Check if page has letter_prefix in frontmatter
    if not hasattr(page, 'meta') or 'letter_prefix' not in page.meta:
        return html
    
    letter_prefix = page.meta['letter_prefix']
    if not letter_prefix or not isinstance(letter_prefix, str):
        return html
    
    # Find the first H1 tag and wrap it with the badge
    # Pattern: <h1 ... > ... </h1>
    h1_pattern = r'(<h1[^>]*>)(.*?)(</h1>)'
    
    def replace_first_h1(match):
        opening_tag = match.group(1)
        h1_content = match.group(2)
        closing_tag = match.group(3)
        
        # Create the badge wrapper HTML
        badge_html = f'''<div class="objective-header-with-badge">
<span class="objective-badge-standalone" data-letter="{letter_prefix}"></span>

{opening_tag}{h1_content}{closing_tag}

</div>'''
        return badge_html
    
    # Replace only the first H1
    modified_html = re.sub(h1_pattern, replace_first_h1, html, count=1, flags=re.DOTALL)
    
    return modified_html
