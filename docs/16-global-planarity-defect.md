# Global Critical Planarity Defect

The active-frame lemmas describe local preferred Fourier planes. This note introduces a single coordinate-free critical tensor whose null set is exactly the globally planar `2D3C` class. It provides a global scalar carrier for plane dispersion and has an exact modulated evolution with viscous Riccati damping.

We work first on the zero-mean periodic domain, so every nonzero Fourier mode satisfies `|k|>=1` after the standard normalization.

## 1. The critical planarity tensor

Let `D=-i grad` and `Lambda=|D|`. Define the symmetric `3 x 3` matrix

\[
\boxed{
\mathsf A(u)_{ij}
:=\left\langle D_i\Lambda^{-1/2}u,
D_j\Lambda^{-1/2}u\right\rangle.
}
\]

Equivalently,

\[
\mathsf A(u)
=\sum_{k\ne0}
\frac{k\otimes k}{|k|}\,|\widehat u(k)|^2.
\]

It is positive semidefinite and

\[
\boxed{
\operatorname{tr}\mathsf A(u)
=\sum_{k\ne0}|k||\widehat u(k)|^2
=K.
}
\]

For a unit vector `n`, define

\[
\mathcal P_n(u)
:=n^T\mathsf A(u)n.
\]

Then

\[
\boxed{
\mathcal P_n(u)
=\sum_{k\ne0}\frac{(n\cdot k)^2}{|k|}|\widehat u(k)|^2
=\|D_n\Lambda^{-1/2}u\|_2^2
=\|\partial_nu\|_{\dot H^{-1/2}}^2.
}
\]

Define the optimal global planarity defect

\[
\boxed{
\mathcal P(u)
:=\min_{|n|=1}\mathcal P_n(u)
=\lambda_{\min}(\mathsf A(u)).
}
\]

Thus `P` is scale-critical, exactly like `K`.

## 2. Exact zero set

Because every summand in `P_n` is nonnegative,

\[
\mathcal P(u)=0
\]

if and only if there exists a unit vector `n` such that

\[
(n\cdot k)\widehat u(k)=0
\qquad\text{for every }k.
\]

Hence

\[
\boxed{
\mathcal P(u)=0
\iff
\operatorname{supp}\widehat u\subset n^\perp
\text{ for some }n.
}
\]

The zero set is exactly the globally fixed Fourier-plane class treated in `09-planar-endpoint.md`, hence the `2D3C` regular endpoint.

Since `A` is positive semidefinite with trace `K`,

\[
\boxed{0\le\mathcal P\le K/3.}
\]

The normalized quantity

\[
\mathfrak p:=\frac{3\mathcal P}{K}\in[0,1]
\]

may be viewed as a global critical nonplanarity fraction when `K>0`.

## 3. Fixed-direction evolution

For fixed unit `n`, define the self-adjoint Fourier multiplier

\[
A_n:=D_n^2\Lambda^{-1}
\]

and

\[
B_n:=D_n\Lambda^{-1/2},
\qquad A_n=B_n^2.
\]

Then

\[
\mathcal P_n=\langle u,A_nu\rangle.
\]

For

\[
\partial_tu=F-\nu\Lambda^2u,
\]

differentiation gives exactly

\[
\boxed{
\mathcal P_n'
=2\Gamma_n-2\nu\mathcal H_n,
}
\]

where

\[
\Gamma_n:=\langle A_nu,F\rangle,
\qquad
\mathcal H_n:=\langle A_nu,\Lambda^2u\rangle
=\|D_n\Lambda^{1/2}u\|_2^2.
\]

Thus viscosity damps precisely the one-directional defect at one derivative higher.

## 4. Envelope theorem without differentiating the minimizing plane

Let `n` be any minimizing eigenvector of `A(u(t))` at time `t`, so

\[
\mathcal P(t)=\mathcal P_n(t).
\]

Even if the minimizing eigenvector is not unique or differentiable in time,

\[
\mathcal P(t+h)
\le\mathcal P_n(t+h).
\]

Therefore the upper Dini derivative obeys

\[
\boxed{
D^+\mathcal P(t)
\le2\Gamma_n(t)-2\nu\mathcal H_n(t)
}
\]

for every minimizing direction `n` at that time.

No `n'(t)` term appears. This is the same envelope mechanism that makes optimized spectral defects useful.

## 5. Viscous Riccati damping on the torus

For zero-mean periodic data, Cauchy-Schwarz gives

\[
\mathcal P_n^2
\le\mathcal H_n
\sum_{k\ne0}
\frac{(n\cdot k)^2}{|k|^3}|\widehat u(k)|^2.
\]

Since

\[
\frac{(n\cdot k)^2}{|k|^3}\le\frac1{|k|}\le1,
\]

we obtain

\[
\boxed{
\mathcal P_n^2\le E\,\mathcal H_n.
}
\]

At a minimizing direction,

\[
\mathcal H_n\ge\frac{\mathcal P^2}{E}.
\]

Hence

\[
\boxed{
D^+\mathcal P
\le
2\Gamma_n
-2\nu\frac{\mathcal P^2}{E}.
}
\]

The global planarity defect therefore carries an exact viscous Riccati damping term. The only remaining source is its Euler production `Gamma_n`.

## 6. Commutator collapse of the Euler production

Because `B_n` commutes with the Leray projector and with spatial derivatives, and `B_nu` is divergence-free,

\[
\Gamma_n
=\langle A_nu,F\rangle
=-\langle B_nu,B_n(u\cdot\nabla u)\rangle.
\]

Put

\[
v_n:=B_nu.
\]

Then

\[
B_n(u\cdot\nabla u)
=u\cdot\nabla v_n+[B_n,u\cdot\nabla]u.
\]

Incompressibility gives

\[
\langle v_n,u\cdot\nabla v_n\rangle=0.
\]

Therefore

\[
\boxed{
\Gamma_n
=-\langle v_n,[B_n,u\cdot\nabla]u\rangle.
}
\]

So the Euler production of global nonplanarity is not a generic cubic term: it is exactly the current directional defect paired with a fractional transport commutator.

## 7. Exact directional-factorization of the source

The commutator source contains the off-plane derivative as an explicit factor, not merely through `v_n` in the outer pairing.

Let

\[
L:=\Lambda^{-1/2},
\qquad
w_n:=D_nu,
\qquad
B_n=LD_n,
\qquad
v_n=Lw_n.
\]

Since `D_n` is an exact derivation,

\[
D_n(u\cdot\nabla u)
=(D_nu)\cdot\nabla u
+u\cdot\nabla(D_nu).
\]

Therefore

\[
\boxed{
[B_n,u\cdot\nabla]u
=
L\bigl(w_n\cdot\nabla u\bigr)
+[L,u\cdot\nabla]w_n.
}
\]

Substituting into the commutator collapse gives

\[
\boxed{
\Gamma_n
=-\langle Lw_n,
L(w_n\cdot\nabla u)\rangle
-\langle Lw_n,
[L,u\cdot\nabla]w_n\rangle.
}
\]

Thus **every Euler term that creates the directional planarity defect contains the directional derivative `w_n=D_nu` at least twice**. Exact planarity (`w_n=0`) is therefore a quadratic zero of the Euler source, not merely an invariant set detected after cancellation.

This identity is exact. Turning it into a critical near-planar estimate without importing a supercritical norm remains open.

## 8. Fourier symbol of the planarity commutator

The symbol of `B_n` is

\[
b_n(k)=\frac{n\cdot k}{|k|^{1/2}}.
\]

Hence

\[
\widehat{[B_n,u\cdot\nabla]u}(k)
=i\sum_{p+q=k}
\left(
\frac{n\cdot k}{|k|^{1/2}}
-
\frac{n\cdot q}{|q|^{1/2}}
\right)
(q\cdot\widehat u(p))\widehat u(q).
\]

The source of global plane motion therefore carries a genuine directional spectral difference in addition to incompressibility.

When the state is exactly planar with normal `n`, `v_n=0` and the production vanishes identically.

## 9. Why this is useful for Composition

The graph-level program had an unresolved slow-turning loophole: local preferred planes might rotate by tiny angles through many generations. The scalar `P` provides a global way to measure the accumulated failure of all active scales to share one plane.

A useful future bridge is to prove a quantitative implication of the form

\[
\text{large weighted active-frame plane dispersion}
\Longrightarrow
\mathcal P\text{ large},
\]

under the already required angular nondegeneracy of the active packet.

Then the evolution above would convert plane turning into a competition between

- commutator production `Gamma_n`, and
- Riccati viscous damping `nu P^2/E`.

The missing theorem is a scale-critical control of the positive part of `Gamma_n` using the exact helical/composition structure already developed in the repository. This is open.

## 10. Finite lifetime action of global nonplanarity

The energy identity gives

\[
E'=-2\nu Z.
\]

Since

\[
K^2\le EZ,
\]

we have

\[
(E^2)'=-4\nu EZ\le-4\nu K^2,
\]

and therefore

\[
\boxed{
\int_0^T K(t)^2\,dt
\le\frac{E(0)^2}{4\nu}.
}
\]

Because `0 <= P <= K/3`, the global planarity defect automatically satisfies

\[
\boxed{
\int_0^T\mathcal P(t)^2\,dt
\le\frac{E(0)^2}{36\nu}.
}
\]

Thus genuinely three-dimensional critical geometry already has a finite lifetime action. As with the earlier critical budget, this does not by itself exclude increasingly short bursts; its intended role is as a compactness/rigidity budget rather than a standalone Gronwall estimate.

## 11. Relation to existing directional-derivative criteria

The identity

\[
\mathcal P_n=\|\partial_nu\|_{\dot H^{-1/2}}^2
\]

shows that planarity is naturally an anisotropic critical regularity variable rather than merely a support geometry. Existing one-directional-derivative regularity criteria provide an external consistency check for this choice of variable, but no such criterion is imported here as a closing theorem.
