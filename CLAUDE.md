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

## Toolkit entries are broad on purpose

An idea's score is the number of papers using it, so an entry only one paper could ever
match is worthless — it sits at score 1 for ever. Names are two or three words
(*stopping time selection*), not clauses describing what one paper did. Before adding
anything, read `data/toolkit.json` in full: the default outcome of a harvest is that
existing entries gain a paper, not that new ones appear. Widen an existing entry rather
than adding a sibling. Paper-specific detail belongs in `ideas-<paper>.md`, filed under
the broad entry's name.

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
The companion skills it calls — `grill-me`, `grilling`, `solve-math-rigorously`,
`wayfinder`, `latex-source-audit` — are vendored as plain copies under
`.claude/skills/`, so a fresh clone is self-contained and a collaborator needs no setup
beyond `sh tools/install.sh`. On this machine they are also installed user-wide at
`~/.claude/skills/<name>/SKILL.md` as symlinks to the Codex originals, so editing one
edits both; the vendored copies are snapshots and can drift. Re-vendor with
`cp -R ~/.codex/skills/<name>/. .claude/skills/<name>/`.
It reads `blueprints/article-blueprint.md`, then `blueprints/idea-blueprint.md`, and
stops to ask between them.

Papers live in `<year>/<slug>/`, year as the parent directory, slug = the paper's `id`
with the leading year stripped. The expansion must be named `<name>-expanded.tex`.

## Mathematical work

Everything under Blueprint A is governed by `solve-math-rigorously`: status is `PROVED`,
`PARTIAL` or `OPEN-GAP`, and it is never promoted. A step that cannot be closed is a
`caution` block in the PDF and an `OPEN-GAP` row in the ledger — visible, not smoothed
over. (On the maintainer's machine there is a further `AGENTS.math.md` one directory up,
outside this repository; nothing here depends on it.)

## Running it locally

`sh tools/install.sh` once, then `Bourgain.local` from anywhere. Both it and
`tools/serve.sh` go through `tools/serve.py`, which sends `Cache-Control: no-store`:
the data files are rewritten in place at a URL that never changes, so without it a
rebuild stays invisible behind the browser cache. That has cost us an hour once. The launcher resolves
the repository from its own symlink, picks the first free port at or after 8017, reuses
a server it already started, and never adopts or kills an unrelated one. Detaching the
server's descriptors matters: without `</dev/null >/dev/null 2>&1` a pipeline such as
`Bourgain.local | tee log` hangs, because the child holds the pipe open.

## The site

Static, no build step. `sh tools/serve.sh` (repo root is the
document root, so the site is at `/site/` and a paper's digestion under
`<year>/<slug>/` resolves) or open `site/index.html`
directly — data ships as JS globals precisely so `file://` works. Titles carry raw TeX
from zbMATH; `BP.tex()` in `site/assets/app.js` transliterates it to Unicode. If a TeX
command shows up raw on the page, add it to the `SYMBOLS` map there.

**Two rendering paths, and they must not be crossed.**

| source | delimiters | renderer | why |
|---|---|---|---|
| zbMATH titles and references | none | `BP.tex()` → Unicode | the TeX arrives undelimited, so there is no way to tell which fragment is mathematics without parsing it |
| our own prose — summaries, glosses, problems | `$…$`, `\[…\]` | `BP.rich()` + KaTeX | we write it, so we delimit it |

`BP.rich()` escapes, converts `\emph{}`/`\textbf{}` to tags, and leaves the TeX alone
for KaTeX. It must **never** call `BP.tex()`: the transliterator would rewrite `\pi` and
swallow the braces, leaving KaTeX nothing to render. Call `BP.math(el)` after any
`innerHTML` write that can contain our prose.

KaTeX is vendored under `site/vendor/katex/` — woff2 fonts only, with the ttf/woff
sources stripped from the CSS so nothing 404s. It is the site's one dependency and it is
local on purpose: nothing is ever fetched from a network, so the site works offline and
in a sealed environment. All paths are relative, so `file://` loads the script and the
CSS; note only that some browsers refuse webfonts from a `file://` opaque origin, in
which case the formulas still typeset but in fallback faces. Serving through
`tools/serve.sh` avoids that, and is the intended way to read the site anyway. If KaTeX
does not load at all, the formulas degrade to readable TeX source plus a console
warning — never to a blank page.

## Weekly upkeep

```sh
python3 tools/refresh_citations.py     # OpenAlex counts + a report of what moved
```

Citation counts are the only thing that changes on its own. `--full` also looks for new
papers; `--dry` reports without writing.
