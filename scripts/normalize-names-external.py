#!/usr/bin/env python3
"""
normalize-names-external.py

Scan the repository for workflow JSON files and rename them based on an external metadata file.
This approach does NOT modify the JSON workflow files themselves.

Usage:
    python3 scripts/normalize-names-external.py
    python3 scripts/normalize-names-external.py --apply
    python3 scripts/normalize-names-external.py --metadata scripts/workflow-metadata.yaml

The metadata file should be in YAML format with the following structure:
    workflows:
      original_filename.json:
        tool: ToolName
        purpose: purpose-description
        version: "1.0"
"""

import argparse
import os
import re
import shutil
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    exit(1)

ROOT = Path(__file__).resolve().parents[1]
JSON_EXT = '.json'


def load_metadata(metadata_path: Path):
    """Load workflow metadata from YAML file."""
    try:
        with metadata_path.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data.get('workflows', {})
    except Exception as e:
        print(f"Error loading metadata file: {e}")
        return {}


def major_from_version(version: str):
    """Extract major version number from version string."""
    if not version:
        return None
    m = re.match(r"(\d+)", str(version))
    return m.group(1) if m else None


def canonical_name(tool: str, purpose: str, major: str):
    """Generate canonical filename: {tool}--{purpose}--v{major}.json"""
    def clean(s):
        return re.sub(r"[^A-Za-z0-9._-]", "-", s).strip('-')
    
    return f"{clean(tool)}--{clean(purpose)}--v{major}{JSON_EXT}"


def find_json_files(root: Path):
    """Find all JSON files in the repository, excluding common directories."""
    for p in root.rglob('*.json'):
        if any(part in ('node_modules', '.git', 'scripts') for part in p.parts):
            continue
        yield p


def main():
    parser = argparse.ArgumentParser(
        description='Normalize workflow JSON filenames using external metadata'
    )
    parser.add_argument('--apply', action='store_true', 
                       help='Apply renames and update references')
    parser.add_argument('--root', default=str(ROOT), 
                       help='Repository root (defaults to script parent)')
    parser.add_argument('--metadata', default=str(ROOT / 'scripts' / 'workflow-metadata.yaml'),
                       help='Path to metadata YAML file')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    metadata_path = Path(args.metadata).resolve()
    
    if not metadata_path.exists():
        print(f"Error: Metadata file not found: {metadata_path}")
        print("Create a workflow-metadata.yaml file with workflow metadata.")
        return
    
    metadata = load_metadata(metadata_path)
    if not metadata:
        print("No metadata found in the metadata file.")
        return
    
    proposals = []
    
    for p in find_json_files(root):
        filename = p.name
        
        # Check if this file has metadata
        if filename not in metadata:
            if args.verbose:
                print(f"Skipping (no metadata entry): {p}")
            continue
        
        meta = metadata[filename]
        tool = meta.get('tool')
        purpose = meta.get('purpose')
        version = meta.get('version')
        
        if not (tool and purpose and version):
            if args.verbose:
                print(f"Skipping (incomplete metadata): {filename}")
            continue
        
        major = major_from_version(version)
        if not major:
            if args.verbose:
                print(f"Skipping (invalid version): {filename}")
            continue
        
        newname = canonical_name(tool, purpose, major)
        newpath = p.with_name(newname)
        
        if p.name == newname:
            if args.verbose:
                print(f"Already canonical: {p.name}")
            continue
        
        proposals.append({'from': p, 'to': newpath, 'original': filename})
    
    if not proposals:
        print('No files proposed for renaming.')
        return
    
    print('Proposed renames:')
    for pr in proposals:
        print(f" - {pr['from'].relative_to(root)} -> {pr['to'].relative_to(root)}")
    
    if not args.apply:
        print('\nPreview mode. Use --apply to perform renames and update references.')
        return
    
    # Apply renames
    applied = []
    for pr in proposals:
        src = pr['from']
        dst = pr['to']
        
        if dst.exists():
            print(f"Skipping rename because destination exists: {dst}")
            continue
        
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            applied.append({'old': src, 'new': dst})
            print(f"Renamed: {src.relative_to(root)} -> {dst.relative_to(root)}")
        except Exception as e:
            print(f"Failed to rename {src}: {e}")
    
    # Update references in .md and .json files
    if applied:
        text_file_patterns = ['*.md', '*.json']
        updated_files = 0
        
        for pattern in text_file_patterns:
            for text_path in root.rglob(pattern):
                if any(part in ('node_modules', '.git') for part in text_path.parts):
                    continue
                
                try:
                    content = text_path.read_text(encoding='utf-8', errors='ignore')
                    original = content
                    
                    for a in applied:
                        old_rel = os.path.relpath(a['old'], start=root).replace(os.sep, '/')
                        new_rel = os.path.relpath(a['new'], start=root).replace(os.sep, '/')
                        content = content.replace(old_rel, new_rel)
                        content = content.replace(a['old'].name, a['new'].name)
                    
                    if content != original:
                        backup = text_path.with_suffix(text_path.suffix + '.bak')
                        shutil.copy2(text_path, backup)
                        text_path.write_text(content, encoding='utf-8')
                        updated_files += 1
                        print(f"Updated references in: {text_path.relative_to(root)}")
                except Exception as e:
                    if args.verbose:
                        print(f"Error processing {text_path}: {e}")
        
        print(f"\nSummary: renamed {len(applied)} file(s), updated references in {updated_files} file(s).")
    else:
        print('No renames were applied.')


if __name__ == '__main__':
    main()
