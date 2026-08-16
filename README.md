# Navier–Stokes Four Primitives

A from-scratch structural research program for the 3D incompressible Navier–Stokes regularity problem.

> **Status:** research program / proof attempt. This repository does **not** claim a proof of global regularity or of the Clay Millennium problem.
>
> The purpose of this repository is to keep a strict separation between exact identities, numerically audited algebra, structural reductions, and genuinely open rigidity statements.

## The four primitives

We organize the nonlinear problem around four statements that exist before any particular norm, shell decomposition, or proof technology.

1. **Transfer** — the Euler nonlinearity redistributes rather than creates kinetic energy, and is tangent to the energy–helicity leaves.
2. **Dissipation** — viscosity destroys finer scales increasingly fast.
3. **Selection** — quadratic transfer is not arbitrary: incompressibility, triad closure, helicity, geometry, and phase determine which interactions are actually allowed and how strongly.
4. **Composition** — finite-time singular escape requires allowed dangerous transfers to remain composable through an unbounded chain of scales.

The guiding question is therefore not whether every nonlinear interaction is weak. It is:

> **Can exact Navier–Stokes selection rules support an infinitely composable critical escape chain?**

## Nonlinear base

For divergence-free velocity `u`, write

\[
\partial_tu=F-\nu\Lambda^2u,
\qquad
F=P(u\times\omega),
\qquad
\omega=\nabla\times u.
\]

On the torus, decompose one Fourier mode in the helical basis

\[
\widehat u(k)=\sum_{s=\pm1}z_s(k)h_s(k),
\qquad
ik\times h_s(k)=s|k|h_s(k).
\]

For a pair `a+b=r`, the exact pair coefficient into output helicity `t` is

\[
\boxed{
C_{r;a,b}^{t,s_a,s_b}
=
(s_b|b|-s_a|a|)
\,\overline{h_t(r)}\cdot
\big(h_{s_a}(a)\times h_{s_b}(b)\big).
}
\]

For same-spin parents `s_a=s_b=s`, with

\[
\alpha=|a|,\quad \beta=|b|,\quad \rho=|a+b|,
\quad S=\alpha+\beta,
\quad \Delta=|\alpha-\beta|,
\quad A=|a\times b|,
\]

our convention gives

\[
\boxed{
|C^{t,s,s}|
=
\frac{1}{2\sqrt2}
\Delta\frac{A}{\rho\alpha\beta}
(S+ts\rho).
}
\]

This single formula exposes radial, angular, and helicity selection at once.

## First exact structural mechanism: the spin shadow

Let `Q^s` and `(-K)^s` be same-helicity parents and

\[
P=Q-K,
\qquad q=|Q|>k=|K|,
\qquad p=|P|,
\qquad S=q+k.
\]

The pair simultaneously forces both helicities at the **same output wavevector** `P`:

\[
|C_{P}^{-s}|=
\frac{1}{2\sqrt2}
(q-k)\frac{|Q\times K|}{pqk}(S-p),
\]

\[
|C_{P}^{s}|=
\frac{1}{2\sqrt2}
(q-k)\frac{|Q\times K|}{pqk}(S+p).
\]

Hence

\[
\boxed{
\frac{|C_P^{s}|}{|C_P^{-s}|}
=
\frac{S+p}{S-p}
\ge1.
}
\]

So the same pair that creates an opposite-spin catalyst required by a heterochiral critical handoff also creates a same-spin **shadow forcing** at least as large in coefficient magnitude.

This does **not** say the shadow receives more instantaneous energy: forcing and modal energy transfer are different when the shadow amplitude is initially small. It does say that a sparse escape skeleton cannot ignore the off-channel forcing created by its own parent pairs.

## Current proof architecture

The working chain is

\[
\text{critical escape}
\Rightarrow
\text{same-spin radial handoff with opposite-spin catalyst}
\Rightarrow
\text{same-wavevector spin shadow}
\]

and then

\[
\text{shadow}
\Rightarrow
\begin{cases}
\text{actual leakage},\\
\text{or cancellation by other convolution pairs}.
\end{cases}
\]

Repeated cancellation requires many identities of the form

\[
a+b=c+d,
\]

hence additive parallelograms in Fourier space. The dense branch therefore leads naturally to weighted additive energy, Pexider-type phase constraints, and possible phase-curvature / projective rigidity.

The central open target is:

> **Dense Composition Rigidity.** Show that a scale-critical, two-spin, forward-transfer network cannot cancel its forced shadows and remain positively coherent through infinitely many adjacent scales without paying a quantitatively non-summable structural cost.

## Repository map

- `docs/00-four-primitives.md` — primitive physical architecture.
- `docs/01-nonlinear-base.md` — Fourier/helical derivation from the quadratic nonlinearity.
- `docs/02-spin-shadow.md` — exact spin-shadow mechanism and its limits.
- `docs/03-composition-program.md` — sparse leakage, additive structure, dense phase rigidity.
- `docs/04-audit-protocol.md` — conventions, falsification rules, and verification discipline.
- `docs/16-global-planarity-defect.md` — global critical planarity tensor and directional defect dynamics.
- `docs/17-planarity-volume-determinant.md` — Cauchy-Binet 3D-volume entropy and exact parabolic-frequency damping.
- `docs/18-two-spin-self-balancing.md` — exact two-spin source/damping balance.
- `docs/20-within-spin-radial-gate.md` — exact radial gate and Riccati width damping.
- `docs/21-optimal-protected-escape-defect.md` — Gram/Schur optimal escape residual after energy-helicity protection.
- `docs/22-optimal-defect-triad-source.md` — triad factorization of optimal-defect reopening.
- `scripts/verify_helical_coefficients.py` — numerical audit of the exact coefficient identities.
- `STATUS.md` — current theorem/target boundary.

## Philosophy

This project deliberately avoids a common failure mode in Navier–Stokes proof attempts: converting a suggestive geometric picture into an unproved inequality and then treating the inequality as established.

Every central step is tagged as one of:

- **Exact identity**
- **Verified algebraic consequence**
- **Structural reduction**
- **Open target**

The project succeeds only if the last category is eventually eliminated by proof.
