---
name: idea-blueprint
purpose: Harvest, from one expanded paper, the ideas and techniques it actually runs on.
consumes: <name>-expanded.tex, produced by blueprints/article-blueprint.md
produces: ideas-<name>.md  and a patch to data/toolkit.json
---

# Blueprint B — harvesting the ideas

Blueprint A produced a paper in which nothing is hidden. This blueprint reads that
paper and asks a single question of every line: *what move is being made here?*

The output is a list of named ideas and techniques. It is the unit of value of this
whole project — the digestion is a means, the toolkit is the end.

Do not run this on the original paper. Run it on the expansion. The point of the
expansion is that the moves Bourgain performed silently are now visible on the page,
and it is exactly those that this pass exists to catch.

## Pass 1 — total harvest

Go through `<name>-expanded.tex` **line by line**. Not section by section, not proof by
proof. Line by line.

At every step where something is *done* — an estimate begun, a decomposition chosen,
an object constructed, a case split made, a parameter fixed, a reduction performed —
write a row:

```
| keyword | line/eq | what is being done | what it buys |
```

- **keyword**: a short name for the move, three words at most. Invent one if the move
  has no standard name; a made-up name that describes the move is better than a
  standard name that does not.
- **what it buys**: the one thing the argument gains. If you cannot say what it buys,
  you have not understood the step — go back and read it again before writing the row.

Rules for this pass:

- **Over-collect.** Pass 1 is not the place for judgement. If in doubt, write the row.
  A pass-1 list for a twenty-page expansion typically has 80–200 rows.
- **Include the moves inside proofs of lemmas**, including lemmas Bourgain treats as
  routine. Some of his most reused tricks live in throwaway lemmas.
- **Include the moves that failed** if the paper shows them: a remark explaining why
  the obvious approach does not work is a genuine entry (keyword the obstruction).
- **Record the same move every time it recurs**, with its line number. Recurrence
  within one paper is evidence that it is structural, and the line numbers become the
  justification for keeping it in pass 2.
- **Do not consult the toolkit yet.** Naming the move in your own words first, before
  seeing what is already catalogued, is what surfaces ideas the existing vocabulary
  cannot express.

## Pass 2 — discard the routine

Now prune. Delete a row if the move is a general-purpose reflex of analysis rather than
a choice the author made.

Discard: the triangle inequality; Cauchy–Schwarz and Hölder used to split a product in
the obvious way; Minkowski; a change of variables that is just a substitution;
Fubini/Tonelli under evident hypotheses; summing a geometric series; Chebyshev/Markov;
integration by parts with no boundary subtlety; taking a subsequence; passing to the
limit under uniform control; relabelling constants.

**Keep** a discarded-by-default move when there is something specific about *how* it is
used. The test is a counterfactual: could a competent reader have chosen this step
unprompted? If yes, discard. If the step required knowing something — which factor to
put in which space, which variable to hold fixed, which exponent to aim for — keep it,
and say in the row what the non-obvious part was.

Concretely, `Cauchy–Schwarz` goes. `Cauchy–Schwarz against the counting measure of a
random subset, to convert an L¹ bound into an L² bound at a cost that the sparsity of
the subset absorbs` stays. The difference is that the second names a *strategy*.

Two rows for the same move merge into one, keeping every line reference.

## Pass 3 — discard again, harder

Reread the surviving list cold, as though you had not written it. Two more cuts:

1. **Redundant rows.** Where two entries are two descriptions of one move at different
   granularity, keep the one that a reader could act on. Prefer the concrete.
2. **Rows that are content, not technique.** "Uses the Fourier transform" is not a
   technique; it is a subject. "Splits the Fourier support at the scale where the
   symbol degenerates" is a technique. If a row does not survive the question *could I
   apply this in another paper?*, cut it.

Then reread once more. On most papers pass 3 runs twice before the list stops moving;
three sweeps in total is the norm, and if a fourth still removes rows, keep going. The
list is finished when a sweep changes nothing.

**Do not cut for length.** A rich paper may leave twenty-five entries and a short one
three. Both are correct outcomes. Cutting a real technique to reach a tidy number
destroys exactly the data this project is collecting.

**But do not inflate either.** Ten entries that recur are worth more than thirty that
cannot. If a paper yields a long list, that is usually a sign that Pass 3½ has not been
run properly rather than that the paper is unusually rich.

## Pass 3½ — is it broad enough to recur?

Before touching the toolkit, apply one more filter, and it is the one that is easiest
to get wrong.

**The score is the point.** An idea's score is the number of papers using it. An entry
so specific that only this paper could ever match it will sit at score 1 for ever, and
a toolkit of score-1 entries is not a toolkit — it is a summary of one paper, filed
under a different name. Every entry must be phrased so that you can imagine writing
*this same entry* after reading a different paper.

Two tests, applied to each survivor:

1. **Would you bet on a second paper matching it?** Not "could it in principle" —
   would you expect it, among the papers still to be digested. If not, either raise the
   level of abstraction until you would, or cut it.
2. **Is the name a name, or a sentence?** Toolkit names are two or three words:
   *stopping time selection*, *small support perturbation*, *dyadic decomposition*. If
   the name is a clause describing what happened in this paper — "corrections with
   small support, so the object barely moves" — it is pitched at the wrong level. Shorten
   the name and the entry usually generalises itself.

**Raise the level, do not delete the detail.** The paper-specific version of the move
belongs in `ideas-<paper>.md`, under the broad entry's name, where it is evidence for
the entry. It is only the *toolkit* that has to be general.

And cut, do not generalise, when the row is a *remark* rather than an idea: a neat
observation local to one proof, which nobody would go looking for. "A weak type (1,1)
bound plus a Hölder bound gives a pointwise bound" is a good remark and a bad toolkit
entry. Put it in the discard list with that reason.

## Pass 4 — reconcile with the toolkit

Only now, open `data/toolkit.json`.

**Read the whole file before adding anything.** The default outcome of this pass is
*no new entry*: the move you just named is usually one the toolkit already has under a
different word. Check the `name`, the `aliases` and the `gloss` of every existing idea
against each survivor, and check the strata — the same move often sits one level up
from where you expected. Only when nothing matches does a new entry get created, and
new entries need the two tests above to have been applied.

For each surviving entry:

- **Existing idea, same move** → add this paper's id to the idea's `papers` list. The
  score is derived from that list; never edit a score by hand. **This is the expected
  case.**
- **Existing idea, but this paper uses it in a way the gloss does not cover** → extend
  the gloss. Glosses grow as evidence accumulates; that growth is the point.
- **Existing idea at the wrong level** → if the toolkit's version is narrower than what
  you are seeing, *widen the existing entry* and add this paper. Do not create a sibling.
- **New idea** → only if nothing above applies. Create an entry:

  ```json
  {
    "id": "kebab-case-stable-key",
    "name": "Display name",
    "stratum": "primitive | technique | strategy | transfer | obstruction",
    "gloss": "Two to four sentences: what the move is, what it buys, when it applies.",
    "aliases": ["other names it travels under"],
    "papers": ["<paper-id>"],
    "first_seen": "<paper-id>",
    "see_also": ["related-idea-id"]
  }
  ```

Choosing the stratum: **primitive** if it is an elementary move that the argument's
architecture rests on; **technique** if it is nameable machinery that lifts out of this
paper into another; **strategy** if it decides the shape of the proof before any
estimate is made; **transfer** if it carries the problem into a different subject;
**obstruction** if it is a counterexample or extremal configuration that later work
will reuse as an object.

Write the gloss so that someone who has not read the paper can use the idea. Say what
it does, not where it appeared — and in particular do not name this paper's objects in
it. A gloss mentioning the specific kernel, exponent or domain of one paper is a sign
the entry is still pitched too low.

Finally, add the idea ids to the paper's `toolkit` array in `data/papers.json`, and run
`python3 tools/build_data.py`. Scores recompute; the toolkit page updates.

## Output

Write `ideas-<name>.md` next to the expansion:

```markdown
# Ideas in <full reference>

Digested from `<name>-expanded.tex`. Pass 1: N rows. Pass 2: M. Final: K.

## Kept

### <Keyword>            — toolkit: `<idea-id>` (new | existing)
**Where.** §2.3, eq. (14), and again in the proof of Lemma 4.
**The move.** ...
**What it buys.** ...
**Why it is not routine.** ...

## Discarded, with reasons
| keyword | why cut |

## Judgement calls
Rows where keep-or-cut was genuinely close, and which way it went. The next reader
needs to see these; they are where the taxonomy is still soft.
```

Keeping the discard list matters. It is the record of what the pruning rules actually
did, and it is the only way to tell later whether they were tuned correctly.
