# Feshbach Passive-Bath Gate Test

**Claim level:** numerical falsification/audit of the frozen finite-packet mechanism in `46-passive-feshbach-bath.md`. This is not a uniform infinite-dimensional theorem.

## 1. Test operator

For a protected two-shell background, build the exact Galerkin operator

\[
\mathcal A_\omega v=P(v\times\omega)
\]

on a Fourier ball of radius `R`, preserving every convolution output that remains in the ball. The background itself is held fixed while the bath radius increases.

Normalize frequencies by the larger protected radius `N`. Put

\[
A=\mathcal A_\omega/N,
\qquad
D_Q=\Lambda_Q^2/N^2,
\]

and compute

\[
\Sigma_\varepsilon
=B^*(\varepsilon D_Q-A_{QQ})^{-*}
(\varepsilon D_Q)
(\varepsilon D_Q-A_{QQ})^{-1}B.
\]

All eigenvalues below are eigenvalues of this positive matrix on the protected shell space.

## 2. Full-shell cutoff convergence

For protected shells `(1,2)` and an equal-amplitude full-shell background, the positive rank is `11/12`, as required by the exact vorticity dark direction.

At `epsilon=0.1`:

| bath radius `R` | normalized gap | smallest positive eigenvalue | largest eigenvalue |
|---:|---:|---:|---:|
| 4 | 0.32748 | 0.20666 | 0.63106 |
| 5 | 0.37095 | 0.23468 | 0.63264 |
| 6 | 0.37217 | 0.23133 | 0.62158 |

The spectrum stabilizes rapidly once the first few bath generations are present.

At the stronger-coupling value `epsilon=0.01`, convergence is slower because long bath excursions matter, but the positive floor remains visible. This is exactly where a Schur-resolvent formulation is preferable to finite bracket depth.

## 3. Sparse noncollinear pair

Take a reality-symmetric protected background with one `+` pair on radius `1` and one `-` pair on radius `2`, with the two parent directions noncollinear.

At `epsilon=0.1` the smallest positive eigenvalue is already cutoff-stable:

| `R` | rank | normalized gap | smallest positive eigenvalue |
|---:|---:|---:|---:|
| 4 | 11/12 | 0.06261 | 0.05577 |
| 5 | 11/12 | 0.08089 | 0.05649 |
| 6 | 11/12 | 0.08070 | 0.05650 |
| 7 | 11/12 | 0.08058 | 0.05649 |
| 8 | 11/12 | 0.08058 | 0.05649 |

At `epsilon=0.01`, the largest resonance eigenvalue is more cutoff-sensitive, but the smallest positive eigenvalue is approximately stable around `6.7e-3` for `R>=5`.

Thus the physically important coercive floor is substantially more stable than the raw condition number.

## 4. Strong-coupling scaling

For the same noncollinear sparse packet at `R=7`:

| `epsilon` | `lambda_min(Sigma_epsilon)` | `lambda_min/epsilon` |
|---:|---:|---:|
| 0.30 | 0.09094 | 0.3031 |
| 0.10 | 0.05649 | 0.5649 |
| 0.03 | 0.01962 | 0.6540 |
| 0.01 | 0.00674 | 0.6744 |

The observed scaling is consistent with

\[
\lambda_{\min,+}(\Sigma_\varepsilon)
\sim C\varepsilon
\]

rather than a faster collapse.

Because the theta-clock effective self-energy is `Sigma_epsilon/epsilon`, this is precisely the scaling required for an order-one strong-coupling damping mechanism.

This is evidence, not an asymptotic theorem.

## 5. Dark heat-line state

If the sparse `+` and `-` parents are collinear, the positive rank drops from `11` to `8`. This reproduces the extra dark directions already found by the curvature Gramian.

That state belongs to the exact zero-cost protected heat-line stratum classified earlier: cross products vanish and the Euler forcing is zero.

Thus the passive-bath mechanism does not artificially damp the known safe endpoint.

For a noncollinear sparse pair, the rank returns immediately to `11/12`.

## 6. Quadratic opening away from the dark stratum

Start from a collinear protected heat-line state and add one off-line `+` shell mode with amplitude `delta`. Use `epsilon=0.1` and bath radius `R=6`.

At `delta=0`, there are four dark directions. For every tested `delta>0`, only the vorticity dark direction remains.

The smallest newly opened Feshbach eigenvalue obeys

\[
\boxed{
\lambda_{\rm new}(\Sigma_{0.1})
\approx0.2017\,\delta^2
}
\]

for `delta` between `1e-3` and `1e-1`. A log-log fit gives slope

\[
\boxed{1.99845.}
\]

Thus the effective passive damping opens quadratically with distance from the exact dark heat-line stratum, matching the quadratic opening previously seen in the finite-depth curvature Gramian.

## 7. Interpretation

Three independent observations now point to the same geometry:

1. first-curvature Gramian: dark directions are generic only on safe/sparse structures;
2. higher-bracket Gramian: weak nonlocal directions are reopened by finite-depth coupling;
3. Feshbach bath: all repeated excursions resum into a positive self-energy with the same exact dark kernel.

The Feshbach mechanism is stronger physically because its positivity comes from the actual pair

\[
\text{skew Euler connection} + \text{viscous bath},
\]

not from an auxiliary mobility.

## 8. Falsification criteria going forward

This direction should be abandoned or sharply revised if any of the following occurs:

- the coercive floor tends to zero faster than `epsilon` on scale-normalized non-safe packets;
- expanding Fourier baths create new dark directions unrelated to the exact safe/composition strata;
- time-dependent frame pumping contributes at the same order without a compensating Composition defect;
- near-protected soft projections destroy passivity or scale normalization.

The next target is therefore a **Passive-Bath / Dark-State Dichotomy** with constants uniform in physical scale, not more finite-packet numerics.
