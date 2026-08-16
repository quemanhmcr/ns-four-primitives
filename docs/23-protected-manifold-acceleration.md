# Acceleration Away from the Protected Two-Shell Manifold

The optimal protected escape defect has zero set

\[
\Lambda u\in\operatorname{span}\{u,\omega\}.
\]

On the nondegenerate two-spin branch this means that each helicity sector is monochromatic, possibly at a different radius. Critical Euler production vanishes instantaneously there. This note computes the exact second-order opening of the defect.

## 1. Nondegenerate protected state

Fix a smooth time `t_0` such that

\[
\mathcal Y(t_0)=0
\]

and

\[
\Delta(t_0):=E Z-H^2>0.
\]

Thus `u` and `omega` are linearly independent and the minimizing coefficients `a,b` are locally smooth. Put

\[
T:=\Lambda-a-b\operatorname{curl}.
\]

At `t_0`,

\[
\boxed{r=Tu=0.}
\]

The pure-spin rank-one branch requires a separate degenerate-envelope analysis and is not included in this note.

## 2. First derivative of the residual

Differentiate

\[
r=Tu.
\]

At the protected instant,

\[
r_t
=T u_t-a'u-b'\omega.
\]

For Navier-Stokes,

\[
u_t=F-\nu\Lambda^2u.
\]

Because `T` commutes with `Lambda`,

\[
T\Lambda^2u
=\Lambda^2Tu
=0
\]

at `t_0`. Hence

\[
\boxed{
r_t
=TF-a'u-b'\omega.}
\]

Now differentiate the normal equations

\[
\langle r,u\rangle=0,
\qquad
\langle r,\omega\rangle=0.
\]

Since `r=0` at `t_0`,

\[
\langle r_t,u\rangle=0,
\qquad
\langle r_t,\omega\rangle=0.
\]

Because `T` is self-adjoint and commutes with curl,

\[
\langle TF,u\rangle
=\langle F,Tu\rangle=0,
\]

and

\[
T\omega=T\operatorname{curl}u
=\operatorname{curl}(Tu)=0,
\qquad
\langle TF,\omega\rangle=0.
\]

Thus `TF` is already orthogonal to the protected span. Since the Gram matrix of `u,omega` is invertible on this branch, the differentiated normal equations force

\[
\boxed{a'(t_0)=b'(t_0)=0.}
\]

Therefore

\[
\boxed{r_t(t_0)=TF.}
\]

This formula is independent of viscosity at the protected instant.

## 3. Exact second-order opening

Since

\[
\mathcal Y=\|r\|_2^2,
\]

we have at `r=0`

\[
\mathcal Y'=2\langle r,r_t\rangle=0
\]

and

\[
\mathcal Y''
=2\|r_t\|_2^2
+2\langle r,r_{tt}\rangle.
\]

The second term vanishes. Hence

\[
\boxed{
\mathcal Y''(t_0)
=2\|TF\|_2^2
\ge0.
}
\]

For the critical defect

\[
\mathcal X=E\mathcal Y,
\]

both `Y` and `Y'` vanish at the protected instant, so

\[
\boxed{
\mathcal X''(t_0)
=2E(t_0)\|TF\|_2^2.
}
\]

## 4. Interpretation

The protected two-shell manifold is tangent-flat for the critical escape defect:

\[
\mathcal X=0,
\qquad
\mathcal X'=0.
\]

It can open only at second order through the exact weighted nonlinear forcing `TF`. At a protected state this vector is automatically transverse to the energy-helicity conservation span.

Viscosity contributes **zero opening acceleration** at the protected instant because it preserves the kernel of `T` mode-by-mode.

Thus repeated singular escape cannot be modeled as cost-free instantaneous resets to `X=0` followed by arbitrary reopening. Every nondegenerate reset has an exact nonlinear acceleration certificate.

## 5. Fourier meaning on the bi-monochromatic branch

When both spin sectors are present and `Y=0`, there are radii `m_+,m_-` such that

\[
\Lambda u_+=m_+u_+,
\qquad
\Lambda u_-=m_-u_-.
\]

The multiplier symbol

\[
t_\sigma(k)=((1-b\sigma)|k|-a)
\]

vanishes on the two protected shells. Therefore `TF` weights every newly generated Fourier output by its signed distance, under the optimal affine helical fit, from those protected shell values.

The acceleration formula consequently measures how strongly the full convolution attempts to populate modes outside the instantaneous protected two-shell geometry.

## 6. Exact zero-acceleration closure criterion

The second-order identity immediately gives

\[
\boxed{
\mathcal Y''(t_0)=0
\iff
TF=0.
}
\]

On the nondegenerate two-spin protected branch, the two shell radii `m_+,m_-` determine

\[
a=\frac{2m_+m_-}{m_++m_-},
\qquad
b=\frac{m_+-m_-}{m_++m_-},
\]

so the helical symbol

\[
t_\sigma(k)=((1-b\sigma)|k|-a)
\]

has exactly two positive radial zeros:

\[
t_+(m_+)=0,
\qquad
t_-(m_-)=0.
\]

Therefore

\[
TF=0
\iff
\operatorname{supp}F
\subset
\{(k,+):|k|=m_+\}
\cup
\{(k,-):|k|=m_-\}.
\]

Thus zero opening acceleration is exactly a **two-shell convolution-closure condition**: every nonlinear Fourier output outside the protected helical shells must cancel.

On the periodic lattice each fixed-radius shell contains only finitely many wavevectors. Hence the exceptional zero-acceleration branch is finite-dimensional at that instant.

## 7. Next rigidity problem

The remaining exact classification question is now sharp:

\[
\boxed{
\text{Which nondegenerate bi-monochromatic states satisfy }TF=0?
}
\]

Same-spin interactions on each protected shell vanish pairwise because the exact coefficient contains the radial factor `|q-k|`. Therefore only heterochiral cross-shell parent pairs can drive opening. The next note resolves the exact pair-level leakage created by those cross-spin interactions.
