# Two-Spin Self-Balancing Law

The helical decomposition gives a second global scalar defect that complements the planarity tensor. It measures how far the critical mass lies from the pure-helicity boundary and has an exact source/damping balance.

## 1. Critical spin masses

Write

\[
u=u_++u_-,
\qquad
\operatorname{curl}u_\pm=\pm\Lambda u_\pm.
\]

Define

\[
K_\pm:=\langle u_\pm,\Lambda u_\pm\rangle,
\qquad
K=K_++K_-,
\]

and helicity

\[
\mathcal H
:=\langle u,\omega\rangle
=K_+-K_-.
\]

Then the unsigned two-spin defect is

\[
\boxed{
\mathcal B
:=K^2-\mathcal H^2
=4K_+K_-\ge0.
}
\]

Thus `B=0` exactly when one critical helicity sector is absent.

The normalized polarization defect is

\[
\boxed{
\mathfrak b
:=\frac{\mathcal B}{K^2}
=1-\left(\frac{\mathcal H}{K}\right)^2
\in[0,1]
}
\]

when `K>0`.

## 2. Exact full Navier-Stokes evolution

Recall

\[
K'=2\kappa-2\nu M_3,
\qquad
M_3=M_{3,+}+M_{3,-},
\]

where

\[
M_{3,\pm}:=\|\Lambda^{3/2}u_\pm\|_2^2.
\]

Euler helicity conservation gives no nonlinear contribution to `H'`, while viscosity gives

\[
\boxed{
\mathcal H'
=-2\nu\left(M_{3,+}-M_{3,-}\right).
}
\]

Therefore

\[
\begin{aligned}
\mathcal B'
&=2KK'-2\mathcal H\mathcal H'\\
&=4K\kappa
-4\nu\left[
K(M_{3,+}+M_{3,-})
-\mathcal H(M_{3,+}-M_{3,-})
\right].
\end{aligned}
\]

Using `K=K_++K_-` and `H=K_+-K_-`, the bracket is

\[
2(K_+M_{3,-}+K_-M_{3,+}).
\]

Hence

\[
\boxed{
\mathcal B'
=4K\kappa
-8\nu\left(
K_+M_{3,-}+K_-M_{3,+}
\right).
}
\]

This identity remains valid when one spin sector vanishes, with the obvious interpretation of the right-hand side.

## 3. Exact spin-defect parabolic frequency

When `K_+,K_->0`, define

\[
\Omega_\pm^2
:=\frac{M_{3,\pm}}{K_\pm}.
\]

These are the critical-mass weighted mean-square frequencies in the two helicity sectors. Since

\[
K_+M_{3,-}+K_-M_{3,+}
=K_+K_-(\Omega_+^2+\Omega_-^2)
=\frac{\mathcal B}{4}
(\Omega_+^2+\Omega_-^2),
\]

we obtain the exact scalar balance

\[
\boxed{
\mathcal B'
=4K\kappa
-2\nu(\Omega_+^2+\Omega_-^2)\mathcal B.
}
\]

This is the helical analogue of the global planarity-volume balance:

- positive critical production `kappa>0` regenerates two-spin mass;
- viscosity damps two-spin mass at the sum of the two spin-sector parabolic frequencies.

## 4. Euler self-balancing

For the inviscid Euler part, helicity is constant and

\[
K'=2\kappa.
\]

Therefore

\[
\boxed{
\mathcal B'_{\rm Euler}=4K\kappa.
}
\]

In particular, whenever `kappa>0`, the unsigned two-spin defect increases.

For the normalized defect,

\[
\mathfrak b
=1-\frac{\mathcal H^2}{K^2},
\]

so under Euler

\[
\boxed{
\mathfrak b'_{\rm Euler}
=\frac{4\kappa\mathcal H^2}{K^3}\ge0
\qquad\text{when }\kappa\ge0.
}
\]

Thus positive critical escape drives the state away from the pure-helicity boundary and toward the balanced two-spin interior. This is an exact feedback law, not merely the statement that heterochiral triads are present.

## 5. High-frequency two-spin damping

Suppose the critical masses of both spin sectors involved in an event are supported at frequencies at least `N`. Then

\[
\Omega_+^2,\Omega_-^2\ge N^2,
\]

and therefore

\[
\boxed{
\mathcal B'
\le4K\kappa-4\nu N^2\mathcal B.
}
\]

So a high-frequency balanced two-spin state has an intrinsic parabolic lifetime unless Euler regenerates `B` at the same `N^2` rate.

More generally, the exact damping frequency

\[
\Omega_{\rm spin}^2:=\Omega_+^2+\Omega_-^2
\]

identifies the scale at which the two-spin obstruction is physically active.

## 6. Finite lifetime action

Since

\[
0\le\mathcal B\le K^2
\]

and the energy-squared identity gives

\[
\int_0^T K(t)^2\,dt
\le\frac{E(0)^2}{4\nu},
\]

we automatically have

\[
\boxed{
\int_0^T\mathcal B(t)\,dt
\le\frac{E(0)^2}{4\nu}.
}
\]

Thus balanced two-spin critical activity has a finite total lifetime budget. As with the planarity and volume budgets, this does not alone exclude shortening bursts; it provides a global action to combine with scale-local rigidity.

## 7. Relation to the Spin-Shadow mechanism

The scalar law and the pair-level Spin-Shadow mechanism describe the same feedback at different resolutions.

At pair level, a same-spin radial handoff requires an opposite-spin catalyst and simultaneously forces a same-spin shadow at that catalyst wavevector.

At global level, positive `kappa` necessarily raises `B` in the Euler dynamics. Hence a critical escape chain cannot remain asymptotically on the pure-helicity boundary while continuing to produce positive critical flux.

Avoiding the resulting high-frequency two-spin damping requires repeated Euler regeneration, which is precisely where the exact catalyst/shadow/composition algebra becomes relevant.

## 8. New combined endgame

A candidate singular escape now has to sustain two separate critical defects against parabolic damping:

1. **two-spin defect** `B`, with damping frequency `Omega_spin`;
2. **three-dimensional volume defect** `det A`, with damping frequency `Omega_vol`.

If the first collapses, the heterochiral critical channel disappears. If the second collapses, the active geometry planarizes toward the regular 2D3C endpoint.

The remaining genuinely dangerous regime must therefore regenerate both

\[
\boxed{
\text{balanced two-spin mass}
\quad+\quad
\text{nonplanar Fourier volume}
}
\]

at parabolic high-frequency rates while preserving positive critical flux. The next target is to exploit the fact that the same exact helical convolution is responsible for both regeneration mechanisms.
