# Defect-Growth Ledger and Regeneration Excess

The No-Zeno problem should not be attacked by assigning an ad hoc time width to every burst. The exact critical balance and the exact optimal-defect balance share enough dissipation to produce a global ledger: critical growth can be paid for by the linear damping already present in the protected defect. The only remaining source of net ledger growth is the positive Euler regeneration of that defect.

Throughout, let

\[
K=\langle u,\Lambda u\rangle,
\qquad
M_3=\|\Lambda^{3/2}u\|_2^2,
\]

and let

\[
r=(\Lambda-a-b\operatorname{curl})u,
\qquad
\mathcal Y=\|r\|_2^2,
\qquad
\mathcal X=E\mathcal Y.
\]

The constant `C_*` is the same Sobolev constant appearing in the optimal protected escape barrier

\[
|\kappa|
\le C_*\mathcal Y^{1/2}Z^{1/2}M_3^{1/2}.
\]

## 1. A growth bound already paid by defect damping

The exact critical balance is

\[
K'=2\kappa-2\nu M_3.
\]

Hence

\[
K'
\le
2C_*\sqrt{\mathcal Y Z}\,M_3^{1/2}
-2\nu M_3.
\]

Maximizing the right-hand side over `M_3^{1/2}` gives

\[
\boxed{
K'
\le
\frac{C_*^2}{2\nu}\,\mathcal Y Z
=
\frac{C_*^2}{2\nu}\frac ZE\mathcal X.
}
\]

This estimate is scale critical. It says that the same quantity `(Z/E) X` which occurs with a favorable sign in the optimal-defect equation already dominates every possible positive derivative of `K`.

## 2. The combined ledger

The exact optimal-defect balance from `21-optimal-protected-escape-defect.md` is

\[
\mathcal X'
=
2E\Gamma_{\rm esc}
-2\nu E\|\Lambda r\|_2^2
-2\nu\frac ZE\mathcal X.
\]

Define

\[
\boxed{
\beta:=\frac{2\nu^2}{C_*^2}
}
\]

and

\[
\boxed{
\mathscr L:=\mathcal X+\beta K.
}
\]

Multiplying the preceding bound for `K'` by `beta` yields

\[
\beta K'\le \nu\frac ZE\mathcal X.
\]

Therefore

\[
\boxed{
\mathscr L'
\le
2E\Gamma_{\rm esc}
-2\nu E\|\Lambda r\|_2^2
-\nu\frac ZE\mathcal X.
}
\]

This is the **defect-growth ledger**.

The important point is structural: no separate budget has been invented. Half of the linear defect damping pays for the worst possible critical growth, while the other half and the full derivative damping remain favorable.

## 3. Integrated source criterion

Since only the positive part of `Gamma_esc` can increase the ledger, for `0<=s<t<T` we have

\[
\boxed{
\begin{aligned}
\mathscr L(t)
&+2\nu\int_s^t E\|\Lambda r\|_2^2\,d\tau
+\nu\int_s^t\frac ZE\mathcal X\,d\tau
\\
&\le
\mathscr L(s)
+2\int_s^t E(\Gamma_{\rm esc})_+\,d\tau.
\end{aligned}
}
\]

Consequently, if `K` is unbounded along a finite smooth interval `[0,T)`, then `L>=beta K` is unbounded and necessarily

\[
\boxed{
\int_0^T E(t)(\Gamma_{\rm esc}(t))_+\,dt
=\infty.
}
\]

Thus a finite-time singular escape cannot be produced merely by making the protected-reset intervals shorter. It must accumulate **infinite positive optimal-defect regeneration source**.

This converts the No-Zeno question into a source-rigidity question.

## 4. Regeneration amplification must become unbounded

The optimal defect itself has finite lifetime action,

\[
\int_0^T\mathcal X(t)\,dt
\le \frac{E(0)^2}{4\nu}.
\]

Since

\[
E(\Gamma_{\rm esc})_+
=\mathcal X\,
\frac{(\Gamma_{\rm esc})_+}{\mathcal Y}
\]

whenever `Y>0`, the preceding divergence implies the following necessary condition for escape:

\[
\boxed{
\limsup_{t\uparrow T,\,\mathcal Y(t)>0}
\frac{(\Gamma_{\rm esc}(t))_+}{\mathcal Y(t)}
=\infty.
}
\]

Indeed, any eventual bound

\[
(\Gamma_{\rm esc})_+\le C\mathcal Y
\]

would give

\[
\int E(\Gamma_{\rm esc})_+dt
\le C\int\mathcal Xdt<\infty,
\]

contradicting critical escape.

So a hypothetical singular chain must produce arbitrarily large **relative regeneration rates** of the optimally unprotected component.

## 5. A second effective-viscosity threshold

When `Y>0`, define the defect-regeneration coefficient

\[
\boxed{
\nu_R
:=
\frac E Z\frac{\Gamma_{\rm esc}}{\mathcal Y}.
}
\]

This quantity is invariant under Navier-Stokes scaling and has the same physical units as viscosity. Since

\[
E\Gamma_{\rm esc}
=\frac ZE\mathcal X\,\nu_R,
\]

the ledger becomes

\[
\boxed{
\mathscr L'
\le
\frac ZE\mathcal X(2\nu_R-\nu)
-2\nu E\|\Lambda r\|_2^2.
}
\]

Thus there are now two distinct nonlinear thresholds:

1. `nu_E>nu` is required for instantaneous growth of the critical quantity `K`;
2. `nu_R>nu/2` is required for the combined critical/defect ledger to regenerate against the damping which already pays for `K` growth.

In particular, if eventually

\[
\nu_R\le \frac\nu2,
\]

then `L` is nonincreasing and critical escape is impossible.

## 6. A Gronwall-type conditional regularity criterion

Dropping the favorable derivative-damping term and using `X<=L` gives

\[
\mathscr L'
\le
2\frac ZE
\left(\nu_R-\frac\nu2\right)_+
\mathscr L.
\]

Therefore

\[
\boxed{
\int_0^T
\frac ZE
\left(\nu_R-\frac\nu2\right)_+dt
<\infty
\quad\Longrightarrow\quad
\sup_{t<T}K(t)<\infty.
}
\]

Equivalently, any finite-time critical escape must satisfy

\[
\boxed{
\int_0^T
\frac ZE
\left(\nu_R-\frac\nu2\right)_+dt
=\infty.
}
\]

This is an exact reduction, not yet a proof of regularity: the missing task is to control this regeneration-excess action using the helical/composition structure of the true convolution.

## 7. Why this is the No-Zeno variable

The naive crossing estimate for `sqrt(Y)` involves `||TF||_2`, a supercritical forcing norm. The ledger avoids that dead end. It does not ask for a universal lower bound on the duration of each reset. Instead it proves that every successful sequence of resets must accumulate an infinite amount of one precisely identified source:

\[
\boxed{E(\Gamma_{\rm esc})_+.}
\]

The triad factorization in `22-optimal-defect-triad-source.md` then becomes directly relevant: this source is built from the same heterochiral currents responsible for critical transfer, while homochiral recharge carries a full radial Vandermonde.

The next problem is therefore not burst timing but **source rigidity**.
