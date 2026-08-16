# Joint Spin-Volume Danger Action

The two-spin defect and the planarity-volume determinant detect two different safe boundaries:

- `B=0`: one critical helicity sector is absent;
- `det A=0`: the critical Fourier geometry is globally planar.

This note combines them into one scale-critical scalar with a finite lifetime budget and an exact parabolic source/damping balance.

## 1. Definition

Let

\[
\mathcal B=K^2-\mathcal H^2=4K_+K_-,
\]

and let

\[
\mathcal D:=\det\mathsf A.
\]

Define

\[
\boxed{
\mathcal J
:=\mathcal B^{1/2}\mathcal D^{1/3}.
}
\]

Both factors are scale invariant under the three-dimensional Navier-Stokes scaling, so `J` is scale invariant.

Its exact zero set is the union

\[
\boxed{
\{\mathcal J=0\}
=\{\mathcal B=0\}
\cup
\{\mathcal D=0\}.
}
\]

Thus `J` vanishes whenever the state lies either on the pure-critical-spin boundary or on the globally planar Fourier boundary.

## 2. Sharp elementary upper bound and finite lifetime action

Since

\[
\sqrt{\mathcal B}\le K
\]

and

\[
\mathcal D^{1/3}\le\frac K3,
\]

we obtain

\[
\boxed{
0\le\mathcal J\le\frac{K^2}{3}.
}
\]

The energy-squared budget therefore gives

\[
\boxed{
\int_0^T\mathcal J(t)\,dt
\le\frac13\int_0^T K(t)^2dt
\le\frac{E(0)^2}{12\nu}.
}
\]

So simultaneous two-spin/nonplanar critical geometry has a finite global lifetime action.

## 3. Exact evolution away from the boundary

Assume temporarily that

\[
\mathcal B>0,
\qquad
\mathcal D>0.
\]

From `18-two-spin-self-balancing.md`,

\[
\mathcal B'
=4K\kappa
-2\nu\Omega_{\rm spin}^2\mathcal B,
\]

where

\[
\Omega_{\rm spin}^2
:=\Omega_+^2+\Omega_-^2.
\]

From `17-planarity-volume-determinant.md`,

\[
\mathcal D'
=2\Xi_{\rm vol}
-2\nu\Omega_{\rm vol}^2\mathcal D.
\]

Taking the logarithmic derivative of

\[
\mathcal J=\mathcal B^{1/2}\mathcal D^{1/3}
\]

gives exactly

\[
\boxed{
\frac{\mathcal J'}{\mathcal J}
=
\frac{2K\kappa}{\mathcal B}
+
\frac{2\Xi_{\rm vol}}{3\mathcal D}
-
\nu\Omega_{\rm spin}^2
-
\frac23\nu\Omega_{\rm vol}^2.
}
\]

Equivalently,

\[
\boxed{
\mathcal J'
=
\mathcal J\left(
\frac{2K\kappa}{\mathcal B}
+
\frac{2\Xi_{\rm vol}}{3\mathcal D}
\right)
-
\nu\left(
\Omega_{\rm spin}^2
+
\frac23\Omega_{\rm vol}^2
\right)\mathcal J.
}
\]

## 4. Interpretation

A genuinely dangerous critical state must keep both factors of `J` alive:

1. two helicity sectors must remain populated strongly enough for heterochiral critical escape;
2. the active Fourier geometry must remain genuinely three-dimensional rather than collapsing toward the regular planar endpoint.

Viscosity attacks these two requirements simultaneously at the combined parabolic rate

\[
\boxed{
\Omega_{\rm joint}^2
:=\Omega_{\rm spin}^2
+\frac23\Omega_{\rm vol}^2.
}
\]

Euler can oppose this only through the two exact sources

\[
\frac{2K\kappa}{\mathcal B}
\quad\text{and}\quad
\frac{2\Xi_{\rm vol}}{3\mathcal D}.
\]

The first source is already tied to the catalyst/shadow algebra. The second is the cofactor-weighted directional commutator source. Hence the remaining proof problem is now naturally a **joint source rigidity problem**, rather than two unrelated estimates.

## 5. Dimensionless joint geometry fraction

Define

\[
\mathfrak b:=\frac{\mathcal B}{K^2}
\in[0,1],
\]

and

\[
\mathfrak V:=\frac{27\mathcal D}{K^3}
\in[0,1].
\]

Then

\[
\boxed{
\frac{3\mathcal J}{K^2}
=\mathfrak b^{1/2}\mathfrak V^{1/3}
\in[0,1].
}
\]

Thus `3J/K^2` is a dimensionless joint-danger fraction:

- it is small if the state is nearly single-spin;
- it is small if the state is nearly planar;
- it is order one only when both two-spin balance and three-dimensional directional volume are order one at the critical level.

This does not by itself measure radial same-spin mismatch, so it is not an instantaneous proxy for `kappa`. It measures the global geometry required for a genuinely three-dimensional heterochiral escape mechanism to persist.

## 6. The missing source theorem

A clean closing theorem would control the positive joint Euler source by quantities already known to incur composition/leakage cost. Schematically, one wants to turn

\[
\boxed{
\frac{2K\kappa}{\mathcal B}
+
\frac{2\Xi_{\rm vol}}{3\mathcal D}
}
\]

into a quantity that cannot dominate

\[
\nu\Omega_{\rm joint}^2
\]

through an infinite sequence of critical parabolic epochs.

No such source theorem is claimed here. The value of `J` is that it identifies exactly what must be regenerated simultaneously and packages the two safe boundaries into one finite-action scalar.
