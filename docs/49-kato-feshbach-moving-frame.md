# Kato–Feshbach Moving-Frame Passivity

**Claim level:** exact Hilbert-space operator algebra. Quantitative scale-uniform coercivity remains open.

The passive Feshbach construction in `46-passive-feshbach-bath.md` was written for a frozen protected projection. This note removes the most immediate sign concern caused by a moving protected frame.

## 1. Kato connection of an orthogonal projector

Let `P(t)` be a differentiable family of orthogonal projections and set

\[
G_P:=[\dot P,P].
\]

Differentiating `P^2=P` gives

\[
P\dot PP=0,
\qquad
Q\dot PQ=0,
\qquad Q=I-P.
\]

Since `P` and `dot P` are self-adjoint,

\[
\boxed{G_P^*=-G_P.}
\]

Moreover

\[
\boxed{\dot P=[G_P,P].}
\]

Let `U(t)` solve

\[
\dot U=G_PU,
\qquad U(0)=I.
\]

Then `U` is unitary and

\[
\boxed{P(t)=U(t)P(0)U(t)^*.}
\]

Thus Kato parallel transport freezes the moving protected subspace without introducing dissipation.

## 2. The transformed Navier–Stokes connection remains skew plus dissipative

Along a smooth trajectory write the linear operator acting on the current state as

\[
L(t)=\mathcal A(t)-D(t),
\qquad
\mathcal A(t)^*=-\mathcal A(t),
\qquad
D(t)=D(t)^*\ge0.
\]

For Navier–Stokes, `A` is the Euler cross-product connection and `D` is viscosity, after whatever positive RG normalization is being used.

In the Kato frame, `v=U^*u`,

\[
\dot v=\widetilde L v,
\]

with

\[
\widetilde L
=U^*LU-U^*G_PU.
\]

Therefore

\[
\boxed{
\widetilde L
=\widetilde{\mathcal A}-\widetilde D,
}
\]

where

\[
\widetilde{\mathcal A}
:=U^*(\mathcal A-G_P)U
\]

is skew-adjoint and

\[
\widetilde D:=U^*DU\ge0.
\]

So motion of the protected frame contributes only another **skew connection**. It does not by itself create negative damping.

## 3. Accretive Schur-complement theorem

Fix `Re z>=0` and define

\[
M(z):=zI-\widetilde L
=zI+\widetilde D-\widetilde{\mathcal A}.
\]

Then

\[
\operatorname{Re}\langle w,M(z)w\rangle
=(\operatorname{Re}z)\|w\|^2
+\langle w,\widetilde Dw\rangle
\ge0.
\]

Block-decompose with respect to the now fixed projection `P(0)` and `Q(0)`. Assume `M_QQ(z)` is invertible. Define the Feshbach Schur complement

\[
S(z)
:=M_{PP}-M_{PQ}M_{QQ}^{-1}M_{QP}.
\]

For any protected vector `x`, put

\[
y:=-M_{QQ}^{-1}M_{QP}x.
\]

Then

\[
M(z)\binom{x}{y}
=\binom{S(z)x}{0}.
\]

Hence

\[
\boxed{
\operatorname{Re}\langle x,S(z)x\rangle
=
\operatorname{Re}
\left\langle
\binom{x}{y},
M(z)\binom{x}{y}
\right\rangle
\ge0.
}
\]

Therefore the effective protected impedance remains **positive real** even after the moving protected frame is frozen by Kato transport.

This statement does not require the dissipative operator to remain block diagonal after the frame transformation.

## 4. Consequence for the physical-shift program

The main concern was that a rapidly moving protected geometry could pump energy back from the bath and destroy the sign of the Feshbach mechanism. The Kato formulation shows that frame motion itself is geometrically skew. The full transformed operator remains accretive after adding viscosity, and its exact Schur complement remains accretive.

Thus the hard question is narrowed from

\[
\text{does moving geometry destroy passivity?}
\]

to

\[
\boxed{
\text{is the positive-real Schur complement quantitatively coercive}
\text{ away from the dark/safe set?}
}
\]

This is a much sharper theorem target.

## 5. Remaining difficulty

Accretivity alone is not enough. A singularity proof would need a lower bound whose constant is stable under

- strong RG coupling;
- increasing Fourier scale;
- near-protected soft shell localization;
- possible dark-state cancellation.

The finite-packet Feshbach tests suggest the correct normalized strength is the theta-clock quantity

\[
\varepsilon^{-1}\Sigma_\varepsilon,
\]

with a gap degenerating quadratically at the known safe heat-line stratum.

The next theorem target is therefore a quantitative **Kato–Feshbach dark-state inequality**, with the deterministic Composition defect controlling any additional near-kernel beyond the classified safe geometry.
