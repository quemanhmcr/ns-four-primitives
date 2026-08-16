# Stochastic-Lagrangian Falsification Test for the Protected Defect

**Claim level:** exact endpoint calculation plus a negative result for the naive martingale-variance closure. The stochastic representation is used as an exact reformulation of a smooth periodic Navier-Stokes solution, not as a random model of turbulence.

Primary references: Constantin--Iyer, arXiv:math/0511067; Constantin, arXiv:math/0112128; Eyink--Gupta--Zaki, arXiv:1912.06677.

## 1. The exact stochastic object

For a smooth Navier--Stokes solution, vorticity satisfies

\[
\partial_t\omega+u\cdot\nabla\omega
=(\nabla u)\omega+\nu\Delta\omega.
\]

Fix a terminal point `(x,t)` and use backward lag `tau=t-s`. In a standard backward stochastic-Cauchy representation one introduces a diffusion

\[
dY_\tau=-u(Y_\tau,t-\tau)\,d\tau+\sqrt{2\nu}\,dW_\tau,
\qquad Y_0=x,
\]

and a deformation matrix `G_tau` with `G_0=I` chosen so that

\[
\mathcal C_\tau(x)
:=G_\tau(x)\,\omega(Y_\tau(x),t-\tau)
\]

is a backward martingale whose mean equals `omega(x,t)`. This is the local flat-space form of the stochastic Cauchy invariant.

Only the terminal infinitesimal coefficient is needed below. Since `G_0=I` and `Y_0=x`, Ito's formula gives

\[
\boxed{
 d\mathcal C_\tau\big|_{\tau=0}
 =\sqrt{2\nu}\sum_{j=1}^3
 (\partial_j\omega)(x,t)\,dW_\tau^j.
}
\]

The nonlinear drift and vortex stretching have been absorbed by the stochastic Cauchy transport; they do not appear in this terminal martingale coefficient.

## 2. Lift the optimal protected residual

Let

\[
B:=\operatorname{curl}^{-1}
\]

on mean-zero divergence-free fields, and let

\[
T_t:=\Lambda-a(t)-b(t)\operatorname{curl}
\]

be the optimal protected multiplier from `21-optimal-protected-escape-defect.md`. Define

\[
Q_t:=T_tB.
\]

Then

\[
\boxed{r(t)=Q_t\omega(t).}
\]

Because `Q_t` is deterministic and linear at the fixed terminal time,

\[
M_\tau:=Q_t\mathcal C_\tau
\]

is an `L^2`-valued martingale with mean `r(t)`. Since `Q_t` is a Fourier multiplier, it commutes with spatial derivatives. Therefore

\[
 dM_\tau\big|_{0}
 =\sqrt{2\nu}\sum_j
 \partial_j r(t)\,dW_\tau^j.
\]

Hence its Hilbert-space quadratic variation has exact terminal density

\[
\boxed{
\left.\frac{d}{d\tau}
\mathbb E\|M_\tau-M_0\|_2^2
\right|_{\tau=0+}
=2\nu\|\nabla r(t)\|_2^2
=2\nu\|\Lambda r(t)\|_2^2.
}
\]

This is precisely the viscous dissipation term already present in

\[
\mathcal Y'
=2\Gamma_{\rm esc}-2\nu\|\Lambda r\|_2^2.
\]

Thus the most direct stochastic-Cauchy lift geometrizes **Dissipation**, not the positive regeneration source.

## 3. The preconditioned lift

There is a second canonical test. Put

\[
\bar Q_t:=\Lambda^{-1}Q_t,
\qquad
N_\tau:=\bar Q_t\mathcal C_\tau.
\]

At the endpoint,

\[
 dN_\tau\big|_0
=\sqrt{2\nu}\sum_j
\partial_j\Lambda^{-1}r\,dW_\tau^j.
\]

Therefore

\[
\boxed{
\left.\frac{d}{d\tau}
\mathbb E\|N_\tau-N_0\|_2^2
\right|_{0+}
=2\nu\|r(t)\|_2^2
=2\nu\mathcal Y(t).
}
\]

So the optimal protected defect itself is an endpoint stochastic-variance production density after one inverse derivative.

This is a genuine representation identity, but it is not yet a new estimate.

## 4. Decisive reset test

At a nondegenerate protected reset,

\[
r(t_0)=0,
\]

and the deterministic opening theorem gives

\[
\boxed{\mathcal Y''(t_0)=2\|T F(t_0)\|_2^2.}
\]

However both endpoint martingale-variance slopes above vanish:

\[
\left.\partial_\tau\operatorname{Var}M_\tau\right|_{0+}=0,
\qquad
\left.\partial_\tau\operatorname{Var}N_\tau\right|_{0+}=0.
\]

Therefore `TF`, the exact nonlinear opening acceleration, is **not** the first quadratic variation of the raw stochastic Cauchy invariant or of its one-derivative preconditioning.

This falsifies the strongest naive hope:

\[
\boxed{
\text{protected nonlinear source}
\not\equiv
\text{first stochastic Cauchy quadratic variation}.
}
\]

Higher backward stochastic jets may contain the opening commutator, but then one has entered a curvature/commutator problem rather than obtained a free martingale budget.

## 5. Heat-translation audit

For the Brownian translation part alone, a Fourier field `f` satisfies the exact identity

\[
\mathbb E\|f(\cdot+\sqrt{2\nu}W_h)
-\mathbb Ef(\cdot+\sqrt{2\nu}W_h)\|_2^2
=
\sum_{k\ne0}|\hat f(k)|^2
\left(1-e^{-2\nu|k|^2h}\right).
\]

Thus

\[
\left.\partial_h\operatorname{Var}\right|_{0+}
=2\nu\|\Lambda f\|_2^2.
\]

`scripts/verify_stochastic_endpoint_qv.py` audits this identity and the preconditioned version on random Fourier data.

## 6. Near-identity reset test

Constantin's diffusive near-identity formulation is structurally relevant: the physical-space map is reset when its Jacobian departs too far from the identity, and the paper gives lower bounds on the minimum reset interval in terms of maximum enstrophy.

This does **not** by itself close our No-Zeno problem. A lower bound depending on a maximum enstrophy over each interval is not automatically summable from the Leray energy-dissipation budget, which controls a time integral rather than the sequence of local maxima. Importing that reset theorem without a new bridge would simply move the Zeno difficulty into the growth of enstrophy peaks.

## 7. Verdict on the naive stochastic candidate

The stochastic-Lagrangian formulation passes the **exactness** and **change-of-object** tests, but fails the decisive first closure test:

- raw protected stochastic variance sees `nu ||Lambda r||^2`;
- preconditioned variance sees `nu ||r||^2`;
- neither first quadratic variation sees `Gamma_esc` or `||TF||^2` at a protected reset.

The useful object must therefore be more geometric than the raw invariant. The next note identifies it: the noncommutativity between the moving protected multiplier and the exact skew-dissipative Navier-Stokes transport.
