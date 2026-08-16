# Complex Spin-Shadow Law and Double-Angle Plane Rigidity

The original Spin-Shadow Lemma used only coefficient magnitudes. The exact complex ratio contains additional geometric information: a spin-two phase twist determined by the azimuth of the parent-pair plane around the common output.

## 1. Output frame and pair-plane azimuth

Fix a nonzero output wavevector `r` and choose an oriented orthonormal frame

\[
(e_1,e_2,\widehat r),
\qquad
e_2=\widehat r\times e_1.
\]

Use the output helical vectors

\[
h_t(r)=\frac{e_1+i t e_2}{\sqrt2}.
\]

Let same-spin parents `a^s,b^s` satisfy

\[
a+b=r.
\]

Write

\[
x=\frac{a-b}{2},
\qquad
x_\perp=x-(x\cdot\widehat r)\widehat r.
\]

For a noncollinear pair, define the unoriented pair-plane azimuth `phi` by

\[
\frac{x_\perp}{|x_\perp|}
=\cos\phi\,e_1+\sin\phi\,e_2.
\]

Changing `phi` by `pi` only swaps the two inputs, so the physical pair plane is naturally defined modulo `pi`.

## 2. Exact complex ratio

Let

\[
\alpha=|a|,\qquad
\beta=|b|,\qquad
\rho=|r|,\qquad
S=\alpha+\beta.
\]

For the two output helicities, denote by

\[
C_{\rm sh}:=C_{r;a,b}^{s,s,s},
\qquad
C_{\rm cat}:=C_{r;a,b}^{-s,s,s}
\]

the same-spin shadow and opposite-spin catalyst coefficients.

Then, for every nondegenerate same-spin pair,

\[
\boxed{
\frac{C_{\rm sh}}{C_{\rm cat}}
=
\frac{S+\rho}{S-\rho}
\,e^{-2is\phi}.
}
\]

The input-helicity gauge phases cancel in this ratio. A rotation of the chosen output frame changes every ratio at this same output by one common phase, so **relative ratio phases between two parent pairs are gauge invariant**.

### Proof

Choose a triad-adapted gauge with unit normal

\[
n=\frac{a\times b}{|a\times b|}
\]

and transverse basis `e_1^triad=n x khat`, `e_2^triad=n` for every wavevector in the pair plane. In this gauge a direct coplanar helical calculation gives a positive real ratio

\[
\frac{C_{\rm sh}^{\rm triad}}
{C_{\rm cat}^{\rm triad}}
=rac{S+\rho}{S-\rho}.
\]

At the output `r`, the triad-adapted transverse frame is obtained from the fixed output frame by a rotation through `phi`. Therefore

\[
h_t^{\rm triad}(r)
=e^{-it\phi}h_t(r).
\]

Projection onto the fixed output basis multiplies the `t` coefficient by `e^{-it phi}`. Taking the quotient of the `t=s` and `t=-s` coefficients yields the factor `e^{-2is phi}`.

## 3. Relative phase law for two pairs

For two same-spin pairs `e,f` feeding the same output,

\[
\boxed{
\arg\left(
\frac{(C_{\rm sh}/C_{\rm cat})_e}
{(C_{\rm sh}/C_{\rm cat})_f}
\right)
=-2s(\phi_e-\phi_f)
\pmod{2\pi}.
}
\]

This is independent of all input helical gauge choices and of the common output-frame gauge.

Thus geometry creates a **double-angle phase twist** between catalyst and shadow channels.

## 4. Perfect-coherence planarity corollary

Let `c_e` denote the complex catalyst pair contribution and `g_e` its shadow contribution. Then

\[
g_e=R_e c_e,
\qquad
R_e=\rho_e e^{-2is\phi_e},
\qquad
\rho_e=\frac{S_e+|r|}{S_e-|r|}>1.
\]

Suppose two nonzero pairs `e,f` satisfy simultaneously

\[
\frac{c_e}{c_f}>0
\]

and

\[
\frac{g_e}{g_f}>0.
\]

That is, their catalyst contributions are perfectly phase aligned and their shadow contributions are also perfectly phase aligned. Then

\[
e^{-2is(\phi_e-\phi_f)}=1,
\]

hence

\[
\boxed{
\phi_e=\phi_f\pmod\pi.
}
\]

Therefore the two parent pairs lie in the same unoriented plane containing the output `r`.

So exact simultaneous catalyst coherence and shadow coherence force local planarity.

## 5. Exact angular defect under coherent catalyst feeding

Assume a family of catalyst contributions at the same output has one common phase,

\[
c_e=a_e e^{i\psi},
\qquad a_e>0.
\]

Then

\[
g_e=\rho_e a_e e^{i\psi}e^{-2is\phi_e}.
\]

The composition defect of the selected shadow family is exactly

\[
\boxed{
\mathfrak D_{\rm sh}^{\rm sel}
=4\sum_{e<f}
\rho_e\rho_f a_ea_f
\sin^2(\phi_e-\phi_f).
}
\]

Thus perfectly coherent catalyst feeding can avoid a shadow composition defect only when the contributing pair planes are all aligned modulo `pi`.

## 6. Quantitative phase-plane tradeoff

For general catalyst phases write

\[
c_e=a_e e^{i(\psi+\delta_e)},
\qquad
w_e:=|g_e|=\rho_e a_e.
\]

Define the shadow-weighted catalyst phase dispersion

\[
\mathfrak D_{\rm cat}^{(w)}
:=2\sum_{e<f}w_ew_f
\bigl(1-\cos(\delta_e-\delta_f)\bigr),
\]

and the plane-angle dispersion

\[
\mathfrak D_{\rm plane}^{(w)}
:=2\sum_{e<f}w_ew_f
\bigl(1-\cos(2(\phi_e-\phi_f))\bigr).
\]

Using

\[
1-\cos(\alpha-\beta)
\ge
\frac12(1-\cos\beta)-(1-\cos\alpha),
\]

pairwise with

\[
\alpha=\delta_e-\delta_f,
\qquad
\beta=2s(\phi_e-\phi_f),
\]

gives the exact quantitative lower bound

\[
\boxed{
\mathfrak D_{\rm sh}^{\rm sel}
\ge
\frac12\mathfrak D_{\rm plane}^{(w)}
-
\mathfrak D_{\rm cat}^{(w)}.
}
\]

Hence the only way to keep shadow composition small is to pay in at least one of two currencies:

1. catalyst phase dispersion, which reduces coherent positive critical transfer; or
2. concentration of the pair-plane azimuths into a nearly planar family.

## 7. New Composition reduction

The dense resonant branch is therefore narrower than "many phase constraints". For same-spin handoffs sharing an output,

\[
\boxed{
\text{coherent catalyst flux}
+\text{small shadow defect}
\Longrightarrow
\text{local plane concentration}.
}
\]

This suggests a new exceptional branch: a cascade may try to escape composition cost by becoming progressively planar in Fourier geometry. A globally fixed Fourier plane corresponds to a two-dimensional/three-component reduction of Navier-Stokes and is regular; the unresolved issue is to prove that a connected critical cascade cannot keep changing its local plane from scale to scale without regenerating a quantitative composition defect.

That propagation statement is the next target, not yet a theorem.

## 8. Coordinate-free projective plane order

For each noncollinear parent pair at the common output `r`, let

\[
n_e:=\frac{a_e\times b_e}{|a_e\times b_e|}.
\]

The plane is unoriented, so `n_e` and `-n_e` represent the same object. For pairs sharing `r`, every `n_e` lies in `r^perp`, and

\[
\sin^2(\phi_e-\phi_f)
=1-(n_e\cdot n_f)^2.
\]

Using the shadow weights `w_e`, put

\[
W:=\sum_e w_e,
\qquad
\mathsf Q_r
:=\frac1W\sum_e w_e\,n_e\otimes n_e.
\]

Then `Q_r` is positive semidefinite, has trace one, and is insensitive to `n_e -> -n_e`. A direct expansion gives

\[
\boxed{
\mathfrak D_{\rm plane}^{(w)}
=2W^2\bigl(1-\operatorname{tr}(\mathsf Q_r^2)\bigr).
}
\]

Since all normals lie in the two-dimensional plane `r^perp`, let the nonzero eigenvalues of `Q_r` be `lambda_1 >= lambda_2 >= 0`, with `lambda_1+lambda_2=1`. Then

\[
\boxed{
\mathfrak D_{\rm plane}^{(w)}
=4W^2\lambda_1\lambda_2.
}
\]

Thus small plane dispersion quantitatively forces `lambda_2` small and the projective normal distribution close to rank one. This is a coordinate-free local planarity order parameter generated directly by the complex Spin-Shadow law.
