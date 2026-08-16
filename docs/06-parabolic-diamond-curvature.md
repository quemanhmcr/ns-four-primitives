# Parabolic Transversality of Cancellation Diamonds

The dense branch of Lemma B can avoid actual leakage only by arranging cancellation among multiple pair contributions at the same output. This note shows that generic two-pair cancellation is not invariant under the linear viscous flow. The exceptional set is an exact geometric resonance class: rectangles.

## 1. One additive diamond

Let

\[
a+b=c+d=r
\]

and fix four helical modal amplitudes (helicity labels may be arbitrary for this calculation). Let the two pair contributions to one chosen output polarization be

\[
X=C_1 z_a z_b,
\qquad
Y=C_2 z_c z_d,
\]

where `C_1,C_2` are the time-independent exact helical coefficients.

Write each modal equation as

\[
\dot z_k=F_k-\nu|k|^2z_k,
\]

where `F_k` denotes the corresponding scalar helical nonlinear forcing.

Define

\[
\lambda_1=|a|^2+|b|^2,
\qquad
\lambda_2=|c|^2+|d|^2,
\qquad
\mathcal Q_\square:=\lambda_1-\lambda_2.
\]

Then exactly

\[
\dot X=-\nu\lambda_1 X
+C_1(F_a z_b+z_aF_b),
\]

\[
\dot Y=-\nu\lambda_2 Y
+C_2(F_c z_d+z_cF_d).
\]

## 2. Tangency condition on the cancellation manifold

Suppose at some instant the two contributions cancel exactly,

\[
X+Y=0.
\]

At that instant,

\[
\boxed{
\frac d{dt}(X+Y)
=-\nu\mathcal Q_\square X
+\mathcal N_\square,
}
\]

where

\[
\mathcal N_\square
:=C_1(F_a z_b+z_aF_b)
+C_2(F_c z_d+z_cF_d).
\]

Therefore first-order persistence of exact cancellation requires the exact compensation law

\[
\boxed{
\mathcal N_\square
=\nu\mathcal Q_\square X.
}
\]

Consequently, if `Q_square != 0`, remaining tangent to the cancellation manifold forces

\[
\boxed{
|\mathcal N_\square|
=\nu|\mathcal Q_\square|\,|X|.
}
\]

This is a new nonlinear burden generated solely by the incompatibility between additive cancellation and parabolic damping.

## 3. Geometry of the parabolic curvature

Because `a+b=c+d`, put

\[
h=a-c=d-b.
\]

A direct expansion gives

\[
\boxed{
\mathcal Q_\square
=2h\cdot(c-b).
}
\]

Thus

\[
\mathcal Q_\square=0
\]

if and only if the two edge vectors of the additive parallelogram are orthogonal. In the ordering `c -> a -> d -> b -> c`, the exceptional parallelogram is a rectangle.

Equivalently, writing

\[
a=\frac r2+x,\quad b=\frac r2-x,
\qquad
c=\frac r2+y,\quad d=\frac r2-y,
\]

gives

\[
\boxed{
\mathcal Q_\square=2(|x|^2-|y|^2).
}
\]

So heat-resonant decompositions of the same output are exactly those whose two input pairs lie at the same distance from the midpoint `r/2`.

## 4. Persistence identity away from zero amplitudes

On an interval where all four modal amplitudes and both pair contributions are nonzero,

\[
\boxed{
\frac d{dt}\log\frac{X}{Y}
=-\nu\mathcal Q_\square
+
\left(
\frac{F_a}{z_a}+\frac{F_b}{z_b}
-\frac{F_c}{z_c}-\frac{F_d}{z_d}
\right).
}
\]

The real part controls relative pair magnitude; the imaginary part controls relative pair phase. Hence maintaining an approximately fixed cancellation ratio on a nonresonant diamond requires the nonlinear logarithmic rates to compensate a deterministic drift of size `nu |Q_square|`.

## 5. Consequence for the Composition program

Lemma B reduces the non-leakage branch to large composition defect. This note splits that branch further:

\[
\boxed{
\text{dense cancellation}
\Rightarrow
\begin{cases}
\text{nonrectangular diamonds with viscous transverse cost},\\
\text{or heat-resonant rectangular diamonds}.
\end{cases}}
\]

Thus the genuinely exceptional dense network is not an arbitrary additive network. A low-cost cancellation network must concentrate on, or dynamically track, the rectangular resonance geometry

\[
a+b=c+d,
\qquad
|a|^2+|b|^2=|c|^2+|d|^2.
\]

The next target is to combine this parabolic resonance condition with the exact helical coefficient phases. If the rectangular network still carries nontrivial gauge-invariant helical phase curvature, then the remaining cancellation branch acquires a second, purely nonlinear composition obstruction.

This last statement is a target, not yet a theorem.
