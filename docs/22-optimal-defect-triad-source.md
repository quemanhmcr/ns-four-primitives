# Triad Factorization of the Optimal Escape-Defect Source

The optimal protected defect

\[
\mathcal Y=\|r\|_2^2,
\qquad
r=(\Lambda-a-b\operatorname{curl})u,
\]

has an Euler source `2 Gamma_esc`. This note resolves that source on a single helical triad. The result shows that defect regeneration is not an independent cubic channel: it is forced through the same radial transfer currents already responsible for critical escape.

Throughout one instantaneous triad calculation, `a,b` are frozen at their globally minimizing values. Stationarity justifies freezing them when computing the Euler derivative of `Y`.

## 1. Helical defect weights

On a mode of radius `k` and helicity `sigma`, the multiplier

\[
T=\Lambda-a-b\operatorname{curl}
\]

has scalar symbol

\[
\boxed{
t_\sigma(k)
=(1-b\sigma)k-a.
}
\]

Hence the contribution of that mode to the quadratic defect is weighted by

\[
q_\sigma(k):=t_\sigma(k)^2.
\]

For any Euler triad with modal energy-transfer rates `T_k,T_p,T_q`, the defect production carried by the triad is

\[
\boxed{
\dot{\mathcal Y}_\triangle
=q_{\sigma_k}(k)T_k
+q_{\sigma_p}(p)T_p
+q_{\sigma_q}(q)T_q.
}
\]

This identity uses only that `Y` is a diagonal quadratic functional in the helical basis at the frozen instant.

## 2. Homochiral factorization

Take a homochiral `+,+,+` triad with radii `k,p,q`. In the orientation

\[
T_k=(p-q)J,
\qquad
T_p=(q-k)J,
\qquad
T_q=(k-p)J,
\]

we have

\[
q_+(x)=((1-b)x-a)^2.
\]

Since the transfer annihilates constant and affine functions of the signed wavenumber, only the quadratic part survives. Direct algebra gives

\[
\boxed{
\dot{\mathcal Y}_\triangle
=(1-b)^2
(p-k)(q-k)(p-q)J.
}
\]

For a `-,-,-` triad the analogous formula is obtained by replacing `b` with `-b` and adjusting the orientation sign of `J`. In magnitude,

\[
\boxed{
|\dot{\mathcal Y}_\triangle|
=|1-b\sigma|^2
|(p-k)(q-k)(p-q)J|.
}
\]

Thus homochiral recharge of the optimally protected defect carries a full three-difference Vandermonde factor. Narrow radial packets are cubically depleted at this source level.

## 3. Heterochiral same-spin handoff

Now take same-spin `+` endpoints of radii

\[
k<q
\]

and an opposite-spin `-` catalyst of radius `p`. Use the oriented transfer current

\[
T_k=(q+p)J,
\qquad
T_q=-(p+k)J,
\qquad
T_p=(k-q)J.
\]

The defect weights are

\[
q_+(x)=((1-b)x-a)^2,
\qquad
q_-(p)=((1+b)p-a)^2.
\]

Direct factorization gives

\[
\boxed{
\dot{\mathcal Y}_\triangle
=(k-q)J\,\mathfrak B_{a,b}(k,q,p),
}
\]

where

\[
\boxed{
\mathfrak B_{a,b}(k,q,p)
=(1-b)^2(p+k)(p+q)
+4p(bp-a).
}
\]

The opposite helicity configuration follows by `b -> -b` and helicity reversal.

The crucial structural point is independent of the sign of the bracket:

\[
\boxed{
\text{heterochiral defect production carries the same factor }(q-k)J
\text{ as the critical handoff.}
}
\]

There is no heterochiral source for `Y` through a same-spin endpoint pair with zero radial mismatch.

## 4. Secant-curvature interpretation

The factor `B_{a,b}` has a useful interpolation meaning.

Regard the same-spin weight as the quadratic function of signed wavenumber

\[
f_+(h)=((1-b)h-a)^2.
\]

Let `ell_{k,q}(h)` be the affine secant through

\[
(k,f_+(k)),
\qquad
(q,f_+(q)).
\]

At the opposite signed wavenumber `h=-p`, the true opposite-spin defect weight is

\[
q_-(p)=((1+b)p-a)^2.
\]

A quadratic interpolation identity gives

\[
\boxed{
\mathfrak B_{a,b}(k,q,p)
=q_-(p)-\ell_{k,q}(-p).
}
\]

Indeed,

\[
f_+(-p)-\ell_{k,q}(-p)
=(1-b)^2(p+k)(p+q),
\]

while

\[
q_-(p)-f_+(-p)
=4p(bp-a).
\]

Thus heterochiral defect regeneration is exactly the **failure of the opposite-spin protected weight to lie on the affine interpolation determined by the two same-spin endpoints**.

This makes the source a second-order compatibility defect in signed spectral geometry.

## 5. Relation to critical production

For the same orientation, the critical quantity `K` has triad production

\[
\dot K_\triangle
=2p(k-q)J.
\]

Therefore whenever `p>0`,

\[
\boxed{
\dot{\mathcal Y}_\triangle
=\frac{\mathfrak B_{a,b}(k,q,p)}{2p}
\dot K_\triangle.
}
\]

Equivalently, if `kappa_triangle=dot K_triangle/2`, then

\[
\boxed{
\Gamma_{{\rm esc},\triangle}
=\frac{\mathfrak B_{a,b}(k,q,p)}{2p}
\kappa_\triangle.
}
\]

So on one dangerous heterochiral handoff, critical escape and reopening of the optimal protected defect are driven by the **same signed transfer current**. Their ratio is a geometric/spectral interpolation coefficient, not an independent phase current.

## 6. Consequence for the reopening problem

The global differential inequality for `X=EY` left `Gamma_esc` as the main reopening source. This note sharply restricts what that source can do triadwise:

- homochiral recharge pays three radial differences;
- heterochiral recharge pays the same same-spin radial handoff factor required for `kappa`;
- on each heterochiral handoff, `Gamma_esc` is proportional to `kappa_triangle` through an explicit coefficient.

Therefore an arbitrarily fast sequence of defect-reopening bursts cannot be modeled by an unrelated generic cubic source. It must be built from the same signed heterochiral currents already subject to Spin-Shadow, Composition-Defect, pair-heat, and plane-closure constraints.

The remaining task is global: control the signed sum of the interpolation coefficients `B_{a,b}/(2p)` over a full convolution network carrying positive net critical flux. No sign-definite bound for that global sum is claimed here.
