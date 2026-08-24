# Ledger — Bourgain–Wolff, *A remark on gradients of harmonic functions in dimension ≥ 3*

Source: IHES/M/89/31 (September 1989), 11 pages, transcribed in
`a-remark-on-gradients-of-harmonic-functions-in-dimension-3-original.tex`.

One row per item. `kind` ∈ {claim, computation, citation, gap, notation}.
A **gap** is a step whose justification is not on the page. The digestion is
finished when every row is `closed`, or is `OPEN-GAP` and visible as a
`caution` block in the PDF.

Locations are pages of the preprint (paper pagination, not PDF pagination).

---

## Status summary

| status | count |
|---|---:|
| closed | 80 |
| **OPEN-GAP** | 1 |
| open | 1 |

**OPEN-GAP: B4** — the Alexandrov–Kargaev inequality, imported from a reference we
could not obtain. Visible as a `caution` block in §2.2 of the expansion. §9(5)
records a formal leading-order computation consistent with it for *d* ≥ 3; that is
not a proof and does not close this row.

**Open: E4** — reference [1], Aleksandrov–Kargaev, cited as "private communication".
A candidate published form is recorded in the row (Zbl 0842.42012: right authors,
subject and period), but we have not read it and cannot confirm it carries the
inequality B4 needs. Bibliographic, not mathematical; it does not block the
digestion. Reference [2] (row E5) **is** now identified: Wolff, Princeton Math. Ser.
42 (1995), Zbl 0836.31004.

*Every other row is closed in the expansion, at the `\Ledger{...}` marker carrying
its id. Passes run: skeleton, expansion, computation, adversarial (three sweeps),
reader, ledger, size.*

---

## A. Statement and framing

| # | location | kind | statement | status |
|---|---|---|---|---|
| A1 | Thm, p.1 | notation | `C'` is printed where $C^1$ is meant. | closed |
| A2 | Thm, p.1 | gap | The theorem as literally stated is satisfied by $f\equiv 0$. Nontriviality is never asserted. Fill: choose $u_0\not\equiv 0$; every modification is supported inside $Q(1)$, so $f=u_0$ off $Q(1)$ and $f\not\equiv 0$. | closed |
| A3 | Thm, p.1 | gap | "$f$ and $\nabla f$ vanish": $f$ is the boundary value, $\nabla f$ the full gradient of the harmonic extension up to the boundary. State the meaning precisely, including which one-sided limits are asserted to exist. | closed |
| A4 | Thm, p.1 | notation | $d/dn$: fix the sign convention (inward vs outward normal) once, at first use, and check every later display against it. | closed |
| A5 | p.1 | notation | $\mathbb{R}^d_+$, $Q(N)=[-N/2,N/2]^{d-1}$, $Q(1)$, $D(0,r)$, $\ell(Q)$, $a_Q$, $\nabla_T$, $\mathcal H_n$, $\mathcal Q_n$, $V_n$: collect in one notation block. | closed |
| A6 | p.1 | gap | Where is $d\ge 3$ used? At least at R20/C13 (convergence of $\sum\varepsilon_n^{(d-1)/2}$ needs $d-1\ge 2$). Whether Lemma 1 also needs it is *not* visible from this paper — it sits inside the imported [1]. Record honestly; do not claim to have located every use. | closed |

## B. Lemma 1 — the Alexandrov–Kargaev building block

| # | location | kind | statement | status |
|---|---|---|---|---|
| B1 | L1 stmt, p.1 | notation | `|x| ⊂ ε^{1/2}` printed for `|x| < ε^{1/2}`. | closed |
| B2 | L1 stmt, p.2 | notation | `∇f̂_ε` printed; the restatement on p.4 uses $F$, so $\widehat F_\varepsilon$ is meant. (N1) | closed |
| B3 | L1 stmt, p.1–2 | gap | Quantifier order. Make explicit: $\exists p_0=p_0(d)>0$ such that $\forall p\in(0,p_0)$ $\exists\eta=\eta(p,d)>0$ and $\varepsilon_0(p,d)$ with the conclusion for all $\varepsilon<\varepsilon_0$. As printed the dependence of $\eta$ on $p$ is left to context. | closed |
| B4 | proof, p.2 | citation | **The import.** [1] supplies $\int(|1+dG_\varepsilon/dn|^p-1)\,dx<-2M<0$ for $p$ below a critical number and $\varepsilon$ small. Reference is "private communication (to appear)" — unavailable. State as a hypothesis in Background; it cannot be checked here. Candidate `OPEN-GAP`. | **OPEN-GAP** |
| B5 | proof, p.2 | computation | $G_\varepsilon(x)=-(\varepsilon+x_d)/|x+\varepsilon e_d|^d$ is harmonic on $\{x_d>-\varepsilon\}$, hence on a neighbourhood of $\overline{\mathbb{R}^d_+}$: it is $-1/c_d$ times the Poisson kernel translated by $\varepsilon e_d$. Verify. | closed |
| B6 | proof, p.2 | notation | $M$ (from [1]) versus $\eta$ (in the conclusion): the proof silently sets $\eta:=M$. Say so. | closed |
| B7 | proof, p.2 | computation | Construct the partition $\{\psi_j\}$: $\operatorname{supp}\psi_j\subset\{2^{j-1}\delta\le|x|\le 2^{j+1}\delta\}$, $\sum_j\psi_j=1$ for $|x|>\delta$, $|\nabla^k\psi_j|\lesssim(2^j\delta)^{-k}$. Existence is asserted, not built. | closed |
| B8 | proof, p.2 | computation | $\psi=0$ on $\{|x|<\delta/2\}$ and $\psi=1$ on $\{|x|>\delta\}$, hence $F_\varepsilon=(1-\psi)G_\varepsilon$ has $\operatorname{supp}F_\varepsilon\subset D(0,\delta)=D(0,\varepsilon^{1/2})$, matching the statement. Verify; also that $F_\varepsilon$ is smooth. | closed |
| B9 | proof, p.2 | computation | $|\nabla_T^k G_\varepsilon|\le\varepsilon|x|^{-(d+k)}$, $k=0,1,2$, on $\mathbb{R}^{d-1}$. Check $k=0$: $|G_\varepsilon|=\varepsilon(|x|^2+\varepsilon^2)^{-d/2}\le\varepsilon|x|^{-d}$. Do $k=1,2$. | closed |
| B10 | proof, p.2 | computation | $|\nabla_T^k\rho^j_\varepsilon|\lesssim\varepsilon(2^j\delta)^{-(d+k)}$ by Leibniz, using $|x|\sim 2^j\delta$ on $\operatorname{supp}\psi_j$. | closed |
| B11 | proof, p.2 | computation | $\|\nabla_T\rho^j_\varepsilon\|_1\lesssim\varepsilon(2^j\delta)^{-2}$: pointwise bound $\times$ measure $(2^j\delta)^{d-1}$ of the annulus. | closed |
| B12 | proof, p.2 | computation | $\|\nabla_T\rho^j_\varepsilon\|_{C^\alpha}\lesssim\varepsilon(2^j\delta)^{-(d+1+\alpha)}$; state which $\alpha$ and that it is fixed once. | closed |
| B13 | proof, p.2 | gap | **The mechanism is left implicit.** $d/dn$ of the harmonic extension is the Dirichlet-to-Neumann operator $|\nabla|=\sum_k R_k\partial_k$ ($R_k$ = Riesz transforms). That is why $L^1\!\to$ weak-$L^1$ and $C^\alpha$ bounds for the Riesz transforms apply to $d\widehat{\rho^j_\varepsilon}/dn$ in terms of $\nabla_T\rho^j_\varepsilon$. Supply this. | closed |
| B14 | proof, p.2 | citation | State the two imported facts in Background with hypotheses: Riesz transforms are weak-$(1,1)$; Riesz transforms are bounded on $C^\alpha$, $0<\alpha<1$. | closed |
| B15 | proof, p.2 | gap | "the weak type 1 estimate implies this holds for *some* $x$ … and the Hölder estimate extends it to *all* such $x$". Write the argument: with $\lambda=\varepsilon(2^j\delta)^{-(d+1)}$ the exceptional set has measure $<(2^j\delta)^{d-1}$, which must be compared against the measure of $D(0,2\cdot 2^{j+1}\delta)$. **Constants matter here**; if they do not close, this becomes a `caution`. | closed |
| B16 | proof, p.3 | computation | $|x|>2\cdot 2^{j+1}\delta$: $|d\widehat{\rho^j}/dn(x)|=|c\int_{|y|<2^{j+1}\delta}|x-y|^{-d}\rho^j(y)dy|\lesssim|x|^{-d}\|\rho^j\|_1\lesssim\varepsilon(2^j\delta)^{-1}|x|^{-d}$. Verify, and justify the representation formula away from the support. | closed |
| B17 | proof, p.3 | computation | Summation over $j$ giving $(*)$: $|d\widehat\rho_\varepsilon/dn|\lesssim\varepsilon\delta^{-1}\min(\delta^{-d},|x|^{-d})$. Check the geometric sum is dominated by $j=0$. | closed |
| B18 | proof, p.3 | computation | The splitting $\int(|1+dF/dn|^p-1)=(\int(|1+dG/dn|^p-1))+(\int|1+dF/dn|^p-|1+dG/dn|^p)$ uses $dF_\varepsilon/dn=dG_\varepsilon/dn-d\rho_\varepsilon/dn$. State it. | closed |
| B19 | proof, p.3 | computation | $\big||1+a|^p-|1+b|^p\big|\le|a-b|^p$ for $0<p\le 1$. Prove (subadditivity of $t\mapsto t^p$). | closed |
| B20 | proof, p.3 | computation | $\int_{|x|\le1}|d\rho_\varepsilon/dn|^p\to0$. Splitting at $|x|=\delta$ gives $\varepsilon^{(d-1)(1-p)/2}$ from the inner region and $\varepsilon^{p/2}$ from the outer, the latter needing $p<(d-1)/d$ for convergence. **The paper says only "for small $p$"; record the explicit constraint $p<\min(1,(d-1)/d)=(d-1)/d$.** | closed |
| B21 | proof, p.3 | gap | "When $|x|>1$ we have a lower hand for $|1+dG_\varepsilon/dn|$" — "hand" is printed for "bound". Supply the bound: $dG_\varepsilon/dn\to0$ as $|x|\to\infty$, so $|1+dG_\varepsilon/dn|\ge\frac12$ for $|x|>1$ and $\varepsilon$ small. Compute. | closed |
| B22 | proof, p.3 | computation | Mean value theorem step: $\big||1+a|^p-|1+b|^p\big|\le C|a-b|$ when $|1+a|,|1+b|\ge c>0$, with $C=pc^{p-1}$. | closed |
| B23 | proof, p.4 | computation | **Verified discrepancy.** Printed: $\int_{|x|>1}|d\rho_\varepsilon/dn|\le C\varepsilon\delta^{-p}$. What $(*)$ yields: $C\varepsilon\delta^{-1}=C\varepsilon^{1/2}$. Both $\to0$, so the conclusion stands; record both. (C7) | closed |
| B24 | proof, p.4 | computation | $|\nabla\widehat F_\varepsilon|\lesssim\min(\varepsilon^{-d},|x|^{-d})$, called "obvious". Verify all three pieces: $|\partial_dG_\varepsilon|$ at $x_d=0$ equals $r^{-d}-d\varepsilon^2r^{-d-2}$ with $r=(|x|^2+\varepsilon^2)^{1/2}$, giving $\sim|x|^{-d}$ for $|x|\gg\varepsilon$ and $\sim(d-1)\varepsilon^{-d}$ for $|x|\ll\varepsilon$; then $\nabla_T\rho_\varepsilon$; then $d\widehat\rho_\varepsilon/dn$ from $(*)$. | closed |

## C. Lemma 2 — the correction step on a cube

| # | location | kind | statement | status |
|---|---|---|---|---|
| C1 | L2 stmt, p.4 | notation | `β ⊂ β(N)` printed for `β = β(N)`. | closed |
| C2 | L2 stmt, p.4 | gap | Quantifier order: $N$ first, then $\beta=\beta(N)$, then an absolute smallness threshold for $N^{d-1}|I(a_Q)|^{-1}\sup_Q|I-I(a_Q)|$ independent of $N,\varepsilon$. Also: which $\varepsilon$? The statement quantifies over $\varepsilon$ small, inherited from Lemma 1. Make explicit. | closed |
| C3 | L2 proof, p.4 | computation | Reduction to $Q=Q(N)$: the affine map $x\mapsto N\ell(Q)^{-1}(x-a_Q)$ carries $Q$ onto $Q(N)$; track how both sides scale. The further reduction to $I(a_Q)=1$ is valid **only for the corrected statement of C9**: with the printed statement the two sides are not homogeneous in $I$ and the reduction fails. | closed |
| C4 | L2 proof, p.5 | computation | **Verified typo.** The first display prints $\int_{Q(N)}\big(|1+dF/dn|^p-|1+dF/dn|^p\big)$, identically zero. The first term must be $|I+dF/dn|^p$. (C8) | closed |
| C5 | L2 proof, p.5 | computation | The split $\int_{Q(N)\setminus D(0,1)}+\int_{D(0,1)}$ and the two different treatments (MVT outside, subadditivity inside). | closed |
| C6 | L2 proof, p.5 | computation | **Discrepancy.** Printed final bound $C\|I-1\|_\infty N^{d-1}+C\|I-1\|_\infty$. The second term comes from $\int_{D(0,1)}|I-1|^p$, so it should be $C\|I-1\|_\infty^{p}$. Harmless (both are small under the hypothesis) but record. | closed |
| C7 | L2 proof, p.5 | gap | "It remains to apply lemma 1." Lemma 1 controls the integral over all of $\mathbb{R}^{d-1}$; here the domain is $Q(N)$. Supply the tail estimate $\int_{\mathbb{R}^{d-1}\setminus Q(N)}\big(|1+dF/dn|^p-1\big)$, small because $dF/dn\lesssim|x|^{-d}$ and $\int_{|x|>N}|x|^{-d}\sim N^{-1}$. | closed |
| C9 | L2 stmt, p.4 | **claim** | **The one substantive slip.** As printed, no factor $I(a_Q)$ multiplies $dF_\varepsilon/dn$ inside the integral. But (i) the proof establishes only the normalised case $I(a_Q)=1$ — it reduces to "$N^{d-1}\|I-1\|_\infty$ small $\Rightarrow\int_{Q(N)}(|I+dF/dn|^p-1)\le-\eta$" — and (ii) Lemma 4 applies it to $I(x)+\frac{du_n}{dn}(a_Q)\,\frac{dF_{\varepsilon_{n+1}}}{dn}(\cdots)$, which *does* carry the factor. With the factor restored the two sides are homogeneous of degree 1 in $I$, so the normalised case gives the general one and the use in Lemma 4 is exactly licensed. Without it, neither step is valid. | closed |
| C8 | L2 proof, p.5 | computation | Where $e^{-2\beta}$ comes from: $\int_Q|\cdot|^p\le(1-\eta)|Q|$ gives $e^{-2\beta}=(1-\eta)^{1/p}$, i.e. $\beta=-\frac{1}{2p}\log(1-\eta)$. **Record that $\beta$ depends on $p$, $d$ and $N$**, and that $N$ is fixed before $\beta$. | closed |

## D. The recursive construction

| # | location | kind | statement | status |
|---|---|---|---|---|
| D1 | p.5 | notation | $\delta_n^{-1}\in\mathbb{Z}$; $\mathcal H_n$ = the $\delta_n^{-(d-1)}$ closed cubes of side $\delta_n$ tiling $Q(1)$; $\mathcal Q_n\subset\mathcal H_n$; $V_n=\bigcup\{Q:Q\in\mathcal Q_n\}$. | closed |
| D2 | p.5 | notation | $u_0$ vanishes **on** $Q(1)$ — correct and intentional: $u_0$ is boundary data, and the normal derivative of its harmonic extension on $Q(1)$ is in general nonzero. Say this explicitly; it is the single most confusing line in the paper. (N3) | closed |
| D3 | p.5 | computation | Base case $n=0$: $\delta_0=1$, $\mathcal Q_0=\{Q(1)\}$, and $(\int_{Q(1)}|du_0/dn|^p)^{1/p}\le A$ for $A$ large, since $u_0$ is smooth. | closed |
| D4 | p.5 | notation | Order of choice: $N$; then $\beta=\beta(N)$; then $A$; then $\{K_n\},\{\varepsilon_n\}$; then, at each stage, $\delta_{n+1}$ depending on everything before. **Constants $C$ are independent of $K_n,\varepsilon_n,\delta_n$ but may depend on $d,p,N$.** Make the whole dependency graph explicit — the paper states only part of it. | closed |
| D5 | p.6 | computation | $\nabla u_{n+1}=\nabla u_n+\sum_Q\frac{du_n}{dn}(a_Q)\nabla F_{\varepsilon_{n+1}}(N\delta_{n+1}^{-1}(x-a_Q))$: the factor $\delta_{n+1}/N$ in $u_{n+1}$ is exactly cancelled by the chain rule. Verify. | closed |
| D6 | p.6 | computation | $u_{n+1}-u_n$ is supported in $\bigcup_Q D(a_Q,\delta_{n+1}\varepsilon_{n+1}^{1/2}/N)\subset Q(1)$, hence $f=u_0$ off $Q(1)$ (used by A2). | closed |
| D7 | L3, p.6 | computation | $\sum_{|x-a_Q|>\rho}|\nabla F_{\varepsilon_{n+1}}(N\delta_{n+1}^{-1}(x-a_Q))|\le CN^{-d}\delta_{n+1}\rho^{-1}$. Verify: $\le N^{-d}\delta_{n+1}^{d}\sum|x-a_Q|^{-d}$ and $\delta_{n+1}^{d-1}\sum|x-a_Q|^{-d}\approx\int_{|y|>\rho}|y|^{-d}dy=c\rho^{-1}$ in $\mathbb{R}^{d-1}$. | closed |
| D8 | L3, p.6 | gap | The Riemann-sum comparison, "justified as long as $\rho/\delta_{n+1}$ does not approach 0", and the parenthetical "$C$ depends on a lower bound for $\rho/\delta_{n+1}$". Make the comparison quantitative. | closed |
| D9 | Cor, p.6 | gap | **Discrepancy.** The proof writes $|\nabla u_n(a_{Q'})|$, but the coefficient in the sum is $\frac{du_n}{dn}(a_{Q'})$, and hypothesis (b) controls only the normal derivative. Replace by $|\frac{du_n}{dn}(a_{Q'})|$; then (b) plus continuity gives the bound $2K_{n+1}e^{-\beta n}$. | closed |
| D10 | Cor, p.6 | gap | "by (b) and smoothness on $u_n$": passing from the $L^p$ average over $Q$ to the pointwise value at $a_Q$, at the cost of a factor 2, requires $\delta_{n+1}$ small **relative to the modulus of continuity of $du_n/dn$**, which depends on $n$. Note that this is legitimate because $\delta_{n+1}$ is chosen after $u_n$. | closed |
| D11 | Cor, p.7 | computation | $|\nabla u_{n+1}-\nabla u_n|\le 2K_{n+1}e^{-\beta n}(C+C\varepsilon_{n+1}^{-d})$: the sum by Lemma 3, the single term $Q'=Q$ by the $\varepsilon^{-d}$ part of Lemma 1. | closed |
| D12 | L4 (*), p.7 | computation | Proof of $(*)$, split at $|x-a_{Q'}|=M\delta_{n+1}$; near part by Lemma 3 with $\rho=\frac12\delta_{n+1}$, far part by Lemma 3 with $\rho=M\delta_{n+1}$ giving $CK_{n+1}e^{-\beta n}M^{-1}$. | closed |
| D13 | L4 (*), p.8 | notation | "$\gamma\to0$ as $\delta_n\to0$" — should be $\delta_{n+1}\to0$; it is the stage-$(n{+}1)$ cubes that shrink. | closed |
| D14 | L4 (*), p.8 | gap | The order of choices inside $(*)$: $\gamma$ given first, then $M$ chosen, then $\delta_{n+1}$. As printed, $M$ is "fixed" before the estimate and "arbitrary" after. Untangle. | closed |
| D15 | L4, p.8 | notation | Type 1: $|\frac{du_n}{dn}(a_Q)|>e^{-4\beta(n+1)}$; type 2 otherwise. | closed |
| D16 | L4, p.8 | computation | The decomposition of $\frac{du_{n+1}}{dn}(x)$ into $\frac{du_n}{dn}(a_Q)$ + bracket + last term; the printed bracket is unbalanced. Reconstruct it and check it is an identity. | closed |
| D17 | L4, p.9 | computation | Type 1: verifying Lemma 2's hypothesis. With $I=\frac{du_n}{dn}(a_Q)+\text{bracket}$ and bracket $<CN^{-d}|\frac{du_n}{dn}(a_Q)|$, the hypothesis needs $N^{d-1}\cdot CN^{-d}=CN^{-1}$ small — this is the content of "we're using here that $CN^{-d}<cN^{-(d-1)}$ for large $N$". | closed |
| D18 | L4, p.9 | computation | $e^{-2\beta}|\frac{du_n}{dn}(a_Q)||Q|^{1/p}<e^{-\frac32\beta}(\int_Q|\frac{du_n}{dn}|^p)^{1/p}$ for $\delta_{n+1}$ small: the slack $e^{\beta/2}$ absorbs the difference between the value at $a_Q$ and the $L^p$ average. | closed |
| D19 | L4, p.9 | computation | Type 2: $\int_Q|\frac{du_{n+1}}{dn}|^p\le 2e^{-4\beta(n+1)p}|Q|$, using $\int_Q|1+\frac{dF}{dn}(\cdots)|^p<|Q|$ "by lemma 2". Check that Lemma 2 really gives this, or supply the direct estimate. | closed |
| D20 | L4, p.9 | computation | $\sum_{Q\text{ type }2}|Q|\le|Q(1)|=1$. | closed |
| D21 | L4, p.9 | computation | **Verified sign error.** Printed $A^pe^{-p\beta(n+1)}(e^{\frac12p\beta}+CA^{-p}e^{-3p\beta(n+1)})$ with the claim that the parenthesis is $<1$; but $e^{+\frac12p\beta}>1$. Recomputation: the type-1 factor $e^{-\frac32p\beta}$ against $A^pe^{-p\beta n}$ gives $A^pe^{-p\beta(n+1)}e^{-\frac12p\beta}$, so the exponent must be $-\frac12p\beta$. With that sign the claim is correct for $A$ large. (C12) | closed |
| D22 | p.10 | computation | Condition (1) $\sum\varepsilon_{n+1}^{-d}K_{n+1}e^{-\beta n}<\infty$. | closed |
| D23 | p.10 | computation | **Verified discrepancy.** Condition (2) is printed $\sum K_{n+1}^{-p}+\varepsilon_{n+1}^{d-1}$; the use made of it on p.10 requires $\sum\varepsilon_{n+1}^{(d-1)/2}$ small, which the printed form does not imply ($\varepsilon<1\Rightarrow\varepsilon^{d-1}<\varepsilon^{(d-1)/2}$). The corrected condition is satisfied by the sequences the paper suggests. (C13) | closed |
| D24 | p.10 | computation | Compatibility: with $\varepsilon_n=C^{-1}n^{-2}$, $K_n=Cn^{2/p}$, check (1) and corrected (2). Note $\sum\varepsilon_{n+1}^{(d-1)/2}=C^{-(d-1)/2}\sum(n+1)^{-(d-1)}$ converges **iff $d-1\ge2$, i.e. $d\ge3$** — one visible place the hypothesis is used. | closed |
| D25 | p.10 | citation | "the corollary to lemma 2" — the Corollary in the text is stated after Lemma 3 and its proof invokes Lemmas 1 and 3. Cite it unambiguously. | closed |
| D26 | p.10 | gap | Condition (1) gives a summable bound on $|\nabla u_{n+1}-\nabla u_n|$ **on the boundary $\mathbb{R}^{d-1}$**. Upgrading to $C^1$ convergence **on the closed half-space** needs an interior argument (each partial derivative of a harmonic function is harmonic; apply the maximum principle, which requires decay at infinity). Supply it. | closed |
| D27 | p.10 | gap | $C^0$ convergence of $u_n$ is never estimated, only the gradients. Supply: $|u_{n+1}-u_n|\le\sup_Q|\frac{du_n}{dn}(a_Q)|\cdot\|F_{\varepsilon_{n+1}}\|_\infty\cdot\delta_{n+1}/N$. | closed |
| D28 | p.10 | computation | $|\{x\in Q(1):f(x)\ne0\}|\le\sum_n|\{u_{n+1}\ne u_n\}|\le C\sum\delta_{n+1}^{-(d-1)}(\delta_{n+1}\varepsilon_{n+1}^{1/2})^{d-1}=C\sum\varepsilon_{n+1}^{(d-1)/2}$. | closed |
| D29 | p.10 | computation | The disc radius is $\delta_{n+1}\varepsilon_{n+1}^{1/2}/N$, not $\delta_{n+1}\varepsilon_{n+1}^{1/2}$: the printed radius omits the $1/N$ from the scaling $x\mapsto N\delta_{n+1}^{-1}(x-a_Q)$. Only affects constants ($N$ is fixed). | closed |
| D30 | p.10 | gap | "Also, $d\widehat f/dn=0$ on $\bigcap_nV_n$." Not argued. Supply: $(\int_{V_n}|du_n/dn|^p)^{1/p}\le Ae^{-\beta n}\to0$ and $du_n/dn\to d\widehat f/dn$ uniformly, so $d\widehat f/dn=0$ a.e. on $\bigcap_mV_m$. | closed |
| D31 | p.10 | computation | **Verified sign error.** From $\frac1{|Q|}\int_Q|\frac{du_n}{dn}|^p>K_{n+1}^pe^{-p\beta n}$ it follows that $|Q|<K_{n+1}^{-p}e^{+\beta pn}\int_Q|\frac{du_n}{dn}|^p$; the printed exponent is $-\beta pn$. The next display (p.11) uses $+\beta pn$, confirming the slip. (C14) | closed |
| D32 | p.11 | computation | $|V_n\setminus V_{n+1}|\le K_{n+1}^{-p}e^{\beta pn}\int_{V_n}|\frac{du_n}{dn}|^p\le A^pK_{n+1}^{-p}$; and $V_n\setminus V_{n+1}$ is exactly the union of the stage-$(n{+}1)$ cubes inside $V_n$ that fail (b). | closed |
| D33 | p.11 | computation | The two measures sum to $<1=|Q(1)|$ under (2), so the good set has positive measure. | closed |
| D34 | p.11 | gap | **The last step of the theorem is missing.** The construction gives $f=0$ and $d\widehat f/dn=0$ on a positive-measure $E\subset Q(1)$; the theorem claims $\nabla f=0$. Supply: at a.e. point of $E$ (density points), $f=0$ on $E$ and $f\in C^1$ force the **tangential** gradient $\nabla_Tf$ to vanish; together with $d\widehat f/dn=0$ this gives $\nabla f=0$ a.e. on $E$. | closed |

## E. Remarks and references

| # | location | kind | statement | status |
|---|---|---|---|---|
| E1 | Rmk 2, p.11 | notation | "$C^2$ of $C^\infty$" printed for "$C^2$ or $C^\infty$". | closed |
| E2 | Rmk 2, p.11 | claim | The $C^{2+\varepsilon}$ variant with $f$ and $D^2f$ vanishing is asserted with no proof and no reference. Reproduce it as an assertion, marked as unproved in the source. | closed |
| E3 | Rmk 1, p.11 | claim | "a Hölder estimate on the gradient … should be possible along the work of [2]" — a statement about future work; keep as such. | closed |
| E4 | refs | citation | [1] A.B. Aleksandrov, P. Kargaev, *Private communication* (to appear). **Candidate identification, unverified:** Aleksandrov & Kargaev, *Hardy classes of functions harmonic in the half-space*, St. Petersb. Math. J. **5**, No. 2, 229–286 (1994); transl. from Algebra Anal. **5**, No. 2, 1–73 (1993); Zbl 0842.42012. Right authors, right subject, right period — but we have not read it and so cannot confirm it contains the inequality B4 needs. Stays open. | open |
| E5 | refs | citation | **Identified.** [2] is T. Wolff, *Counterexamples with harmonic gradients in $\mathbb{R}^3$*, in: C. Fefferman et al. (eds.), *Essays on Fourier Analysis in Honor of Elias M. Stein*, Princeton Math. Ser. **42**, Princeton Univ. Press, 321–384 (1995); Zbl 0836.31004. Verified from the zbMATH record; not read. Recorded in §9 of the expansion and in `data/problems.json`. | closed |

## F. Cross-cutting

| # | location | kind | statement | status |
|---|---|---|---|---|
| F1 | throughout | notation | $\lesssim$ is used without ever saying what the implicit constant may depend on. Fix a convention and apply it. | closed |
| F2 | throughout | notation | The hat is dropped from p.5 on ("we will drop the $\widehat{\ }$ notation"), so $F_{\varepsilon}$, $u_n$ denote both boundary functions and their harmonic extensions. Every later occurrence must be disambiguated. | closed |
| F3 | throughout | gap | The paper uses $\|\cdot\|_p$ for $p<1$, which is not a norm. Every "triangle inequality" step must be justified by $p$-subadditivity instead. Check each. | closed |
| F4 | throughout | computation | The preprint is dated Sept 1989; the journal version is Colloq. Math. 60/61 (1990). Text and numbering may differ. Anything asserted here is an assertion about the **preprint**. | closed |
