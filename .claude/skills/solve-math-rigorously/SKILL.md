---
name: solve-math-rigorously
description: Solve and audit substantive mathematical problems with explicit hypotheses, gap-checked proofs, counterexamples, and honest partial-result status. Use for proofs, counterexamples, sharp constants, extremizers, or mathematical corrections where rigor matters; do not use for routine arithmetic or simple formula lookup.
---

# Solve Math Rigorously

## Establish the Claim

- State the exact goal, quantifiers, hypotheses, conventions, and permitted background results before committing to an approach. Ask only when an ambiguity would materially change the theorem.
- When the problem belongs to a manuscript or repository, identify the governing definitions and lemmas first. Prefer current TeX or other source files over rendered PDFs, and verify every cited equation or section against those sources.
- Separate established results, new deductions, computational evidence, heuristics, and conjectures. Never use numerical evidence as a proof without a certified argument.

## Construct the Argument

- Pursue a proof or counterexample while viable approaches remain. Change methods when a route reaches a genuine obstruction instead of repeating it cosmetically.
- Make dependencies explicit: identify imported theorems, verify that their hypotheses apply, and prove any new lemma needed by the main claim.
- Track the strongest justified status throughout: `PROVED`, `COUNTEREXAMPLE`, `PARTIAL`, or `OPEN/GAP`. Do not promote a conditional, local, or computational result to an unconditional theorem.
- If the user requests step-by-step control, pause before each nontrivial inference, approach choice, auxiliary lemma, case split, or imported theorem and ask for guidance one question at a time.

## Audit Publication-Critical Claims

For a proof, counterexample, extremizer classification, sharp constant, or substantive correction intended for research or publication, use the installed `math-harness` before asserting the main result only when working API authentication and billing are already available. A ChatGPT or Codex subscription is not API authentication.

- Do not ask the user to buy API access, provide a key, reveal a secret, or retry repeatedly when only subscription access is available.
- Put the user's exact request in a UTF-8 prompt file and attach the governing source files. A typical fresh audit is:

  ```sh
  math-harness ask --fresh --audit --session paper \
    --prompt-file /path/to/task.md \
    --file /path/to/main.tex \
    --output /path/to/math-audit.md
  ```

- Treat the audit as a candidate argument, not an authority. Check its claims and citations against the current sources before changing a manuscript or asserting the result.
- Reuse `--session paper` without `--fresh` for follow-ups on the same unchanged problem. Attach the source again after it changes.
- Preserve every `PARTIAL` or `OPEN/GAP` finding unless a later checked argument actually closes it.

## No-API or Unavailable-Harness Fallback

When an independent harness audit is unavailable:

1. Produce a constructive proof or counterexample pass from the governing definitions and sources.
2. Perform a separate adversarial referee pass. Try to falsify each new claim, check boundary cases and quantifiers, expand hidden regularity or convergence assumptions, and independently recompute exact calculations where possible.
3. Repair every identified issue and repeat the adversarial pass until no known gap remains or the available approaches are genuinely exhausted.
4. Preserve `PARTIAL` or `OPEN/GAP` status for anything unresolved. State the precise obstruction and the strongest result proved.
5. In research notes or a publication handoff, disclose that the independent `math-harness` audit was unavailable and that the result received only a self-audit.

## Final Presentation

- Give a self-contained proof at the level requested, with definitions placed before use and each logical dependency visible.
- If space requires a compressed proof, identify every omitted routine calculation and never hide the central difficulty behind phrases such as “standard” or “clearly.”
- End with the exact result established and any surviving assumptions, exceptions, or gaps.
