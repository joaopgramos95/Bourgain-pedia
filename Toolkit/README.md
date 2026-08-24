# Toolkit

The toolkit lives in `../data/toolkit.json` and is rendered at
`../site/toolkit.html`. This directory holds the long-form notes that do not fit in a
gloss.

## How an idea gets here

Only one way: a paper goes through `blueprints/article-blueprint.md`, then through
`blueprints/idea-blueprint.md`, and the surviving keywords are reconciled against
`data/toolkit.json`. Nothing is added by sitting down and listing what Bourgain was
known for. The list has to be the residue of actual reading, or its scores mean nothing.

## Strata

| key | name | what belongs here |
|---|---|---|
| `primitive` | Primitives | Elementary moves the architecture of a proof rests on — *orthogonality*, *stopping time*, *dyadic decomposition*. Kept only when removing the move breaks the structure, not just a line. |
| `technique` | Techniques | Nameable machinery that lifts out of one paper into another — *TT\**, *induction on scales*, *random selection*. |
| `strategy` | Strategies | Ideas that decide the shape of an argument before any estimate is made — *sparseness*, *large deviations*, the *probabilistic method*. |
| `transfer` | Transfers | Moves that carry a problem into a subject with different tools. His signature. |
| `obstruction` | Obstructions and examples | Counterexamples and extremal configurations later work reuses as objects — Kakeya-type constructions, Λ(p) sets. |

## Scores

An idea's score is the number of catalogued papers whose `toolkit` array names it. It is
recomputed by `tools/build_data.py` on every build. **Never edit a score by hand** — if
a score looks wrong, the paper list is wrong.

## Long-form notes

When a gloss is no longer enough — an idea has five distinct uses, or its relation to a
neighbouring idea needs an argument — write `Toolkit/<idea-id>.md` and link to it from
the gloss.
