# Periodic Helical Galerkin Rank Audit for the H-Flow

**Claim level:** numerical structural audit, not a theorem for all cutoffs.

The H-flow equilibrium is globally Kraichnan-affine only when the full active transfer matrix satisfies

\[
\ker A=\operatorname{span}\{\mathbf1,h\}.
\]

A previous version of this research program learned the hard way that ordinary one-mode connectivity of a triad hypergraph is not enough to prove such a statement. This note therefore tests the rank directly on genuine periodic helical Galerkin networks.

## 1. Periodic mode set

Take nonzero integer wavevectors

\[
k\in\mathbb Z^3,
\qquad |k|^2\le R^2,
\]

with the reality identification `k ~ -k`. Each representative carries two helical labels `sigma=+/-` and signed frequency

\[
h=\sigma |k|.
\]

A geometric triad is retained when

\[
k+p+q=0
\]

and the three vectors are noncollinear.

For every one of the eight helicity assignments, the exact helical triple product is evaluated. Only channels with nonzero geometric coupling are retained.

Each retained channel contributes the exact transfer row

\[
\lambda=(h_p-h_q,h_q-h_k,h_k-h_p).
\]

## 2. Audit result

For the tested Galerkin balls:

| `R^2` | helical modes | retained helical triad rows | `dim ker A` |
|---:|---:|---:|---:|
| 2 | 18 | 144 | 2 |
| 3 | 26 | 336 | 2 |
| 4 | 32 | 528 | 2 |
| 5 | 56 | 1680 | 2 |
| 6 | 80 | 3840 | 2 |

No noncollinear helical assignment in these balls was lost through a zero geometric triple product.

Thus every tested full Galerkin network has exactly the two expected diagonal invariant directions:

\[
\boxed{
\ker A=\operatorname{span}\{\mathbf1,h\}
}
\]

at the level of numerical linear algebra.

## 3. Interpretation

This supports three structural claims of the H-flow program:

1. sparse subnetworks can have extra diagonal invariants;
2. full Fourier convolution appears to destroy those extra invariant directions;
3. once full rank rigidity is reached, the zero-curvature H-equilibrium has the Kraichnan form
   \[
   C_i^{-1}=\alpha+\beta h_i.
   \]

## 4. What remains to prove

A uniform theorem for all periodic Galerkin cutoffs is still open in this repository.

The correct statement cannot rely on naive hypergraph connectivity. A proof must exploit the special arithmetic and helicity structure of the full Fourier convolution network, or establish a constructive spanning family of transfer rows whose orthogonal complement is exactly `span{1,h}`.

This is now a sharply defined finite-dimensional algebra problem, independent of Navier-Stokes regularity itself.
