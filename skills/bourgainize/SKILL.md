---
name: bourgainize
description: Add one paper by Jean Bourgain to the Bourgain-pedia — locate and download it, expand it into a version where no step is omitted, then harvest the ideas and techniques it runs on into the toolkit. Use when the user says $bourgainize or /bourgainize, or asks to digest, expand, or add a Bourgain article to the encyclopedia.
---

# bourgainize

One paper, start to finish: **choose → download → expand → confirm → harvest**.

This skill runs inside the Bourgain-pedia repository. Everything it writes lands under
`<year>/<slug>/`, and the site picks it up on the next `tools/build_data.py`.

Two long-running stages sit inside it, and both are governed by files in this repo, not
by this one:

- `blueprints/article-blueprint.md` — how to expand a paper.
- `blueprints/idea-blueprint.md` — how to harvest its ideas.

Read the relevant blueprint in full before starting its stage. Do not work from your
memory of it.

## Host note: the three companion skills

Stage 3 leans on three skills. Both hosts have them under the same names:

| Codex | Claude Code | What it is for here |
|---|---|---|
| `$solve-math-rigorously` | `/solve-math-rigorously` | Every reconstructed step. Status discipline: `PROVED` / `PARTIAL` / `OPEN-GAP`, never promoted. |
| `$grill-me` | `/grill-me` | Checkpointing the user on any genuine mathematical choice, one question at a time. |
| `$wayfinder` | `/wayfinder` | Long papers: chart the expansion as decision tickets and work them one at a time. |

The Codex originals are in `~/.codex/skills/`. For Claude Code they are installed
user-wide at `~/.claude/skills/<name>/SKILL.md`, each a symlink to the Codex file so the
two hosts can never drift, and mirrored as plain copies in this repository's
`.claude/skills/` so the project is self-contained if it moves to another machine. If a
host is missing one, follow its written procedure inline rather than skipping it, and say
in `notes.md` that it ran unassisted.

---

## Stage 1 — choose the paper

Ask the user which article to add. Ask once, plainly, and offer help choosing:

> Which Bourgain paper should I add? Give me a title, a year, a Zbl or arXiv number, or
> a DOI — or say "suggest" and I will propose a few.

If they say *suggest*, read `data/papers.json` and offer a short menu drawn from what is
actually there: the most-cited papers not yet digested, the earliest not yet digested,
and anything whose `toolkit` array is empty in a year that is otherwise well covered.
Show reference and citation count for each. Do not invent candidates.

Resolve their answer against `data/papers.json`. Match on `id`, `zbl`, `doi`, `arxiv`,
or a title search. Then confirm the exact entry back to them — title, full reference,
year, citation count — and get a yes before proceeding. Bourgain has papers with nearly
identical titles a decade apart; the wrong one is a very expensive mistake.

If the paper is not in `data/papers.json`, stop and say so. Either the bibliography
needs a rebuild (`tools/fetch_sources.py` then `tools/build_data.py`) or the item is not
his. Do not create an entry by hand to get past this.

## Stage 2 — download it

Create the working directory. The **year is the parent**:

```
<year>/<slug>/          e.g. 1998/refinements-of-strichartz-inequality/
```

`<slug>` is the paper's `id` from `data/papers.json` with the leading year stripped.

Fetch the paper, trying in this order:

1. **arXiv e-print source** (`https://arxiv.org/e-print/<id>`) — a real TeX source is
   worth far more than a PDF, and the expansion should be built on it.
2. arXiv PDF.
3. The open-access PDF or landing page in the entry's `links`.
4. NUMDAM / EuDML / Project Euclid / EMIS — these cover most of the early French and
   Belgian papers.
5. DOI, last, since it is usually paywalled.

Save as `<name>.pdf` (and `<name>-source.tar.gz`, unpacked, if TeX was available), where
`<name>` is the slug.

If nothing downloads, tell the user exactly which links you tried and what each returned,
and ask them to supply a copy. Do not proceed on an abstract, a review, or your own
recollection of the paper. Do not circumvent a paywall.

Write `notes.md` with the reference, the source used, and the date.

## Stage 3 — expand it

Read `blueprints/article-blueprint.md` now, in full, and follow it. The short form of
its six rules, as a reminder and not as a substitute:

1. When in doubt, expand.
2. Stick to his argument; no substituted proofs, no modernisation in the body.
3. New notation is fine, declared and attributed.
4. Strictly longer than the original.
5. No computation of his omitted.
6. Every omitted argument supplied.

How the companion skills fit into the blueprint's passes:

- Build the **ledger** first. It is the definition of done.
- Run every reconstruction under `solve-math-rigorously`. A step you cannot close is
  recorded as `OPEN-GAP` in the ledger and as a `caution` in the TeX. It is never
  written up as though it were proved.
- On a long or difficult paper, open the expansion with `wayfinder`: the destination is
  the finished digestion, and each hard lemma is a ticket.
- When a real mathematical choice appears — the paper admits two readings, a constant
  does not come out as printed, a cited theorem's hypotheses do not visibly apply —
  stop and use `grill-me`. Ask one question. Do not silently pick a branch.

The blueprint's passes are iterative on purpose. Expect several sweeps; the adversarial
pass in particular is run until it produces nothing.

The result is:

```
<year>/<slug>/<name>-expanded.tex        <- required name: original filename + "-expanded"
<year>/<slug>/<name>-expanded.pdf
<year>/<slug>/ledger.md
<year>/<slug>/notes.md
```

Compile it. Report the page counts, original versus expansion, and any `caution` blocks
that survived.

## Stage 4 — stop and ask

The expansion is a natural stopping point, and harvesting is a separate piece of work.
Show the user:

- where the files are;
- original and expanded page counts;
- the ledger tally: rows closed, rows left `OPEN-GAP`, with the open ones listed;
- anything that surprised you in the paper.

Then ask:

> The expansion is in place. Continue to the idea harvest (Blueprint B)?

**Wait for an explicit yes.** If they say no, or want changes first, stop here — the
expansion stands on its own, and the harvest can be resumed later by invoking this skill
again on the same paper.

## Stage 5 — harvest the ideas

On yes, read `blueprints/idea-blueprint.md` in full and follow it: total harvest line by
line, then two or three pruning passes, then reconciliation against the toolkit.

Write the result to:

```
<year>/<slug>/ideas-<name>.md
```

Then wire it up:

1. Add new ideas to `data/toolkit.json`, or extend the gloss of existing ones.
2. Add the idea ids to this paper's `toolkit` array in `data/papers.json`.
3. Add every question the paper leaves open to `data/problems.json`, each with the
   paper it came from, the year, what the paper itself settles, and a `status` list
   of the two or three most noteworthy articles making progress on it — full
   references, links, and a `verified_from` naming the bibliographic source you
   queried. `read: false` unless someone here has actually read the article.
4. Set the paper's `digestion` field to the path of the expanded PDF.
5. Write the paper's `summary` — three or four sentences, our précis, **not** the
   abstract: what it proves, what the difficulty was, and what the paper introduced that
   outlived it.
6. Run `python3 tools/build_data.py`. Scores recompute from the papers that cite each
   idea; the summary, digestion link and toolkit tags appear on the site.

Never edit an idea's `score` by hand. It is derived.

## Finish

Report:

- the paper, with its reference;
- expanded page count against the original;
- ideas harvested, split into new and existing, with the new ones' names;
- open problems added, and for each the status you were able to verify;
- any `OPEN-GAP` rows still standing;
- what the next reader should look at — usually the paper this one leans on hardest.

Then offer the obvious next step: the neighbouring paper in the same line of work, or
another paper that uses one of the ideas just added.

## Standing rules

- **One paper per invocation.** If the user names several, do the first and ask.
- **Nothing gets asserted that was not read.** No expansion from an abstract, a review,
  or memory of a famous theorem.
- **Gaps stay visible.** A `caution` in the PDF, an `OPEN-GAP` in the ledger, and a
  sentence in the final report. Never a smoothed-over paragraph.
- **His argument, not a better one.** Improvements go in the closing remarks section,
  labelled as later than the paper.
- **Ask before overwriting.** If `<year>/<slug>/` already exists with an expansion in
  it, show the user what is there before touching it.
