/**
 * Inline PlantUML SVGs (rendered via mkdocs-build-plantuml) so that:
 * - Clickable hyperlinks keep working
 * - Light/dark variants can be swapped even though Material only supports
 *   #darkable on <img>, not <object>
 * - Backgrounds remain transparent because we inject the SVG directly into DOM
 */
(function () {
  if (window.__ekgfInlineDiagramsInitialized) {
    return;
  }
  window.__ekgfInlineDiagramsInitialized = true;

  const DARK_SCHEME = 'slate';
  const OBJECT_SELECTOR = 'object[type="image/svg+xml"][data*="#darkable"]';
  const diagrams = new Set();
  const MAX_WIDTH = 1400;
  const VIEWPORT_PADDING = 64;
  let resizeTimeout = null;

  function getPaletteHost() {
    return document.body || document.documentElement;
  }

  function isDarkMode() {
    const host = getPaletteHost();
    return (host && host.getAttribute('data-md-color-scheme')) === DARK_SCHEME;
  }

  function getVariantPaths(rawValue) {
    if (!rawValue) return null;
    const cleaned = rawValue.replace('#darkable', '');
    const match = cleaned.match(/(.*?)(\.svg(?:\?.*)?)$/i);
    if (!match) return null;

    const light = cleaned.replace(/_dark(?=\.svg(\?.*)?$)/i, '');
    const dark = light.replace(/\.svg(\?.*)?$/i, '_dark.svg');
    return { light, dark };
  }

  function getNaturalWidth(svg) {
    const viewBox = svg.getAttribute('viewBox');
    if (viewBox) {
      const parts = viewBox.trim().split(/\s+/);
      if (parts.length === 4) {
        const width = parseFloat(parts[2]);
        if (!Number.isNaN(width)) {
          return width;
        }
      }
    }
    const widthAttr = svg.getAttribute('width');
    if (widthAttr) {
      const numeric = parseFloat(widthAttr);
      if (!Number.isNaN(numeric)) {
        return numeric;
      }
    }
    return null;
  }

  function getTargetWidth(naturalWidth) {
    const viewportCap = Math.max(
      320,
      Math.min(window.innerWidth - VIEWPORT_PADDING, MAX_WIDTH)
    );
    if (naturalWidth) {
      return Math.min(viewportCap, naturalWidth);
    }
    return viewportCap;
  }

  function applySizing(diagram, svg) {
    const targetWidth = getTargetWidth(diagram.naturalWidth);
    diagram.container.style.width = `${targetWidth}px`;
    svg.style.width = `${targetWidth}px`;
    svg.style.maxWidth = '100%';
    svg.style.height = 'auto';
    svg.removeAttribute('height');
  }

  function renderDiagram(diagram) {
    const markup =
      (isDarkMode() ? diagram.darkMarkup : diagram.lightMarkup) ||
      diagram.lightMarkup;
    if (!markup) return;
    diagram.container.innerHTML = markup;
    const svg = diagram.container.querySelector('svg');
    if (svg) {
      diagram.naturalWidth = getNaturalWidth(svg) || diagram.naturalWidth;
      applySizing(diagram, svg);
    }
  }

  async function inlineDiagram(obj) {
    const variants = getVariantPaths(obj.getAttribute('data'));
    if (!variants) return;

    const container = document.createElement('div');
    container.classList.add('ekgf-diagram');
    container.setAttribute('role', 'img');

    obj.replaceWith(container);

    try {
      const [lightMarkup, darkMarkup] = await Promise.all([
        fetch(variants.light).then((response) => response.text()),
        fetch(variants.dark)
          .then((response) => response.text())
          .catch(() => null),
      ]);

      const diagram = {
        container,
        lightMarkup,
        darkMarkup: darkMarkup || lightMarkup,
        naturalWidth: null,
      };

      diagrams.add(diagram);
      renderDiagram(diagram);
    } catch (error) {
      console.error('[darkable] Failed to inline SVG diagram', error);
    }
  }

  async function transformObjects(root = document) {
    const objects = Array.from(root.querySelectorAll(OBJECT_SELECTOR));
    diagrams.clear();
    await Promise.all(objects.map(inlineDiagram));
  }

  const paletteObserver = new MutationObserver(() => {
    diagrams.forEach(renderDiagram);
  });

  const paletteHost = getPaletteHost();
  if (paletteHost) {
    paletteObserver.observe(paletteHost, {
      attributes: true,
      attributeFilter: ['data-md-color-scheme'],
    });
  }

  async function initPage() {
    await transformObjects();
  }

  if (window.document$ && window.document$.subscribe) {
    document$.subscribe(() => {
      initPage();
    });
  }

  initPage();

  window.addEventListener('resize', () => {
    if (resizeTimeout) {
      clearTimeout(resizeTimeout);
    }
    resizeTimeout = setTimeout(() => {
      diagrams.forEach(renderDiagram);
    }, 150);
  });
})();

