# Protected Output Moment Hierarchy

At a nondegenerate protected state the exact nonlinear forcing has a natural signed coordinate: its output distance from the two protected helical shells. The first two moments of that output distribution are exactly the initial acceleration of critical production and the second-order opening of the optimal protected defect.

## 1. Protected instant

Assume at time `t_0`

\[
\mathcal Y=\|r\|_2^2=0,
\qquad
\Delta=EZ-H^2>0.
\]

Let

\[
T=\Lambda-a-b\operatorname{curl}.
\]

From `23-protected-manifold-acceleration.md`,

\[
Tu=0,
\qquad
a'=b'=0,
\qquad
r_t=TF,
\]

and

\[
\mathcal Y''=2\|TF\|_2^2.
\]

Also

\[
\kappa=\langle r,F\rangle=0.
\]

## 2. Exact initial derivative of critical production

Differentiate

\[
\kappa=\langle r,F\rangle.
\]

At the protected instant `r=0`, the term containing `F_t` vanishes, so

\[
\boxed{
\kappa'(t_0)
=\langle r_t,F\rangle
=\langle TF,F\rangle.
}
\]

No viscosity term appears explicitly: viscosity preserves `ker T` at that instant, while the nonlinear output determines how critical production begins to reopen.

## 3. Fourier output moments

On the bi-monochromatic protected branch let the shell radii be

\[
\alpha=m_+,
\qquad
\beta=m_-.
\]

Then

\[
t_+(\rho)
=\frac{2\beta}{\alpha+\beta}(\rho-\alpha),
\]

\[
t_-(\rho)
=\frac{2\alpha}{\alpha+\beta}(\rho-\beta).
\]

Thus `t_sigma(rho)` is a signed radial distance from the protected shell in that output helicity, up to a positive constant factor.

Write the exact *total* nonlinear forcing after all pair cancellations as

\[
F=\sum_{k,\sigma}F_\sigma(k)h_\sigma(k)e^{ik\cdot x}.
\]

Define

\[
\mathcal N_0
:=\|F\|_2^2,
\]

\[
\mathcal N_1
:=\sum_{k,\sigma}
 t_\sigma(|k|)|F_\sigma(k)|^2,
\]

and

\[
\mathcal N_2
:=\sum_{k,\sigma}
 t_\sigma(|k|)^2|F_\sigma(k)|^2.
\]

Then exactly

\[
\boxed{
\mathcal N_1=\kappa'(t_0),
}
\]

and

\[
\boxed{
\mathcal N_2=\frac12\mathcal Y''(t_0).
}
\]

Therefore the first two signed output moments are dynamical derivatives of the two main escape variables.

## 4. Moment inequality

Cauchy-Schwarz gives

\[
|\langle F,TF\rangle|^2
\le\|F\|_2^2\|TF\|_2^2.
\]

Hence

\[
\boxed{
|\kappa'(t_0)|^2
\le
\frac12\|F(t_0)\|_2^2\mathcal Y''(t_0).
}
\]

Equivalently, if `F != 0`,

\[
\boxed{
\mathcal Y''(t_0)
\ge
2\frac{|\kappa'(t_0)|^2}{\|F(t_0)\|_2^2}.
}
\]

Thus critical production cannot begin changing rapidly while the protected defect remains quadratically flat.

## 5. Output mean and variance

When `N_0>0`, normalize the forcing energy into a probability distribution on helical output modes:

\[
\mathbb P_F(k,\sigma)
:=\frac{|F_\sigma(k)|^2}{\mathcal N_0}.
\]

Let the random variable

\[
T_F(k,\sigma):=t_\sigma(|k|).
\]

Then

\[
\boxed{
\mathbb E_F T_F
=\frac{\kappa'}{\|F\|_2^2},
}
\]

and

\[
\boxed{
\mathbb E_F T_F^2
=\frac{\mathcal Y''}{2\|F\|_2^2}.
}
\]

Consequently

\[
\boxed{
\operatorname{Var}_F(T_F)
=
\frac{\mathcal Y''}{2\|F\|_2^2}
-
\left(\frac{\kappa'}{\|F\|_2^2}\right)^2
\ge0.
}
\]

This separates two distinct opening patterns:

1. **biased opening:** forcing is preferentially generated on one signed side of the protected shells, giving large `|kappa'|`;
2. **symmetric spreading:** forcing has large second moment but small first moment, so the protected defect opens without immediately creating a large signed critical production.

Both patterns have a positive opening cost; they differ only in the signed direction of the newly generated modes.

## 6. Zero-moment rigidity

If

\[
\mathcal Y''=0,
\]

then `N_2=0`, hence every actual nonlinear output with nonzero forcing lies in the zero set of `T`. This recovers the exact two-shell closure criterion

\[
TF=0.
\]

If instead

\[
\kappa'=0
\]

but `Y''>0`, the forcing is not closed: it spreads to both signed sides in such a way that the first moment cancels. Such a state is not protected against future escape; only its first signed output moment vanishes.

This distinction prevents a false shortcut in which `kappa'=0` is treated as nonlinear closure.

## 7. Relation to the reopening barrier

At a protected instant the Navier-Stokes critical balance is

\[
K'=-2\nu M_3<0
\]

for a nonzero state, because `kappa=0`. Before `K` can grow again, nonlinear dynamics must first create enough protected defect to satisfy the barrier

\[
\mathcal X>a_*K
\]

at every later time with `K'>0`.

The moment hierarchy identifies the exact initial mechanism for that reopening:

\[
\boxed{
\text{actual nonlinear output distance from the protected shells}.
}
\]

A full quantitative reset theorem would combine this second-order opening with parabolic decay of the protected shell amplitudes and the Composition constraints on the output forcing. That theorem remains open.
