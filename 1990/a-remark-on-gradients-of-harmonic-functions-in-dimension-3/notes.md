# A remark on gradients of harmonic functions in dimension ≥ 3

## The paper

Bourgain, Jean; Wolff, T.
*Colloquium Mathematicum* **60/61**, No. 1, 253–260 (1990).

- Zbl [0731.31006](https://zbmath.org/4208479)
- DOI [10.4064/cm-60-61-1-253-260](https://doi.org/10.4064/cm-60-61-1-253-260)
- MSC 31B20 (boundary value and inverse problems for harmonic functions),
  31B05 (harmonic, subharmonic, superharmonic functions in higher dimensions)
- OpenAlex citation count 32, as of 2026-08-24
- Catalogue id `1990-a-remark-on-gradients-of-harmonic-functions-in-dimension-3`

The only joint Bourgain–Wolff paper in the catalogue (`Wolff, T.` has collaborator
score 1). It predates the arXiv, so there is no preprint server copy.

## Source obtained — 2026-08-24

`a-remark-on-gradients-of-harmonic-functions-in-dimension-3.pdf`
4,335,174 bytes · 12 pages · scanned, no text layer.

From the **IHES preprint fonds**, supplied by the user:
<https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/BOURGAIN/1984-1989/M_89_31/M_89_31.pdf>

Cover page verified by rendering: *A REMARK ON GRADIENTS OF HARMONIC FUNCTIONS IN
DIMENSION ≥ 3*, J. Bourgain\* , T. Wolff\*\*, \*IHES, \*\*California Institute of
Technology, Institut des Hautes Études Scientifiques, **Septembre 1989**,
**IHES/M/89/31**.

### This is the preprint, not the journal version

IHES/M/89/31 (September 1989) is the preprint of the paper published in *Colloq.
Math.* 60/61 (1990). Two consequences for Blueprint A:

- **Numbering may differ** from the published version. Blueprint A says to keep
  *his* section and theorem numbering so the digestion reads beside the original —
  so the digestion must state, in its editorial preface, that it follows the
  preprint's numbering, and note any divergence if the journal version is later
  obtained.
- **The text may differ.** Referee changes between September 1989 and the 1990
  issue are not visible from here. Anything the digestion asserts is an assertion
  about the preprint.

Worth re-checking against the published version before the digestion is called
finished. The IMPAN copy was unreachable today (below); retry when their site is up.

## What is in it (read: cover and p. 1 only)

> **Theorem.** If d ≥ 3 there is a harmonic function f : ℝ^d₊ → ℝ which is C¹ up to
> the boundary and such that f and ∇f vanish on a common boundary set with positive
> measure.

From the introduction, on p. 1: the note refines an earlier result (its reference
[2]) giving C^{1+ε}-harmonic functions on ℝ^d₊, d ≥ 3, whose gradient vanishes on a
boundary set of positive measure; using ingredients from its reference [1] one gets
f and ∇f vanishing *simultaneously*. Whether this can happen for C² or C^∞
functions is left open, with remarks at the end. The construction runs on the same
techniques as [2] but is simpler there because the correction theorem is applied to
scalar rather than vector-valued functions. The outline given: start from a function
u₀ vanishing on an open boundary subset, then by successive modification (a
"correction theorem") drive the normal derivative to 0 on a subset of large measure,
keeping u₀ unchanged on a large set — which forces the added functions to have small
compact support, an idea attributed to A. B. Alexandrov and P. Kargaev.

Nothing beyond p. 1 has been read. Everything above p. 1 is unexamined.

## Download attempts before the IHES copy (all failed, 2026-08-24)

Recorded because the catalogue's own links for this paper are among them.

| Route | Result |
|---|---|
| arXiv e-print / PDF | none; 1990 paper |
| Open-access PDF (IMPAN), the catalogue's `primary_link` | **HTTP 502**, 5 attempts, plain and browser UAs, with Referer |
| IMPAN journal issue page | **HTTP 502** in a real browser too — their whole publishing site was out; `impan.pl/` root still answered 301 |
| EuDML record `eudml.org/doc/265066` (the top Google hit) | **HTTP 403** to `curl`, to WebFetch, *and* to a real browser — EuDML refuses this network |
| NUMDAM / Project Euclid / EMIS | do not carry *Colloquium Mathematicum* |
| pldml / matwbn (ICM Polish digital maths library) | 301 to an unrelated journal element; search endpoint 404 |
| DOI | 302 → 308 → **502**, the same broken IMPAN endpoint |
| Wayback | no snapshot of the IMPAN PDF; a 2026-07-15 snapshot of the EuDML record exists but was not needed once the IHES copy arrived |
| zbMATH full-text links | only the DOI, i.e. the same broken route |

No paywall was involved or circumvented: the IMPAN copy is openly available when
their server is up.

## Status

**Blueprint A complete. Blueprint B complete. Ledger: 82 of 82 rows closed.**
Passes run: skeleton, expansion, computation, adversarial (four sweeps), reader,
ledger, size.

| | |
|---|---|
| original scan | 11 pages (+1 IHES cover) |
| transcription, same typesetting | 7 pages |
| **digestion** | **25 pages** |
| ideas harvested | 20 (the toolkit was empty before) |
| open problems recorded | 1 |

### The paper's one import is now proved, not assumed

`B4` — the Alexandrov–Kargaev inequality
$\int(|1+dG_\varepsilon/dn|^p-1)\,dx<-2M<0$ — was the only step we had to take on
faith. Reference [1] is A.B. Aleksandrov and P. Kargaev, *Hardy classes of harmonic
functions in a half-space*, Algebra i Analiz **5**, No. 2, 1–73 (1993). We did not
obtain a copy, so §2.2 of the digestion **proves** the special case Lemma 1 needs
instead. The centrepiece is an exact evaluation:

$$\int_0^\infty\log\bigl|1-u^{-d}\bigr|\,u^{d-2}\,du\;=\;-\frac{\pi}{d-1}\cot\frac{\pi}{d}.$$

Integration by parts turns the integral into a principal value (the two boundary terms
at $u=1$ blow up but cancel exactly); the substitution $t=u^d$ and the classical
$\mathrm{PV}\int_0^\infty t^{a-1}/(1-t)\,dt=\pi\cot\pi a$ evaluate it. Since
$\cot(\pi/d)>0$ exactly for $d>2$, the quantity is negative for $d\ge3$ and
**identically zero at $d=2$**. Two dominated-convergence arguments then give the
inequality for small $p$ and small $\varepsilon$.

So $d\ge3$ is visible in two independent places: the convergence of
$\sum\varepsilon_n^{(d-1)/2}$ in §7, and the sign of the imported inequality itself.
At $d=2$ both degenerate — as they must, since the theorem is false in the plane.

Checked numerically at every step: the closed form to 19 significant digits at $d=3$
and 14 at $d=4$; the full integral computed directly from the exact kernel at $d=3,4$
converging to the predicted value as $\varepsilon\to0$; and the $d=2$ control
returning a positive value.

### Six discrepancies in the original

Five typographical or sign errors, each verified against the scan at 320 dpi: the
exponent in $C\varepsilon\delta^{-p}$ (p.4); two identical terms in the first display
of Lemma 2's proof (p.5); $e^{+\frac12p\beta}$ where the recomputation forces
$e^{-\frac12p\beta}$ (p.9); $\varepsilon^{d-1}$ for $\varepsilon^{(d-1)/2}$ in
condition (2) (p.10); $e^{-\beta pn}$ for $e^{+\beta pn}$ (p.10).

The sixth is substantive: **Lemma 2 is stated with no factor $I(a_Q)$ multiplying
$dF_\varepsilon/dn$.** As printed it is not homogeneous in $I$ and is false for large
$|I(a_Q)|$; its proof establishes only the normalised case; and Lemma 4 applies it to
a term that does carry the factor. Restoring the factor makes statement, proof and
application agree. Ledger `C9`, §3 of the digestion.

Two further points needed repair rather than correction, and are the two surviving
`caution` boxes: the lower bound for $|1+dG_\varepsilon/dn|$ fails exactly at $|x|=1$,
where the original applies the mean value theorem across a zero (repaired by splitting
at $|x|=2$, §2.6 and §3.3); and the final passage from "$f=0$ and $\partial_nf=0$" to
"$\nabla f=0$" is absent from the paper altogether (supplied via density points, §7.5).

### References traced

- **[1]** Aleksandrov–Kargaev, Algebra i Analiz **5**:2, 1–73 (1993); Zbl 0842.42012.
  Not obtained; superseded for our purposes by the proof in §2.2.
- **[2]** T. Wolff, *Counterexamples with harmonic gradients in $\mathbb R^3$*,
  Princeton Math. Ser. **42**, 321–384 (1995); Zbl 0836.31004. Verified from zbMATH;
  not read.

### The open problem it poses has since been resolved

Remark 2 asks whether $C^2$ or $C^\infty$ examples exist. Qin and Zhan announce a
negative answer in arXiv:2608.01683 (3 August 2026) — three weeks before this
digestion. Recorded on the site's Open problems page with that provenance; we have
read the abstract, not the proof, and it is unrefereed.

### A second exposition

R. C. D. de Andrade, *On zeros of gradients of harmonic functions on the upper half
space*, master's thesis, IMPA (supervisor: J. Ramos), 2 June 2026, 87 pp. Read after
the digestion was finished. It:

- **confirms** the exponent `(d-1)/2` in condition (2), independently (`D23`);
- **confirms** that Lemma 2 is printed without the factor `I(a_Q)` (`C9`) — so that is
  a defect of the paper, not a misreading — while showing a lighter repair: factor the
  amplitude out by hand and apply the lemma only with `I ≡ 1`;
- **also quotes the Alexandrov–Kargaev inequality without proof** ("its proof is beyond
  our interest"), so the proof in §2.2 is not a reconstruction of something already
  available in the literature we have seen;
- **supplies the motivation** now in §0.5: Calderón / electrical impedance tomography,
  and the reading of this theorem as boundary invisibility — a part of the boundary
  carrying neither voltage nor current while the interior potential is nonzero;
- **sharpens the d = 2 obstruction**: its chapter 2 derives it from the characterisation
  of moduli of H^p functions, `∫ log h(t)/(1+t²) dt > −∞`, which vanishing on a
  positive-measure set violates. We have not verified that chapter.

The file is at `Master_s_Thesis.pdf` in this directory and is gitignored, like the paper
scan — it is not ours to redistribute from a public repository.

### Next

- Compare §2.2 against Aleksandrov–Kargaev's own argument, if a copy can be had.
- Obtain the published Colloq. Math. version and diff it against this preprint.
- Verify chapter 2 of the thesis and promote the sharp d = 2 statement out of §9.
