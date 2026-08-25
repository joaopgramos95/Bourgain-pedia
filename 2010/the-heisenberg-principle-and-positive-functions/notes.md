# Principe d'Heisenberg et fonctions positives

*(The Heisenberg principle and positive functions)*

## The paper

Bourgain, Jean; Clozel, Laurent; Kahane, Jean-Pierre.
*Annales de l'Institut Fourier* **60**, No. 4, 1215–1232 (2010).

- Zbl [1298.11105](https://zbmath.org/5793930)
- DOI [10.5802/aif.2552](https://doi.org/10.5802/aif.2552)
- arXiv [0811.4360](https://arxiv.org/abs/0811.4360) (26 November 2008)
- NUMDAM [AIF_2010__60_4_1215_0](http://www.numdam.org/item?id=AIF_2010__60_4_1215_0)
- MSC 11R42 (zeta and *L*-functions of number fields), 42A38 (Fourier transforms),
  42B10 (Fourier transforms in several variables)
- OpenAlex citation count 30, as of 2026-08-24
- Catalogue id `2010-the-heisenberg-principle-and-positive-functions`

Bourgain's only joint paper with either Clozel or Kahane, and the only paper in the
catalogue carrying all three names.

## Source obtained — 2026-08-24

**The authors' own LaTeX**, from the arXiv e-print service:
<https://arxiv.org/e-print/0811.4360> → `prin_Heisen11-08.tex`, dated
26 November 2008, 34,685 bytes, 888 lines. Kept byte-exact as
`...-original.tex`; the arXiv PDF is alongside it as `...pdf` (19 pages).

This is a much better starting point than a scan: every formula is the authors'
own, so the digestion cannot introduce transcription errors, and the six-odd
slips listed below are demonstrably theirs.

### Building the original

The file does not compile on a 2026 TeX distribution. Two reasons, both trivial and
both worth recording rather than fixing, since the file is the historical record:

1. `\usepackage[francais]{babel}` — `francais` is the deprecated spelling; modern
   babel wants `french`. Symptom: `! Undefined control sequence \bbl@main@language`.
2. Two stray `0xCA` bytes (Mac OS Roman non-breaking space, so the file was written
   on a Mac) at line 58 and line 400. The file is ISO-8859, not UTF-8.

With `[french]` and those two bytes replaced by spaces it compiles clean and gives
**exactly 19 pages**, matching the arXiv PDF. That is the reference length.

## The paper in one paragraph

A Fourier pair `(f, f̂)` on ℝ, both real and even and not identically zero, with
`f(0) ≤ 0` and `f̂(0) ≤ 0`, and with `f ≥ 0` beyond `a_f` and `f̂ ≥ 0` beyond `a_f̂`.
How small can the product `a_f · a_f̂` be? Call the infimum `B₁`. That it is positive
at all is not obvious. §1 reduces the question to self-dual `f = f̂` with `f(0) = 0`,
so `B₁ = A²`, and proves `A ≥ 1/(2(1+λ)) = 0.4107…` where `λ = −inf(sin x / x)`.
§2 produces test functions and gets `A ≤ 0.64`. §3 does both in dimension `d`, with
`B_d ≥ d/(2πe)` and `B_d ≤ (d+2)/2π` — linear growth, pinned between explicit
constants. §4 is the surprise: via Tate's thesis, a Fourier pair of this kind on the
adeles of a number field `F` would force `ζ_F` to have no zero in `]0,1[`; running
that backwards, Armitage's degree-48 field with `ζ_F(1/2) = 0` and class field towers
show that number theory *already implied* the linear growth in `d`.

## Editorial decision: the digestion is in English

The paper is in French. The digestion will be in English, because the project, its
site, its blueprints and its other digestion are; the French is preserved exactly in
`...-original.tex`, which is the authors' own file and not a transcription of ours,
so nothing is lost by it. Where a term of art matters, the French is kept alongside.

This is a judgement call, not a rule of the blueprint. If it should be in French
instead, only Stage 3 needs re-running.

## What the paper leaves open

Harvested from the paper's own words, per Blueprint A. Nothing here is a question we
believe is open; each is one the authors state.

1. **The exact value of `B₁`** (equivalently of `A`). The paper brackets it as
   `0.4107… ≤ A ≤ 0.64` and stops: *"Plus loin, les calculs semblent difficiles et
   nous n'avons pas poursuivi cette voie"* (§2.1), and of the upper bound,
   *"Celle-ci n'est pas optimale"* (§0). Our §2.3 pushes their own correction
   argument to `A ≤ 0.5973`, so the bracket in the digestion is
   `0.4108 ≤ A ≤ 0.5973`. The gap is a factor of 1.45 and is entirely open.

2. **Is the bound (3.4) optimal in dimension `d > 2`?** Twice stated:
   *"Il est donc possible que la valeur (3.4) soit optimale. Pour `d=1`, ce n'est pas
   le cas, comme on l'a vu au §2"* (§3), and again after the `a→1` analysis,
   *"Là encore, il est possible que la borne donnée par (3.4) soit optimale"*. So the
   authors know `d=1` fails and conjecture nothing beyond possibility.

3. **The linear growth constant of `B_d`.** Theorems 3 and 4 pin `B_d` between
   `d/(2πe) = d/17.079…` and `(d+2)/2π`, a factor of `e` apart. Which end is right —
   or whether `B_d/d` converges at all — is not addressed.

4. **The `(p-1)` in the arithmetic tower** (§4, closing): the degrees for which the
   class-field-tower argument gives linear growth are `d = 48(p-1)p^n`; the authors
   remark that *"le terme en `(p-1)` n'est pas nécessaire si l'on est prêt à utiliser
   la conjecture d'Artin ou la conjecture de divisibilité de Dedekind"*. A
   conditional refinement rather than a problem of the subject, recorded for
   completeness.

Items 1–3 are candidates for `data/problems.json`. They are **not** written there
yet: each entry needs a `status` list of two or three post-2010 articles, every one
verified against a bibliographic source and honestly marked `read: false` where we
have only the abstract. That is Stage 5 work and waits on approval.

## Status

Stages 1 (choose), 2 (download) and 3 (Blueprint A) **complete**.

- `...-expanded.tex` — 0 errors, 0 overfull boxes, no undefined references,
  `latex-source-audit` passes.
- **19 pages → 23 pages**; body 32,773 → 66,185 characters at hand-off, more after
  the reading pass below — a factor of **2.02** or better.
  (The page ratio understates the expansion badly: the original is 12pt with generous
  `\vskip`s, the digestion 11pt `amsart` at 1.05in margins.)
- `ledger.md`: **110 rows**, none open — 91 closed with an explicit `\Ledger{}`
  marker, 17 closed by verbatim reproduction of a statement of the paper, 2 standing
  as `caution` (six at hand-off; see the reading pass below). No `OPEN-GAP`: no step of
  the authors' own argument we could not reconstruct.
- 28 `expansion` blocks, 8 `filled`, 8 `ournotation`, 1 `caution`.

Stage 4 approved; Stage 5 (Blueprint B) **complete**.

- `ideas-the-heisenberg-principle-and-positive-functions.md` — pass 1: 70 rows,
  pass 2: 48, final: **11**. Four existing toolkit entries gain this paper
  (`scaling-normalisation` and `iterative-correction` widened, `dimension-threshold`
  and `extremal-datum` extended); **seven new**: `symmetrisation-to-fixed-space`,
  `mass-volume-bound`, `leading-coefficient-sign`, `positive-type-convolution`,
  `regularisation-at-epsilon-cost`, `functional-equation-positivity`,
  `tower-propagation`. Toolkit 13 → 20 entries, and four of them now score 2 — the
  first cross-paper matches the project has.
- `data/problems.json` — the three open questions of the harvest are now entries,
  each with verified status references.

## What the follow-up literature says

Checked against zbMATH and arXiv on 2026-08-24; abstracts and bibliographic records
only, nothing read, and the entries say so.

- The problem is now called the **sign uncertainty principle** and is an active
  subject. Cohn–Gonçalves (Invent. Math. 2019) settled dimension **12** exactly,
  `B₁₂ = 2`, by Viazovska's modular-form method — and their abstract says no sharp
  value is known or conjectured in any other dimension.
- That already **answers the paper's second question in the negative**: the paper's own
  upper bound gives `B₁₂ ≤ 14/2π = 2.2282`, and the truth is 2. Lee (arXiv, 15 August
  2026 — nine days before this was written) names `√((d+2)/2π)`, which is Theorem 4 of
  this paper, as "the previously best known bound" and improves on it for every
  `d ≥ 52` divisible by 4. So Theorem 4 stood as the best known bound in those
  dimensions for sixteen years.
- **The linear growth constant is now known.** Chapter 1 of OpenAI's *Ten Advances in
  Mathematics and Theoretical Computer Science* (1 August 2026, chapter updated 6
  August) states as Theorem 1.2 that `A₊(d)/√d → 1/π`, hence `B_d/d → 1/π² =
  0.101321`. That is the third open question of the harvest, answered. It lands inside
  this paper's own bracket `[1/2πe, 1/2π] = [0.05855, 0.15915]` — a factor `π/2` below
  their upper constant and `2e/π` above their lower. Both 2010 bounds were within a
  factor of two of the truth. It also refutes the second question asymptotically:
  `1/π² < 1/2π`, so `X(d) = d/2+1` is not optimal for large `d`.
  Provenance matters here and the entry says so: the results are stated to be the work
  of an internal OpenAI model, the manuscript is self-published, not refereed, and we
  read Chapter 1's statements, not its proof.
- The d = 12 comparison is ours: it is Cohn–Gonçalves's sharp value put against
  Theorem 4. Both sides are verified bibliographically; neither proof has been read.
- Two of the follow-up papers are by **João P. G. Ramos**, this project's maintainer,
  with Gonçalves and Oliveira e Silva (J. Geom. Anal. 2021; Discrete Anal. 2023). The
  2021 one proves minimising sequences exist in the Schwartz class for `d = 1`, which
  bears directly on the factor 2 this paper left in `B₁ ≤ 𝓑₁ ≤ 2B₁`.

## The §4 imports: reading pass, 2026-08-24

The digestion shipped with one `caution` block covering six citation rows. Four are now
closed against sources actually read; two remain.

**Closed.**

| row | claim | read against |
|---|---|---|
| E1 | Tate's functional equation: simple poles only at `s=0,1`, residues `∓Vol(C¹)f(0)`, `+Vol(C¹)f̂(0)` | Leahy, *An introduction to Tate's Thesis*, McGill M.A. 2010, **Thm 4.9.2** |
| E5 | `κ = 2^{r₁}(2π)^{r₂}hR/(w√|D|)` | Leahy **§4.11**, `Vol(C_K¹)` computation |
| E8 | `f̂_v⁰ = (N𝔡_v)^{−1/2}·1_{𝔡_v^{−1}}`, `∏N𝔡_v = |D|` | Poonen, *Tate's thesis*, MIT 18.786 notes — the computation is explicit; cross-checked in Leahy |
| E21 | Odlyzko's discriminant bound | Odlyzko, *Bounds for discriminants…*, Sém. Théor. Nombres Bordeaux **2** (1990) 119–141, **(2.5)** |

Two things came out of that reading.

- **Odlyzko's constant is 22.3816, not 22.2.** (2.5) reads
  `rd > (4πe^{1+C})^{r₁/n}(4πe^C)^{2r₂/n} − O(n^{−2/3}) = (60.8395…)^{r₁/n}(22.3816…)^{2r₂/n} − O(n^{−2/3})`.
  The minimum over signatures is the totally imaginary case, 22.3816. The paper's 22.2
  is that rounded down; since all the argument needs is `22.2 > 2πe = 17.079`, §4 is
  untouched.
- **Odlyzko's method is a cousin of this paper's problem.** His explicit-formula bound
  needs a function `F` with `F > 0` and `F̂ ≥ 0`, and his survey poses as an open
  problem: which such functions give the best discriminant bounds? That is an extremal
  problem with sign conditions on a function *and* its transform. §4 relates the two
  constants; it does not notice that the two *methods* are of the same kind. Recorded
  in §5(6) of the expansion.

**Still open, and now the only conditional points in the digestion.**

- **E16 — Armitage.** Invent. Math. **15** (1972) 199–205, paywalled at $39.95; not
  read, and I did not use institutional credentials. What was done instead: the degree
  arithmetic is verified here — `E = ℚ(√(3(1+i)))` contains `ℚ(i)` since `i = y²/3 − 1`,
  and `3+3i` is not a square in `ℚ(i)` because `(a²+b²)² = N(3+3i) = 18` forces
  `a²+b² = 3√2 ∉ ℚ`; so `[E:ℚ] = 4` and `[F:ℚ] = 12·4 = 48`. (Eisenstein at 3 does *not*
  do it: `y⁴−6y²+18` has `9 | 18`.) The statement `ζ_F(1/2)=0` and its mechanism —
  `ζ_F` factors into Artin L-functions, one of which has root number `−1` and so
  vanishes at `1/2` — are confirmed by a refereed secondary source (Inventiones 2025,
  arXiv:2107.10900, introduction), which also pins the construction to **Serre §9**.
- **E23 — Roquette Cor. 7.** Cassels–Fröhlich was not obtainable. The degree bookkeeping
  checks (`[ℚ(ζ_p):ℚ] = p−1`, times `p`), and the discriminant half of the argument is
  now *proved* rather than cited: for `L/K` unramified of degree `n` the relative
  different is trivial, so `D_L = D_K^n` and the root discriminant is constant along the
  tower (Background). What is taken on trust is the *existence* of the tower.

**A finding worth more than either.** Proposition 2 uses the degree-48 field only as a
seed: any field whose zeta has a real zero, of any degree `d₀`, gives `𝓑_d > 0` for
every multiple of `d₀` by the identical argument. Fröhlich (*Artin root numbers and
normal integral bases for quaternion fields*, Invent. Math. **17** (1972) 143–166)
constructed infinitely many quaternion fields of degree **8** with `ζ_K(1/2)=0`. So
Proposition 2 holds for every multiple of 8, which contains `48 = 8·6`. Fröhlich is
unread too, so the expansion records this in §5(8) without restating the proposition.

Ledger after this pass: **110 rows — 91 closed, 17 closed by reproduction, 2 caution.**
Expansion now 23 pages.

## Still worth doing

- Two imports remain unread: Armitage (paywalled) and Roquette's Cor. 7
  (Cassels–Fröhlich unobtainable here). Anyone with a library can close both in an
  afternoon; everything around them is now proved or cited to a source we read.
- The superposition `∫₁^∞ g_a dτ(a)` of (2.2): the paper raises it and abandons it,
  saying no simple characterisation of `τ` is apparent. Nothing in the harvest, but a
  live direction.
