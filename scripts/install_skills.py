#!/usr/bin/env python3
"""Copy selected skills without overwriting existing installations."""

import argparse
from pathlib import Path
import re
import shutil


def install(source, destination, names, *, apply=False):
    source = Path(source).resolve()
    destination = Path(destination).expanduser().resolve()
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        raise ValueError('Source and destination must not overlap')
    if not names or len(names) != len(set(names)):
        raise ValueError('Select one or more unique skill names')
    plan = []
    for name in names:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError(f'Invalid skill name: {name}')
        origin = source / name
        if origin.is_symlink() or not (origin / 'SKILL.md').is_file():
            raise ValueError(f'Unknown skill or symlink: {name}')
        if any(p.is_symlink() for p in origin.rglob('*')):
            raise ValueError(f'Symlink inside skill: {name}')
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError(f'Already exists; left unchanged: {target}')
        plan.append((origin, target))
    if apply:
        destination.mkdir(parents=True, exist_ok=True)
        for origin, target in plan:
            shutil.copytree(origin, target)
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, type=Path, help='Agent skill directory in your target project')
    parser.add_argument('--skills', nargs='+', required=True, help='Skill folder names, or all')
    parser.add_argument('--apply', action='store_true', help='Copy files; default is a preview')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'skills'
    names = sorted(p.name for p in source.iterdir() if p.is_dir()) if args.skills == ['all'] else args.skills
    try:
        plan = install(source, args.dest, names, apply=args.apply)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')
    for origin, target in plan:
        print(f'{"Copied" if args.apply else "Would copy"} {origin.name} → {target}')
    if not args.apply:
        print('Preview only. Add --apply to copy.')


if __name__ == '__main__':
    main()
