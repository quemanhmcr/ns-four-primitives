# Protected Reset Trichotomy

The protected manifold is the only place where the optimal escape defect vanishes exactly. The preceding notes show that leaving this manifold has a positive even-order nonlinear opening jet, while a real cross-spin pair necessarily generates reality-twin leakage. This note combines those facts into a quantitative reset trichotomy.

The conclusion is sharp at zero cost: a nondegenerate protected state can avoid both defect-opening acceleration and hidden composition cost only when the Euler nonlinearity vanishes identically. Such a state then evolves by pure heat decay and is globally regular.

## 1. Protected shell geometry

Let

\[
\Lambda u_+=\alpha u_+,
\qquad
\Lambda u_-=\beta u_-,
\qquad
\alpha,\beta>0,
\]

at a nondegenerate protected instant. Put

\[
m:=\min\{\alpha,\beta\},
\qquad
M:=\max\{\alpha,\beta\}.
\]

For an active cross-spin parent pair

\[
A^+,
\qquad
B^-,
\]

write

\[
\sin\theta_{AB}
:=\frac{|A\times B|}{\alpha\beta}.
\]

Define

\[
\Phi(s)
:=s\left(1-\sqrt{1-s^2}\right),
\qquad
0\le s\le1.
\]

This function is nonnegative and vanishes exactly at `s=0`.

For the parent amplitudes define the critical pair product

\[
\pi_{AB}
:=\sqrt{\alpha\beta}\,
|z_+(A)z_-(B)|.
\]

## 2. Quantitative reality-twin pair lower bound

By `27-reality-twin-protected-leakage.md`, one of the two reality-twin outputs

\[
A+B,
\qquad
A-B
\]

has radius `rho_*` satisfying

\[
\operatorname{dist}
(\rho_*,\{\alpha,\beta\})
\ge\frac{m^2}{3M}.
\]

At that selected twin, both protected multiplier symbols obey

\[
|t_\pm(\rho_*)|
\ge\frac{m^3}{3M^2}.
\]

Let `phi` be the angle between `A` and the selected signed parent `+/- B`. Its sine equals `sin theta_AB`. The triangle gap satisfies

\[
\rho_*-|\alpha-\beta|
\ge
m\left(1-\sqrt{1-\sin^2\theta_{AB}}\right).
\]

The general helical coefficient formula therefore gives, for either output helicity `t=+/-`,

\[
|C_t(\rho_*)|
\ge
\frac{m}{2\sqrt2}
\Phi(\sin\theta_{AB}).
\]

Multiplying by the protected multiplier and modal amplitudes yields the exact scale-compatible lower bound

\[
\boxed{
|x_{AB,t}|
\ge
c_{\alpha,\beta}
M\,
\Phi(\sin\theta_{AB})
\pi_{AB},
}
\]

where

\[
\boxed{
c_{\alpha,\beta}
:=\frac1{6\sqrt2}
\left(\frac mM\right)^4.}
\]

Here `x_AB,t` denotes the pair contribution to the opening force `TF` at the selected reality-twin output and helicity `t`.

Thus for comparable protected shells `m/M >= c>0`, every angularly nondegenerate cross-spin parent pair creates an order-frequency opening pair contribution.

## 3. Aggregate twin-opening mass

Choose any subfamily `S` of distinct cross-spin pair channels, with no duplicate canonical pair contribution. For each pair select the reality twin supplied by Section 2 and retain both output helicities. Define

\[
\mathcal M_{\rm twin}
:=\sum_{(A,B)\in\mathcal S}
\sum_{t=\pm}|x_{AB,t}|^2.
\]

Then

\[
\boxed{
\mathcal M_{\rm twin}
\ge
2c_{\alpha,\beta}^2M^2
\sum_{(A,B)\in\mathcal S}
\Phi(\sin\theta_{AB})^2
\pi_{AB}^2.
}
\]

The right-hand side measures the amount of cross-spin critical pair mass that is also genuinely angularly three-dimensional at the protected reset.

## 4. Opening composition defect

At every helical output `(r,t)`, decompose the exact opening force into all canonical pair contributions

\[
(TF)_t(r)
=\sum_{e\in\mathcal P_t(r)}x_e.
\]

Define the total opening composition defect

\[
\boxed{
\mathfrak D_{\rm open}
:=
\sum_{r,t}
\left[
\left(\sum_{e\in\mathcal P_t(r)}|x_e|\right)^2
-
\left|\sum_{e\in\mathcal P_t(r)}x_e\right|^2
\right]
\ge0.
}
\]

Since

\[
\frac12\mathcal Y''
=\|TF\|_2^2
=
\sum_{r,t}
\left|\sum_e x_e\right|^2,
\]

and selected pair squares are bounded by the full absolute envelope at each output,

\[
\boxed{
\mathcal M_{\rm twin}
\le
\frac12\mathcal Y''
+
\mathfrak D_{\rm open}.
}
\]

Combining with Section 3 gives the **Protected Reset Inequality**

\[
\boxed{
\frac12\mathcal Y''
+
\mathfrak D_{\rm open}
\ge
2c_{\alpha,\beta}^2M^2
\sum_{(A,B)\in\mathcal S}
\Phi(\sin\theta_{AB})^2
\pi_{AB}^2.
}
\]

No phase-randomness or multiplicity assumption enters this inequality.

## 5. Exact zero-cost rigidity

Assume simultaneously

\[
\mathcal Y''=0
\]

and

\[
\mathfrak D_{\rm open}=0.
\]

Then at every output

\[
\sum_e x_e=0
\]

and

\[
\left(\sum_e|x_e|\right)^2=0.
\]

Therefore every individual opening pair contribution vanishes.

Take any active cross-spin pair. If it were noncollinear, the reality-twin lower bound would give a nonzero opening contribution. Hence every active `+/-` parent pair is collinear.

Because both spin sectors are nonempty, fixing one active mode in either sector shows that **all active modes lie on one common Fourier line**.

Same-spin protected-shell interactions already vanish pairwise. Cross-spin interactions now also vanish pairwise because

\[
A\times B=0.
\]

Consequently

\[
\boxed{F=0.}
\]

This is the **Zero-Cost Protected Reset Rigidity Theorem**:

\[
\boxed{
\mathcal Y=0,
\quad
\mathcal Y''=0,
\quad
\mathfrak D_{\rm open}=0
\Longrightarrow
F=0.
}
\]

## 6. The zero-cost endpoint is an exact global heat solution

If `F=0` at such a protected state, then

\[
u_t=-\nu\Lambda^2u.
\]

Because the two sectors each occupy one radial shell,

\[
u_+(t)
=e^{-\nu\alpha^2(t-t_0)}u_+(t_0),
\]

\[
u_-(t)
=e^{-\nu\beta^2(t-t_0)}u_-(t_0).
\]

The nonlinear cross term is bilinear in `u_+,u_-`, while same-spin terms vanish identically on each shell. Therefore

\[
F(t)
=e^{-\nu(\alpha^2+\beta^2)(t-t_0)}F(t_0)
=0.
\]

Hence the heat evolution above is the exact Navier-Stokes solution for all later times. It is smooth and globally regular.

Thus the unique zero-cost protected endpoint of this trichotomy is dynamically safe.

## 7. The protected reset trichotomy

Every nondegenerate protected state therefore lies in one of three branches:

\[
\boxed{
\begin{cases}
\mathcal Y''>0,
&\text{actual defect-opening acceleration},\\[1mm]
\mathcal Y''=0,\ \mathfrak D_{\rm open}>0,
&\text{hidden additive/phase cancellation cost},\\[1mm]
\mathcal Y''=0,\ \mathfrak D_{\rm open}=0,
&F=0\text{ and exact global heat decay}.
\end{cases}}
\]

This removes cost-free resets from the protected manifold. A singular escape chain can revisit `Y=0` only by paying either nonlinear opening acceleration or a positive composition defect, unless it falls into the globally regular heat branch.

## 8. Remaining quantitative problem

The theorem is pointwise in time. To close a global regularity proof one still needs a scale-invariant time-integrated lower bound showing that repeated protected resets cannot pay the first two costs on increasingly short intervals while respecting the available global action budgets.

The natural next step is to combine

- the protected contact hierarchy,
- the reset inequality above,
- the finite action of `X`, `K^2`, and global nonplanarity,
- and the parabolic pair-heat observability estimates,

into a **reset-counting / no-Zeno lemma** for positive critical-growth epochs.
