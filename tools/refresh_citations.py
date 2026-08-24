#!/usr/bin/env python3
"""Weekly citation refresh.

    python3 tools/refresh_citations.py

Re-fetches OpenAlex (the only source whose numbers move), rebuilds the dataset,
and prints what changed.  Everything hand-written -- summaries, digestion links,
toolkit tags, collaborator bios -- is preserved by the builder.

    --full   also re-fetch zbMATH and arXiv, i.e. look for new papers too.
    --dry    report what would change without writing the new counts.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(HERE, "data", "papers.json")
RAW = os.path.join(HERE, "data", "raw")


def snapshot():
    if not os.path.exists(PAPERS):
        return {}, None
    with open(PAPERS, encoding="utf-8") as fh:
        d = json.load(fh)
    return {p["id"]: (p["title"], p.get("cited_by")) for p in d["papers"]}, d.get("citations_updated")


def run(*args):
    print(f"$ {' '.join(args)}")
    subprocess.run([sys.executable, *args], cwd=HERE, check=True)


def main():
    full = "--full" in sys.argv
    dry = "--dry" in sys.argv

    before, stamp_before = snapshot()
    print(f"previous citation snapshot: {stamp_before or 'none'} "
          f"({len(before)} papers, {sum(v[1] or 0 for v in before.values()):,} citations)\n")

    backups = {}
    if dry:
        import shutil, tempfile
        for path in [PAPERS] + [os.path.join(RAW, f) for f in os.listdir(RAW)]:
            if os.path.exists(path):
                backups[path] = tempfile.mkstemp(suffix=".json")[1]
                shutil.copy(path, backups[path])

    sources = ["zbmath", "openalex", "arxiv"] if full else ["openalex"]
    run("tools/fetch_sources.py", *sources)
    run("tools/build_data.py")

    after, stamp_after = snapshot()
    print()

    gained = []
    for pid, (title, cites) in after.items():
        old = before.get(pid, (None, None))[1]
        if old is None or cites is None:
            continue
        if cites != old:
            gained.append((cites - old, cites, title))
    gained.sort(reverse=True)

    new_ids = set(after) - set(before)
    gone = set(before) - set(after)

    total_before = sum(v[1] or 0 for v in before.values())
    total_after = sum(v[1] or 0 for v in after.values())
    print(f"citations: {total_before:,} -> {total_after:,}  "
          f"({total_after - total_before:+,} since {stamp_before or 'the first build'})")
    print(f"papers:    {len(before)} -> {len(after)}"
          + (f"  (+{len(new_ids)} new, -{len(gone)} dropped)" if new_ids or gone else ""))

    if gained:
        print(f"\ntop movers ({len(gained)} papers changed):")
        for delta, now, title in gained[:15]:
            print(f"  {delta:+5d} -> {now:6,}   {title[:72]}")
    if new_ids:
        print("\nnew in the bibliography:")
        for pid in sorted(new_ids):
            print(f"  {after[pid][0][:80]}   ({pid})")
    if gone:
        print("\nno longer matched (check before assuming these are gone):")
        for pid in sorted(gone):
            print(f"  {before[pid][0][:80]}   ({pid})")

    if dry:
        import shutil
        for path, backup in backups.items():
            shutil.copy(backup, path)
            os.unlink(backup)
        run("tools/build_data.py")
        print("\n--dry: raw dumps and counts restored to their previous state")


if __name__ == "__main__":
    main()
