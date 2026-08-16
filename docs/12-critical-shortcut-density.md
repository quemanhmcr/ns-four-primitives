# Critical-Amplitude Shortcut Density

The Plane-Turning Bridge Lemma is a coefficient statement. This note adds an exact amplitude algebra showing that a strong critical backbone cannot suppress all two-step bridge amplitudes by alternating large and small modal amplitudes.

## 1. Critical modal amplitudes

For a same-spin backbone of modes

\[
K_0,K_1,\dots,K_m,
\qquad
k_j:=|K_j|,
\]

define the critical modal amplitudes

\[
a_j:=k_j^{1/2}|z_s(K_j)|.
\]

Then `a_j^2` is exactly the modal contribution to the critical quantity

\[
K_s=\sum_k |k||z_s(k)|^2.
\]

Define adjacent critical pair products

\[
\pi_j:=a_ja_{j+1}
\]

and two-step shortcut products

\[
\beta_j:=a_ja_{j+2}.
\]

## 2. Exact shortcut product identity

For every index for which both sides are defined,

\[
\boxed{
\beta_j\beta_{j+1}=\pi_j\pi_{j+2}.
}
\]

Indeed,

\[
(a_ja_{j+2})(a_{j+1}a_{j+3})
=(a_ja_{j+1})(a_{j+2}a_{j+3}).
\]

Consequently, if the selected backbone obeys the uniform critical parent-product lower bound

\[
\pi_j\ge P>0
\]

for every adjacent handoff, then

\[
\boxed{
\beta_j\beta_{j+1}\ge P^2.
}
\]

Therefore

\[
\boxed{
\max\{\beta_j,\beta_{j+1}\}\ge P.
}
\]

In words: **two consecutive two-step shortcuts cannot both have subcritical endpoint product.**

Pairing consecutive shortcut indices also gives the density estimate

\[
\boxed{
\sum_{j=0}^{m-2}\beta_j
\ge
2P\left\lfloor\frac{m-1}{2}\right\rfloor.
}
\]

up to a possible unpaired final shortcut. Thus strong adjacent critical products force a linear amount of total two-step shortcut product.

## 3. Bridge forcing in critical variables

For the triple `K_j,K_{j+1},K_{j+2}`, let

- `theta_j` be the angle between `K_j,K_{j+1}`,
- `theta_{j+1}` the angle between `K_{j+1},K_{j+2}`,
- `delta_j` the projective turning angle between the two handoff planes.

The Plane-Turning Bridge Lemma gives

\[
|C_{{\rm bridge},j}|
\ge
\frac{k_{j+2}-k_j}{\sqrt2}
\sin\theta_j\sin\theta_{j+1}|\sin\delta_j|
\]

for a radially increasing backbone.

Since

\[
|z_s(K_j)z_s(K_{j+2})|
=\frac{\beta_j}{\sqrt{k_jk_{j+2}}},
\]

the actual selected pair contribution to the same-spin bridge output satisfies

\[
\boxed{
|G_{{\rm bridge},j}|
\ge
\frac{k_{j+2}-k_j}
{\sqrt{2k_jk_{j+2}}}
\,\beta_j
\sin\theta_j\sin\theta_{j+1}|\sin\delta_j|.
}
\]

This is scale invariant when written in critical amplitudes.

## 4. Local strong-turn corollary

Assume a local backbone block obeys

\[
\frac{k_{j+2}-k_j}{\sqrt{k_jk_{j+2}}}\ge\gamma>0,
\qquad
\sin\theta_j\ge\eta>0,
\]

and all adjacent critical pair products satisfy `pi_j >= P`.

For two consecutive turning indices `j,j+1`, if

\[
|\sin\delta_j|,|\sin\delta_{j+1}|\ge\tau,
\]

then at least one of the two bridge pair forcings obeys

\[
\boxed{
\max\{|G_{{\rm bridge},j}|,
       |G_{{\rm bridge},j+1}|\}
\ge
\frac{\gamma\eta^2\tau}{\sqrt2}P.
}
\]

Thus amplitude zig-zag cannot hide **two consecutive definite plane turns** along a uniformly strong critical backbone.

## 5. Remaining loophole and the correct next reduction

The exact identity does leave one structured possibility: strong and weak two-step shortcut products may alternate, and the plane may attempt to turn only at isolated weak shortcuts.

This is not treated as a negligible technicality. It identifies the next renormalization problem:

1. weak turning shortcuts are isolated by the product identity;
2. neighboring strong shortcuts define a coarser backbone;
3. if the plane turn merely moves to that coarser backbone, the Plane-Turning Bridge Lemma applies again;
4. if it does not, the strong modes are approaching a common planar geometry, suggesting a near-2D rigidity branch.

A rigorous iteration of this coarse-graining is still open. The purpose of this note is to remove the simpler false loophole that arbitrary amplitude alternation could make every turning bridge weak.
