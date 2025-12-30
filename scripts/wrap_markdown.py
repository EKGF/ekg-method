#!/usr/bin/env python3
"""
Wrap markdown lines at 70 characters while respecting MkDocs Material syntax.
This handles indented content (tabs), code blocks, lists, and other markdown structures.
"""
import re
import sys
from pathlib import Path
from textwrap import wrap


def is_code_block_delimiter(line: str) -> bool:
    """Check if line is a code block delimiter (```)."""
    stripped = line.strip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def is_yaml_frontmatter_delimiter(line: str) -> bool:
    """Check if line is YAML frontmatter delimiter (---)."""
    return line.strip() == "---"


def should_skip_wrapping(line: str) -> bool:
    """Check if a line should not be wrapped."""
    stripped = line.strip()
    
    # Skip empty lines
    if not stripped:
        return True
    
    # Skip headings
    if stripped.startswith("#"):
        return True
    
    # Skip HTML tags
    if stripped.startswith("<") and stripped.endswith(">"):
        return True
    
    # Skip horizontal rules
    if re.match(r'^[-*_]{3,}$', stripped):
        return True
    
    # Skip tab delimiters
    if stripped.startswith('===') and '"' in stripped:
        return True
    
    # Skip MkDocs includes
    if '--8<--' in stripped:
        return True
    
    # Skip tables
    if '|' in stripped:
        return True
    
    return False


def is_list_item(line: str) -> bool:
    """Check if a line is a list item."""
    stripped = line.strip()
    return bool(re.match(r'^[-*+]\s+|\d+\.\s+', stripped))


def get_indent(line: str) -> str:
    """Get the leading whitespace of a line."""
    return line[:len(line) - len(line.lstrip())]


def wrap_paragraph(lines: list[str], width: int = 70) -> list[str]:
    """Wrap a paragraph of lines to the specified width."""
    if not lines:
        return lines
    
    # Get the indent from the first line
    indent = get_indent(lines[0])
    
    # Join all lines and strip
    text = " ".join(line.strip() for line in lines)
    
    # Check if this is a list item
    list_match = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', lines[0])
    if list_match:
        # For list items, preserve the list marker
        list_indent = list_match.group(1)  # The leading spaces
        list_marker = list_match.group(2)   # The marker (-, *, +, or number.)
        
        # Get just the text content without marker
        text_content = text[len(text) - len(list_match.group(3)):]
        text_content = " ".join(line.strip() for line in lines)
        # Remove the marker and spaces from the beginning
        marker_pattern = re.escape(list_marker) + r'\s+'
        text_content = re.sub(r'^.*?' + marker_pattern, '', text_content)
        
        # Calculate available width for text
        list_marker_with_space = list_marker + " "
        available_width = width - len(list_indent) - len(list_marker_with_space)
        
        # Wrap the text
        wrapped = wrap(
            text_content,
            width=available_width,
            break_long_words=False,
            break_on_hyphens=False
        )
        
        if not wrapped:
            return [lines[0]]
        
        # Add the list prefix to the first line
        result = [list_indent + list_marker_with_space + wrapped[0]]
        # Indent subsequent lines to align with the text
        subsequent_indent = list_indent + " " * len(list_marker_with_space)
        result.extend(subsequent_indent + line for line in wrapped[1:])
        return result
    else:
        # Regular paragraph
        wrapped = wrap(
            text,
            width=width - len(indent),
            break_long_words=False,
            break_on_hyphens=False
        )
        
        return [indent + line for line in wrapped] if wrapped else lines


def wrap_markdown(content: str, width: int = 70) -> str:
    """Wrap markdown content at the specified width."""
    lines = content.splitlines()
    result = []
    
    i = 0
    in_code_block = False
    in_frontmatter = False
    frontmatter_started = False
    paragraph_buffer = []
    
    while i < len(lines):
        line = lines[i]
        
        # Handle YAML frontmatter
        if is_yaml_frontmatter_delimiter(line):
            # Flush paragraph buffer
            if paragraph_buffer:
                result.extend(wrap_paragraph(paragraph_buffer, width))
                paragraph_buffer = []
            
            result.append(line)
            if not frontmatter_started:
                frontmatter_started = True
                in_frontmatter = True
            else:
                in_frontmatter = False
            i += 1
            continue
        
        # Inside frontmatter, don't wrap
        if in_frontmatter:
            result.append(line)
            i += 1
            continue
        
        # Handle code blocks
        if is_code_block_delimiter(line):
            # Flush paragraph buffer
            if paragraph_buffer:
                result.extend(wrap_paragraph(paragraph_buffer, width))
                paragraph_buffer = []
            
            result.append(line)
            in_code_block = not in_code_block
            i += 1
            continue
        
        # Inside code block, don't wrap
        if in_code_block:
            result.append(line)
            i += 1
            continue
        
        # Check if we should skip wrapping this line
        if should_skip_wrapping(line):
            # Flush paragraph buffer
            if paragraph_buffer:
                result.extend(wrap_paragraph(paragraph_buffer, width))
                paragraph_buffer = []
            
            result.append(line)
            i += 1
            continue
        
        # Empty line signals end of paragraph
        if not line.strip():
            if paragraph_buffer:
                result.extend(wrap_paragraph(paragraph_buffer, width))
                paragraph_buffer = []
            result.append(line)
            i += 1
            continue
        
        # List item starts a new paragraph
        if is_list_item(line):
            if paragraph_buffer:
                result.extend(wrap_paragraph(paragraph_buffer, width))
                paragraph_buffer = []
            paragraph_buffer = [line]
            i += 1
            continue
        
        # Check if indent level changed (new paragraph)
        if paragraph_buffer and get_indent(line) != get_indent(paragraph_buffer[0]):
            result.extend(wrap_paragraph(paragraph_buffer, width))
            paragraph_buffer = [line]
        # If previous line was a list item, current line (if not a list item) ends it
        elif paragraph_buffer and is_list_item(paragraph_buffer[0]):
            result.extend(wrap_paragraph(paragraph_buffer, width))
            paragraph_buffer = [line]
        else:
            # Add to current paragraph
            paragraph_buffer.append(line)
        
        i += 1
    
    # Flush any remaining paragraph
    if paragraph_buffer:
        result.extend(wrap_paragraph(paragraph_buffer, width))
    
    return "\n".join(result) + "\n" if content.endswith("\n") else "\n".join(result)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: wrap_markdown.py <file.md> [<file2.md> ...]")
        sys.exit(1)
    
    for file_path in sys.argv[1:]:
        path = Path(file_path)
        if not path.exists():
            print(f"Error: {file_path} does not exist", file=sys.stderr)
            continue
        
        if not path.suffix == ".md":
            print(f"Skipping {file_path} (not a markdown file)", file=sys.stderr)
            continue
        
        print(f"Wrapping {file_path}...")
        content = path.read_text()
        wrapped = wrap_markdown(content)
        path.write_text(wrapped)
        print(f"✓ {file_path}")


if __name__ == "__main__":
    main()
