# Ideas in Bourgain, Clozel & Kahane, *Principe d'Heisenberg et fonctions positives*

Ann. Inst. Fourier **60** (2010), 1215–1232. Zbl 1298.11105, arXiv 0811.4360.

Digested from `the-heisenberg-principle-and-positive-functions-expanded.tex`
(21 pages, 110 ledger rows). **Pass 1: 70 rows. Pass 2: 48. Pass 3 and 3½: 11.**

Of the 11, **four were already in the toolkit** and gain this paper; **seven are new**.
The toolkit goes from 13 entries to 20. That is a high proportion of new entries and
it needs saying why: the only other digested paper is the 1990 Bourgain–Wolff note on
harmonic gradients, a construction in potential theory. This paper is an extremal
problem in Fourier analysis with an arithmetic second half. The two barely intersect,
so the existing vocabulary had little to say about it. Expect the ratio to reverse as
the catalogue fills.

---

## Kept

### Invariance normalisation — toolkit: `scaling-normalisation` (existing, **widened**)

**Where.** §1.2(a) and Background (dilation); again at §1.4 to balance the pair
`(2a, a)`; again in §3 with the exponent `λ^d`; and in the reparametrisations of §2.2.

**The move.** The quantity under study, `a_f · a_f̂`, is invariant under
`f(x) ↦ f(x/λ)`. Three separate uses follow. *First*, each threshold on its own can be
driven to zero, so no statement about a single threshold can be true — only the product
is a real invariant, and that is precisely why Theorem 1 is not obvious. *Second*,
choosing `λ = (A(f̂)/A(f))^{1/2}` equalises the two thresholds at no cost, cutting the
problem from two parameters to one. *Third*, when a construction leaves the two sides
with unequal thresholds `2a` and `a`, the dilation `λ = 1/√2` balances them at `a√2`,
and the loss is exactly the geometric mean.

**Why it widens the entry.** The entry was about dilations. §2.2 does the same thing
with a different group: the last sign change of `g_a` is unchanged by multiplication by
a strictly positive function, so the paper multiplies by `e^X` and turns a combination
of Gaussians into `H_a(X) = a e^{(1−a²)X} + e^{(1−a^{−2})X} − 1 − a`, a sum of two
exponentials and a constant — for which convexity, `H(0)=0`, `H'(0)<0` and
`H(+∞)=+∞` immediately give a unique positive zero. Same manoeuvre, different
invariance group. The gloss now names the group rather than the dilation.

**What it buys.** Two parameters become one; a transcendental sign question becomes
convexity.

---

### Symmetrisation into an invariant class — toolkit: `symmetrisation-to-fixed-space` (**new**)

**Where.** §1.2(b), §2.1, §3 — three distinct instances in one paper.

**The move.** Three times the paper replaces an object by an average of its images
under the symmetry in play, landing in the fixed subspace.

1. *`f + f̂`.* The problem concerns a pair. Since `(f+f̂)^ = f̂+f`, the sum is its own
   transform, and `A(f+f̂) ≤ A(f) = A(f̂)` once the thresholds are equalised. A problem
   about pairs becomes a problem about one self-dual function: `B₁ = A²`.
2. *The Hermite eigenspace.* `F` has eigenvalues `i^n` on `H_n`, so self-duality means
   the expansion is supported on `n ≡ 0 (mod 4)`. Searching for a self-dual function
   becomes searching one eigenspace, and in the span of `H₀, H₂, H₄` it is a
   two-line coefficient match.
3. *Spherical averaging.* In §3, `f^#` is the average over the rotation group;
   `(f^#)^ = (f̂)^#` because `F` commutes with rotations, and `A(f^#) ≤ A(f)`. The
   problem reduces to radial functions, hence to one variable in any dimension.

**Why it is not routine.** In all three cases the averaging is the easy half. The step
that needs work is **non-degeneracy** — that the symmetrised object is not zero — and
in all three cases the paper argues it the same way: if it vanished, `f` would be
supported in a ball, hence `f̂` too, hence `f ≡ 0`. The digestion supplies that
argument twice where the original leaves it implicit (ledger B3, D3).

**What it buys.** Two functions become one; all functions become radial; an
infinite-dimensional search becomes finite-dimensional.

---

### Mass forces volume — toolkit: `mass-volume-bound` (**new**)

**Where.** Proof of Theorem 1 (the bound `A ≥ 1/4`); proof of Theorem 3, where it is
the whole proof.

**The move.** Normalise `∫|f| = 1`. Because `f̂(0) = ∫f = 0`, the positive and negative
parts each carry mass exactly `1/2`; because `f ≥ 0` outside the ball of radius `A`,
all of the negative mass sits inside it, so the ball carries at least half the total.
Meanwhile `‖f‖_∞ ≤ ‖f̂‖₁ = ‖f‖₁ = 1` — the sup bound is *free*, delivered by
self-duality rather than assumed. A set carrying mass `1/2` under a function bounded by
`1` has measure at least `1/2`. In dimension 1 that is `2A ≥ 1/2`. In dimension `d` it
is `vol B(0,A) ≥ 1/2`, i.e. `π^{d/2} A^d / Γ(d/2+1) ≥ 1/2`, which is Theorem 3.

**Why it is not routine.** The soft argument produces the paper's *sharp* dimensional
growth. The ball of radius `A` is exponentially small in `d`, so demanding that it hold
half the mass forces `A` to grow — and Stirling converts the Gamma function into the
readable `B_d > d/(2πe)`. §4 then shows this crude bound has the right growth rate.

**What it buys.** Positivity of `B_d`, and its linear growth, from two lines.

---

### Leading coefficient decides — toolkit: `leading-coefficient-sign` (**new**)

**Where.** §2.2 (`a = 1+h`, order 4); §3 (`a² = 1+k`, order 4); §3 again for `d = 2`,
where order 4 is not enough and the expansion is pushed to order 6.

**The move.** Expand `H_a(X)` in the perturbation parameter about the degenerate value
`a = 1`. The first coefficients vanish identically at the critical `X` — that vanishing
is what makes `X` critical — and the sign of the first survivor says which way the zero
`X_a` actually moves.

- `d = 1`: `P₂` and `P₃` vanish at `X = 3/2` and `P₄(3/2) = +3/2 > 0`, so `H_a(3/2) > 0`
  for small `h ≠ 0`, forcing `X_a < 3/2`. **The limit can be beaten.**
- `d > 2`: with `P₄ = (X/12)Q₄`, one finds `Q₄(c+1) = −c²+1 < 0`, so `X_a > X(d)`.
  **The limit cannot be beaten by this family** — the opposite direction.
- `d = 2`: `Q₄(c+1) = 0` exactly. The order-4 test is silent, and the expansion must be
  carried to order 6. The residue theorem, via the Möbius substitution `w = z/(1+z)`
  which turns `e^{2z/(1+z)}` into `e^{2w}`, gives `p₅ = 0` and `p₆ = −4/45 < 0`. So
  `d = 2` sides with high dimension.

**Why it is not routine.** The order of vanishing is the answer, not an obstacle to it.
That `d = 2` requires two more orders than either neighbour is exactly the statement
that 2 is the threshold dimension.

**What it buys.** Whether `X(d) = d/2 + 1` is a barrier or merely a limit — and the
answer differs with the dimension.

---

### Convolution by a positive-type measure — toolkit: `positive-type-convolution` (**new**)

**Where.** §1.4, proof of `B₁⁻ ≤ 2B₁`; and §3, the same argument with `b` a vector.

**The move.** Take `T = δ_b + δ_{−b} + 2δ₀`, with `f(b) < 0` and `0 < b < a`. It is a
positive measure, and `T̂ = 2cos(2πby) + 2 ≥ 0` — positive *and* of positive type. So
convolving by `T` preserves one-sided positivity on both sides at once: on the space
side because `T ≥ 0`, on the transform side because `ĝ = T̂ f̂` multiplies by a
non-negative symbol. Meanwhile `(T*f)(0) = f(b) + f(−b) + 2f(0) < 0`, which is the
point — the value at the origin is moved strictly negative, crossing between the two
classes whose constants are being compared.

**Why it is not routine.** The atom at the origin is not decoration: its coefficient is
what makes `T̂ ≥ 0` rather than merely real. And the two sides are enlarged by
*different* amounts — the space side to `2a`, the transform side only to `a` — so the
manoeuvre is incomplete without the rebalancing dilation. That mismatch is the entire
source of the factor 2 in `B₁ ≤ 𝓑₁ ≤ 2B₁`.

**What it buys.** Comparability of the constant over `f(0) = 0` with the constant over
`f(0) < 0`, at the cost of a factor 2.

---

### Regularise at epsilon cost — toolkit: `regularisation-at-epsilon-cost` (**new**)

**Where.** §1.4, `𝓑₁⁻ = B₁⁻`.

**The move.** Show the constant over `L¹` equals the constant over the Schwartz class
by mollifying. Convolving with `φ = ψ*ψ` moves `A` by `ε` and preserves the sign at the
origin.

**Why it is not routine.** Mollification is a reflex; what is not is that the class is
defined by **self-duality**, which mollification destroys — `g = f*φ` has
`ĝ = f̂ φ̂`, a *product* where a convolution was needed. The repair is to perform the
operation on both sides: with `ψ` real and even, `h = (f*φ)·φ̂` satisfies `ĥ = h`. The
paper says only "performing the same operation on `ĝ`"; the digestion spells out why
one pass cannot work (ledger B21). Note also where this argument **fails**: it does not
apply when `f(0) = 0`, which is exactly why the separate constant `B₁⁻` and the
positive-type convolution above are needed at all.

**What it buys.** The `L¹` and Schwartz problems are the same problem — where the
symmetry can be restored; a factor 2 apart where it cannot.

---

### Iterative correction — toolkit: `iterative-correction` (existing, **widened**)

**Where.** §2.3, the correction giving Theorem 2.

**The move.** The family `g_a` does not reach `A`. Take `a₀` minimising `X_{a₀}`, and
`a < a₀` with `X_a > X₀`. On `[X_a, ∞)` both `H_{a₀}` and `H_a` are `≥ 0`, but
`H_{a₀}` grows like `e^{(1−a₀^{−2})X}` and `H_a` like `e^{(1−a^{−2})X}` — and since
`a < a₀` the corrector is **dominated at infinity**. So `H_{a₀}/H_a → +∞`, the infimum
`T = inf_{X ≥ X_a} H_{a₀}/H_a` is strictly positive, and `H_{a₀} − T H_a ≥ 0` on
`[X_a, ∞)`. On `[X₀, X_a)` the corrector is *negative*, so the difference is strictly
positive there, and by continuity it stays positive slightly to the left of `X₀`. The
last sign change has moved left: that is the gain.

**Why it widens the entry.** The entry was written from a paper that iterates a
correction infinitely often and needs a stage-uniform gain. Here a **single** step is
taken, and the interesting content is what makes the correction admissible: a growth
comparison at infinity, the corrector dominated exactly where the constraint has to
survive. That mechanism is the general one; the iteration is a special case of using it
repeatedly. The gloss now leads with the single step.

**What it buys.** `A ≤ 0.64` (and, optimised, `A ≤ 0.5973` — see §5(2) of the
digestion, where the paper's own method beats the paper's own theorem).

---

### Dimension threshold — toolkit: `dimension-threshold` (existing, **gloss extended**)

**Where.** §3, in the sign of `Q₄(c+1) = −c²+1`.

**The move.** The family `g_a` improves on its limiting value `X(d) = d/2+1` when
`d = 1`, and fails to when `d > 2`. The threshold is `d = 2`, where the deciding
coefficient is **exactly zero** and the question is settled two orders later by
`p₆ = −4/45 < 0`, putting `d = 2` on the high-dimensional side.

**Why it extends the entry.** The entry described a statement true above a dimension
and false below. This paper shows the *mechanism* by which the threshold announces
itself: the coefficient that decides the question vanishes identically at the threshold
dimension, so the borderline case must be carried to a higher order than either side
requires. That is a diagnostic worth having — when an expansion degenerates at one
value of `d`, that value is the threshold.

---

### Extremal datum reused at every scale — toolkit: `extremal-datum` (existing, **gloss extended**)

**Where.** §2.1 (the explicit Hermite extremiser) and §4.3 (Armitage's field).

**The move, twice.** The digestion carries out the Hermite computation the paper
describes but does not perform, and gets the unique self-dual combination of
`H₀, H₂, H₄` vanishing at the origin:

    f(x) = x²(x² − 3/(2π)) e^{−πx²},   last sign change at √(3/(2π)),   πA² = 3/2.

That single explicit function does three jobs: it proves the problem is not vacuous
(§1.1, which the paper asserts with "de tels couples existent à l'évidence"), it gives
an upper bound, and it turns out to give *exactly* the bound `(2.5)` that the `g_a`
family reaches by a completely different route — a coincidence the paper does not
remark on.

In §4 the same role is played by an arithmetic object: Armitage's degree-48 field with
`ζ_F(1/2) = 0`, whose existence is the hardest input of the section and is **quoted,
not proved** — it sits inside the digestion's `caution` block.

**Why it extends the entry.** The entry was phrased for an analytic building block
inserted at every scale. The role — one object with an exceptional property, carrying
the whole force of the argument, usually imported rather than constructed — is
identical when the object is a number field. The gloss now says so.

---

### Positivity against a functional equation — toolkit: `functional-equation-positivity` (**new**)

**Where.** §4, Lemmas 1 and 2 and Proposition 1. The intellectual core of the paper.

**The move.** Tate's formula writes the zeta integral as

    Z(f,s) = ∫_{I_F^+} f|x|^s + ∫_{I_F^+} f̂|x|^{1−s} + κ f̂(0)/(s−1) − κ f(0)/s.

Now impose exactly the conditions of the Fourier problem. `f(0) = f̂(0) = 0` kills both
polar terms — the normalisation that looked like a convenience in §1 is the
arithmetically essential one. One-sided positivity of `f` and of `f̂` makes both
integrals `≥ 0`. A single further hypothesis — that `f > 0` on an open piece of
`{|x_∞| = 1}` — upgrades one of them to `> 0`. Hence `Z(f,s) > 0` for real
`s ∈ ]0,1[`. But `Z(f,s) = Z(f_∞,s) ζ_F(s)` vanishes wherever `ζ_F` does. So `ζ_F` has
no zero in `]0,1[`.

**Why it is not routine.** Every hypothesis does exactly one job and the digestion
tabulates which (ledger E11); strictness in particular has to come from somewhere, and
there is only one place it can. The *asymmetry* is where the arithmetic enters: the
first integral is supported on `|x_∞| ≥ 1`, the second only on `|x_∞| ≥ D_F^{−1}`,
because `f̂_v` lives on the inverse different and `∏_v |𝔡_v| = |D_F|`. That gap between
`1` and `D_F^{−1}` is what puts the discriminant into the conclusion.

The hinge back to §3 is an AM–GM applied to the right `d` quantities — each complex
place contributing its `‖x_v‖²` **twice** — giving `|x|^{2/d} ≤ ‖x‖²/d`, which converts
the multiplicative idele norm into the additive Euclidean norm and so turns the adelic
hypotheses into the radial hypotheses of §3. Running the whole thing backwards gives
Proposition 1: a field whose zeta has a real zero forces `𝓑_d ≥ d|D|^{−1/d}`.

**What it buys.** The extremal Fourier problem *is* a question about zeros of zeta
functions. It also buys a **negative** result the authors include deliberately: since
Odlyzko gives `|D|^{1/d} ≥ 22.2(1+o(1))` while Theorem 3 gives `d/𝓑_d < 2πe = 17.08`,
the resulting inequality is automatic and yields nothing new.

---

### Propagation along a tower — toolkit: `tower-propagation` (**new**)

**Where.** §4.3, Proposition 2 and the closing argument.

**The move, twice.** One field of degree 48 has to become infinitely many degrees.

1. *Multiples of 48.* For `d = 48c`, take a cyclotomic `L/ℚ` of degree `c` linearly
   disjoint from `F`. Then `LF/F` is abelian, so `ζ_{LF}` factors into Dirichlet
   `L`-functions over `F` and `ζ_F | ζ_{LF}` — the zero is **inherited**. The digestion
   supplies both silent steps: that a cyclotomic field of *each* degree `c` exists (take
   the degree-`c` subfield of `ℚ(ζ_p)` for `p ≡ 1 mod c`), and the factorisation itself
   (ledger E18).
2. *Linear growth.* By Golod–Šafarevič and Brumer there is an infinite tower with each
   step abelian, unramified, of degree `p`. Inheritance again gives `ζ_F | ζ_{F_m}`. The
   second half is the real content: with no fresh ramification, `D(F_m) = D(F₀)^{p^m}`,
   so the **root discriminant** `|D(F_m)|^{1/d}` is *constant* along the tower. Feeding
   that into Proposition 1 gives `𝓑_d ≥ Cd` with `C = |D|^{−1/d₀}` independent of `m`.

**Why it is not routine.** Inheritance alone gives nothing: without the discriminant
growing at exactly the rate that keeps its normalised form constant, the bound would
decay and the tower would be useless. The point of §4, easy to lose in the machinery:
along an infinite sequence of degrees, the linear growth of Theorem 3 was already
implied by known facts about ramification — so it is not an artefact of the crude
volume bound of `mass-volume-bound`, it is the truth.

**What it buys.** From one exceptional field, a linear lower bound along an infinite
sequence of dimensions.

---

## Discarded, with reasons

| keyword | why cut |
|---|---|
| positive/negative part split `f = f⁺ − f⁻` | Routine bookkeeping. |
| Tonelli interchange in the `∫₀^A` step | Non-negative integrand, evident hypotheses. |
| differentiating `γ' = −2πxγ` repeatedly | Mechanical; the Hermite computation is the idea, not this. |
| coefficient matching for self-duality | Linear algebra; the *observation* that the `x²` and constant conditions coincide is a pleasant accident, not a technique. |
| analytic continuation by the identity theorem | Standard, and the hypotheses are evident. |
| Proposition 1 is the contrapositive of Lemma 2 | Logic, not technique. |
| change of variable `X = πx²` | A substitution. Merged into `scaling-normalisation`, where the content (multiply by `e^X`, which does not move sign changes) actually lives. |
| convexity gives a unique zero | A convex function with `H(0)=0`, `H'(0)<0`, `H(∞)=∞` has one positive zero. A competent reader chooses this unprompted. Folded into `scaling-normalisation` as what the reparametrisation is *for*. |
| subtracting `∫f = 0` to insert the `−1` in `cos2πyx − 1` | Real but local: it makes the kernel `1 − cos ≥ 0` sign-definite. A good remark, and pitched too low to recur as its own entry. |
| `AM–GM` from idele norm to Euclidean norm | Kept as evidence *inside* `functional-equation-positivity`, where it is the hinge, rather than as a separate entry — on its own it is AM–GM. |
| the surrogate `log(1+a)/(1−a^{−2})` and its minimiser `a = 2.08137` | Optimising a tractable asymptotic stand-in is real, but here it is a remark with a caution attached: the surrogate's minimiser is **not** the true minimiser of `X_a` (which is `a ≈ 1.89`). Recorded in the digestion, §5(3), not in the toolkit. |
| `B₁ ≤ 𝓑₁ ≤ 2B₁` as a statement | The *output* of `positive-type-convolution` and `regularisation-at-epsilon-cost`, not a move of its own. |
| "two independently-known constants show a method is vacuous" (`22.2 > 2πe`) | Genuinely instructive — the authors include the negative result on purpose — but it is a remark about this comparison, not a technique anyone would go looking for. |
| plane wave `T̂ = 2cos(2πb·y)+2` is not radial | A detail of the `d`-dimensional bookkeeping; folded into `positive-type-convolution`. |
| superposition `∫₁^∞ g_a dτ(a)` over the family | The paper raises it and abandons it — "it seems difficult to determine a simple characteristic property of `τ`". Not enough content to name; recorded as an open direction in `notes.md`. |
