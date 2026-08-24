#!/usr/bin/env python3
"""Merge the hand-written prose from data/collaborator_bios_manual.json into
data/collaborator_bios.json, which also holds the Wikidata-derived dates and
affiliations.

Kept separate on purpose: the Wikidata pass rewrites collaborator_bios.json,
and the prose must survive that.  This script only ever fills the "bio" field.
"""
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "data")


def main():
    manual_path = os.path.join(DATA, "collaborator_bios_manual.json")
    bios_path = os.path.join(DATA, "collaborator_bios.json")
    roster_path = os.path.join(DATA, "collaborators.json")

    with open(manual_path, encoding="utf-8") as fh:
        manual = json.load(fh)["bios"]
    with open(bios_path, encoding="utf-8") as fh:
        bios = json.load(fh)
    with open(roster_path, encoding="utf-8") as fh:
        roster = {p["name"] for p in json.load(fh)["collaborators"]}

    written, unknown = 0, []
    for name, text in manual.items():
        if not text:
            continue
        if name not in roster:
            unknown.append(name)
            continue
        entry = bios.setdefault(name, {"born": "", "died": "", "institution": "", "bio": ""})
        if entry.get("bio") != text:
            entry["bio"] = text
            written += 1

    with open(bios_path, "w", encoding="utf-8") as fh:
        json.dump(bios, fh, ensure_ascii=False, indent=1, sort_keys=True)

    print(f"wrote {written} biographies into {bios_path}")
    if unknown:
        print(f"! {len(unknown)} name(s) in the manual file are not in the roster "
              f"(spelling drift?): {', '.join(unknown)}", file=sys.stderr)
    print("now run: python3 tools/build_data.py")


if __name__ == "__main__":
    main()
