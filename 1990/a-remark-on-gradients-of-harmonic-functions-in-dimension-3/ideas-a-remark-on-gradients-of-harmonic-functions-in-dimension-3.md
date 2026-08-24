# Ideas in Bourgain–Wolff, *A remark on gradients of harmonic functions in dimension ≥ 3*

IHES/M/89/31 (September 1989); Colloq. Math. 60/61, No. 1, 253–260 (1990). Zbl 0731.31006.

Harvested from `a-remark-on-gradients-of-harmonic-functions-in-dimension-3-expanded.tex`
(1745 lines, 24 pages, 95 sectioning and editorial blocks) under
`blueprints/idea-blueprint.md`.

**Pass 1:** 62 rows. **Pass 2:** 31. **Pass 3:** three sweeps → 24, then 21, then 20.
**Pass 3½ (broadness):** 20 → **13**. **Final: 13**, all new to the toolkit — it was
empty before this paper.

The first version of this harvest produced twenty entries pitched at the level of *this
paper*, which was a design error: an idea's score is the number of papers using it, so
an entry only this paper could match would sit at score 1 for ever and the toolkit would
become a summary of one paper filed under another name. Pass 3½ exists because of that
mistake, and is now part of `blueprints/idea-blueprint.md`. Below, each kept entry is
the *broad* idea; how this paper instantiates it is the detail underneath, which is
where the paper-specific version now lives.

A note on what was *not* harvested. The expansion contains four kinds of boxed
material that is ours, not the authors': `expansion`, `filled`, `ournotation`,
`caution`. Moves that exist only because we made them — checking a statement's
homogeneity to expose the missing factor in Lemma 2, splitting `{|x|>1}` at `|x|=2`
to repair a mean value argument — are recorded under *Judgement calls* below and
deliberately kept **out** of the toolkit. The toolkit is Bourgain's, not ours.

---

## Kept

Thirteen entries. Each is named as it appears in the toolkit; the paper-specific form is
given underneath as evidence for it.

### Iterative correction — `iterative-correction` (new, strategy)
**Here.** §4, §6. Build `f` as the limit of `u_n`, each stage adding corrections that
multiply the local `L^p` size of `∂_n u_n` by `e^{-2β} < 1` on every surviving cell.
**Why broad.** Any construction that reaches its object as a limit of improvements
rather than directly. The recurring difficulty — a gain uniform in the stage from
ingredients chosen afresh each stage — is the same everywhere.

### Summable loss budget — `summable-loss-budget` (new, strategy)
**Here.** §7.2–§7.4: `Σ ε^{(d-1)/2}` (measure where `f` moved) plus `Σ K^{-p}` (measure
discarded) must be `< |Q(1)| = 1`.
**Why broad.** The standard way an iteration is made to leave something behind.

### Stopping time selection — `stopping-time-selection` (new, technique)
**Here.** §4.2, conditions (a) and (b): keep a cube iff its parent survived and its local
`L^p` average is below `K_{n+1}e^{-βn}`; §7.3 reads the discarded measure off the failed
test.
**Why broad.** Bourgain's most characteristic organisational move.

### Small support perturbation — `small-support-perturbation` (new, technique)
**Here.** `supp F_ε ⊂ D(0,ε^{1/2})`, and the corrections at stage `n+1` live in discs of
radius `δ_{n+1}ε_{n+1}^{1/2}/N`. This is exactly the improvement over the predecessor
construction: it is what lets `f` and `∇f` vanish on *one* set instead of two.
**Why broad.** Any surgery designed to change a derivative without moving the object.
*(The first draft called this "corrections with small support, so the object barely
moves" — a sentence, not a name.)*

### Dyadic decomposition — `dyadic-decomposition` (new, primitive)
**Here.** §2.3, the annular partition `ψ_j` used to truncate `G_ε` to compact support
while keeping its singular core; the errors are controlled scale by scale and sum
geometrically.
**Why broad.** Ubiquitous.

### Scaling normalisation — `scaling-normalisation` (new, primitive)
**Here.** Two instances. The factor `δ_{n+1}/N` in eq. (un1), which makes the correction's
*gradient* `O(1)` while its *amplitude* is `O(δ)` — the reconciliation on which
convergence depends. And §3.1, reducing Lemma 2 to `I(a_Q) = 1` by homogeneity.
**Why broad.** And note the diagnostic: Lemma 2's failure to be homogeneous is exactly
what exposed the missing factor `I(a_Q)` (ledger `C9`).

### Large/small dichotomy — `large-small-dichotomy` (new, technique)
**Here.** §6.2, type 1 / type 2 at threshold `e^{-4β(n+1)}`; the multiplicative lemma
must divide by the local value, so cells where it is tiny are handled absolutely instead.
**Why broad.** Any argument whose machinery degenerates at zero.

### Working below exponent one — `sub-unit-exponent` (new, technique)
**Here.** `p < (d-1)/d` throughout; `|·|^p` subadditive with no norm available; and
crucially, the strict negativity of `∫(|1+∂_nG_ε|^p − 1)` is possible *only* because
`p < 1` flattens the large values.
**Why broad.** The sub-unit range is where a whole family of Bourgain's arguments live,
and the trade — lose the norm, gain a strict deficit — is always the same.

### Parameter hierarchy — `multiscale-parameter-hierarchy` (new, primitive)
**Here.** `d,p → η → N → τ,β → A → {K_n},{ε_n} → δ_{n+1}`. Two steps are legitimate
*only* because `δ_{n+1}` is chosen after `u_n` exists.
**Why broad.** Every multi-parameter construction has one, and most papers leave it
implicit.

### Boundary problem as singular integral — `boundary-to-singular-integral` (new, transfer)
**Here.** `∂_n` of a harmonic extension is `−Σ R_k ∂_k`, which is why Riesz transform
estimates appear in §2.4 at all. The original states none of this.
**Why broad.** The transfer that turns potential theory into harmonic analysis.

### Extremal datum reused at every scale — `extremal-datum` (new, obstruction)
**Here.** The Alexandrov–Kargaev function `G_ε`, and rescaled copies of `F_ε` inserted at
every cell of every stage. It carries the entire sign of the argument.
**Why broad.** The pattern — one hard object, quoted rather than proved, then reused
mechanically — recurs across Bourgain's constructions.

### Dimension threshold — `dimension-threshold` (new, obstruction)
**Here.** `d ≥ 3`, visible in two independent places: convergence of `Σ n^{-(d-1)}` in §7,
and the sign of `L(d) = −π cot(π/d)/(d−1)` in §2.2, which vanishes at `d = 2`.
**Why broad.** A reusable audit: a proof of a statement false in low dimension must
degenerate exactly at the threshold, and checking that it does catches errors.

### Density point endgame — `density-point-endgame` (new, primitive)
**Here.** §7.5, the step the paper omits entirely: `f = 0` on `E` and `f ∈ C¹` give
`∇_T f = 0` a.e. on `E`, so only the normal derivative ever needed separate control.
**Why broad.** The standard measure-theoretic closing move.


### Folded into a broader entry at Pass 3½

| first-draft entry | where it went |
|---|---|
| Successive correction with geometric decay | `iterative-correction` |
| Two-budget accounting | `summable-loss-budget` |
| Corrections with small support, so the object barely moves | `small-support-perturbation` (renamed: it was a sentence) |
| Amplitude/gradient decoupling by scaling | `scaling-normalisation` |
| Normalise at the cell centre | `scaling-normalisation` |
| Additive deficit to multiplicative gain | `iterative-correction` — it is *how* the gain is obtained, not a separate idea |
| Nested grids with a local-average survivor rule | `stopping-time-selection` |
| Size dichotomy per cell | `large-small-dichotomy` |
| Dyadic cut-off preserving the singular core | `dyadic-decomposition` |
| Subadditivity near a zero, MVT away from it | `sub-unit-exponent` |
| Explicit parameter ordering | `multiscale-parameter-hierarchy` |
| The Dirichlet-to-Neumann map as a singular integral | `boundary-to-singular-integral` |
| The Alexandrov–Kargaev extremal datum | `extremal-datum` |
| Translate the singularity off the boundary | `extremal-datum` — a construction detail of the datum |
| Dimension two is different, by analyticity | `dimension-threshold` |
| Density points kill the tangential gradient | `density-point-endgame` |

### Cut at Pass 3½ as remarks, not ideas

| entry | why cut |
|---|---|
| Weak type (1,1) plus Hölder gives a pointwise bound | A neat local observation, not something anyone would go looking for in a toolkit. It stays in the digestion at §2.4, where it does its work. |
| Riemann sum for lattice interference | A computation. What is reusable about it — that superposed bumps must not be allowed to interfere — is already carried by `small-support-perturbation`. |
| Whole-space inequality transferred to a cube by its tail | Routine localisation; the only content is that it forces `N` to be chosen early, which is `multiscale-parameter-hierarchy`. |
| Pointwise value from an average, by choosing the next scale late | A technical convenience, and the part that matters is the ordering — `multiscale-parameter-hierarchy`. |

## Discarded, with reasons

| keyword | why cut |
|---|---|
| Poisson kernel, harmonic extension | Definitions, not moves. |
| Leibniz on a product with a cut-off | Routine; nothing about the choice is informative. |
| pointwise bound × measure of support = `L¹` bound | Routine. |
| interpolation `‖·‖_{C^α} ≲ ‖·‖_∞^{1-α}‖∇·‖_∞^α` | Standard, used off the shelf. |
| geometric summation over dyadic scales | Routine once the per-scale bounds exist. |
| the `min(|x|^{-d},(2^jδ)^{-d})` bookkeeping form | Notation for the two regimes, not a move. |
| change of variables `x = εy`, `s = |x|/ε` | Substitution. |
| kernel representation off the support | Standard; kept only as part of `dirichlet-to-neumann-as-riesz`. |
| maximum principle for `∂_j v` | Standard, and used exactly as stated. |
| `Σ_{Q} |Q| ≤ |Q(1)| = 1` | Arithmetic. |
| exhibiting `ε_n = C^{-1}n^{-2}`, `K_n = Cn^{2/p}` | Verification that the conditions are non-vacuous, not a technique. |
| "`CN^{-d} < cN^{-(d-1)}` for large `N`" | Merged into `size-dichotomy-per-cell`, where it does its work. |
| tracking which constants depend on what | Merged into `parameter-ordering-discipline`. |
| three-piece assembly of the gradient bound | Bookkeeping over pieces already harvested. |
| the `C^{2+ε}` variant of Remark 2 | Asserted without proof in the source; not a move we can see. |
| splitting `∫(|1+∂_nF|^p-1)` into imported term + difference | Merged into `subadditivity-vs-mvt-split`, which is where the content is. |
| the exponent constraint `p < (d-1)/d` | A consequence of a computation, not a technique — though see *Judgement calls*. |

---

## Judgement calls

**Homogeneity as a correctness check — cut, though it is the best move in the digestion.**
Testing how both sides of Lemma 2 scale under `I → cI` is what exposed the missing factor
`I(a_Q)`. It is exactly the kind of reusable habit the toolkit exists for. It is cut
because it is *ours*, not the authors': the original does not perform it, and had it, the
statement would have been right. Recorded here so the next reader can promote it if the
project decides the toolkit should also hold the reading techniques.

**Splitting `{|x| > 1}` at `|x| = 2` — cut, same reason.** The repair in §2.6 and §3.3 is
ours; the paper's own argument applies the mean value theorem across a zero. The general
pattern (partition by which comparison tool is available) *is* kept, as
`subadditivity-vs-mvt-split`, because the paper does make that split — just at the wrong
place.

**`p < (d-1)/d` — cut, but it was close.** Extracting the exact admissible range from the
convergence of `∫ r^{d-2-dp}dr` is a real piece of work that the original compresses to
"for small `p`". It was cut as a computation rather than a technique. What is reusable is
the habit of pinning the implicit range in a "for small `p`" hypothesis, and that habit
is not distinctive enough to name.

**`keep-most-of-the-object` versus `amplitude-gradient-decoupling` — both kept.** These
look like one move at two granularities, which Pass 3 would normally merge. They are not:
the first is a *requirement* on the construction (supports must be summably small), the
second is the *mechanism* that makes the requirement compatible with correcting the
gradient. A paper could satisfy one without the other.

**`ak-extremal-boundary-datum` — kept as an obstruction, not a technique.** It is an
imported object, and we could not verify the inequality that makes it work (ledger `B4`).
It is catalogued because later work reuses such data as objects, which is what the
`obstruction` stratum is for; the gloss says plainly that the key property is unverified
here.
