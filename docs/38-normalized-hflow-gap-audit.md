# Normalized Geometric Mobility and Galerkin H-Flow Gap Audit

**Claim level:** definition plus numerical audit. Uniform-in-cutoff spectral expansion is an open theorem.

The H-flow has an arbitrary overall artificial time scale. To compare different Galerkin cutoffs, only clock-invariant spectral information should be used.

## 1. Dimensionless geometric normalization

For a spherical cutoff with top radius `N`, normalize signed frequencies by

\[
\widehat h_i=h_i/N.
\]

For each noncollinear helical triad, let `g_tau` be the exact dimensionless helical triple-product geometry. Use

\[
\boxed{w_\tau=|g_\tau|^2.}
\]

Build the dimensionless transfer matrix `A_hat` from the normalized signed frequencies and define

\[
L_N=\widehat A^T W\widehat A.
\]

Multiplying all weights by one positive scalar merely rescales artificial H-time. Therefore the invariant expansion quantity is not `lambda_+` itself but

\[
\boxed{
\eta_N
:=\frac{\lambda_+(L_N)}{\lambda_{\max}(L_N)}.
}
\]

Equivalently, divide `L_N` by `lambda_max`; then its nonzero spectrum lies in `[eta_N,1]`.

## 2. Why this matters

For the clock-normalized H-flow with `lambda_max=1`, the curvature theorem gives

\[
\mathscr R_H'
\le-\frac{2\eta_N}{E^2}\mathscr R_H.
\]

Thus a uniform bound

\[
\boxed{
\inf_N\eta_N>0
}
\]

would give cutoff-uniform canonicalization in artificial H-time.

Combined with the exact no-collapse theorem, this would be the finite-network analogue of a scale-uniform canonical-neighborhood/noncollapsing mechanism.

## 3. Numerical audit

Using the full periodic reality-quotiented helical Galerkin balls, all noncollinear geometric triads, exact helical triple-product magnitudes, and normalized signed frequencies, the current audit gives:

| `R^2` | `eta_N` |
|---:|---:|
| 2 | 0.189851 |
| 3 | 0.125190 |
| 4 | 0.227628 |
| 5 | 0.189036 |
| 6 | 0.257900 |
| 8 | 0.236411 |
| 9 | 0.208851 |

No downward trend is visible at these small cutoffs. This is evidence only, not a uniform theorem.

## 4. Open spectral-expansion theorem

The finite-dimensional algebraic target is now precise:

**Uniform H-Expansion Problem.** Prove or disprove that the normalized full helical Galerkin transfer Laplacians satisfy

\[
\inf_{N\ge N_0}
\frac{\lambda_+(L_N)}{\lambda_{\max}(L_N)}>0.
\]

If false, identify the approximate null modes responsible for collapse. Such modes would themselves be structured near-invariants and therefore potential candidates for a new protected geometry.

Either outcome is informative:

- a positive gap gives uniform H-smoothing;
- a collapsing gap exposes a new asymptotic invariant that must be incorporated into the V-geometry.
