# Markdown Wrapping Script

## Overview

This directory contains a Python script (`wrap_markdown.py`) that
automatically wraps markdown lines at 70 characters while respecting
MkDocs Material syntax, including:

- Material for MkDocs tab syntax (`=== "..."`)
- Indented content within tabs
- Code blocks
- YAML frontmatter
- Lists (preserving proper indentation)
- HTML tags and special markdown constructs

## Why Not Prettier?

Prettier doesn't wrap indented content (4+ spaces) because it treats
it as code blocks according to standard Markdown spec. Since MkDocs
Material tabs require indentation, we need a custom solution.

## Setup

### 1. Install the "Run on Save" Extension

Open VS Code/Cursor and install:

- **Extension**: "Run On Save" by emeraldwalk
- **ID**: `emeraldwalk.runonsave`

OR run:

```bash
code --install-extension emeraldwalk.runonsave
```

### 2. Reload the Workspace

After installing the extension:

1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Developer: Reload Window"
3. Press Enter

### 3. Test It

1. Open any markdown file
2. Add a line longer than 70 characters
3. Save the file (`Cmd+S` or `Ctrl+S`)
4. The line should automatically wrap at 70 characters

## Manual Usage

You can also run the script manually:

```bash
# Wrap a single file
python3 scripts/wrap_markdown.py docs/concept/use-case.md

# Wrap multiple files
python3 scripts/wrap_markdown.py docs/concept/*.md

# Wrap all markdown files in a directory (use find)
find docs -name "*.md" -exec python3 scripts/wrap_markdown.py {} \;
```

## Configuration

The script is configured in `ekg-method.code-workspace` to run
automatically when you save any `.md` file:

```json
"emeraldwalk.runonsave": {
  "commands": [
    {
      "match": "\\.md$",
      "cmd": "python3 ${workspaceFolder}/scripts/wrap_markdown.py ${file}"
    }
  ]
}
```

## Troubleshooting

### Script Not Running on Save

1. Verify the extension is installed and enabled
2. Reload the workspace
3. Check the Output panel (View → Output) and select "Run On Save"
   from the dropdown

### Lines Not Wrapping

The script intentionally skips:

- Headings
- Code blocks (between ` ``` `)
- YAML frontmatter (between `---`)
- HTML tags
- Tables (lines with `|`)
- MkDocs include directives (`--8<--`)
- Tab delimiters (`===`)

### Wrong Line Length

The script is configured for 70 characters. To change this, edit the
`width` parameter in the script:

```python
def wrap_markdown(content: str, width: int = 70) -> str:
```
