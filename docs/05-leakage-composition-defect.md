# Lemma B: Exact Leakage / Composition-Defect Dichotomy

This note proves the first global-in-convolution composition inequality of the program. It is finite-dimensional algebra on a Galerkin truncation; no probabilistic phase assumption and no support-cardinality assumption is used.

## 1. Full pair decomposition at an output

Fix an output helicity `s` and a finite set of nonzero output wavevectors `Omega`. For each `r in Omega`, write the exact scalar helical forcing as a sum over canonical unordered input-pair/helicity channels

\[
F_s(r)=\sum_{\alpha\in\mathcal P(r)}x_\alpha(r).
\]

Each `x_alpha(r)` already includes the exact helical coefficient and the two modal amplitudes. Thus it is the actual complex pair contribution to the nonlinear forcing at `(r,s)`.

Let `S(r) subset P(r)` be a selected family of same-spin handoffs whose same-wavevector spin shadows occur at `(r,s)`. Define the selected shadow pair mass

\[
\mathcal M_{\rm sh}
:=\sum_{r\in\Omega}\sum_{\alpha\in\mathcal S(r)}|x_\alpha(r)|^2.
\]

## 2. The composition defect

At each output define

\[
\mathcal B(r)
:=\left(\sum_{\alpha\in\mathcal P(r)}|x_\alpha(r)|\right)^2
\]

and

\[
\boxed{
\mathfrak D_{\rm comp}(r)
:=\mathcal B(r)-|F_s(r)|^2\ge0.
}
\]

If `x_alpha=rho_alpha exp(i theta_alpha)`, then exactly

\[
\boxed{
\mathfrak D_{\rm comp}(r)
=2\sum_{\alpha<\beta}
\rho_\alpha\rho_\beta
\bigl(1-\cos(\theta_\alpha-\theta_\beta)\bigr)
=4\sum_{\alpha<\beta}
\rho_\alpha\rho_\beta
\sin^2\frac{\theta_\alpha-\theta_\beta}{2}.
}
\]

Thus `D_comp` is gauge invariant and positive. It vanishes when there is only one pair channel, and also when all nonzero pair contributions at an output have the same complex phase. Positive `D_comp` requires both additive multiplicity and phase disagreement.

Every off-diagonal term corresponds to two representations of the same output,

\[
a+b=c+d,
\]

so the defect is a coefficient- and amplitude-weighted additive-collision quantity.

## 3. Exact leakage/composition inequality

Define actual shadow leakage

\[
\mathcal L
:=\sum_{r\in\Omega}|F_s(r)|^2
\]

and total composition defect

\[
\mathfrak D_{\rm comp}
:=\sum_{r\in\Omega}\mathfrak D_{\rm comp}(r).
\]

Since for every output

\[
\sum_{\alpha\in\mathcal S(r)}|x_\alpha|^2
\le
\left(\sum_{\alpha\in\mathcal P(r)}|x_\alpha|\right)^2,
\]

summing gives the exact deterministic inequality

\[
\boxed{
\mathcal M_{\rm sh}
\le
\mathcal L+\mathfrak D_{\rm comp}.
}
\]

This is the clean form of the sparse/dense dichotomy. There is no separate hidden "cross-pair" loophole: all additional pairs are already included in the full composition envelope and therefore in `D_comp` if they are used to cancel the selected shadows.

## 4. Conversion of positive critical production into shadow mass

For a selected same-spin handoff `e`, let

- `p_e` be the catalyst/shadow output radius,
- `z_{-s}(p_e)` be the opposite-spin catalyst amplitude,
- `c_e` be the pair forcing into the opposite-spin catalyst,
- `x_e` be the same-wavevector same-spin shadow forcing.

The Spin-Shadow Lemma gives

\[
|x_e|\ge|c_e|.
\]

With the triad convention used in `02-spin-shadow.md`, the Euler critical production carried by the handoff is

\[
\kappa_e
=2p_e\,\operatorname{Re}
\bigl(\overline{z_{-s}(p_e)}\,c_e\bigr).
\]

For a family selected with `kappa_e >= 0`, put

\[
\kappa_{\mathcal T}:=\sum_e\kappa_e,
\qquad
\mathcal W_{\mathcal T}
:=\sum_e p_e^2|z_{-s}(p_e)|^2.
\]

Then

\[
\kappa_{\mathcal T}
\le2\sum_e p_e|z_{-s}(p_e)|\,|x_e|
\le2\mathcal W_{\mathcal T}^{1/2}
\mathcal M_{\rm sh}^{1/2}.
\]

Hence, whenever `W_T > 0`,

\[
\boxed{
\mathcal M_{\rm sh}
\ge
\frac{\kappa_{\mathcal T}^2}{4\mathcal W_{\mathcal T}}.
}
\]

If `W_T=0`, then necessarily `kappa_T=0`.

Combining with the previous section gives the proved form of Lemma B:

\[
\boxed{
\mathcal L+\mathfrak D_{\rm comp}
\ge
\frac{\kappa_{\mathcal T}^2}
{4\mathcal W_{\mathcal T}}.
}
\]

In particular,

\[
\boxed{
\mathcal L
\ge\frac{\kappa_{\mathcal T}^2}{8\mathcal W_{\mathcal T}}
\quad\text{or}\quad
\mathfrak D_{\rm comp}
\ge\frac{\kappa_{\mathcal T}^2}{8\mathcal W_{\mathcal T}}.
}
\]

No phase randomness, multiplicity cap, or turbulence phenomenology enters the proof.

## 5. Scaling audit

Under Navier-Stokes scaling in three dimensions,

- `kappa_T` has the scaling of `dK/dt`, namely `lambda^2`,
- `W_T` has the scaling of `||Lambda u||_2^2`, namely `lambda`,
- `L` and `D_comp` have the scaling of `||F||_2^2`, namely `lambda^3`.

Therefore both sides scale like `lambda^3`. Lemma B is critical-scale compatible.

## 6. What Lemma B does and does not prove

Lemma B proves that positive critical escape cannot remain both pairwise strong and compositionally invisible. It must appear as either

1. **actual forcing leakage**, measured by `L`, or
2. **large composition defect**, which requires multiple additive representations with nontrivial relative phases.

It does not yet control the time integral of `D_comp`. The dense branch therefore remains open. The next note identifies a new exact obstruction to persistent cancellation: viscosity is transverse to generic additive diamonds.
