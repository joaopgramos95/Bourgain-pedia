# Ledger — Bourgain, Clozel & Kahane, *Principe d'Heisenberg et fonctions positives*

Source: the authors' own arXiv LaTeX (`0811.4360`, 26 Nov 2008), kept byte-exact as
`...-original.tex`. Published as Ann. Inst. Fourier **60** (2010), 1215–1232.
Reference length: **19 pages**.

One row per item. `kind` ∈ {claim, computation, citation, gap, notation}.
A **gap** is a step whose justification is not on the page.

Section and equation numbers are the paper's. The paper is in French; the digestion
is in English (see `notes.md`).

---

## Status summary

| status | count |
|---|---:|
| closed | 87 |
| closed (reproduced) | 17 |
| **caution** (visible in the PDF) | 6 |
| open | 0 |
| **OPEN-GAP** | 0 |
| **total rows** | **110** |

Every row is accounted for. The three statuses mean different things and the
distinction is the point:

- **closed** — the digestion contains text answering the row, carrying a
  `\Ledger{}` marker naming it. 87 rows; 28 `expansion` blocks, 8 `filled`
  blocks and 8 `ournotation` blocks between them.
- **closed (reproduced)** — the row *is* a statement of the paper (a theorem, a
  displayed condition, one of the authors' own remarks) or a convention settled in
  §0. It is closed by appearing verbatim in the digestion; there was nothing to add,
  and adding a marker would have claimed otherwise.
- **caution** — the six citation rows of §4. We state each import precisely and
  check how the paper uses it, but we have **not read the sources**: Tate, Armitage,
  Serre, Odlyzko, Golod–Šafarevič/Brumer. This is visible to the reader as a
  `caution` box at the head of §4, not buried here. §4 is conditional on them.

No row is an `OPEN-GAP`: there is no step of the paper's own argument that we could
not reconstruct.

**Everything numerical in this paper has already been recomputed independently**
(computation pass, run before drafting): λ, Theorem 1's two constants, every
coefficient of both Taylor expansions, `P₄(3/2)=3/2`, `Q₄(c+1)=−c²+1`, the `a=√2`
and `a=2` reductions, `p₅=0` and `p₆=−4/45`, and Theorem 3's inequality chain for
`d = 1,2,3,4,8,12,24,48,100`. Every one matches the paper. The single exception is
`C21`, where the paper's own bound is weaker than its method delivers.

---

## A. Framing and the problem

| # | location | kind | statement | status |
|---|---|---|---|---|
| A1 | preamble | notation | The paper opens with an unlabelled four-paragraph summary rather than an abstract. Reproduce it as a signposted overview. | closed |
| A2 | §1, (1–3) | notation | Two families of constants are introduced and never tabulated: `a_f, a_f̂` (thresholds attached to one pair) versus `A(f), A(f̂)` (infima over admissible thresholds), and then `B₁, 𝓑₁, B₁⁻, 𝓑₁⁻`. Give one table. | closed |
| A3 | §1, after (3) | gap | "la condition 2) et la non-nullité de `f, f̂` impliquent que `a_f` et `a_f̂` sont `>0`". Not argued. Fill: if `a_f = 0` then `f ≥ 0` everywhere, with `f(0) ≤ 0`; then `f̂(0)=∫f ≥ 0` and `≤0` force `∫f=0`, so `f ≡ 0`. | closed |
| A4 | §1 | gap | "de tels couples existent à l'évidence" — no example is given. Exhibit one explicitly, so the problem is visibly non-vacuous before `B₁ > 0` is proved. | closed |
| A5 | §1 | claim | The point of the paper: `B₁ > 0` is *not* obvious. Say why the naive scaling argument fails, since that is what makes the question interesting. | closed |
| A6 | throughout | notation | Fourier convention `f̂(y)=∫f(x)e^{-2πixy}dx`; state it once, note that it makes `γ(x)=e^{-πx²}` self-dual, and that all constants below depend on it. | closed |

## B. §1 — reduction and Theorem 1

| # | location | kind | statement | status |
|---|---|---|---|---|
| B1 | §1 | computation | Scale invariance of `A(f)A(f̂)` under `f(x) ↦ f(x/λ)`, `f̂(y) ↦ λf̂(λy)`. Verify the transform convention and that `A` scales as `λ^{±1}`. | closed |
| B2 | §1 | gap | Reduction to `A(f)=A(f̂)`: the choice of `λ` is not written. Supply it. | closed |
| B3 | §1 | gap | "`f+f̂ ≠ 0` (considérer ses valeurs en des points voisins de `A(f)` et supérieur à celui-ci)" — a parenthetical, not an argument. Write it out. | closed |
| B4 | §1 | computation | `A(f+f̂) ≤ A(f) = A(f̂)`, and `f+f̂` is admissible: self-dual (uses `f̂̂=f` for even `f`) with `(f+f̂)(0) ≤ 0`. | closed |
| B5 | §1 | gap | `B₁ = inf A²(f+f̂)`: the passage from an infimum of products to an infimum of squares needs both inequalities, only one of which is indicated. | closed |
| B6 | §1 | computation | Normalising `f(0)=0` by subtracting `f(0)γ`: check `(f-f(0)γ)(0)=0`, self-duality, non-vanishing, and `A(f-f(0)γ) ≤ A(f)`. Note `f(0)<0` means a *positive* multiple of `γ` is added. | closed |
| B7 | §1, (1.1) | claim | The final reduced form of the problem. State it as a proposition, since everything later refers to it. | closed (reproduced) |
| B8 | Thm 1 | computation | `λ = -inf(sin x / x) = 0.2172…`, attained at the first positive root of `tan x = x`. **Recomputed: `x=4.4934094579`, `λ=0.2172336282`.** | closed |
| B9 | Thm 1 | computation | `A ≥ 1/(2(1+λ)) = 0.4107…`, `B₁ ≥ 0.1687…`. **Recomputed: 0.4107674882 and 0.1687299294.** | closed |
| B10 | Thm 1 pf | computation | Normalisation `∫|f| = 1` is legitimate by homogeneity: `A` is invariant under `f ↦ cf`, `c>0`. Say so. | closed |
| B11 | Thm 1 pf | computation | `∫f = f̂(0) = 0` hence `∫f⁺ = ∫f⁻ = ½`; and `∫f⁻ = ∫_{-A}^{A} f⁻` because `f ≥ 0` outside `[-A,A]`. | closed |
| B12 | Thm 1 pf | computation | `∫_{|x|≥A}|f| = ∫_{|x|≥A}f⁺ ≤ ½` hence `∫_{|x|≤A}|f| ≥ ½`. | closed |
| B13 | Thm 1 pf | computation | `‖f‖_∞ ≤ ∫|f̂| = 1` (uses self-duality and inversion), so `2A·1 ≥ ½`, i.e. `A ≥ ¼`. This is the crude bound the paper then refines. | closed |
| B14 | Thm 1 pf | claim | "On verra que cet argument s'étend aux dimensions supérieures" — forward reference to Theorem 3. Flag it as such. | closed |
| B15 | Thm 1 pf | computation | `f(x)=∫f(y)cos(2πyx)dy` (even + self-dual) `=∫f(y)(cos 2πyx-1)dy` (since `∫f=0`). | closed |
| B16 | Thm 1 pf | gap | The step to `f⁻(x) ≤ ∫f⁺(y)(1-cos 2πyx)dy` is stated as "ceci implique, les deux intégrales étant positives". Write the sign bookkeeping: `-f(x) = ∫f⁺(1-cos) - ∫f⁻(1-cos) ≤ ∫f⁺(1-cos)`, then `f⁻ = max(-f,0)` and the right side is `≥0`. | closed |
| B17 | Thm 1 pf | computation | `∫₀^A f⁻ = ¼` (evenness), and the Fubini step `∫₀^A∫f⁺(y)(1-cos2πyx)dy dx = ∫f⁺(y)[A - sin(2πyA)/(2πy)]dy`. Justify the interchange. | closed |
| B18 | Thm 1 pf | computation | `¼ ≤ (A/2)·sup_u(1-sin u/u) = (A/2)(1+λ)`: the substitution `u=2πyA` and `∫f⁺=½`. | closed |
| B19 | §1, (1.2)–(1.4) | claim | The four constants and the trivial inequalities among them. | closed |
| B20 | §1, before (1.5) | notation | **Printed slip.** "on en déduit que `𝓑₁⁻ ≤ B₁` soit `𝓑₁⁻ = B₁⁻`" — the displayed conclusion needs `𝓑₁⁻ ≤ B₁⁻`; `B₁` is a different constant. | closed |
| B21 | §1, (1.5) | gap | The mollification `φ=ψ*ψ`, `g=f*φ`, then "en performant la même opération sur `ĝ`". Self-duality is *not* preserved by one convolution; the second operation is what restores it. Write both steps and check `h=ĥ`, `h(0)<0`, `A(h) ≤ a+ε`. | closed |
| B22 | §1, (1.6) | computation | `T = δ_b+δ_{-b}+2δ₀` is a positive measure of positive type: `T̂ = 2cos(2πby)+2 ≥ 0`. | closed |
| B23 | §1, (1.6) | computation | `(T*f)(0) = f(b)+f(-b)+2f(0) = f(b)+f(-b) < 0`; the paper drops the `2f(0)` term silently because `f(0)=0` under (1.1). Say so. | closed |
| B24 | §1, (1.6) | gap | `g = T*f ≥ 0` on `[2a,∞)`: because `supp T ⊂ {0,±b}` with `b<a`, so for `x ≥ 2a` all three translates are `≥ a`. Not stated. | closed |
| B25 | §1, (1.6) | computation | `ĝ = T̂f̂ ≥ 0` on `[a,∞)` and `ĝ(0)=T̂(0)f̂(0)=0`. | closed |
| B26 | §1, (1.6) | gap | "Par dilatation, on obtient alors une fonction `h`" — the dilation balances the two thresholds `2a` and `a` at their geometric mean `a√2`. The scaling factor is not given. Supply it. | closed |
| B27 | §1, (1.6) | computation | **Printed slip.** "`B₁⁻ ≤ (a√2)² = 2a`" — the square is `2a²`, and `2a²` is what the argument needs to give `B₁⁻ ≤ 2B₁`. | closed |
| B28 | §1, (1.7) | computation | Assembling `B₁ ≤ 𝓑₁ ≤ 2B₁` from (1.2)–(1.6). Check the chain. | closed |

## C. §2 — upper bounds

| # | location | kind | statement | status |
|---|---|---|---|---|
| C1 | §2 | citation | Hermite functions: `H_n` are eigenfunctions of `ℱ` with eigenvalue `i^n`, `H_n(x)=e^{-πx²}P_n(x)`, `deg P_n = n`. State the normalisation used, and that `f=f̂` selects `n ≡ 0 (mod 4)`. | closed |
| C2 | §2 | gap | "Une combinaison linéaire convenable de `H₀` et `H₄` (telle que `f(0)=0`) donne `πA² ≤ 3`." The combination is never exhibited and the bound never computed. **Fill it**: this is a concrete, checkable claim. | closed |
| C3 | §2 | computation | "Plus loin, les calculs semblent difficiles et nous n'avons pas poursuivi cette voie" — record that the Hermite route is abandoned, and that the rest of §2 is a different construction. | closed (reproduced) |
| C4 | §2, (2.1) | computation | `g_a(x)=aγ(ax)+γ(x/a)-(1+a)γ(x)` is self-dual and `g_a(0)=0`. Verify using `(γ(a·))^ = a^{-1}γ(·/a)`. | closed |
| C5 | §2, (2.2) | claim | The superposition `∫₁^∞ g_a dτ(a)` as a candidate family, with the authors' own caveat that no usable characterisation of admissible `τ` is known. Reproduce, do not develop. | closed (reproduced) |
| C6 | §2, (2.3) | computation | `X=πx²`, `G_a(X)=ae^{-a²X}+e^{-a^{-2}X}-(1+a)e^{-X}`, `H_a(X)=e^XG_a(X)`. | closed |
| C7 | §2 | computation | `H_a` convex (both exponents real), `H_a(0)=0`, `H_a(+∞)=+∞`. | closed |
| C8 | §2 | computation | `H_a'(0) = -a^{-2}(a²-1)(a³-1) < 0` for `a>1`. **Verify the factorisation** against the direct derivative `a(1-a²)+(1-a^{-2})`. | closed |
| C9 | §2 | gap | Uniqueness of the positive zero `X_a`: convexity plus `H(0)=0`, `H'(0)<0` gives it, but the argument is not written. | closed |
| C10 | §2 | computation | `A(g_a)=√(X_a/π)`: the last sign change of `g_a` is at `X=X_a`. | closed |
| C11 | §2 | notation | **Printed slip.** In the `h`-expansion, `e^{X(2h-3h²+3h³-4h⁴)X}` carries a doubled `X`; and the series is written `P₁h+P₂h²+P₃h³+P₄h⁵+O(h⁵)`, where `P₄h⁴` is meant. | closed |
| C12 | §2 | computation | `P₁=0`, `P₂=2X(2X-3)`, `P₃=-X(2X-3)`, `P₄=-5X+15X²-(28/3)X³+(4/3)X⁴`. **All four recomputed and confirmed.** | closed |
| C13 | §2, (2.4)–(2.5) | computation | `lim_{a→1⁺}X_a = 3/2`, hence `A ≤ √(3/2π) = 0.6909883`. **Confirmed numerically.** | closed |
| C14 | §2 | computation | `P₄(3/2) = 3/2 > 0`, hence `X_a < 3/2` for small `h>0` — so (2.5) is not attained. **Confirmed.** | closed |
| C15 | §2 | gap | "Si `a→+∞`, `X_a→+∞` ; en fait, un calcul simple montre que `X_a = log a + O(1)`." The "calcul simple" is not given. | closed |
| C16 | §2 | computation | `a=√2`: reduction to `q³-(1+√2)q²+√2=0`, `q=e^{X/2}`, then the quadratic factor `q²-√2q-√2=0`, `q=(√2/2)(1+√(1+2√2))`, `X_a=2log q=1.4749…`. **Confirmed to 10 digits: 1.474957555.** Supply the factorisation step, which is omitted. | closed |
| C17 | §2 | computation | `a=2`: `q⁴-2(q⁴-1)/(q-1)=0`, `q=e^{3X/4}`, `q=2.9744…`, `X_a=1.4534…`. **Confirmed: q=2.974449245, X=1.453411859.** Supply the derivation of the quartic. | closed |
| C18 | §2 | computation | **Printed slip.** The extremum condition for the large-`a` surrogate is printed `a(1-a)=2log(1+a)`, which has no root `>1` (left side negative, right side positive). It must be `a(a-1)=2log(1+a)`, whose root **is** `a=2.081376974` as printed. | closed |
| C19 | §2 | claim | "Il est vraisemblable que c'est à peu près la valeur optimale accessible par cette méthode." **Recomputed: the true minimiser of `X_a` is `a ≈ 1.89` with `X ≈ 1.45200`, not `a=2.08137` (`X=1.45623`); `a=2` gives `1.45341`.** The value `2.08137` minimises the large-`a` *surrogate* `log(1+a)/(1-a^{-2})`, not `X_a` itself. The paper's hedging is fair, but the distinction should be drawn. | closed |
| C20 | §2 | gap | The correction argument: given `a₀` with `X₀=X_{a₀}` and `a` with `X_a>X₀`, there is `T>0` with `H_{a₀}-TH_a ≥ 0` on `[X_a,∞)` and `>0` on `[X₀,X_a)`, hence `≥0` from some `X'<X₀`. Three claims compressed into a paragraph; each needs writing, and the growth comparison `e^{(1-a^{-2})X}` needs `a<a₀`. | closed |
| C21 | §2, (2.6) | claim | "`X''=1.25…`, `A ≤ 0.63…`", with the authors' own caveat "nous n'avons fait qu'un calcul très approché". **Recomputed: with `a₀=2` and `a→1⁺` the method gives `X''=1.1512203`, `A ≤ 0.6053468`; optimising `a₀≈1.5–1.7` gives `X''≈1.1210`, `A ≤ 0.5973`.** So Theorem 2 is true but strictly weaker than its own method delivers. Record both, and do not silently improve the theorem. | closed |
| C22 | Thm 2 | claim | `A ≤ 0.64`, `B₁ ≤ 0.41`. Consistent with (2.6) and with our recomputation (`0.605² = 0.366 < 0.41`). | closed (reproduced) |

## D. §3 — higher dimensions

| # | location | kind | statement | status |
|---|---|---|---|---|
| D1 | §3, (3.1)–(3.2) | notation | The `d`-dimensional convention, and the normalisation of Haar measure on an abstract Euclidean space (unit cube of an orthonormal basis has measure 1). This is used in §4 and should be stated once. | closed |
| D2 | §3, (3.3) | claim | The conditions in dimension `d`, with `‖x‖ ≥ a_f`. | closed (reproduced) |
| D3 | §3 | gap | Radialisation: `f^#` = spherical average, `(f̂)^# = (f^#)^`, `A(f^#) ≤ A(f)`. The claim that `f^#` and `f̂^#` are not identically zero is argued by "sinon `f` et `f̂` seraient à support compact d'après 3)" — and then the contradiction (a function and its transform cannot both have compact support unless both vanish) is left unsaid. Supply both halves. | closed |
| D4 | §3, (3.4) | computation | `B_d = A²` with the infimum over radial self-dual `f` with `f(0)=0`. Same argument as §1, in `d` variables. | closed |
| D5 | §3 | notation | **Printed slip.** The label `(3.4)` is used twice: once for `B_d=A²` and once for `X(d)=d/2+1`. | closed |
| D6 | Thm 3 | claim | `B_d ≥ (1/π)((1/2)Γ(d/2+1))^{2/d} > d/(2πe)`. | closed (reproduced) |
| D7 | Thm 3 pf | gap | "Elle est calquée sur le cas `d=1`" — the proof is one sentence. Write it: `‖f‖_∞ ≤ 1`, `∫_{‖x‖≤A}|f| ≥ ½`, so `vol(B(0,A)) ≥ ½`, and `vol = π^{d/2}A^d/Γ(d/2+1)`. | closed |
| D8 | Thm 3 | computation | The strict inequality `(1/π)((1/2)Γ(d/2+1))^{2/d} > d/(2πe)`: needs `Γ(d/2+1)^{2/d} > d/(2e)·2^{2/d}`, i.e. a Stirling-type lower bound. Not proved in the paper. **Verified numerically for `d = 1,2,3,4,8,12,24,48,100`**; supply an argument. | closed |
| D9 | §3 | computation | `G_a`, `H_a` in dimension `d`: `H_a(X)=a^de^{(1-a²)X}+e^{(1-a^{-2})X}-(1+a^d)`. | closed |
| D10 | §3 | computation | Substitution `a²=1+k`, `d=2c`; derivative at the origin `(k/(1+k))(1-(1+k)^{c+1}) < 0`. | closed |
| D11 | §3 | computation | `P₁=0`, `P₂=X(X-c-1)`, `P₃=½(c-2)X(X-c-1)`, `P₄=(X/12){X³-(2c+6)X²+(3c(c-1)+18)X-(2c(c-1)(c-2)+12)}`. **All recomputed and confirmed.** | closed |
| D12 | §3 | computation | `X(d)=d/2+1` is the common zero of `P₂` and `P₃`; `P₂>0` above it, `<0` below; hence `lim_{a→1}X_a = d/2+1`. | closed |
| D13 | §3 | computation | `Q₄(c+1) = -c²+1`, where `P₄=(X/12)Q₄`. **Confirmed.** Hence `<0` for `d>2`, so `X_a > d/2+1` for `a` near 1. | closed |
| D14 | §3 | claim | "Il est donc possible que la valeur (3.4) soit optimale" for `d>2` — an explicit open guess. Candidate for `problems.json`. | closed (reproduced) |
| D15 | §3, (3.5) | computation | `d=2`: `Q₄(c+1)=0`, so the expansion must go to order 5 and 6. The residue computation for `q_n` via `w=z/(1+z)`. | closed |
| D16 | §3 | notation | The order-5 and order-6 coefficients are called `p₅, p₆` while the earlier coefficients are `P₁,…,P₄`. Different objects, near-identical names. | closed |
| D17 | §3, (3.6)–(3.9) | computation | `p₅=0` and `p₆=-4/45<0`. **Both recomputed exactly.** Hence `X_a > X(2)=2` for `a` near 1 in `d=2` as well. | closed |
| D18 | §3, (3.10) | computation | `B_d ≤ 𝓑_d ≤ (d+2)/2π`, from `A² ≤ X(d)/π`. | closed |
| D19 | §3 | gap | The `d`-dimensional version of (1.6): `T=δ_b+δ_{-b}+2δ₀` with `‖b‖<a`, `T̂=2cos(2πb·y)+2` "une onde plane positive", and the spherical average taken at the end to stay radial. Compressed to three lines; expand. | closed |
| D20 | Thm 4 | claim | `B_d ≤ 𝓑_d ≤ (d+2)/2π` and `B_d ≥ ½𝓑_d`. | closed (reproduced) |

## E. §4 — the arithmetic argument

| # | location | kind | statement | status |
|---|---|---|---|---|
| E1 | §4 | citation | Tate's thesis is used wholesale. State what is imported: adeles, ideles, the idele norm, self-dual local measures, the local transforms, and the functional equation (4.3). Reference [tate]. | **caution** |
| E2 | §4 | notation | Local conventions: `dz=2dxdy` at a complex place, `Tr(zw)=2Re(zw)`, `|z|=‖z‖²`. These differ from §3's Euclidean convention and the paper reconciles them in one sentence; make the reconciliation explicit. | closed |
| E3 | §4, (4.1) | notation | The decomposable test function; `f_v⁰ = char(𝒪_v)` at finite places. | closed (reproduced) |
| E4 | §4, (4.3) | citation | Tate's formula `Z(f,s)=∫_{I_F^+}f|x|^s + ∫_{I_F^+}f̂|x|^{1-s} + κf̂(0)/(s-1) - κf(0)/s`, with `κ` the residue of `ζ_F` at `s=1`. State hypotheses `(z₁),(z₂),(z₃)` and check they hold for the functions used. | closed (reproduced) |
| E5 | §4 | computation | `κ = 2^{r₁}(2π)^{r₂}hR/(√{D_F}w)` — the class number formula. Cite; do not re-derive. | **caution** |
| E6 | Lemma 1 | claim | If `ζ_F(s)=0` and `Re s>0` then `Z(f,s)=0` for every `f_∞ ∈ 𝒮(F_∞)`. | closed (reproduced) |
| E7 | Lemma 1 pf | gap | The proof is "`Z(f,s)=Z(f_∞,s)ζ_F(s)` for `Re s>1`, then analytic continuation". The factorisation itself is not derived, and the continuation argument needs `Z(f_∞,s)` holomorphic. Supply both. | closed |
| E8 | §4 | citation | `f̂_v⁰ = |𝔡_v|^{-1/2}char(𝔡_v^{-1})`, `∏_v|𝔡_v| = |D_F|` — standard, cite Tate. | **caution** |
| E9 | §4, (4.5)–(4.6) | computation | `f(x)≠0 ⟹ |x_f| ≤ 1 ⟹ |x_∞| ≥ 1`; and for `f̂`, `|x_f| ≤ |D_F| ⟹ |x_∞| ≥ D_F^{-1}`. Both use `|x|≥1` on `I_F^+`. | closed |
| E10 | Lemma 2 | claim | If a Fourier pair on `F_∞=ℝ^d` exists with `f ≥ 0` where `|x_∞|≥1`, `f>0` somewhere near the locus `|x_∞|=1`, `f̂ ≥ 0` where `|y_∞| ≥ D_F^{-1}`, and `f(0)=f̂(0)=0`, then `ζ_F` has no zero in `]0,1[`. | closed (reproduced) |
| E11 | Lemma 2 pf | gap | "(4.3) est alors réduit à ses termes intégraux" — because `f(0)=f̂(0)=0` kills the two polar terms. Then strict positivity of the first integral needs the "prend des valeurs strictement positives" hypothesis, and that is where it is used. Make the role of each hypothesis explicit. | closed |
| E12 | §4 | computation | AM–GM: `|x|^{2/d} ≤ (1/d)‖x‖²` from `|x|²=∏|x_v|²∏‖x_v‖⁴` and `‖x‖²=Σ|x_v|²+2Σ‖x_v‖²`. Check the bookkeeping of real versus complex places, where the factor 2 appears twice for different reasons. | closed |
| E13 | §4 | computation | Consequently `|x|≥1 ⟹ r ≥ √d` and `|y| ≥ |D_F|^{-1} ⟹ ρ ≥ |D_F|^{-1/d}√d`. | closed |
| E14 | Prop 1 | claim | If `ζ_F` has a zero in `]0,1[` then `𝓑_d ≥ d|D|^{-1/d}`. Note this bounds the *product* `A(f)A(f̂)`, which is what `𝓑_d` is. | closed |
| E15 | Prop 1 pf | gap | "La démonstration est maintenant évidente" — it is the contrapositive of Lemma 2 plus E13, and it needs the radial reduction of §3. Write it. | closed |
| E16 | §4 | citation | Armitage's example: a degree-12 extension `F` of `E=ℚ(√(3(1+i)))`, hence degree 48 over `ℚ`, built by Serre, with `ζ_F(1/2)=0`. Cite [armi] §5 and [serre]; verify the degrees stated. | **caution** |
| E17 | Prop 2 | claim | If `48 | d` then `𝓑_d > 0`. | closed (reproduced) |
| E18 | Prop 2 pf | gap | The lifting `d=48c`: a cyclotomic `L/ℚ` of degree `c` linearly disjoint from `F`, then `ζ_F | ζ_{LF}` since `LF/F` is abelian. Two facts are used silently: existence of a disjoint cyclotomic field of each degree, and the factorisation of `ζ_{LF}` into Dirichlet `L`-functions over `F`. | closed |
| E19 | §4, (4.7) | computation | If `ζ_F` has a real zero then `|D|^{1/d} ≥ d/𝓑_d`. | closed (reproduced) |
| E20 | §4 | computation | `d/𝓑_d < 2πe = 17.079…` from Theorem 3 (via `𝓑_d ≥ B_d ≥ d/(2πe)`). Check the direction of each inequality. | closed |
| E21 | §4 | citation | **Printed slip.** Odlyzko's bound is written `|D|^{1/d} ≥ 22.2(1+0(d))`; `o(1)` is meant. Cite [odly] and state the bound correctly. | **caution** |
| E22 | §4 | claim | Since `22.2 > 17.079`, (4.7) is automatic, so Proposition 2 yields no new bound on `𝓑_d`. The authors say so; record that this is a negative result, deliberately included. | closed |
| E23 | §4 | citation | Golod–Shafarevich and Brumer: an infinite class field tower `E_p^1 ⊂ E_p^2 ⊂ ⋯` with `E_p^1/ℚ` of degree `p(p-1)` and each `E_p^{n+1}/E_p^n` abelian unramified of degree `p`. Cite [roqu] Cor. 7. | **caution** |
| E24 | §4, (4.8) | computation | `D(F_m)=D(F_0)^{p^m}` for an unramified tower — the conductor–discriminant / tower formula. State the version used. | closed |
| E25 | §4, (4.9) | computation | `𝓑_d ≥ Cd` with `C=|D|^{-1/d₀}` along `d=d₀p^m`. **Printed slip**: the exponent is typeset `-1_/d_0`. | closed |
| E26 | §4 | notation | **Printed slip.** "(3.10) et (4.8) montrent donc que la croissance de `𝓑_d` est linéaire" — (3.10) is the upper bound and (4.9), not (4.8), is the lower bound just derived. | closed |
| E27 | §4 | claim | The closing point, which is the reason the section exists: for these degrees, number theory *already implied* the linear growth of Theorem 3. Make sure this lands, since it is easy to lose in the details. | closed |
| E28 | §4 | claim | The final remark on `p ∤ D_F`, linear disjointness, and `d=48(p-1)p^n`, with Artin/Dedekind conjectures removing the `(p-1)`. | closed (reproduced) |

## F. Cross-cutting

| # | location | kind | statement | status |
|---|---|---|---|---|
| F1 | source | notation | `\bb` and `\Bb` are both defined as `\mathcal{B}` (lines 25 and 32 of the source), so `\bb_d` and `\Bb_d` render identically. In §4 both spellings appear for the same constant. | closed |
| F2 | source | notation | Two stray `0xCA` bytes (Mac Roman non-breaking space) at lines 58 and 400; the file is ISO-8859, not UTF-8. | closed |
| F3 | source | notation | `\usepackage[francais]{babel}` — deprecated spelling; the file does not compile on a modern distribution without `[french]`. | closed |
| F4 | throughout | notation | The paper mixes `≥ 0` "beyond `a`" in the sense of the threshold and in the sense of the infimum of thresholds. Fix one usage in the digestion. | closed (reproduced) |
| F5 | §1 vs §3 | notation | `γ` denotes `e^{-πx²}` in dimension 1 and `e^{-π‖x‖²}` in dimension `d`; harmless but state it. | closed |
| F6 | throughout | claim | The digestion is in English; the original is French and is preserved verbatim. Every quotation is given in French with a translation. | closed (reproduced) |
