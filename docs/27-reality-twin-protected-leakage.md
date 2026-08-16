# Reality-Twin Protected Leakage

A single complex cross-spin pair can have an exceptional shell-closing geometry. A real velocity field cannot keep only that pair: reality supplies the reflected partner at the opposite wavevector. The resulting pair of outputs obeys a parallelogram law that forces one of them quantitatively away from both protected shell radii.

This removes the apparent isolated equilateral loophole from `24-general-helical-and-protected-leakage.md` unless additional convolution pairs are recruited for cancellation.

## 1. Reality supplies a twin interaction

Let a protected bi-monochromatic state have shell radii

\[
\alpha=m_+>0,
\qquad
\beta=m_->0.
\]

Take active cross-spin modes

\[
A^+,
\qquad
B^-.
\]

Because the physical field is real, the Fourier modes at `-A` and `-B` are also present, with the corresponding reality-related amplitudes. Helicity sign is preserved under `k -> -k` after complex conjugation.

Therefore the parent `A^+` participates in both cross-spin pairs

\[
A^++B^-
\quad\text{and}\quad
A^++(-B)^-.
\]

Their output wavevectors are

\[
r_+:=A+B,
\qquad
r_-:=A-B.
\]

Write

\[
\rho_\pm:=|r_\pm|.
\]

## 2. Parallelogram obstruction

The exact parallelogram identity gives

\[
\boxed{
\rho_+^2+\rho_-^2
=2(\alpha^2+\beta^2).
}
\]

Let

\[
m:=\min\{\alpha,\beta\},
\qquad
M:=\max\{\alpha,\beta\}.
\]

For a nonnegative number `x`, define its squared-radius distance from the protected set by

\[
d_2(x)
:=\operatorname{dist}
\left(x,\{\alpha^2,\beta^2\}\right).
\]

Then

\[
\boxed{
\max\{d_2(\rho_+^2),d_2(\rho_-^2)\}
\ge m^2.
}
\]

### Proof

Choose for each `rho_±^2` a nearest protected squared radius `s_±` in `{alpha^2,beta^2}`. Since

\[
s_++s_-\le2M^2,
\]

we have

\[
(\rho_+^2-s_+)+(\rho_-^2-s_-)
\ge2(M^2+m^2)-2M^2
=2m^2.
\]

Therefore

\[
d_2(\rho_+^2)+d_2(\rho_-^2)
\ge2m^2,
\]

which proves the claim.

## 3. Radial distance from both protected shells

Select a twin output `rho_*` satisfying

\[
\operatorname{dist}
(\rho_*^2,\{\alpha^2,\beta^2\})
\ge m^2.
\]

For either protected radius `s in {alpha,beta}`,

\[
|\rho_*-s|
=\frac{|\rho_*^2-s^2|}{\rho_*+s}.
\]

Since

\[
\rho_*\le\alpha+\beta\le2M,
\]

we obtain

\[
\boxed{
\operatorname{dist}
(\rho_*,\{\alpha,\beta\})
\ge\frac{m^2}{3M}.
}
\]

Thus one reality-twin output is quantitatively separated from **both** protected radii.

## 4. Lower bound for both protected multiplier symbols

At the protected state,

\[
t_+(\rho)
=\frac{2\beta}{\alpha+\beta}(\rho-\alpha),
\]

\[
t_-(\rho)
=\frac{2\alpha}{\alpha+\beta}(\rho-\beta).
\]

Since

\[
\min\left\{
\frac{2\alpha}{\alpha+\beta},
\frac{2\beta}{\alpha+\beta}
\right\}
\ge\frac mM,
\]

the selected twin satisfies

\[
\boxed{
\min\{|t_+(\rho_*)|,|t_-(\rho_*)|\}
\ge\frac{m^3}{3M^2}.
}
\]

If the two protected shell radii are comparable,

\[
m\ge cM,
\]

then

\[
\boxed{
\min\{|t_+(\rho_*)|,|t_-(\rho_*)|\}
\ge\frac{c^3}{3}M.
}
\]

Thus the reality-twin leakage is order-frequency in the local comparable-shell regime.

## 5. Pair coefficient at the selected twin

For the noncollinear cross-spin parent pair, let

\[
A_\times:=|A\times B|.
\]

The general helical formula gives, at either twin radius `rho`,

\[
|C_t(\rho)|
=
\frac1{2\sqrt2}
(\alpha+\beta)
\frac{A_\times}{\rho\alpha\beta}
|\alpha-\beta+t\rho|.
\]

For a noncollinear pair,

\[
|\alpha-\beta|<\rho<\alpha+\beta,
\]

so both output-helicity coefficients are positive. Their minimum is

\[
\boxed{
\min_{t=\pm}|C_t(\rho)|
=
\frac1{2\sqrt2}
(\alpha+\beta)
\frac{A_\times}{\rho\alpha\beta}
\left(\rho-|\alpha-\beta|\right).
}
\]

Combining with the multiplier lower bound gives an explicit pairwise lower bound for both protected-opening channels at the selected twin.

The remaining degeneracy `rho-|alpha-beta| -> 0` is exactly the nearly collinear triangle limit, where `A_cross` also degenerates. It is therefore a known Selection-depletion branch rather than a new loophole.

## 6. Elimination of the isolated equal-shell equilateral loophole

Suppose

\[
\alpha=\beta=m.
\]

A single complex pair can satisfy

\[
|A+B|=m,
\]

making that output lie on the common protected shell for both helicities. But then

\[
|A-B|^2
=4m^2-|A+B|^2
=3m^2.
\]

Hence the reality twin has

\[
\boxed{|A-B|=\sqrt3\,m,}
\]

which lies far outside the protected shell.

Therefore the equilateral-radius interaction is not pairwise closed in a real field. Its reflected twin necessarily produces protected leakage unless additional parent pairs cancel that output.

## 7. Composition consequence

For every noncollinear active cross-spin pair in a real protected state, at least one of its two reality-twin outputs is quantitatively outside the protected shell set. Therefore

\[
\boxed{
\text{zero protected acceleration}
\Longrightarrow
\text{systematic multi-pair cancellation of reality-twin leakage}
}
\]

unless all active cross-spin pairs are angularly degenerate.

This sends the entire nondegenerate zero-acceleration branch back into the additive/composition framework: each hidden reality-twin output requires another representation of the same Fourier wavevector.

The next target is to aggregate these twin constraints over the full protected shell graph and obtain a quantitative lower bound on opening acceleration or additive collision mass.
