# Bourgain-pedia

An encyclopedia of the work of **Jean Bourgain** (1954–2018): every paper he wrote,
listed by year; each one digested into a version where nothing is left to the reader;
and the ideas those papers run on, collected into a shared toolkit.

The bibliography is the easy part. The project is the reading.

---

## Getting started

```sh
git clone https://github.com/joaopgramos95/Bourgain-pedia.git
cd Bourgain-pedia
sh tools/install.sh
Bourgain.local
```

That is the whole setup. `install.sh` puts a link to `tools/bourgain-local.sh` on your
PATH; `Bourgain.local` then serves *your* clone and opens the site in your browser,
from any directory.

```sh
Bourgain.local          # serve and open (reuses a running server)
Bourgain.local status   # is it running, and where
Bourgain.local stop     # stop it
Bourgain.local -p 9000  # force a port
```

If port 8017 is busy — including by something unrelated — the next free port is used
automatically, and nothing else on your machine is disturbed. The link points back into
the clone, so `git pull` updates the command too.

**Requirements:** `python3` and a browser. Nothing else, no build step, no package
manager. To rebuild the dataset or compile a digestion you also want a LaTeX
distribution.

> Why one command rather than none: git has no post-clone hook, by design — cloning a
> repository must never execute code from it. One command after cloning is as close to
> automatic as it can safely get. If you would rather not install anything, `sh
> tools/serve.sh` does the same thing without touching your PATH.

## What is here

```
Papers/            one Markdown file per year: numbered, referenced, with download links
data/              the canonical dataset (papers, collaborators, toolkit, problems)
site/              the website — static, no build step, no dependencies
blueprints/        the two procedures the project runs on
skills/            the $bourgainize skill, shared by Codex and Claude Code
.claude/skills/    the companion skills it calls, vendored so a clone is self-contained
tools/             install, serve, fetch, merge, enrich, refresh
<year>/<slug>/     one directory per digested paper (created by $bourgainize)
```

`data/raw/` (the source dumps) and the paper PDFs are deliberately not tracked — see
*Honest blanks* below. Everything the site needs is committed, so a fresh clone renders
immediately.

## The website

```sh
Bourgain.local             # see "Getting started" above
sh tools/serve.sh          # or by hand, without installing anything
```

The document root is the repository, not `site/`, so that a paper's digestion under
`<year>/<slug>/` resolves.

or just open `site/index.html` — the data ships as JS globals, so it works off the
filesystem too.

| Page | What it is |
|---|---|
| **All articles** | The whole bibliography by year. Each entry: full reference, citation count, download links, and two slots we fill in — a **summary** (our précis, not the abstract) and a **digestion** (the expanded paper). |
| **Bourgain's toolkit** | Ideas and techniques, from *orthogonality* and *stopping time* up to *sparseness* and *large deviations*. Each has a name, our explanation, and a **score** — the number of papers using it. Scaffolding only for now; entries arrive by reading. |
| **Collaborators** | Everyone who wrote a paper with him, A–Z, with dates, affiliation, and a **collaborator score**. |
| **Open problems** | Questions the papers leave open, by field. Each carries the source, the year, what that paper settles, and a **Status** list: the two or three most noteworthy articles making progress, with verified references and a flag saying whether we have read them. |
| **Method** | The blueprints, and what is ours versus what is not. |

## Adding a paper

In Codex:

```
$bourgainize
```

In Claude Code:

```
/bourgainize
```

It asks which paper, downloads it into `<year>/<slug>/`, expands it under
**Blueprint A** into `<name>-expanded.tex`, stops and asks whether to continue, and then
harvests the ideas under **Blueprint B** into `ideas-<name>.md`.

The two blueprints are `blueprints/article-blueprint.md` and
`blueprints/idea-blueprint.md`. They are the substance of the project; the skill is only
the thing that runs them in order.

### Blueprint A in one breath

His paper at full length, not a survey of it and not a better proof.

1. When in doubt, expand.
2. Do not deviate from the line of work in the article; stick to his arguments.
3. Introducing notation to explain the article is fine.
4. The expansion is strictly larger than the original.
5. No computation in the original is omitted from the new one.
6. Arguments left out of the original are explained in the new one.

Rule 6 does the work: every *one checks easily*, *standard argument*, *similarly* is a
hole, logged in a ledger, and filled with a proof. What cannot be closed is marked
`OPEN-GAP` and stays visible.

### Blueprint B in one breath

Read the **expansion**, line by line. Harvest every move with a keyword (80–200 rows is
normal). Discard the routine — triangle inequality, Cauchy–Schwarz, Fubini — unless the
*way* it is used was a choice. Prune again, twice or three times, until a sweep changes
nothing. Then reconcile with `data/toolkit.json`.

## Keeping it current

```sh
python3 tools/refresh_citations.py        # weekly: new OpenAlex counts + what moved
python3 tools/refresh_citations.py --full # also look for new papers
python3 tools/refresh_citations.py --dry  # report without writing
```

Citation counts move; the rest does not. The footer of every page shows when they were
last refreshed. Rebuilding never destroys hand-written work: summaries, digestion links,
toolkit tags and collaborator bios are carried across.

`data/raw/` is git-ignored: it is regenerable in about a minute and changes every week.
Full rebuild from scratch:

```sh
python3 tools/fetch_sources.py            # zbMATH + OpenAlex + arXiv -> data/raw/
python3 tools/build_data.py               # merge -> data/, site/data/, Papers/<year>.md
python3 tools/enrich_collaborators.py     # Wikidata: dates, affiliations
python3 tools/enrich_collaborators.py --fallback   # second pass via the search API
```

## Where the bibliography comes from

- **zbMATH Open** — the spine. A disambiguated mathematical bibliography, complete back
  to 1976, and the only source that carries the early French and Belgian seminar papers.
- **OpenAlex** — citation counts, DOIs, open-access copies.
- **arXiv** — preprints and their PDFs.

Matching is on DOI first, then on a normalised title (accents, LaTeX and punctuation
stripped) within a ±3-year window, then on token containment for OCR-mangled titles. A
short curated map in `tools/build_data.py` handles what automation cannot see —
translations, chapter-level records of his own monographs, one non-mathematician
namesake — and each entry there says why.

Two things this means in practice:

- A blank citation count means *not indexed by OpenAlex*, not *never cited*. Coverage of
  the pre-1990 literature is poor.
- Counts are not comparable across decades.

## Honest blanks

Where something is not known, the field is empty and the site says so.

Collaborator dates and affiliations come from Wikidata, and a candidate is accepted only
if it survives three checks: whole-word name matching (without it, *Sato* matches
*Satoshi*), a plausible academic occupation, and — the one that does the real work — the
collaboration itself. A person must have been born at least eighteen years before the
first joint paper and not have died before it. That test alone removed a Gromov who died
in 1985 and three birth years later than the papers they were attached to. Where two
people remain plausible for an initials-only byline, the entry stays blank; a handful of
known-wrong matches are listed in `BLOCKED` in `tools/enrich_collaborators.py`, each with
the paper that settles which person it is.

The affiliation shown is the most recently *started* one Wikidata records, which is not
always the current one — Wikidata often lacks start dates for recent posts. Where the two
disagree, the hand-written biography is the one we checked.

Summaries and digestions are blank until someone does the reading.

## What is ours

Ours: the summaries, the digestions, the toolkit and its glosses, the collaborator prose.

Not ours: bibliographic records, citation counts, and the papers. Links point at
publishers, arXiv and repositories; no copyrighted full text is redistributed here.
