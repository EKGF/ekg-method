/**
 * Automatically inject objective letter badges when letter_prefix is
 * present in page frontmatter.
 *
 * This script:
 * 1. Checks for letter_prefix in page metadata
 * 2. Finds the first H1 heading on the page
 * 3. Wraps it with the badge component if not already wrapped
 * 4. Works with Material for MkDocs instant loading
 */
(function () {
  if (window.__ekgfObjectiveBadgesInitialized) {
    return;
  }
  window.__ekgfObjectiveBadgesInitialized = true;

  function injectBadge() {
    // Check if letter_prefix exists in page metadata
    const metaScript = document.getElementById(
      'page-meta-letter-prefix'
    );
    if (!metaScript) {
      return; // No letter_prefix on this page
    }

    let letterPrefix;
    try {
      letterPrefix = JSON.parse(metaScript.textContent);
    } catch (e) {
      console.error(
        '[objective-badges] Failed to parse letter_prefix',
        e
      );
      return;
    }

    if (!letterPrefix || typeof letterPrefix !== 'string') {
      return;
    }

    // Find the first H1 in the main content area
    const mainContent = document.querySelector(
      '.md-content__inner, article'
    );
    if (!mainContent) {
      return;
    }

    // Check if H1 is already wrapped in objective-header-with-badge
    const existingWrapper = mainContent.querySelector(
      '.objective-header-with-badge'
    );
    if (existingWrapper) {
      return; // Already has badge, skip
    }

    // Find the first H1
    const firstH1 = mainContent.querySelector('h1:first-of-type');
    if (!firstH1) {
      return; // No H1 found
    }

    // Create the badge span
    const badge = document.createElement('span');
    badge.className = 'objective-badge-standalone';
    badge.setAttribute('data-letter', letterPrefix);

    // Create the wrapper div
    const wrapper = document.createElement('div');
    wrapper.className = 'objective-header-with-badge';

    // Wrap the H1 with the badge
    firstH1.parentNode.insertBefore(wrapper, firstH1);
    wrapper.appendChild(badge);
    wrapper.appendChild(document.createTextNode('\n\n'));
    wrapper.appendChild(firstH1);
    wrapper.appendChild(document.createTextNode('\n\n'));
  }

  function initPage() {
    // Small delay to ensure DOM is ready
    setTimeout(injectBadge, 0);
  }

  // Handle Material for MkDocs instant loading
  if (window.document$ && window.document$.subscribe) {
    document$.subscribe(() => {
      initPage();
    });
  }

  // Initial page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPage);
  } else {
    initPage();
  }
})();

