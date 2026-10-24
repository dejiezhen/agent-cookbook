#!/usr/bin/env python3
"""Validate this library's skill manifests, UI metadata, and local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate_skill(folder):
    folder = Path(folder)
    errors = []
    manifest = folder / 'SKILL.md'
    if folder.is_symlink() or not manifest.is_file():
        return ['Missing SKILL.md or symlinked skill directory']
    match = re.match(r'\A---\n(.*?)\n---(?:\n|\Z)', manifest.read_text(encoding='utf-8'), re.S)
    if not match:
        return ['Missing YAML frontmatter']
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f'Invalid YAML: {exc}']
    if not isinstance(data, dict):
        return ['Frontmatter must be a mapping']
    name = data.get('name')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != folder.name:
        errors.append('Name must be lowercase hyphenated, at most 64 characters, and match its folder')
    description = data.get('description')
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append('Description must be a nonempty string of at most 1024 characters')
    if not manifest.read_text(encoding='utf-8')[match.end():].strip():
        errors.append('Instructions are empty')
    ui_path = folder / 'agents/openai.yaml'
    try:
        ui = yaml.safe_load(ui_path.read_text(encoding='utf-8'))
        interface = ui.get('interface', {}) if isinstance(ui, dict) else {}
        if not isinstance(interface, dict):
            errors.append('UI interface must be a mapping')
            interface = {}
        display = interface.get('display_name')
        short = interface.get('short_description')
        prompt = interface.get('default_prompt')
        if not isinstance(display, str) or not display.strip():
            errors.append('Missing interface.display_name')
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            errors.append('UI short description must have 25–64 characters')
        if not isinstance(prompt, str) or f'${name}' not in prompt:
            errors.append('UI default prompt must mention the skill as $name')
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f'Invalid agents/openai.yaml: {exc}')
    for path in folder.rglob('*'):
        if path.is_symlink():
            errors.append(f'Symlink is not distributable: {path.relative_to(folder)}')
            continue
        if path.suffix != '.md' or not path.is_file():
            continue
        for raw in re.findall(r'\[[^\]\n]*\]\(([^)\s]+)\)', path.read_text(encoding='utf-8')):
            url = urlsplit(raw.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(folder.resolve()) or not target.exists():
                errors.append(f'{path.relative_to(folder)}: missing or external local link {raw}')
    return errors


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'skills'
    folders = sorted(p for p in root.iterdir() if p.is_dir())
    if not folders:
        print('No skills found', file=sys.stderr)
        return 1
    failures = 0
    for folder in folders:
        errors = validate_skill(folder)
        failures += len(errors)
        for error in errors:
            print(f'{folder.name}: {error}', file=sys.stderr)
    print(f'Validated {len(folders)} skills; {failures} error(s).')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
