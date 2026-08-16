# Planarity Volume Determinant

The global critical planarity tensor

\[
\mathsf A
=\sum_{k\ne0}m_k\,\widehat k\otimes\widehat k,
\qquad
m_k:=|k||\widehat u(k)|^2,
\]

contains more information than its smallest eigenvalue. Its determinant is an exact weighted sum of squared three-dimensional volumes of Fourier direction triples. This gives a scalar global measure of genuinely three-dimensional spectral composition.

## 1. Cauchy-Binet volume identity

For a finite Galerkin field, form the `3 x N` matrix whose `k`-th column is

\[
w_k:=m_k^{1/2}\widehat k.
\]

Then

\[
\mathsf A=WW^T.
\]

Cauchy-Binet gives

\[
\boxed{
\det\mathsf A
=\sum_{i<j<\ell}
 m_i m_j m_\ell
\left[
\widehat k_i\cdot
(\widehat k_j\times\widehat k_\ell)
\right]^2.
}
\]

Every summand is nonnegative. Hence

\[
\det\mathsf A=0
\]

if and only if all active Fourier directions span a space of dimension at most two, equivalently the Fourier support lies in one plane through the origin.

Thus the determinant gives a global algebraic certificate of nonplanarity.

## 2. Dimensionless three-dimensionality fraction

Let the eigenvalues of `A` be

\[
\lambda_1\ge\lambda_2\ge\lambda_3\ge0,
\qquad
\lambda_1+\lambda_2+\lambda_3=K.
\]

By arithmetic-geometric mean,

\[
\det\mathsf A
\le\left(\frac K3\right)^3.
\]

Define

\[
\boxed{
\mathfrak V
:=\frac{27\det\mathsf A}{K^3}
\in[0,1]
}
\]

when `K>0`.

- `V=0` exactly on globally planar/linear Fourier support;
- `V=1` exactly when `A=(K/3)I`, i.e. the critical directional second moment is isotropic.

This scalar is invariant under rotations and under Navier-Stokes scaling.

## 3. Triple-volume lower bound for the global planarity defect

Take any three active modes with critical masses `m_1,m_2,m_3` and unit directions `v_1,v_2,v_3`. Let

\[
\tau:=|v_1\cdot(v_2\times v_3)|
\]

and

\[
M_3:=m_1+m_2+m_3.
\]

Their tensor contribution is

\[
A_3=\sum_{j=1}^3m_jv_j\otimes v_j.
\]

Cauchy-Binet gives

\[
\det A_3=m_1m_2m_3\tau^2.
\]

If `mu_1>=mu_2>=mu_3` are the eigenvalues of `A_3`, then

\[
\mu_1\mu_2\le\frac{M_3^2}{4}.
\]

Therefore

\[
\boxed{
\lambda_{\min}(A_3)
\ge
\frac{4m_1m_2m_3}{M_3^2}\tau^2.
}
\]

Since adding positive-semidefinite mode contributions can only increase the smallest eigenvalue,

\[
\boxed{
\mathcal P(u)
\ge
\frac{4m_1m_2m_3}{M_3^2}\tau^2
}
\]

for every chosen triple of active modes.

For consecutive backbone modes `K,Q,R`,

\[
\tau
=\sin\theta_{KQ}\sin\theta_{QR}|\sin\delta|,
\]

so a definite plane turn between nondegenerate handoffs creates a quantitative **global** planarity defect, not merely a local bridge coefficient.

## 4. Additivity over disjoint blocks

If the Fourier modes are partitioned into disjoint blocks with positive-semidefinite tensors `A^(b)`, then

\[
\mathsf A=\sum_bA^{(b)}.
\]

For every unit vector `n`,

\[
n^T\mathsf A n
=\sum_bn^TA^{(b)}n
\ge\sum_b\lambda_{\min}(A^{(b)}).
\]

Hence

\[
\boxed{
\mathcal P(u)
\ge
\sum_b\lambda_{\min}(A^{(b)}).
}
\]

Thus disjoint genuinely three-dimensional mode blocks accumulate in the global planarity defect. This is a scalar alternative to summing projective graph-turning angles.

## 5. Determinant evolution

Write the matrix evolution from `16-global-planarity-defect.md` as

\[
\mathsf A'
=2\mathsf N-2\nu\mathsf H,
\]

where

\[
\mathsf N_{ij}
:=\langle D_iD_j\Lambda^{-1}u,F\rangle,
\]

and

\[
\mathsf H_{ij}
:=\left\langle
D_i\Lambda^{1/2}u,
D_j\Lambda^{1/2}u
\right\rangle.
\]

Since determinant is a polynomial in the matrix entries,

\[
\boxed{
(\det\mathsf A)'
=2\,\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf N)
-2\nu\,\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H).
}
\]

For positive-semidefinite `A`, its cofactor matrix is also positive semidefinite.

## 6. Quantitative viscous damping of three-dimensional volume

Work in an eigenbasis of `A`. For each eigenvector `e_i`, the directional Cauchy-Schwarz estimate from `16-global-planarity-defect.md` gives

\[
H_{ii}\ge\frac{\lambda_i^2}{E}.
\]

In this basis

\[
\operatorname{cof}(\mathsf A)
=\operatorname{diag}
(\lambda_2\lambda_3,
 \lambda_1\lambda_3,
 \lambda_1\lambda_2).
\]

Therefore

\[
\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H)
\ge
\frac1E
\left(
\lambda_2\lambda_3\lambda_1^2
+\lambda_1\lambda_3\lambda_2^2
+\lambda_1\lambda_2\lambda_3^2
\right).
\]

Factoring the determinant yields

\[
\boxed{
\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H)
\ge
\frac K E\det\mathsf A.
}
\]

Hence

\[
\boxed{
(\det\mathsf A)'
\le
2\Xi_{\rm vol}
-2\nu\frac K E\det\mathsf A,
}
\]

where

\[
\Xi_{\rm vol}
:=\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf N).
\]

Viscosity therefore damps genuine three-dimensional spectral volume at a rate at least `2 nu K/E`.

## 7. Cofactor-weighted commutator collapse

Let

\[
C:=\operatorname{cof}(\mathsf A)\succeq0.
\]

Define the self-adjoint multiplier

\[
A_C:=D^TCD\,\Lambda^{-1}.
\]

Then

\[
\Xi_{\rm vol}=\langle A_Cu,F\rangle.
\]

Choose a matrix square root `C=S^TS`, and let `s_alpha` be the row vectors of `S`. Define

\[
B_{s_\alpha}:=(s_\alpha\cdot D)\Lambda^{-1/2}.
\]

Then

\[
A_C=\sum_\alpha B_{s_\alpha}^2.
\]

Using the same transport cancellation as in the scalar planarity defect,

\[
\boxed{
\Xi_{\rm vol}
=-\sum_\alpha
\left\langle
B_{s_\alpha}u,
[B_{s_\alpha},u\cdot\nabla]u
\right\rangle.
}
\]

Thus Euler can regenerate three-dimensional Fourier volume only through a cofactor-weighted family of directional fractional transport commutators.

## 8. Finite lifetime volume action

The arithmetic-geometric mean bound

\[
(\det\mathsf A)^{1/3}\le\frac K3
\]

implies

\[
(\det\mathsf A)^{2/3}\le\frac{K^2}{9}.
\]

Combining with the energy-squared budget yields

\[
\boxed{
\int_0^T(\det\mathsf A(t))^{2/3}\,dt
\le\frac{E(0)^2}{36\nu}.
}
\]

Equivalently, the dimensionless volume fraction satisfies

\[
\int_0^T K(t)^2\,\mathfrak V(t)^{2/3}\,dt
\le\frac{E(0)^2}{4\nu}.
\]

So nonplanar critical volume has a finite global action even before using the new determinant evolution. A singular scenario must concentrate this action into increasingly short events or drive the normalized volume fraction toward zero.

## 9. New global rigidity target

The local Composition lemmas say that avoiding shadow/bridge/cross leakage drives active interactions toward shared planes. The determinant identity says the complementary statement globally:

\[
\boxed{
\text{persistent non-coplanar critical mass}
\Longrightarrow
\det\mathsf A>0.
}
\]

The next analytic target can therefore be stated without any graph language:

**Volume-Production Control Problem.** Control the positive Euler source `Xi_vol` strongly enough, using exact helical/composition structure, to prevent `det A` from sustaining a singular critical escape against the damping

\[
2\nu(K/E)\det\mathsf A.
\]

A successful estimate here would turn the local plane-rigidity program into a single global differential mechanism.

## 10. Exact volume-weighted viscous spectrum

The cofactor viscous term has an exact Cauchy-Binet expansion that is substantially sharper than the lower bound in Section 6.

Recall

\[
m_k=|k||\widehat u(k)|^2,
\qquad
v_k=\widehat k,
\]

so

\[
\mathsf A=\sum_km_kv_k\otimes v_k,
\qquad
\mathsf H=\sum_k|k|^2m_kv_k\otimes v_k.
\]

For a finite Galerkin field, differentiate the Cauchy-Binet polynomial

\[
\det\mathsf A
=\sum_{i<j<\ell}
m_im_jm_\ell\tau_{ij\ell}^2,
\qquad
\tau_{ij\ell}:=
|v_i\cdot(v_j\times v_\ell)|,
\]

under the artificial weight variation

\[
m_k(\varepsilon)
=(1+\varepsilon|k|^2)m_k.
\]

On the matrix side,

\[
\mathsf A(\varepsilon)
=\mathsf A+\varepsilon\mathsf H,
\]

so Jacobi's polynomial derivative gives

\[
\left.\frac d{d\varepsilon}\det\mathsf A(\varepsilon)
\right|_{\varepsilon=0}
=\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H).
\]

On the Cauchy-Binet side, differentiating each triple product yields

\[
\boxed{
\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H)
=
\sum_{i<j<\ell}
\left(|k_i|^2+|k_j|^2+|k_\ell|^2\right)
m_im_jm_\ell\tau_{ij\ell}^2.
}
\]

Thus viscosity sees every genuinely three-dimensional Fourier triple separately and damps its volume contribution at the sum of the three modal heat rates.

Whenever `det A>0`, define the volume-weighted parabolic frequency

\[
\boxed{
\Omega_{\rm vol}^2
:=
\frac{
\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H)
}{\det\mathsf A}.
}
\]

Then `Omega_vol^2` is exactly the weighted average

\[
\boxed{
\Omega_{\rm vol}^2
=
\frac{
\sum_{i<j<\ell}
(|k_i|^2+|k_j|^2+|k_\ell|^2)
 m_im_jm_\ell\tau_{ij\ell}^2
}{
\sum_{i<j<\ell}
 m_im_jm_\ell\tau_{ij\ell}^2
}.
}
\]

The determinant evolution becomes the exact scalar balance

\[
\boxed{
(\det\mathsf A)'
=2\Xi_{\rm vol}
-2\nu\Omega_{\rm vol}^2\det\mathsf A.
}
\]

This is the global analogue of the pair-heat observability mechanism: nonplanarity carried by high-frequency triples is automatically assigned a high parabolic damping rate.

## 11. High-frequency nonplanarity cannot hide in the low-rate kernel

Let `D_{>=N}` denote the portion of the Cauchy-Binet determinant sum over triples containing at least one mode with `|k|>=N`:

\[
\mathcal D_{\ge N}
:=
\sum_{\substack{i<j<\ell\\
\max(|k_i|,|k_j|,|k_\ell|)\ge N}}
 m_im_jm_\ell\tau_{ij\ell}^2.
\]

Then the exact formula gives

\[
\boxed{
\operatorname{tr}(\operatorname{cof}(\mathsf A)\mathsf H)
\ge
N^2\mathcal D_{\ge N}.
}
\]

Hence the viscous contribution to determinant evolution contains

\[
\boxed{
-2\nu N^2\mathcal D_{\ge N}.
}
\]

A singular cascade therefore has only two ways to avoid a parabolic-rate penalty in the global volume variable:

1. make the high-frequency contribution `D_{>=N}` small, i.e. high-frequency critical mass becomes increasingly coplanar with the rest of the active spectrum; or
2. regenerate high-frequency three-dimensional volume through the Euler source at an `O(nu N^2)` rate.

This is a sharp global `Dissipation / Composition` dichotomy. The remaining source-control problem is to show that branch 2 cannot persist through an infinite critical escape chain without triggering the already established shadow/composition mechanisms.
