# Within-Spin Radial Gate

Critical escape needs more than two helicity sectors. The same-helicity endpoint modes that perform a heterochiral handoff must also possess radial spectral width. This note records the exact global form of that requirement and its own viscous defect dynamics.

## 1. Sector-centered radial variables

For each nonzero helicity sector define

\[
E_\sigma:=\|u_\sigma\|_2^2,
\qquad
K_\sigma:=\langle u_\sigma,\Lambda u_\sigma\rangle,
\qquad
Z_\sigma:=\|\Lambda u_\sigma\|_2^2,
\]

and

\[
m_\sigma:=\frac{K_\sigma}{E_\sigma},
\qquad
s_\sigma:=(\Lambda-m_\sigma)u_\sigma,
\qquad
W_\sigma:=\|s_\sigma\|_2^2.
\]

Then

\[
\langle u_\sigma,s_\sigma\rangle=0
\]

and

\[
\boxed{
W_\sigma
=Z_\sigma-\frac{K_\sigma^2}{E_\sigma}.
}
\]

Define the scale-critical within-spin radial defect

\[
\boxed{
\mathcal R_{\rm rad}
:=\sum_{\sigma=\pm}E_\sigma W_\sigma
=\sum_{\sigma=\pm}
(E_\sigma Z_\sigma-K_\sigma^2).
}
\]

Each term is nonnegative by Cauchy-Schwarz.

## 2. Exact collapse of critical production onto the radial defects

Let

\[
F_\sigma=P_\sigma F,
\qquad
A_\sigma:=\langle\Lambda u_\sigma,F_\sigma\rangle,
\qquad
B_\sigma:=\langle u_\sigma,F_\sigma\rangle.
\]

Euler energy and helicity tangency give

\[
B_++B_-=0,
\qquad
A_+-A_-=0.
\]

Since

\[
\kappa=A_++A_-,
\]

we have

\[
A_+=A_-=\frac\kappa2.
\]

Define

\[
c_\sigma:=\langle s_\sigma,F_\sigma\rangle
=A_\sigma-m_\sigma B_\sigma.
\]

Solving the two conservation constraints gives the exact identity

\[
\boxed{
\kappa
=2\frac{m_-c_++m_+c_-}{m_++m_-}.
}
\]

Therefore, if

\[
W_+=W_-=0,
\]

then `c_+=c_-=0` and

\[
\boxed{\kappa=0.}
\]

If one spin sector is absent, the pure-spin identity `kappa=0` follows directly from Euler helicity conservation because `K=|H|` at that instant.

Hence

\[
\boxed{
\kappa\ne0
\Longrightarrow
\mathcal B>0
\quad\text{and}\quad
\mathcal R_{\rm rad}>0.
}
\]

This is the global **Spin + Radial Gate Theorem** for critical production.

## 3. Exact within-spin width evolution

Let

\[
Q_\sigma:=\Lambda-m_\sigma,
\qquad
\Gamma_\sigma:=
\langle Q_\sigma^2u_\sigma,F_\sigma\rangle,
\]

and

\[
H_\sigma:=\|\Lambda s_\sigma\|_2^2.
\]

Because `m_sigma` is the minimizer of

\[
m\mapsto\|(\Lambda-m)u_\sigma\|_2^2,
\]

its stationarity removes the `m_sigma'` term when differentiating `W_sigma`. Direct differentiation gives

\[
\boxed{
W_\sigma'
=2\Gamma_\sigma-2\nu H_\sigma.
}
\]

Moreover

\[
W_\sigma
=\langle u_\sigma,\Lambda s_\sigma\rangle,
\]

so Cauchy-Schwarz gives

\[
\boxed{
W_\sigma^2\le E_\sigma H_\sigma.
}
\]

Thus

\[
\boxed{
W_\sigma'
\le2\Gamma_\sigma
-2\nu\frac{W_\sigma^2}{E_\sigma}.
}
\]

The within-spin radial gate therefore has its own exact Riccati viscous damping.

## 4. Finite lifetime action of the critical radial gate

Since

\[
\mathcal R_{\rm rad}
\le E_+Z_++E_-Z_-
\le(E_++E_-)(Z_++Z_-)
=EZ,
\]

and

\[
(E^2)'=-4\nu EZ,
\]

we obtain

\[
\boxed{
\int_0^T\mathcal R_{\rm rad}(t)\,dt
\le\frac{E(0)^2}{4\nu}.
}
\]

Thus within-spin critical spectral width, like the two-spin and global nonplanarity defects, has a finite total lifetime budget.

## 5. Dimensionless radial gate fraction

When `EZ>0`, define

\[
\boxed{
\mathfrak r
:=\frac{\mathcal R_{\rm rad}}{EZ}
\in[0,1].
}
\]

This measures how much of the available energy-enstrophy product is stored in radial variance *inside* the two helicity sectors rather than in their monochromatic cores.

Combining with

\[
\mathfrak b
=\frac{\mathcal B}{K^2},
\qquad
\mathfrak V
=\frac{27\det\mathsf A}{K^3},
\]

gives the dimensionless three-gate geometry factor

\[
\boxed{
\mathfrak G
:=\mathfrak r^{1/2}
\mathfrak b^{1/2}
\mathfrak V^{1/3}
\in[0,1].
}
\]

Its three zeros have distinct meanings:

- `r=0`: no within-spin radial handoff is available, so `kappa=0`;
- `b=0`: one critical spin sector is absent, so `kappa=0` instantaneously;
- `V=0`: the Fourier geometry is globally planar, the regular 2D3C endpoint on the periodic domain.

## 6. Full danger action

Multiply the joint spin-volume action from `19-joint-danger-action.md` by `sqrt(r)`:

\[
\boxed{
\mathcal J_{\rm full}
:=\mathcal J\,\mathfrak r^{1/2}
=\frac{K^2}{3}\mathfrak G.
}
\]

Because `0<=r<=1`,

\[
0\le\mathcal J_{\rm full}
\le\mathcal J
\le\frac{K^2}{3}.
\]

Hence

\[
\boxed{
\int_0^T\mathcal J_{\rm full}(t)\,dt
\le\frac{E(0)^2}{12\nu}.
}
\]

This scalar is not claimed to be monotone, and its full derivative is not yet a closed expression because the normalized radial factor has its own nonlinear source. Its role is to identify, in one finite-action quantity, the three structural gates that a genuinely three-dimensional critical escape must keep open simultaneously.
