# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when
working with code in this repository.

## Project overview

This is the **Use Case Tree Method** documentation site, published
at <https://method.ekgf.org>. It uses MkDocs with the Material theme
to generate a static documentation site from Markdown files.

## Commands

### Installation

```bash
make install              # Full setup (Homebrew packages + Python via uv)
uv sync                   # Install Python dependencies only
```

### Development

```bash
make docs-serve           # Serve with live reload (strict mode)
make docs-serve-fast      # Quick serve
make docs-serve-fresh     # Clean diagrams first, then serve
```

### Building

```bash
make docs-build           # Build site to /site directory
make docs-build-clean     # Clean build
```

### Linting

```bash
make lint                 # Python linting (ruff)
npm run lint:md           # Markdown linting
```

### Useful commands

```bash
make info                 # Show environment versions
make clean                # Remove .venv, site/, lock files
make docs-sync            # Sync with sibling projects (ekg-maturity, ekg-principles)
```

## Architecture

- **docs/** - Markdown source files organized by domain
  (concept/, objective/, process/, vocab/)
- **docs/diagrams/** - PlantUML diagrams with auto-generated SVGs in out/
- **docs/fragment/** - Reusable Markdown snippets included across pages
- **docs/main.py** - MkDocs hook that injects objective badges
- **docs-overrides/** - Template overrides synced with sibling projects
- **mkdocs.yml** - MkDocs configuration with plugins
- **site/** - Generated output (never edit)

Navigation structure is defined by `.pages.yaml` files
(awesome-pages plugin).

## Critical conventions

### Markdown formatting

- **70-character line length** (strictly enforced by linter)
- Use `-` for unordered lists
- Sentence case for headers (not Title Case)
- Do not trim trailing whitespace

### Git workflow

- **NEVER execute `git push`** - users must push manually
- **NEVER bypass hooks** with `--no-verify`
- **NEVER use `git merge`** - always use `git rebase` for linear history
- Commit only when explicitly requested
- Use Angular Conventional Commits: `<type>(<scope>): <subject>`
  - Types: feat, fix, docs, refactor, test, style, perf, build,
    ci, chore, revert
  - All lowercase, imperative mood, no period at end

### Multi-line commit messages

Use multiple `-m` flags to avoid body-max-line-length violations:

```bash
git commit -m "feat(component): add xyz" \
           -m "Short descriptive line"
```

## Dependencies

- Python 3.14.2+ with `uv` package manager
- System packages: cairo, pango, freetype, graphviz (for diagram rendering)
- Node.js for linting tools (commitlint, markdownlint, prettier)
