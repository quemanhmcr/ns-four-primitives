# Sector-Normalized Direction Geometry

**Claim level:** exact definition plus numerical discovery and falsification results.

The critical-weighted global planarity tensor is useful for global PDE geometry, but it is not the natural local variable for frozen protected-curvature observability when the two protected shell radii are very different. The bracket geometry sees the directional support of each helicity sector before it sees how much critical mass each shell carries.

## 1. Direction tensor

For a nonempty helicity sector define

\[
Q_\sigma
:=
\frac{1}{E_\sigma}
\sum_{k}|z_\sigma(k)|^2\,
\widehat k\otimes\widehat k.
\]

Then put

\[
\boxed{
Q_{\rm dir}:=\frac12(Q_++Q_-).
}
\]

It is positive semidefinite with trace one. Moreover

\[
\boxed{
\lambda_{\min}(Q_{\rm dir})=0
}
\]

if and only if there exists one direction normal to every active Fourier direction in both sectors, i.e. the active support lies in a common plane.

Thus `Q_dir` detects the exact planar support stratum without suppressing a low-frequency sector merely because it contributes little to `K`.

## 2. Near-planar opening experiment

On shells `(1,R^2)`, take a `+` mode on the `x` axis, a `-` mode on the `y` axis, and add a second `-` mode on the `z` axis with relative amplitude `epsilon`.

Then exactly for this family

\[
q_{\rm dir}:=\lambda_{\min}(Q_{\rm dir})
=\frac{\epsilon^2}{2(1+\epsilon^2)}.
\]

At `R=80`, after subtracting the tiny exactly planar depth-two baseline, the audit gives

\[
\eta_2-\eta_2^{\rm planar}
\sim c\,q_{\rm dir}
\]

with log-log slope `0.995455` and measured coefficient range

\[
0.2886\le c\le0.2986.
\]

The number

\[
1-1/\sqrt2=0.292893\ldots
\]

lies strikingly inside this range. No exact identification of the coefficient is claimed.

See `scripts/verify_sector_direction_gap.py`.

## 3. Planar versus 3D branch

For a sparse planar two-direction state the depth-two gap decays numerically like

\[
\eta_2^{\rm planar}\asymp R^{-4}.
\]

The fitted exponent on `R=10,20,40,80` is `4.012152`.

Adding one reality-paired out-of-plane high-shell direction changes the behavior to

\[
\eta_2^{\rm 3D}\approx
0.0456,0.0382,0.0349,0.0338
\]

on the same ratios.

See `scripts/verify_planar_vs_3d_depth2.py`.

## 4. Q_dir is not a global coercivity scalar

The near-planar law is real, but a stronger conjecture

\[
\eta_2\gtrsim q_{\rm dir}
\]

for all protected states is false without a density/coherence assumption.

Reality-constrained sparse three-mode adversaries give

| `R` | `eta_2` | `q_dir` | `eta_2/q_dir` |
|---:|---:|---:|---:|
| 10 | 2.686e-2 | 5.129e-2 | 5.24e-1 |
| 20 | 9.191e-3 | 4.135e-2 | 2.22e-1 |
| 40 | 8.776e-3 | 1.421e-1 | 6.18e-2 |

See `scripts/verify_qdir_sparse_counterexamples.py`.

Therefore `Q_dir` should be treated as the correct **planarity coordinate** inside a branch theorem, not as a universal replacement for Composition.
