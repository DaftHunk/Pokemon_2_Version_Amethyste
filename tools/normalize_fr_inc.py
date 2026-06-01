#!/usr/bin/env python3
"""Apply HnS-FR mechanical conventions to one or more .inc text files.

Transformations (only inside .string "..." content, macros {...} preserved):
- POKé<CAPS>  → Poké<lowercase>          (POKéMON → Pokémon, POKéDEX → Pokédex…)
- WORD ≥ 3 letters ALL-CAPS → Title Case (CHAMPION → Champion, BOURG → Bourg…)
- Add a regular space before ! ? : ;     (French typography)

Usage:
    tools/normalize_fr_inc.py data/text/foo.inc [data/text/bar.inc ...]
    tools/normalize_fr_inc.py --no-backup data/text/foo.inc
    tools/normalize_fr_inc.py --dry-run data/text/foo.inc
"""
import argparse
import re
import shutil
import sys

POKE_PATTERN    = re.compile(r'POKé([A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŒ]+)')
ALLCAPS_PATTERN = re.compile(r'\b[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŒ]{3,}\b')
PUNCT_PATTERN   = re.compile(r'(?<=[^\s\\!?:;])([!?:;])')
LINE_RE         = re.compile(r'^(\s*\.string\s+")(.*?)("\s*)$', re.DOTALL)


def to_proper(m):
    w = m.group(0)
    return w[0] + w[1:].lower()


def fix_poke(m):
    return "Poké" + m.group(1).lower()


def transform_content(content: str) -> str:
    # Split into segments: macros preserved, rest transformed
    parts = re.split(r'(\{[^}]+\})', content)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(p)
        else:
            p = POKE_PATTERN.sub(fix_poke, p)
            p = ALLCAPS_PATTERN.sub(to_proper, p)
            p = PUNCT_PATTERN.sub(r' \1', p)
            out.append(p)
    return ''.join(out)


def transform_line(line: str) -> str:
    m = LINE_RE.match(line)
    if not m:
        return line
    prefix, content, suffix = m.groups()
    return prefix + transform_content(content) + suffix


def process_file(path: str, backup: bool, dry_run: bool) -> tuple[int, int]:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = [transform_line(line) for line in lines]
    changed = sum(1 for a, b in zip(lines, new_lines) if a != b)

    if dry_run or changed == 0:
        return changed, len(lines)

    if backup:
        shutil.copy(path, path + ".bak")

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    return changed, len(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs='+', help=".inc files to normalize")
    ap.add_argument("--no-backup", action='store_true', help="don't create .bak file before writing")
    ap.add_argument("--dry-run", action='store_true', help="report changes without writing")
    args = ap.parse_args()

    total_changed = 0
    for path in args.files:
        try:
            changed, total = process_file(path, backup=not args.no_backup, dry_run=args.dry_run)
        except FileNotFoundError:
            print(f"[SKIP] {path} : fichier introuvable", file=sys.stderr)
            continue
        tag = "[dry]" if args.dry_run else ("[mod]" if changed else "[ok ]")
        print(f"{tag} {path} : {changed}/{total} ligne(s) modifiée(s)")
        total_changed += changed

    if args.dry_run:
        print(f"\nDry-run terminé. Total changements potentiels : {total_changed}")


if __name__ == "__main__":
    main()