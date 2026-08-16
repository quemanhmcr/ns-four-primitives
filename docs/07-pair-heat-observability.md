# Pair-Heat Observability and the Exact Resonant Kernel

The parabolic diamond identity extends to arbitrary many-to-one cancellation. The right object is a finite-dimensional pair-product system at each Fourier output.

## 1. Pair state at a fixed output

Fix an output wavevector `r` and one output helicity. For every canonical pair channel `alpha=(a,b,...)` with

\[
a+b=r,
\]

let

\[
X_\alpha=C_\alpha z_a z_b
\]

be its complex contribution to the chosen scalar helical forcing. Define its pair heat rate

\[
\lambda_\alpha:=|a|^2+|b|^2.
\]

The actual observed forcing at the output is

\[
y=\sum_\alpha X_\alpha.
\]

If one temporarily keeps only the linear viscous evolution of the modal factors, then

\[
\boxed{
\dot X_\alpha=-\nu\lambda_\alpha X_\alpha,
\qquad
y=\mathbf 1^T X.
}
\]

Thus cancellation is an observability problem for a diagonal dissipative system.

## 2. Group by equal heat rate

Let the distinct values among the `lambda_alpha` be

\[
\mu_1,\ldots,\mu_m,
\]

and define the group resultants

\[
Y_j:=\sum_{\alpha:\lambda_\alpha=\mu_j}X_\alpha.
\]

Under pure viscosity,

\[
\boxed{
y(t)=\sum_{j=1}^m e^{-\nu\mu_j t}Y_j(0).
}
\]

The functions `exp(-nu mu_j t)` are linearly independent for distinct `mu_j`. Therefore:

### Exact persistent-cancellation theorem

If

\[
y(t)=0
\]

for every `t` in a nontrivial interval under the pure viscous flow, then

\[
\boxed{Y_j(0)=0\quad\text{for every heat-rate class }j.}
\]

Conversely, if every class resultant vanishes, then `y(t)=0` for all time under the pure viscous flow.

Hence the exact unobservable subspace is

\[
\boxed{
\ker_{\rm heat}
=
\left\{X:
\sum_{\alpha:\lambda_\alpha=\mu}X_\alpha=0
\text{ for every }\mu
\right\}.
}
\]

Persistent cancellation between distinct heat rates is impossible without nonlinear compensation.

## 3. Vandermonde proof

At `t=0`,

\[
y^{(n)}(0)
=(-\nu)^n\sum_{j=1}^m\mu_j^nY_j,
\qquad n=0,1,\ldots,m-1.
\]

If `y` vanishes on an interval then all these derivatives vanish. Therefore

\[
\begin{pmatrix}
1&1&\cdots&1\\
\mu_1&\mu_2&\cdots&\mu_m\\
\vdots&\vdots&&\vdots\\
\mu_1^{m-1}&\mu_2^{m-1}&\cdots&\mu_m^{m-1}
\end{pmatrix}
\begin{pmatrix}Y_1\\Y_2\\\vdots\\Y_m\end{pmatrix}=0.
\]

The Vandermonde determinant is

\[
\prod_{i<j}(\mu_j-\mu_i)\neq0,
\]

so every `Y_j` vanishes.

This proof also shows why a quantitative observability constant deteriorates when distinct heat rates become close. Near-resonance must therefore be retained as a genuine branch rather than discarded by a non-uniform estimate.

## 4. Geometry of a heat-rate class

Write the two inputs around the midpoint of their common output:

\[
a=\frac r2+x,
\qquad
b=\frac r2-x.
\]

Then

\[
\boxed{
\lambda_{ab}
=|a|^2+|b|^2
=\frac{|r|^2}{2}+2|x|^2.
}
\]

Therefore, for fixed `r`, an equal-rate class is exactly a sphere

\[
\boxed{|x|=R}
\]

in the pair-coordinate centered at `r/2`.

Two representations `a+b=c+d=r` belong to the same class iff

\[
|a|^2+|b|^2=|c|^2+|d|^2,
\]

which is precisely the rectangular condition from `06-parabolic-diamond-curvature.md`.

Thus the many-pair exceptional set is not merely "high additive energy". It is additive multiplicity stratified onto common midpoint spheres.

## 5. Selection geometry inside a resonant sphere

For same-spin parents, let

\[
\rho=|r|,
\qquad
R=|x|,
\]

and let `theta` be the angle between `r` and `x`. Put

\[
\alpha=|r/2+x|,
\qquad
\beta=|r/2-x|,
\qquad
S=\alpha+\beta.
\]

The elementary identities

\[
|a\times b|=|r\times x|=\rho R|\sin\theta|,
\]

and

\[
|\alpha-\beta|
=\frac{2|r\cdot x|}{S}
=\frac{2\rho R|\cos\theta|}{S}
\]

insert into the exact same-spin helical coefficient to give

\[
\boxed{
|C^{t,s,s}|
=
\frac{\rho R^2}{2\sqrt2\,S\alpha\beta}
(S+ts\rho)
|\sin2\theta|.
}
\]

Therefore heat resonance does not remove Navier-Stokes selection. Inside every resonant sphere the same-spin interaction still vanishes at both angular extremes:

- `theta = 0, pi`: angular/collinear degeneracy;
- `theta = pi/2`: equal-radius degeneracy.

Dangerous resonant transfer must occupy intermediate angular bands.

## 6. Full Navier-Stokes interpretation

For the full nonlinear evolution, the pair state has the controlled form

\[
\dot X=-\nu D X+U,
\]

where `D=diag(lambda_alpha)` and `U` contains the nonlinear changes of the two input modal factors. The observation remains

\[
y=\mathbf1^T X.
\]

The exact linear analysis proves that any cancellation involving distinct heat-rate classes is transverse to viscosity. To keep such cancellation hidden, `U` must continually act as a control that compensates this parabolic observability.

This leaves two quantitatively different branches:

\[
\boxed{
\text{dense cancellation}
\Rightarrow
\begin{cases}
\text{inter-rate cancellation requiring nonlinear control},\\
\text{intra-rate cancellation on resonant midpoint spheres}.
\end{cases}}
\]

The first branch is now a control-cost problem. The second is the genuinely exceptional geometric branch and must be attacked using the exact helical phase/polarization structure on the resonant spheres.

## 7. Next rigorous targets

1. Prove a scale-local observability/control inequality for heat-rate classes separated by a fixed fraction of the active parabolic rate.
2. Keep near-equal rates as a thin resonant cluster rather than paying a non-uniform Vandermonde constant.
3. On an exact/near resonant sphere, derive a gauge-invariant composition law for helical coefficient phases and test whether dense cancellation can be globally compatible with positive critical flux.
