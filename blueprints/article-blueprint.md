---
name: article-blueprint
purpose: Turn one Bourgain paper into an expanded version in which nothing is left to the reader.
consumes: the original article (PDF or TeX) in <year>/<slug>/
produces: <name>-expanded.tex  (and <name>-expanded.pdf)
---

# Blueprint A — expanding an article

You are producing the **digestion** of a single paper by Jean Bourgain: a version of
that paper in which every step he compressed is written out, and nothing else has
changed. This is not a survey, not a modernisation, and not your own account of the
subject. It is his argument, at full length.

The reader you are writing for is a competent graduate student who knows the ambient
field but has never seen this paper, and who will not be able to consult a second
source while reading. If that reader can follow your text from the first line to the
last without stopping to reconstruct anything, the digestion is finished.

## The six rules

These are the standing constraints. Every other instruction in this file exists to
serve them.

1. **When in doubt, expand.** Doubt is the trigger, not a reason to hesitate. If you
   cannot say with certainty that a reader will follow a step, the step gets written
   out. Length is never the objection.
2. **Do not deviate from the line of work in the article.** Stick to his arguments.
   You may not substitute a proof you find cleaner, reorder the logic to suit a modern
   taste, or replace a lemma with a later reference that supersedes it. If a modern
   route exists, it belongs in a remark, clearly marked, at the end of the section —
   never in the body.
3. **New notation is allowed, and encouraged, when it buys clarity.** Bourgain often
   carries an unnamed object through three pages. Name it. Declare every symbol you
   introduce in a notation block, and say explicitly that it is yours.
4. **The expanded article is strictly larger than the original.** Section for section,
   proof for proof. There is no part of the paper that comes out shorter than it went in.
5. **No computation in the original is omitted from the new one.** Every displayed
   estimate he writes must appear, and must appear with the intermediate steps that
   produce it. A computation you find routine is still a computation he chose to include.
6. **Arguments left out of the original are supplied in the new one.** "One checks
   easily", "a standard argument gives", "by the same reasoning", "it is well known
   that" — each of these is a hole, and each hole gets filled with an actual proof.

## Before you write

1. **Get the source.** Prefer TeX (arXiv e-print source) over PDF. If only a PDF
   exists, transcribe it faithfully first, formulas included, and keep the
   transcription as `<name>-original.tex`. Never work from a summary of the paper.
2. **Read it once, whole, without writing.** You are looking for the architecture: what
   is the theorem, what is the one difficulty, and where does the paper turn.
3. **Build a ledger.** Before expanding a line, write `ledger.md` in the paper's
   directory with one row per item:

   | # | location | kind | statement | status |
   |---|----------|------|-----------|--------|

   `kind` is one of: *claim*, *computation*, *citation*, *gap*, *notation*.
   A **gap** is any step whose justification is not on the page. Mark every
   "clearly", "easily", "standard", "similarly", every unexplained inequality,
   every constant that appears without derivation, and every appeal to an
   unnamed result.

   The ledger is the definition of done: the digestion is complete when every row
   is `closed`, and not before.
4. **Resolve the citations.** For each external theorem he invokes, state it in full,
   with hypotheses, in a *Background* section — and check that the hypotheses actually
   hold where he applies them. If they do not obviously hold, that is a gap; open a row.

## Structure of the expanded article

```
\documentclass{amsart}
% Bourgain-pedia digestion of:
%   <full bibliographic reference>
%   <DOI / arXiv / Zbl>
% Original: N pages. This expansion: M pages.

§0  Editorial preface     what this document is; what was added and where
§0' Notation              his notation, then ours, clearly separated
§0'' Background           every imported theorem, stated in full with hypotheses
§1..  The paper           his sections, his numbering, his order
§App  Deferred computations, if any grew long enough to interrupt the flow
§End  Remarks             anything later than the paper: corrections, modern routes,
                          subsequent improvements. Strictly quarantined here.
```

Keep **his** section and theorem numbering, so that the digestion can be read
side by side with the original. Anything you add gets a marker:

- `\begin{expansion}...\end{expansion}` — a step he compressed, written out.
- `\begin{filled}...\end{filled}` — an argument he omitted entirely, supplied by us.
- `\begin{ournotation}...\end{ournotation}` — notation we introduced.
- `\begin{caution}...\end{caution}` — a step we could not fully justify. See below.

Define these as environments at the top of the file, visually distinct in the PDF. A
reader must be able to see, at a glance, where Bourgain stops and where we start.

## While you write

- **Every constant is tracked.** When he writes `C`, say what it depends on. When an
  implicit constant changes from one line to the next, say so.
- **Every quantifier is explicit.** Bourgain routinely leaves the order of quantifiers
  to context. Fix the order in writing, at the point where the object is introduced.
- **Every "similarly" is done.** If the second case really is symmetric, say precisely
  which symmetry, and check it. If it is not symmetric, do it in full.
- **Every numerical claim is recomputed.** Exponents, dimensional counts, the
  arithmetic inside an interpolation — redo them independently. If your value differs
  from his, do not silently correct it: open a `caution` and record both.
- **Diagrams and tables** are yours to add freely; a scale decomposition or a case
  split is usually much clearer as a picture or a table than as prose.

## Honesty about what you could not close

You will meet steps you cannot reconstruct. The failure mode to avoid is producing
confident prose that hides a hole. When a step resists:

1. State exactly what is claimed and exactly what you can prove.
2. Say what is missing, in one sentence.
3. Wrap it in `\begin{caution}` and mark the ledger row `OPEN`.
4. Keep going. One open row does not stop the digestion.

Never promote a plausible reconstruction into a proof, and never write "it can be
shown" in your own voice. That phrase is the thing this project exists to remove.

## Passes

Run these in order. Each is a full sweep of the document.

1. **Skeleton pass.** Reproduce the paper's structure and all statements verbatim,
   with proofs left as stubs. Populate the ledger.
2. **Expansion pass.** Work the ledger top to bottom. Every row becomes text.
3. **Computation pass.** Recompute every displayed formula independently, ignoring
   what is written. Reconcile differences.
4. **Adversarial pass.** Reread as a hostile referee whose goal is to find one place
   where the text asserts more than it proves. Every hit opens a new ledger row.
   Repeat this pass until it produces nothing.
5. **Reader pass.** Read it start to finish as the graduate student. Every place you
   have to stop and think is a row. This pass catches the ordering problems the others
   miss.
6. **Ledger check.** Nothing `open` except genuine `caution` rows, each visible in the
   PDF.
7. **Size check.** Compare compiled page counts. If the expansion is not strictly
   longer than the original, rule 4 has been violated somewhere; find where.

Passes 4 and 5 are not optional and are not one-shot. Expect to run pass 4 three or
four times on a dense paper.

## Handoff

When the digestion is done, the paper's directory holds:

```
<year>/<slug>/
  <name>.pdf                 the original
  <name>-original.tex        transcription, if the original was PDF-only
  <name>-expanded.tex        the digestion
  <name>-expanded.pdf        compiled
  ledger.md                  every row closed or explicitly OPEN
  notes.md                   what was hard, what is still open, what to read next
```

Then, and only then, Blueprint B runs on `<name>-expanded.tex`.
