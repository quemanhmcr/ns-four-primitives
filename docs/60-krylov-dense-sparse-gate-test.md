# Krylov Dense/Sparse Gate Test

**Claim level:** numerical audit of the first two exact no-output-cutoff Krylov hoppings. It is designed to compare the dense depth-two plateau with the sparse near-planar branch.

## 1. Large shell-separation data

Using protected shells `(1,n^2)` and the exact frozen connection with no Fourier output cutoff, the actual protected state was mapped into the viscously whitened bath and the first two chiral Lanczos hoppings were computed.

### Dense random protected background

| shell ratio `n` | `b_1` | `b_2` | `b_2/b_1` |
|---:|---:|---:|---:|
| 10 | 1.571 | 4.379 | 2.79 |
| 20 | 2.545 | 9.917 | 3.90 |
| 40 | 4.712 | 20.854 | 4.43 |
| 80 | 9.195 | 42.212 | 4.59 |

The independently audited depth-two protected Gramian gap stays approximately

\[
0.110,\ 0.113,\ 0.117,\ 0.119.
\]

### Sparse genuinely three-dimensional background

| shell ratio `n` | `b_1` | `b_2` | `b_2/b_1` | planarity defect |
|---:|---:|---:|---:|---:|
| 10 | 0.3010 | 0.1397 | 0.464 | 0.0909 |
| 20 | 0.3037 | 0.1343 | 0.442 | 0.0476 |
| 40 | 0.3049 | 0.1333 | 0.437 | 0.0244 |
| 80 | 0.3056 | 0.1334 | 0.437 | 0.0123 |

Its depth-two gap is smaller,

\[
0.0456,\ 0.0382,\ 0.0349,\ 0.0338,
\]

while its global critical planarity defect tends toward zero.

## 2. Interpretation

The dense and sparse branches that looked complicated in Fourier graph language are sharply separated in the first two Krylov hoppings:

\[
\boxed{
\text{dense: }b_2\gg b_1,
\qquad
\text{sparse near-planar: }b_1>b_2.
}
\]

This is only an empirical classifier. It is not yet a theorem and no SSH/topological label is asserted.

The useful fact is that the obstruction has been reduced to a scalar recursion profile. A future theorem can ask whether a protected state with small FGR response and non-small three-dimensionality can sustain a hopping profile of the sparse type indefinitely.

## 3. Proposed exact dichotomy target

A possible scale-normalized theorem is

\[
\boxed{
\text{either }b_2\ge c_1 b_1
\quad\text{or}\quad
\mathscr F_{\rm comp}+\mathscr F_{\rm plane}
\ge c_2\,\mathcal M_{\rm twin}.
}
\]

The first branch is a genuine second-layer bath opening and should feed a finite-depth hypocoercive/FGR lower bound. The second branch sends the state to the already developed deterministic sparse/planarity rigidity machinery.

The numerical data above suggest that this formulation is better aligned with the observed dense/sparse split than a direct uniform bound on the first curvature coefficient.

## 4. What would falsify this direction

The Krylov representation would lose its value as a closing machine if one can construct normalized, strongly three-dimensional protected packets with

- small Composition and planarity defects;
- nonzero direct bath coupling;
- arbitrarily weak FGR response;
- and an arbitrarily long Krylov hopping profile that avoids every finite-depth opening without approaching a classified safe stratum.

Such a construction would expose a genuinely new coherent invariant rather than a failure of the current estimates.
