# Bourgain-pedia — working notes for agents

An encyclopedia of Jean Bourgain's work: the complete bibliography, each paper expanded
into a version where nothing is omitted, and the ideas those papers run on collected into
a toolkit. Read `README.md` first for the shape of the repository.

## The one rule

**Nothing is asserted that was not read.** No summary written from an abstract, no
digestion written from memory of a famous theorem, no idea added to the toolkit that was
not found in an expansion of an actual paper. Where something is not known, the field
stays empty — an honest blank is a feature of this project, not a gap to be papered over.

## Generated vs. hand-written

`tools/build_data.py` regenerates almost everything. It **carries editorial fields
across rebuilds** — `summary`, `digestion`, `toolkit`, `notes` in `data/papers.json`, and
`data/collaborator_bios.json` — so rebuilding is always safe. Everything else in those
files is derived and will be overwritten.

| File | Written by |
|---|---|
| `data/raw/*.json` | `tools/fetch_sources.py`. Never edit. |
| `data/papers.json` | the builder, except the four editorial fields |
| `data/collaborators.json` | the builder, from `coauthors` + `collaborator_bios.json` |
| `data/collaborator_bios.json` | Wikidata pass (dates, institution) + `merge_bios.py` (prose) |
| `data/collaborator_bios_manual.json` | by hand — prose only |
| `data/toolkit.json` | by hand, except `score` and `papers`, which are derived |
| `data/problems.json` | by hand; the builder only validates its cross-references |
| `site/data/*.js` | the builder. Never edit. |
| `Papers/<year>.md`, `Papers/INDEX.md` | the builder. Never edit. |

After touching anything in `data/`, run `python3 tools/build_data.py`.

## Open problems

`data/problems.json` follows the toolkit's rule: a problem is listed only because it
was found stated in a paper we digested. Each carries a `status` list of the two or
three most noteworthy articles making progress. Every such reference must be checked
against a bibliographic source and record `verified_from`; `read` is `false` unless
someone here has read the article, and when it is `false` the description must not
claim more than the title, abstract and venue support. `status_now` starts at
`unchecked` and only moves on evidence.

## Scores are derived, never typed

- A **collaborator score** is the number of papers whose `coauthors` contain that person.
- An **idea score** is the number of papers whose `toolkit` array contains that idea id.

If a score looks wrong, the paper list is wrong. Fix the list.

## Bibliography conventions

- **zbMATH is the spine.** When zbMATH and OpenAlex disagree on a year, a title or a
  reference, zbMATH wins.
- Matching is DOI → normalised title → token containment, within a ±3-year window.
  Duplicates the matcher cannot see live in two curated maps at the top of
  `tools/build_data.py`: `OPENALEX_EXCLUDE` (not this Bourgain) and
  `OPENALEX_DUPLICATE_OF` (a translation, an OCR-mangled title, or a chapter of one of
  his own monographs, keyed to the Zbl number of the item it duplicates). Add to those
  rather than special-casing inside the merge.
- A blank `cited_by` means *not indexed by OpenAlex*, not *never cited*. Do not fill it in
  from another source without saying so.
- Collaborator dates and affiliations come from Wikidata, and a candidate is rejected
  unless the person could have written the joint paper (born ≥ 18 years before it, not
  dead before it). Known-wrong matches go in `BLOCKED` in `tools/enrich_collaborators.py`
  with a comment saying which paper settles it.

## Adding a paper

Use the skill. `/bourgainize` in Claude Code, `$bourgainize` in Codex — one canonical
`skills/bourgainize/SKILL.md`, symlinked into `.claude/skills/` and `~/.codex/skills/`.
The three skills it leans on (`grill-me`, `solve-math-rigorously`, `wayfinder`) are
imported from Codex: `~/.claude/skills/<name>/SKILL.md` symlinks to the Codex original,
so editing one edits both. This repository also carries plain copies under
`.claude/skills/` so it stands alone if it moves.
It reads `blueprints/article-blueprint.md`, then `blueprints/idea-blueprint.md`, and
stops to ask between them.

Papers live in `<year>/<slug>/`, year as the parent directory, slug = the paper's `id`
with the leading year stripped. The expansion must be named `<name>-expanded.tex`.

## Mathematical work

Everything under Blueprint A is governed by `solve-math-rigorously`: status is `PROVED`,
`PARTIAL` or `OPEN-GAP`, and it is never promoted. A step that cannot be closed is a
`caution` block in the PDF and an `OPEN-GAP` row in the ledger — visible, not smoothed
over. See also `../AGENTS.math.md`.

## The site

Static, no build step, no dependencies. `sh tools/serve.sh` (repo root is the
document root, so the site is at `/site/` and a paper's digestion under
`<year>/<slug>/` resolves) or open `site/index.html`
directly — data ships as JS globals precisely so `file://` works. Titles carry raw TeX
from zbMATH; `BP.tex()` in `site/assets/app.js` transliterates it to Unicode rather than
loading a math renderer, so the site stays offline-capable. If a TeX command shows up raw
on the page, add it to the `SYMBOLS` map there.

## Weekly upkeep

```sh
python3 tools/refresh_citations.py     # OpenAlex counts + a report of what moved
```

Citation counts are the only thing that changes on its own. `--full` also looks for new
papers; `--dry` reports without writing.
