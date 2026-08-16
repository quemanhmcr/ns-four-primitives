# Optimal Energy-Helicity Protected Escape Defect

The separate spin and within-spin radial gates admit a more primitive coordinate-free formulation. Euler has two quadratic conservation directions, represented in the `L^2` geometry by `u` and `omega`. The critical gradient `Lambda u` can drive Euler growth only through its component orthogonal to both protected directions.

This note constructs that optimal residual and derives a sharper critical escape barrier.

## 1. Orthogonal projection away from the protected directions

Choose real scalars `a,b` minimizing

\[
\|\Lambda u-a u-b\omega\|_2^2.
\]

Set

\[
\boxed{
r:=\Lambda u-a u-b\omega,
\qquad
\mathcal Y:=\|r\|_2^2.
}
\]

The normal equations are

\[
\boxed{
\langle r,u\rangle=0,
\qquad
\langle r,\omega\rangle=0.
}
\]

Thus `r` is exactly the orthogonal projection of the critical gradient `Lambda u` onto the tangent complement left after removing the two quadratic Euler protections.

## 2. Exact critical-production collapse

For the Euler forcing

\[
F=P(u\times\omega)=-P(u\cdot\nabla u),
\]

energy and helicity tangency give

\[
\langle u,F\rangle=0,
\qquad
\langle\omega,F\rangle=0.
\]

Therefore

\[
\boxed{
\kappa
=\langle\Lambda u,F\rangle
=\langle r,F\rangle.
}
\]

This is the optimal global Selection identity: only the unprotected residual can produce the critical norm.

## 3. Gram determinant formula

Define

\[
E=\|u\|_2^2,
\qquad
H=\langle u,\omega\rangle,
\qquad
K=\langle u,\Lambda u\rangle,
\qquad
Z=\|\Lambda u\|_2^2=\|\omega\|_2^2,
\]

and

\[
C:=\langle\omega,\Lambda u\rangle.
\]

The Gram matrix of the protected directions is

\[
G_2=
\begin{pmatrix}
E&H\\
H&Z
\end{pmatrix}.
\]

When

\[
\Delta:=EZ-H^2>0,
\]

the minimizers are

\[
\boxed{
a=\frac{KZ-HC}{\Delta},
\qquad
b=\frac{EC-HK}{\Delta}.
}
\]

The residual norm is the Schur complement

\[
\boxed{
\mathcal Y
=Z-
\begin{pmatrix}K&C\end{pmatrix}
G_2^{-1}
\begin{pmatrix}K\\C\end{pmatrix}.
}
\]

Equivalently,

\[
\boxed{
\mathcal Y
=
\frac{
\det
\begin{pmatrix}
E&H&K\\
H&Z&C\\
K&C&Z
\end{pmatrix}
}{EZ-H^2}.
}
\]

Thus the optimal escape defect is itself a Gram-determinant quotient measuring the failure of `Lambda u` to lie in the conservation span.

If `Delta=0`, Cauchy-Schwarz forces `omega` to be a scalar multiple of `u`; for a nonzero divergence-free periodic field this is a curl eigenstate supported on one helical shell, and `Lambda u` already lies in the protected span, so `Y=0`.

## 4. Exact zero set in helical variables

The equation `r=0` is

\[
\Lambda u=a u+b\omega.
\]

In the two helicity sectors this becomes

\[
(1-b)\Lambda u_+=a u_+,
\qquad
(1+b)\Lambda u_-=a u_-.
\]

Therefore `Y=0` has exactly the following possibilities:

1. one helicity sector is absent; then `b=+/-1,a=0` can absorb an arbitrary radial distribution in the surviving pure-spin sector;
2. both sectors are present, and each sector is individually supported on one radial shell, with possibly different shell radii.

Hence the optimal defect unifies the two exact instantaneous escape gates:

\[
\boxed{
\mathcal Y=0
\Longrightarrow
\kappa=0,
}
\]

covering both pure-spin protection and absence of within-spin radial width.

## 5. Scale-critical version and finite action

`Y` scales like `Z`. Define

\[
\boxed{
\mathcal X:=E\mathcal Y
}
\]

and the dimensionless unprotected fraction

\[
\boxed{
\chi_{\rm esc}
:=\frac{\mathcal Y}{Z}
=\frac{\mathcal X}{EZ}
\in[0,1].
}
\]

Because orthogonal projection can only decrease norm,

\[
0\le\mathcal Y\le Z,
\qquad
0\le\mathcal X\le EZ.
\]

Using

\[
(E^2)'=-4\nu EZ,
\]

we obtain the finite lifetime budget

\[
\boxed{
\int_0^T\mathcal X(t)\,dt
\le\frac{E(0)^2}{4\nu}.
}
\]

## 6. Exact optimized-defect evolution

Let

\[
T:=\Lambda-a-b\operatorname{curl},
\qquad
r=Tu.
\]

Because `a,b` are minimizers, the envelope/stationarity conditions kill the `a'` and `b'` terms when differentiating `Y`. Since all three multipliers commute with `Lambda`,

\[
\boxed{
\mathcal Y'
=2\Gamma_{\rm esc}
-2\nu\|\Lambda r\|_2^2,
}
\]

where

\[
\Gamma_{\rm esc}
:=\langle r,TF\rangle.
\]

Moreover

\[
\mathcal Y
=\langle\Lambda u,r\rangle
=\langle u,\Lambda r\rangle,
\]

because `r` is orthogonal to `u,omega`. Hence

\[
\boxed{
\mathcal Y^2
\le E\|\Lambda r\|_2^2.
}
\]

For the critical defect `X=EY`,

\[
\boxed{
\mathcal X'
=2E\Gamma_{\rm esc}
-2\nu E\|\Lambda r\|_2^2
-2\nu\frac ZE\mathcal X.
}
\]

Therefore

\[
\boxed{
\mathcal X'
\le
2E\Gamma_{\rm esc}
-2\nu\frac{\mathcal X^2}{E^2}
-2\nu\frac ZE\mathcal X.
}
\]

The optimal protected escape defect has both Riccati damping and a linear energy-dissipation damping term.

## 7. Commutator form of the optimized source

Using

\[
\operatorname{curl}(u\cdot\nabla u)
=u\cdot\nabla\omega-\omega\cdot\nabla u,
\]

we have

\[
T(u\cdot\nabla u)
=u\cdot\nabla r
+[\Lambda,u\cdot\nabla]u
+b\,\omega\cdot\nabla u.
\]

Since `r` is divergence-free,

\[
\langle r,u\cdot\nabla r\rangle=0.
\]

Therefore

\[
\boxed{
\Gamma_{\rm esc}
=-\left\langle r,
[\Lambda,u\cdot\nabla]u
+b\,\omega\cdot\nabla u
\right\rangle.
}
\]

Again the optimized defect itself appears as the outer factor in its Euler regeneration source.

## 8. Sharpened critical escape barrier

From the exact collapse,

\[
|\kappa|
\le\|r\|_2\,\|F\|_2.
\]

Sobolev estimates give

\[
\|F\|_2
\le\|u\|_6\|\omega\|_3
\le C_* Z^{1/2}M_3^{1/2}.
\]

Hence

\[
|\kappa|
\le C_*\mathcal Y^{1/2}Z^{1/2}M_3^{1/2}.
\]

For

\[
\nu_E:=\frac\kappa{M_3},
\]

and using the moment inequality

\[
Z^2\le KM_3,
\]

we obtain

\[
\boxed{
|\nu_E|
\le C_*\sqrt{K\,\chi_{\rm esc}}.
}
\]

This is the critical barrier after quotienting out **both** energy and helicity protection.

If

\[
K'>0,
\]

then `nu_E>nu`. Put

\[
a_*:=\frac{\nu^2}{C_*^2}.
\]

Necessarily

\[
\boxed{
\chi_{\rm esc}>\frac{a_*}{K}.
}
\]

Since

\[
\mathcal X=\chi_{\rm esc}EZ
\]

and

\[
EZ\ge K^2,
\]

we get the stronger scale-critical defect barrier

\[
\boxed{
K'>0
\Longrightarrow
\mathcal X
>a_*\frac{EZ}{K}
\ge a_*K.
}
\]

Thus critical growth cannot occur merely with nonzero escape defect: the optimally unprotected energy-helicity defect must grow at least linearly with the critical norm.

## 9. Consequence for positive-growth time

Let

\[
\mathcal G_+:=\{t:K'(t)>0\}.
\]

The barrier and finite action give

\[
\boxed{
\int_{\mathcal G_+}K(t)\,dt
\le
\frac{1}{a_*}
\int_0^T\mathcal X(t)dt
\le
\frac{C_*^2E(0)^2}{4\nu^3}.
}
\]

This does not by itself exclude unbounded `K`, because growth may occur in increasingly short bursts. It does, however, give a finite global budget **specifically on the times when the critical norm is increasing**, after all quadratic Euler protections have already been removed.

The remaining task is to combine this positive-growth budget with the composition/planarity mechanisms to prevent arbitrarily fast reopening of `X` at successive scales.

## 10. Sequential projection formula: spectral width minus helicity-protected width

The optimal defect can be written as an exact refinement of the ordinary centered spectral variance.

First remove only the energy direction. Set

\[
m:=\frac KE,
\qquad
s:=(\Lambda-m)u.
\]

Then

\[
\|s\|_2^2
=Z-\frac{K^2}{E}.
\]

Next center the helicity direction against energy:

\[
\eta
:=\omega-\frac HEu.
\]

We have

\[
\eta\perp u,
\qquad
\|\eta\|_2^2
=Z-\frac{H^2}{E},
\]

and

\[
\langle s,\eta\rangle
=C-\frac{HK}{E}.
\]

Because `span{u,omega}=span{u,eta}`, the optimal residual is exactly the component of `s` orthogonal to `eta`. Therefore

\[
\boxed{
\mathcal Y
=\left(Z-\frac{K^2}{E}\right)
-
\frac{
\left(C-\frac{HK}{E}\right)^2
}{
Z-\frac{H^2}{E}
}.
}
\]

Multiplying by `E`,

\[
\boxed{
\mathcal X
=(EZ-K^2)
-
\frac{(EC-HK)^2}{EZ-H^2}.
}
\]

Hence

\[
\boxed{
0\le\mathcal X\le EZ-K^2.
}
\]

The optimal protected defect is literally the ordinary radial spectral defect **minus the part explained by helicity covariance**.

## 11. Alignment form of the sharpened barrier

When `s` and `eta` are both nonzero, let `Theta` be their Hilbert-space angle:

\[
\cos\Theta
:=
\frac{\langle s,\eta\rangle}
{\|s\|_2\|\eta\|_2}.
\]

Then the sequential projection identity becomes

\[
\boxed{
\mathcal X
=(EZ-K^2)\sin^2\Theta.
}
\]

Define the ordinary normalized radial defect

\[
\delta_{\rm rad}
:=1-\frac{K^2}{EZ}
=\frac{EZ-K^2}{EZ}.
\]

The optimized unprotected fraction is therefore

\[
\boxed{
\chi_{\rm esc}
=\delta_{\rm rad}\sin^2\Theta.
}
\]

Consequently the critical barrier from Section 8 sharpens to

\[
\boxed{
|\nu_E|
\le
C_*\sqrt{K\,\delta_{\rm rad}}\,|\sin\Theta|.
}
\]

Thus ordinary spectral width is not enough. The centered radial escape direction must also have a component transverse to the centered helicity direction. Alignment of those two centered directions depletes critical production even when the spectrum is broad.

## 12. Statistical regression interpretation

Normalize the Fourier energy into a probability distribution

\[
d\mu(k,\sigma)
:=\frac{|z_\sigma(k)|^2}{E}.
\]

Let

\[
R:=|k|,
\qquad
S:=\sigma\in\{+1,-1\}.
\]

Then

\[
\frac KE=\mathbb E_\mu R,
\qquad
\frac HE=\mathbb E_\mu(SR),
\]

\[
\frac ZE=\mathbb E_\mu R^2,
\qquad
\frac CE=\mathbb E_\mu(SR^2).
\]

Therefore

\[
EZ-K^2
=E^2\operatorname{Var}_\mu(R),
\]

\[
EZ-H^2
=E^2\operatorname{Var}_\mu(SR),
\]

and

\[
EC-HK
=E^2\operatorname{Cov}_\mu(R,SR).
\]

The critical optimal defect is exactly

\[
\boxed{
\frac{\mathcal X}{E^2}
=
\operatorname{Var}(R)
-
\frac{\operatorname{Cov}(R,SR)^2}
{\operatorname{Var}(SR)}.
}
\]

Thus `X/E^2` is the residual variance of radial frequency after optimal linear regression against signed-helicity frequency. The two Euler conservation directions remove exactly the linearly predictable part; singular escape can use only the regression residual.

## 13. Exact spin-times-radial factorization of the regression determinant

The statistical regression formula can be resolved completely into helicity-sector populations and within-spin radial variances.

Let

\[
p_+:=\frac{E_+}{E},
\qquad
p_-:=\frac{E_-}{E},
\qquad
p_++p_-=1.
\]

For each nonempty sector define the conditional radial mean and variance

\[
m_\pm
:=\mathbb E(R\mid S=\pm1)
=\frac{K_\pm}{E_\pm},
\]

\[
v_\pm
:=\operatorname{Var}(R\mid S=\pm1)
=\frac{W_\pm}{E_\pm}.
\]

A direct two-population calculation gives

\[
\boxed{
\det\operatorname{Cov}(R,SR)
=4p_+p_-
\left(
 p_-m_+^2v_-
+p_+m_-^2v_+
+v_+v_-
\right).
}
\]

On the other hand,

\[
\frac{\mathcal X}{E^2}
=\frac{
\det\operatorname{Cov}(R,SR)
}{
\operatorname{Var}(SR)
},
\]

and

\[
\frac ZE=\mathbb E(R^2).
\]

Therefore the optimized unprotected fraction has the exact form

\[
\boxed{
\chi_{\rm esc}
=
\frac{
4p_+p_-
\left(
 p_-m_+^2v_-
+p_+m_-^2v_+
+v_+v_-
\right)
}{
\operatorname{Var}(SR)\,\mathbb E(R^2)
}.
}
\]

This formula quantitatively unifies the two instantaneous critical-production gates:

- the factor `p_+ p_-` measures coexistence of both helicity sectors at the energy level;
- `v_+,v_-` measure radial width inside those sectors;
- if either spin population disappears, the optimized defect vanishes;
- if both within-spin variances vanish, the optimized defect vanishes;
- if one sector is monochromatic but the other is broadband, the defect remains positive through the mean-frequency term of the opposite sector.

Thus the Gram residual is not merely qualitatively equivalent to the separate spin/radial conditions. It is their exact regression coupling.
