# Adversarial Null-Hunting Flow

**Claim level:** computational discovery architecture. The exact protected-connection identities are proved elsewhere; the minimization results in this note are numerical stress tests, not theorems.

The protected-curvature program should not be tested only on random states. A useful falsification engine is to make the state itself adversarial: minimize the smallest positive protected-curvature eigenvalue while constraining the state away from already known safe strata.

## 1. Frozen protected geometry

At a protected two-shell state let

\[
T=\Lambda-a-b\operatorname{curl},\qquad P=\mathbf 1_{\ker T},
\]

and freeze the Euler connection

\[
\mathcal A_\omega v=P_{\rm Leray}(v\times\omega).
\]

Normalize by the top protected shell `N` and define

\[
B_j:=\frac{T}{N}\left(\frac{\mathcal A_\omega}{N}\right)^jP,
\qquad
G_m:=\sum_{j=1}^m B_j^*B_j.
\]

The unavoidable null direction is `omega`, because

\[
\mathcal A_\omega\omega=0.
\]

The adversarial objective is the normalized smallest positive eigenvalue

\[
\eta_m
:=\frac{\lambda_{\min,+}(G_m)}{\lambda_{\max}(G_m)}.
\]

## 2. Null-hunting flow

Conceptually one may write

\[
\partial_\tau z
=-\Pi_{\mathcal C}\nabla_z\log\eta_m,
\]

where `C` denotes chosen normalization and safe-set exclusion constraints. In practice the first experiments used derivative-free minimization because singular values become nonsmooth at rank changes.

The purpose is not to produce a turbulence model. It is to ask:

> Where does the protected connection lose observability when the state is allowed to choose its own worst geometry?

## 3. Stratum peeling

The optimizer repeatedly moved toward already recognizable structures.

1. Without spin-balance constraints it drove one helicity sector toward the pure-spin boundary.
2. After spin balance was fixed it preferred sparse nearly collinear configurations.
3. After angular separation was imposed it preferred sparse low-dimensional support.
4. After participation and nonplanarity constraints were imposed, the minimum first-curvature gap on the audited `(1,4)` packet stayed positive, around `8.8e-2` in the exploratory complexified search.

This does not prove a positive gap. It identifies the boundary strata that an attempted proof must separate rather than hide inside one coercivity estimate.

## 4. The important falsification

A tempting conjecture was that one sector-normalized directional tensor might control the full depth-two gap on every state. Sparse reality-constrained counterexamples in

`scripts/verify_qdir_sparse_counterexamples.py`

show that this is false. A state can have a genuinely three-dimensional directional span while remaining weakly observable because its active convolution graph is too sparse/coherent.

Thus the machine rejects the single-scalar closure

\[
G_2\gtrsim \lambda_{\min}(Q_{\rm dir})I
\]

without an additional density/coherence hypothesis.

## 5. What survived the machine

The robust architecture is not one global coercive estimate. It is a branch decomposition:

\[
\boxed{
\text{dense protected packet}
\Rightarrow
\text{finite-depth observability},
}
\]

while

\[
\boxed{
\text{sparse/coherent protected packet}
\Rightarrow
\text{Composition branch}.
}
\]

Safe zero-cost strata remain separate exact endpoints.

This is the role of the null-hunting flow: every time a proposed global scalar is too optimistic, the optimizer should expose the missing geometric branch before that scalar is promoted into a proof lemma.
