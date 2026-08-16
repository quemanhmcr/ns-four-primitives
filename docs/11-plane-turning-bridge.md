# Plane Turning Creates a Mandatory Cross-Generation Bridge

This note proves a coefficient-level Plane-Turning Lemma directly from the exact same-spin helical coefficient. It is the first exact mechanism coupling two consecutive selected handoffs.

## 1. Two consecutive same-spin handoffs

Let three nonzero Fourier modes `K,Q,R` carry the same helicity `s`, with radii

\[
0<k:=|K|<q:=|Q|<r:=|R|.
\]

Think of the selected consecutive handoffs as using the parent pairs

\[
Q^s+(-K)^s\to (Q-K)^{-s},
\]

and

\[
R^s+(-Q)^s\to (R-Q)^{-s}.
\]

The two parent planes are

\[
\Pi_1=\operatorname{span}\{K,Q\},
\qquad
\Pi_2=\operatorname{span}\{Q,R\}.
\]

Assume both are nondegenerate. Define

\[
A_1:=|Q\times K|,
\qquad
A_2:=|R\times Q|,
\]

and unit normals

\[
n_1=\frac{Q\times K}{A_1},
\qquad
n_2=\frac{R\times Q}{A_2}.
\]

The projective turning angle `delta` is measured by

\[
|\sin\delta|:=|n_1\times n_2|.
\]

Let `theta_1` be the angle between `K,Q` and `theta_2` the angle between `Q,R`.

## 2. Exact scalar-triple geometry

The full quadratic convolution necessarily also contains the cross-generation parent pair

\[
R^s+(-K)^s\to B,
\qquad
B:=R-K,
\qquad
b:=|B|.
\]

The scalar triple product satisfies exactly

\[
|Q\cdot(R\times K)|
=\frac{A_1A_2}{q}|\sin\delta|.
\]

Since

\[
|Q\cdot(R\times K)|\le q|R\times K|,
\]

we obtain

\[
\boxed{
|R\times K|
\ge
\frac{A_1A_2}{q^2}|\sin\delta|.
}
\]

Using

\[
A_1=qk\sin\theta_1,
\qquad
A_2=rq\sin\theta_2,
\]

this becomes the scale-free angular identity

\[
\boxed{
|R\times K|
\ge
rk\,\sin\theta_1\sin\theta_2|\sin\delta|.
}
\]

Thus genuine turning between two individually nondegenerate handoff planes forces the endpoint pair `R,K` itself to be noncollinear.

## 3. Exact bridge coefficient and lower bound

For the same-spin output `B^s`, the exact coefficient from `01-nonlinear-base.md` is

\[
|C_{\rm bridge}|
=
\frac1{2\sqrt2}(r-k)
\frac{|R\times K|}{brk}
(r+k+b).
\]

Because the triangle inequality gives `r+k >= b`,

\[
\frac{r+k+b}{b}\ge2.
\]

Combining with the previous section yields

\[
\boxed{
|C_{\rm bridge}|
\ge
\frac{r-k}{\sqrt2}
\sin\theta_1\sin\theta_2|\sin\delta|.
}
\]

This is the coefficient-level **Plane-Turning Bridge Lemma**.

It is uniform in the intermediate radius `q` and respects Navier-Stokes scaling: the coefficient has one derivative and therefore scales like frequency.

## 4. Quantitative propagation form

Equivalently, whenever both selected handoffs are angularly nondegenerate,

\[
\sin\theta_1,\sin\theta_2\ge\eta>0,
\]

we have

\[
\boxed{
|\sin\delta|
\le
\frac{\sqrt2\,|C_{\rm bridge}|}
{(r-k)\eta^2}.
}
\]

Hence a connected same-spin backbone has only two ways to avoid a strong cross-generation bridge coefficient:

1. the preferred planes propagate with small projective turning angle; or
2. one of the selected handoffs itself becomes angularly degenerate.

The second branch is already a Selection depletion branch. The first is the beginning of global planarization.

## 5. Local critical corollary

Suppose on a local cascade block

\[
k,q,r\asymp N,
\qquad
r-k\ge\gamma N,
\]

and

\[
\sin\theta_1,\sin\theta_2\ge\eta,
\qquad
|\sin\delta|\ge\tau.
\]

Then

\[
\boxed{
|C_{\rm bridge}|
\ge
\frac{\gamma\eta^2\tau}{\sqrt2}N.
}
\]

Thus a definite plane turn across two nondegenerate local critical handoffs creates an order-`N` cross-generation coupling. It is not a perturbative remainder.

## 6. What this does and does not prove

This lemma is at the exact coefficient level. The corresponding pair forcing is

\[
G_{\rm bridge}
=C_{\rm bridge}\,z_s(R)z_s(-K),
\]

so a global lower bound also requires information on the endpoint amplitudes. Moreover, the full forcing at `B^s` may cancel against other convolution pairs.

However, such cancellation is not a new loophole: it falls back into the already proved Leakage / Composition-Defect machinery at the bridge output `B`.

The remaining global task is therefore to combine:

- critical amplitude balance along a selected backbone,
- the bridge coefficient lower bound above,
- full-output composition defect at `B`, and
- the parabolic/phase rigidity already proved for cancellation networks.

The key structural point is exact: **plane turning is not dynamically invisible to the full Navier-Stokes convolution.** It creates a mandatory shortcut interaction between nonadjacent backbone modes.
