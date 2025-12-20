# PlantUML diagrams at a glance

This repository standardises on PlantUML for **all** diagrams.  The setup
gives us:

- On-brand styling (EKGF blue/orange, Roboto, hand-drawn lines)
- Automatic light/dark variants (including white labels in dark mode)
- Clickable SVG links that keep working inside MkDocs
- Transparent backgrounds and responsive sizing without any manual tweaks

The sections below describe how everything fits together and how to add or
update diagrams in the future.

---

## Directory layout & build flow

```text
docs/
├── diagrams/
│   ├── include/          # Shared PlantUML themes
│   │   ├── light.puml    # Light palette
│   │   ├── dark.puml     # Dark palette
│   │   └── general.puml  # Style primitives used by both themes
│   ├── src/              # Author your *.puml files here
│   └── out/              # Auto-generated SVGs (never edit manually)
│
├── fragment/             # Reusable Markdown snippets that embed diagrams
└── stylesheets/extra.css # Layout tweaks (left align, spacing, etc.)
```

`mkdocs.yml` enables the `mkdocs-build-plantuml` plugin.  When you run:

```bash
uv run mkdocs serve    # or `uv run mkdocs build` or `gmake docs-serve`
```

the plugin renders every `docs/diagrams/src/*.puml` file to an SVG pair
(light + dark) inside `docs/diagrams/out/`.  Never commit hand-edited SVGs.

---

## Embedding diagrams in Markdown

1. Add a Markdown fragment (or inline block) that wraps the SVG with an HTML
   `<object>`, **not** the usual `![]()` syntax.  
   Example (`docs/fragment/uctm-diagram-persona.md`):

   ```md
   <figure markdown>
     <object
       data="/diagrams/out/uctm-persona.svg#darkable"
       type="image/svg+xml">
     </object>
   </figure>
   ```

   - The `#darkable` suffix tells Material/MkDocs that both light and dark
     SVGs exist (`foo.svg` + `foo_dark.svg`).
   - Using `<object>` keeps all SVG hyperlinks clickable (essential for
     cross-linking class diagrams to concept pages).

2. Insert the fragment wherever you need it:

   ```md
   --8<-- "fragment/uctm-diagram-persona.md"
   ```

---

## Runtime behaviour (`darkable-objects.js`)

We load `docs/javascripts/darkable-objects.js` via `extra_javascript`.  The
script performs the following on every page load (and when Material’s instant
navigation swaps content):

1. Finds every `<object ... #darkable>` element.
2. Fetches both SVG variants and inlines the markup directly into the page.
   - Keeps all hyperlinks working.
   - Ensures backgrounds remain transparent.
3. Detects the current theme (light or dark) and swaps in the appropriate SVG
   whenever the palette toggle changes.
4. Reads the SVG’s natural width (from `viewBox`/`width`) and sets a responsive
   width capped at `min(natural width, viewport - 64px, 1400px)`.  
   - Huge diagrams can stretch across large monitors.  
   - Smaller diagrams (like `Term`) stay compact and never get blown up.
5. Listens for window resize events and re-applies sizing with a short debounce.

Because of this script you should **always** embed diagrams using `<object
... #darkable>` — it is the trigger for everything above.

---

## Creating or updating a diagram

1. **Author the PlantUML file** under `docs/diagrams/src/`.  Every file should
   start with:

   ```puml
   @startuml
   !include ../include/themes/light.puml
   ...
   @enduml
   ```

   - Use the shared theme; do not duplicate styling.
   - For state/process diagrams, use `[ * ]` start/end states — the dark theme
     now renders those nodes white so they remain visible at night.

2. **Serve or build the docs.**  `mkdocs-build-plantuml` will emit
   `docs/diagrams/out/<filename>.svg` and `<filename>_dark.svg`.

3. **Embed the generated SVG** using the `<figure> + <object ... #darkable>`
   pattern described above (ideally as a reusable fragment).

4. **Commit only the `.puml`, fragment, and any Markdown/JS/CSS changes.**
   The `out/` folder is re-generated during builds.

---

## Troubleshooting tips

- **Links not clickable?**  
  Check that you used `<object ... type="image/svg+xml">` and that
  `darkable-objects.js` is loaded (should happen automatically via
  `mkdocs.yml`).

- **Diagram shows white box in dark mode?**  
  Ensure your PlantUML file includes the shared theme, and confirm the fragment
  appends `#darkable` so the script can swap to `<name>_dark.svg`.

- **Sizing looks odd?**  
  Confirm the SVG has a correct `@startuml` / `@enduml` structure.  The script
  relies on PlantUML emitting a proper `viewBox`.  If you see issues, run a
  fresh `uv run mkdocs serve` so the SVGs regenerate.

---

Following these steps keeps every diagram on-brand, accessible in both light
and dark themes, and guarantees link-friendly, responsive SVGs throughout the
site.  Happy modelling!

