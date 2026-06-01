#!/usr/bin/env python3
"""Apply HnS-FR mechanical conventions to one or more .inc text files.

Transformations (only inside .string "..." content, macros {...} preserved):
- POKé<CAPS>  → Poké<lowercase>          (POKéMON → Pokémon, POKéDEX → Pokédex…)
- OE/oe + u/i → Œ/œ                      (OEUF → Œuf, coeur → cœur, oeil → œil…)
- WORD ≥ 3 letters ALL-CAPS → Title Case (CHAMPION → Champion, BOURG → Bourg…)
- French cognates already in source get their missing accents and proper case
  (DEFENSE → Défense, SPECIAL → Spécial, DEF → Déf, SPE → Spé, ATQ. SPE. → Atq. Spé., …)
- Short connectors (de/du/des/la/le/les/en/et) lowercased mid-title
  (TOUR DE COMBAT → Tour de Combat, ZONE DE LA RÉCOMPENSE → Zone de la Récompense…)
  — left untouched at start of a sentence/string.
- Add a regular space before ! ? : ;     (French typography)

The script does NOT translate English terms (ATTACK, SPEED, SP. ATK, etc.) — only
fixes typography on what is already French.

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
# OE/oe ligature: only before u/i (the typical French context: œuf, cœur, sœur,
# vœu, nœud, œil…). Lookahead protects coexister, moelle, Goethe, etc.
OE_PATTERN      = re.compile(r'(OE|Oe|oe)(?=[UuIi])')
# Short connectors lowercased only when preceded by another word + space (i.e.
# mid-sentence / mid-title). Lookbehind \w\s preserves sentence-start cases.
# Matches both ALL-CAPS leftovers (DE, DU, LA, LE, EN, ET) and Title-Cased
# forms produced by ALLCAPS_PATTERN (Des, Les).
SHORT_CONN_PATTERN = re.compile(r'(?<=\w\s)\b(DE|DU|DES|LA|LE|LES|EN|ET|Des|Les)\b')
LINE_RE         = re.compile(r'^(\s*\.string\s+")(.*?)("\s*)$', re.DOTALL)

# Accent/typography fixes for French cognates already present in the source.
# Each pattern only matches a term that is already French (DEFENSE = same letters
# as Défense). English-only terms (ATTACK, SPEED, SP. ATK…) are deliberately left
# alone — the script is not a translator.
# Ordered: longest/most-specific patterns first.
STAT_REPLACEMENTS = [
    # Multi-word forms
    (re.compile(r'\bDEF\.\s*SPE\.'), 'Déf. Spé.'),
    (re.compile(r'\bATQ\.\s*SPE\.'), 'Atq. Spé.'),
    # Full cognates (same letters in EN/FR, only accents/casing differ)
    (re.compile(r'\bDEFENSE\b'),     'Défense'),
    (re.compile(r'\bSPECIAL\b'),     'Spécial'),
    # 3-letter FR abbreviations missing their accent
    (re.compile(r'\bDEF\b'),         'Déf'),
    (re.compile(r'\bSPE\b'),         'Spé'),
]


def to_proper(m):
    w = m.group(0)
    return w[0] + w[1:].lower()


def fix_poke(m):
    return "Poké" + m.group(1).lower()


def fix_oe(m):
    # Use Œ if the original matched group starts with uppercase, else œ
    return 'Œ' if m.group(0)[0].isupper() else 'œ'


def transform_content(content: str) -> str:
    # Split into segments: macros preserved, rest transformed
    parts = re.split(r'(\{[^}]+\})', content)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(p)
        else:
            for pattern, replacement in STAT_REPLACEMENTS:
                p = pattern.sub(replacement, p)
            p = POKE_PATTERN.sub(fix_poke, p)
            p = OE_PATTERN.sub(fix_oe, p)
            p = ALLCAPS_PATTERN.sub(to_proper, p)
            p = SHORT_CONN_PATTERN.sub(lambda m: m.group(0).lower(), p)
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