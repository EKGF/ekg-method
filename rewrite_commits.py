#!/usr/bin/env python3
"""
Script to rewrite git commit messages to follow conventional commits format.
This script analyzes commit messages and converts them to conventional commit format.
"""

import re
import subprocess
import sys

def get_commit_type_and_message(msg):
    """Convert a commit message to conventional commit format."""
    
    # Remove "#1 " prefix if present
    msg = re.sub(r'^#1\s+', '', msg)
    
    # Fix typo "fromt" -> "from" regardless of format
    if 'fromt' in msg.lower() and 'last call' in msg.lower():
        # If already in conventional commit format, fix the typo in place
        if re.match(r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)(\(.+\))?:', msg):
            return re.sub(r'fromt', 'from', msg, flags=re.IGNORECASE)
        else:
            return f"chore(docs): updates from the last call"
    
    # Already in conventional commit format
    if re.match(r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)(\(.+\))?:', msg):
        return msg
    
    # Merge commits - keep as is
    if msg.startswith('Merge '):
        return msg
    
    # Deployed commits - convert to ci(deploy)
    if msg.startswith('Deployed '):
        return f"ci(deploy): {msg.lower()}"
    
    # Bump commits - convert to chore(deps)
    if msg.startswith('Bump '):
        # Extract package name
        match = re.search(r'Bump (.+?) from', msg)
        if match:
            pkg = match.group(1).replace('/', '-')
            return f"chore(deps): {msg.lower()}"
        return f"chore(deps): {msg.lower()}"
    
    # Fix commits
    if any(word in msg.lower() for word in ['fix', 'fixed', 'fixing', 'fixes']):
        scope = 'ci' if any(word in msg.lower() for word in ['workflow', 'github', 'action', 'ci', 'build', 'labeler', 'mkdocs', 'config']) else 'docs'
        if 'typo' in msg.lower():
            scope = 'docs'
        elif 'plantuml' in msg.lower() or 'diagram' in msg.lower():
            scope = 'docs'
        elif 'pip' in msg.lower() or 'install' in msg.lower() or 'wheel' in msg.lower():
            scope = 'build'
        return f"fix({scope}): {msg.lower()}"
    
    # Add/Added commits
    if msg.startswith('Add') or msg.startswith('Added') or msg.startswith('add'):
        scope = 'docs'
        if 'content' in msg.lower():
            scope = 'docs'
        elif 'plantuml' in msg.lower() or 'mermaid' in msg.lower() or 'diagram' in msg.lower():
            scope = 'docs'
        elif 'github' in msg.lower() or 'action' in msg.lower() or 'workflow' in msg.lower() or 'ci' in msg.lower():
            scope = 'ci'
        elif 'insiders' in msg.lower() or 'mkdocs' in msg.lower():
            scope = 'docs'
        elif 'menu' in msg.lower():
            scope = 'docs'
        elif 'tool' in msg.lower() or 'pre-requisite' in msg.lower():
            scope = 'build'
        elif 'venv' in msg.lower() or '.gitignore' in msg.lower():
            scope = 'build'
        elif 'charter' in msg.lower() or 'lock file' in msg.lower() or 'settings' in msg.lower():
            scope = 'chore'
        elif 'analytics' in msg.lower():
            scope = 'chore'
        elif 'objective' in msg.lower() or 'modularity' in msg.lower():
            scope = 'docs'
        elif 'process' in msg.lower():
            scope = 'docs'
        elif 'article' in msg.lower() or 'interoperability' in msg.lower():
            scope = 'docs'
        elif 'point' in msg.lower() or 'tubbax' in msg.lower():
            scope = 'docs'
        else:
            scope = 'docs'
        return f"feat({scope}): {msg.lower()}"
    
    # Update/Updated commits
    if msg.startswith('Update') or msg.startswith('Updated') or msg.startswith('update'):
        # Special case: fix typo "fromt" -> "from"
        if 'fromt' in msg.lower() and 'last call' in msg.lower():
            return f"chore(docs): updates from the last call"
        scope = 'ci'
        if 'analytics' in msg.lower():
            scope = 'chore'
        elif 'tool' in msg.lower() or 'version' in msg.lower():
            scope = 'build'
        elif 'workflow' in msg.lower() or 'action' in msg.lower():
            scope = 'ci'
        elif 'asdf' in msg.lower():
            scope = 'ci'
        elif 'cname' in msg.lower():
            scope = 'docs'
        else:
            scope = 'ci'
        return f"chore({scope}): {msg.lower()}"
    
    # Remove/Removed commits
    if msg.startswith('Remove') or msg.startswith('Removed') or msg.startswith('remove'):
        scope = 'build'
        if 'java' in msg.lower() or 'node' in msg.lower() or 'plantuml' in msg.lower():
            scope = 'build'
        elif 'diagram' in msg.lower():
            scope = 'docs'
        elif 'job' in msg.lower() or 'macos' in msg.lower():
            scope = 'ci'
        else:
            scope = 'build'
        return f"chore({scope}): {msg.lower()}"
    
    # Rename/Renamed commits
    if msg.startswith('Rename') or msg.startswith('Renamed') or msg.startswith('rename'):
        scope = 'docs'
        if 'website' in msg.lower() or 'ekgf' in msg.lower():
            scope = 'docs'
        return f"chore({scope}): {msg.lower()}"
    
    # Enable/Enabling commits
    if msg.startswith('Enable') or msg.startswith('Enabling') or msg.startswith('enable'):
        scope = 'docs'
        if 'url' in msg.lower() or 'edit' in msg.lower():
            scope = 'docs'
        return f"feat({scope}): {msg.lower()}"
    
    # Disable/Disabling commits
    if msg.startswith('Disable') or msg.startswith('Disabling') or msg.startswith('disable'):
        scope = 'docs'
        if 'pic' in msg.lower() or 'process' in msg.lower():
            scope = 'docs'
        return f"fix({scope}): {msg.lower()}"
    
    # Create/Delete CNAME
    if 'CNAME' in msg:
        action = 'create' if 'Create' in msg else 'delete'
        return f"chore(docs): {action} CNAME"
    
    # Minor changes/updates/improvements
    if any(phrase in msg.lower() for phrase in ['minor change', 'minor update', 'minor improvement', 'minor fix', 'minor fixes']):
        scope = 'docs'
        if 'text' in msg.lower() or 'content' in msg.lower():
            scope = 'docs'
        elif 'concept' in msg.lower() or 'use case' in msg.lower() or 'plan' in msg.lower():
            scope = 'docs'
        else:
            scope = 'docs'
        return f"chore({scope}): {msg.lower()}"
    
    # Content improvements
    if any(phrase in msg.lower() for phrase in ['content improvement', 'many content', 'more content', 'some more content', 'added more content']):
        return f"feat(docs): {msg.lower()}"
    
    # "Many content improvements" or similar
    if 'improvement' in msg.lower() and 'content' in msg.lower():
        return f"feat(docs): {msg.lower()}"
    
    # "First stab", "First push", "First boilerplate"
    if msg.startswith('First '):
        if 'push' in msg.lower():
            return f"chore(ci): {msg.lower()}"
        elif 'boilerplate' in msg.lower():
            return f"chore: {msg.lower()}"
        elif 'stab' in msg.lower():
            return f"feat(docs): {msg.lower()}"
    
    # "Trying to" commits
    if msg.startswith('Trying ') or msg.startswith('trying '):
        scope = 'ci'
        if 'mermaid' in msg.lower():
            scope = 'docs'
        elif 'python' in msg.lower() or 'brew' in msg.lower() or 'asdf' in msg.lower():
            scope = 'ci'
        return f"chore({scope}): {msg.lower()}"
    
    # "Making sure" or "making Makefile"
    if msg.startswith('Making ') or msg.startswith('making '):
        scope = 'ci'
        if 'makefile' in msg.lower():
            scope = 'build'
        elif 'pat' in msg.lower() or 'env' in msg.lower():
            scope = 'ci'
        elif 'push' in msg.lower() or 'fetch' in msg.lower():
            scope = 'ci'
        return f"chore({scope}): {msg.lower()}"
    
    # "Installing" or "install"
    if 'install' in msg.lower():
        scope = 'build'
        if 'insiders' in msg.lower() or 'mkdocs' in msg.lower():
            scope = 'build'
        return f"chore({scope}): {msg.lower()}"
    
    # "Fetching" commits
    if msg.startswith('Fetching ') or 'fetch' in msg.lower():
        return f"chore(ci): {msg.lower()}"
    
    # "Switching" commits
    if 'switching' in msg.lower() or 'switch' in msg.lower():
        return f"chore(docs): {msg.lower()}"
    
    # "Added proposed" or "Added some points"
    if 'proposed' in msg.lower():
        return f"feat(docs): {msg.lower()}"
    
    # Default: treat as feat(docs) for content-related, chore for others
    if any(word in msg.lower() for word in ['content', 'text', 'page', 'section', 'concept', 'usecase', 'faq']):
        return f"feat(docs): {msg.lower()}"
    
    # Default fallback
    return f"chore: {msg.lower()}"

def main():
    # Read from stdin (for git filter-branch) or command line argument
    if len(sys.argv) >= 2:
        original_msg = sys.argv[1]
    else:
        original_msg = sys.stdin.read().strip()
    
    if not original_msg:
        # Empty commit message - return a default
        print("chore: initial commit")
        return
    
    new_msg = get_commit_type_and_message(original_msg)
    print(new_msg)

if __name__ == '__main__':
    main()
