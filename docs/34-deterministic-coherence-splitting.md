# Exact Deterministic / H-Flow Current Splitting

The H-flow is auxiliary. This note connects it to the exact deterministic Euler transfer without claiming that the two dynamics are equal.

The key point is that both live in the same triad-current space.

## 1. Exact deterministic triad currents

On a finite helical Galerkin network, write modal energies as

\[
n_i=|z_i|^2>0
\]

on a time interval where the selected modes are nonzero. The Euler part of the exact modal-energy dynamics can be written

\[
\boxed{
\dot n_{\rm E}=A^T J_{\rm E}(z),
}
\]

where `J_E` is the vector of signed helical triad currents determined by the exact amplitudes and phases.

This representation automatically gives

\[
\mathbf1\cdot\dot n_{\rm E}=0,
\qquad
h\cdot\dot n_{\rm E}=0.
\]

## 2. The H-current at the same covariance state

For the same positive modal energies `n`, put

\[
q=n^{-1}
\]

and define

\[
\boxed{
J_H:=WAq.
}
\]

The corresponding H-flow drift is

\[
\boxed{
Q_H(n):=A^T J_H=Lq.
}
\]

Now define the exact coherence current

\[
\boxed{
J_{\rm coh}:=J_{\rm E}-J_H.
}
\]

Then the deterministic Euler dynamics has the exact identity

\[
\boxed{
\dot n_{\rm E}
=Q_H(n)+A^T J_{\rm coh}.
}
\]

This is a definition, not an approximation.

The point is that the deterministic current has been decomposed into

- an entropy-gradient current fixed by amplitudes alone;
- a remainder carrying everything the exact phases do beyond that current.

## 3. Exact entropy balance of deterministic Euler

Let

\[
S(n)=\sum_i\log n_i.
\]

For the Euler part,

\[
\dot S_{\rm E}
=q^T A^T J_{\rm E}
=(Aq)^T J_{\rm E}.
\]

Using `J_E=J_H+J_coh`,

\[
\boxed{
\dot S_{\rm E}
=\mathcal D_H+\mathcal E_{\rm coh},
}
\]

where

\[
\boxed{
\mathcal D_H
:=(Aq)^TW(Aq)
=2\mathscr R_H
\ge0,
}
\]

and

\[
\boxed{
\mathcal E_{\rm coh}
:=(Aq)^T J_{\rm coh}.
}
\]

Thus every failure of deterministic Euler to follow the H-theorem direction is carried explicitly by the coherence current.

## 4. Coherence action and an exact dichotomy

Define

\[
\boxed{
\mathcal C_H
:=J_{\rm coh}^T W^{-1}J_{\rm coh}\ge0.
}
\]

Cauchy-Schwarz gives

\[
|\mathcal E_{\rm coh}|
\le
\sqrt{\mathcal D_H\mathcal C_H}.
\]

Therefore

\[
\boxed{
\dot S_{\rm E}
\ge
\mathcal D_H-
\sqrt{\mathcal D_H\mathcal C_H}.
}
\]

Consequences:

- if `C_H <= theta^2 D_H` with `theta<1`, then
  \[
  \boxed{\dot S_{\rm E}\ge(1-\theta)\mathcal D_H>0;}
  \]
- if `dot S_E <= 0` while `D_H>0`, then necessarily
  \[
  \boxed{\mathcal C_H\ge\mathcal D_H.}
  \]

Hence there is an exact instantaneous **H-flow-or-coherence dichotomy**:

\[
\boxed{
\text{failure of entropy production requires a coherence current at least as large as the H-current in the natural current metric.}
}
\]

No random-phase assumption is used.

## 5. Critical flux splitting

Let

\[
v_i=|h_i|,
\qquad
c_V=Av.
\]

The exact Euler critical production is

\[
\dot K_{\rm E}
=c_V^T J_{\rm E}.
\]

Hence

\[
\boxed{
\dot K_{\rm E}
=c_V^TWAq+c_V^T J_{\rm coh}.
}
\]

With

\[
\mathcal D_V:=c_V^TWc_V=2\mathscr R_V,
\]

we obtain

\[
\boxed{
|\dot K_{\rm E}|
\le
\sqrt{\mathcal D_V}
\left(
\sqrt{\mathcal D_H}
+\sqrt{\mathcal C_H}
\right).
}
\]

Thus critical transfer requires three ingredients:

1. nonzero network V-curvature `D_V`;
2. thermodynamic H-curvature `D_H`, or
3. a large deterministic coherence remainder `C_H`.

## 6. Addition of viscosity

For Navier-Stokes,

\[
\dot n
=A^T J_{\rm E}
-2\nu\,\operatorname{diag}(|k_i|^2)n.
\]

The current splitting remains exact for the Euler part. Raw `S=sum log n_i` acquires a cutoff-dependent viscous term, so it should not be used directly as an infinite-dimensional entropy.

The correct next step is a **renormalized packet entropy / relative entropy** on a moving finite active packet, compared with the H-flow equilibrium on that same packet.

## 7. Connection to existing Composition machinery

The new quantity

\[
\mathcal C_H
=\|J_{\rm E}-J_H\|_{W^{-1}}^2
\]

is a current-space definition of deterministic coherence.

The repository already has independent physical-space/Fourier signatures of coherence:

- Spin-Shadow cancellation;
- additive composition defect;
- pair-heat resonance;
- double-angle phase-plane locking;
- plane-turning bridges;
- protected reset cancellation.

The central new target is to connect them quantitatively:

\[
\boxed{
\mathcal C_H\text{ large}
\Longrightarrow
\text{large exact Composition/phase rigidity cost}.
}
\]

If this bridge is proved, the two branches become:

\[
\begin{cases}
\mathcal C_H\ll\mathcal D_H
&\Rightarrow\text{H-flow / thermalizing branch},\\
\mathcal C_H\gtrsim\mathcal D_H
&\Rightarrow\text{coherent branch controlled by exact NS geometry}.
\end{cases}
\]

This is the current candidate architecture for the project's auxiliary `Ricci-flow` mechanism.
