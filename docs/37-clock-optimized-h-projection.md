# Clock-Optimized Projection onto the H-Flow Direction

**Claim level:** exact finite-network Hilbert-space decomposition.

The geometric H-flow uses an artificial time `s`, while the deterministic Euler/Navier-Stokes evolution uses physical time `t`. Therefore a physically meaningful comparison must not identify the two clocks arbitrarily.

This note removes that ambiguity by optimizing over the H-flow clock at each state.

## 1. Current-space metric

At a fixed positive modal covariance `n`, define

\[
q=n^{-1},
\qquad
a:=Aq,
\qquad
J_H:=Wa.
\]

Use the current-space inner product

\[
\langle J_1,J_2\rangle_{W^{-1}}
:=J_1^TW^{-1}J_2.
\]

Then

\[
\|J_H\|_{W^{-1}}^2
=a^TWa
=:\mathcal D_H.
\]

The exact deterministic Euler current is `J_E`.

## 2. Optimize the artificial clock

A time change `ds/dt=gamma` changes the H-current in physical time to

\[
J_H^{(\gamma)}=\gamma J_H.
\]

Consider

\[
\mathcal C(\gamma)
:=\|J_E-\gamma J_H\|_{W^{-1}}^2.
\]

For `D_H>0`, the unconstrained minimizer is

\[
\gamma_{\rm lin}
=\frac{\langle J_E,J_H\rangle_{W^{-1}}}
{\|J_H\|_{W^{-1}}^2}.
\]

But

\[
\langle J_E,J_H\rangle_{W^{-1}}
=(Aq)^T J_E
=\dot S_E.
\]

Hence

\[
\boxed{
\gamma_{\rm lin}=\frac{\dot S_E}{\mathcal D_H}.
}
\]

If the comparison flow is required to run forward, `gamma>=0`, then

\[
\boxed{
\gamma_*
=\frac{(\dot S_E)_+}{\mathcal D_H}.
}
\]

Thus the optimal H-flow clock is determined intrinsically by the exact deterministic entropy production.

## 3. Orthogonal coherence current

On the entropy-producing branch `dot S_E>0`, define

\[
\boxed{
J_\perp
:=J_E-\gamma_*J_H.
}
\]

Then

\[
\boxed{
\langle J_\perp,J_H\rangle_{W^{-1}}=0.
}
\]

The clock-optimized coherence action is

\[
\boxed{
\mathcal C_\perp
:=\|J_\perp\|_{W^{-1}}^2.
}
\]

By Pythagoras,

\[
\boxed{
\mathcal C_\perp
=J_E^TW^{-1}J_E
-\frac{(\dot S_E)^2}{\mathcal D_H}
}
\]

when `dot S_E>0`.

If `dot S_E<=0`, the best forward H-clock is `gamma_*=0`, so the whole exact current is non-H-flow:

\[
\boxed{
\mathcal C_\perp=J_E^TW^{-1}J_E.
}
\]

## 4. H-angle

When `J_E` and `J_H` are nonzero, define

\[
\boxed{
\cos\Theta_H
:=
\frac{\dot S_E}
{\sqrt{\mathcal D_H}\,
 \sqrt{J_E^TW^{-1}J_E}}.
}
\]

This is the current-space angle between deterministic transfer and the entropy-gradient H-direction.

On the positive-alignment branch,

\[
\boxed{
\frac{\mathcal C_\perp}
{J_E^TW^{-1}J_E}
=\sin^2\Theta_H.
}
\]

Thus the coherence fraction is literally an angular defect after the optimal clock has been removed.

## 5. Exact physical-time decomposition

On `dot S_E>0`, the deterministic covariance dynamics becomes

\[
\boxed{
\dot n_E
=\gamma_*L(n^{-1})
+A^T J_\perp.
}
\]

Define the renormalized H-time

\[
\boxed{
s(t)=\int_0^t\gamma_*(\tau)\,d\tau.
}
\]

If the integrated orthogonal current is small, the deterministic covariance path is a perturbation of the canonical H-flow after this intrinsic time change.

No phenomenological relaxation time is inserted.

## 6. Critical-flux decomposition

Let

\[
c_V=A|h|,
\qquad
\mathcal D_V=c_V^TWc_V.
\]

Then

\[
\dot K_E
=c_V^T J_E
=\gamma_*c_V^TWa+c_V^T J_\perp.
\]

Cauchy-Schwarz gives

\[
|c_V^TWa|
\le\sqrt{\mathcal D_V\mathcal D_H},
\]

and

\[
|c_V^T J_\perp|
\le\sqrt{\mathcal D_V\mathcal C_\perp}.
\]

Since `gamma_* D_H=dot S_E` on the positive branch,

\[
\boxed{
|\dot K_E|
\le
\sqrt{\mathcal D_V}
\left(
\frac{|\dot S_E|}{\sqrt{\mathcal D_H}}
+\sqrt{\mathcal C_\perp}
\right).
}
\]

This separates critical transfer into

1. an entropy-carrying H-flow component;
2. an orthogonal coherence component.

## 7. Revised branch architecture

The auxiliary-flow dichotomy should therefore be formulated after clock optimization:

\[
\boxed{
\begin{cases}
\mathcal C_\perp\ll J_E^TW^{-1}J_E,
&\text{H-aligned / thermalizing branch},\\
\mathcal C_\perp\gtrsim J_E^TW^{-1}J_E,
&\text{genuinely coherent branch}.
\end{cases}
}
\]

The first branch can be compared to the exact H-flow using the intrinsic time `s(t)`. The second branch must be controlled by deterministic helical phase/composition rigidity.

This clock optimization removes the arbitrary physical-time normalization from the original current split.
