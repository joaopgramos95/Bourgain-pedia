---
name: grilling
description: Grill the user one decision at a time about a plan, mathematical argument, or idea. Use when the user wants to stress-test or direct the reasoning, asks for a Socratic collaboration, or uses any “grill” trigger phrase.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **single-question rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask now without guessing at answers you have not heard yet. Select the highest-leverage item on the frontier, ask only that question, give your recommended answer, and wait. Never answer your own question or continue into a dependent branch before the user responds.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each answer reshapes the tree: settled decisions push the frontier outward and unblock dependent questions. Recompute the frontier after every answer. Do not batch multiple questions merely because they are simultaneously askable.

Finding _facts_ is your job, never the user's. Inspect supplied sources, the filesystem, and available tools before asking. Use subagents only when the user or applicable instructions explicitly authorize delegation. The _decisions_ are the user's: put each to them and wait.

## Mathematical Reasoning

For a proof, counterexample, calculation, or theorem audit, treat the proof itself as the tree. If `solve-math-rigorously` is available, apply its rigor and audit rules as well.

- Start with the exact claim, quantifiers, hypotheses, conventions, and allowed background results.
- State the immediate subgoal and the relevant equations or established facts before each question.
- Pause before every nontrivial inference, normalization, construction, approach choice, auxiliary lemma, case split, imported theorem, substantial computation, or change of strategy.
- When alternatives exist, offer two or three mathematically distinct moves, identify the recommended one, and briefly explain its likely payoff and risk.
- After the user chooses, carry out only that move. Show the resulting equation, lemma, obstruction, or counterexample, then pause at the next substantive step.
- Do not silently complete the proof in the background and use the interview as ceremonial approval.
- If the user's proposed step is invalid, show the exact failed implication, hypothesis, or computation, then ask whether to repair it, strengthen the assumptions, or take another branch.
- When a candidate argument is complete, ask before beginning an adversarial gap audit. Audit one possible failure point at a time and preserve `PARTIAL` or `OPEN/GAP` status while anything remains unresolved.

Do not claim to expose private hidden chain-of-thought. Give the user control through concise reasoning summaries, explicit mathematical objects, genuine alternatives, assumptions, and consequences.

The user may explicitly suspend checkpoints or delegate a stated portion of the reasoning. Otherwise, approval applies only to the current move.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
