# Global Transfer-Moment Form of Critical and Defect Production

The optimal-defect source admits a simple global interpretation which is useful for ruling out false sign arguments. At a frozen time, the Euler transfer defines a signed measure on helical Fourier modes. Critical production is its first moment in the protected coordinate; defect regeneration is its second moment.

## 1. Modal Euler transfer rates

For each nonzero Fourier mode and helicity label `i=(k,sigma)`, write

\[
\widehat u_i=z_i h_i,
\qquad
\widehat F_i=F_i h_i,
\]

and define the Euler modal energy-transfer rate

\[
\boxed{
\tau_i:=2\operatorname{Re}(\overline{z_i}F_i).
}
\]

Energy and helicity conservation give

\[
\boxed{
\sum_i\tau_i=0,
\qquad
\sum_i h_i\tau_i=0,
}
\]

where

\[
h_i=\sigma_i|k_i|.
\]

The Euler contribution to the critical derivative is

\[
\sum_i |k_i|\tau_i=2\kappa.
\]

## 2. Protected coordinate

Freeze the globally minimizing coefficients `a,b` and define

\[
\boxed{
t_i:=|k_i|-a-bh_i.
}
\]

Because constants and signed frequency have zero transfer moment,

\[
\sum_i t_i\tau_i
=
\sum_i|k_i|\tau_i.
\]

Hence

\[
\boxed{
2\kappa=\sum_i t_i\tau_i.
}
\]

The optimal quadratic defect has weight `t_i^2`. Its Euler derivative is therefore

\[
\boxed{
2\Gamma_{\rm esc}
=\sum_i t_i^2\tau_i.
}
\]

Thus `(kappa,Gamma_esc)` are exactly the first two moments of the same signed transfer distribution in the optimally protected coordinate `t`.

## 3. Centering freedom

For every scalar `c`,

\[
\boxed{
2(\Gamma_{\rm esc}-c\kappa)
=\sum_i t_i(t_i-c)\tau_i.
}
\]

This identity is useful when a dangerous family is localized in a narrow interval of protected coordinates: one may center the quadratic weight around that interval without altering any conservation law.

It also explains why no universal sign relation between `Gamma_esc` and `kappa` should be expected. The transfer measure `tau` is signed. A positive first moment does not force a positive or negative second moment.

## 4. Triad compatibility

On one helical triad the transfer vector is one dimensional. Substituting the triad current into the two global moment formulas reproduces exactly the factorization in `22-optimal-defect-triad-source.md`:

- homochiral second-moment production carries the radial Vandermonde;
- heterochiral second-moment production is proportional to the same radial current as the first moment.

The global moment form therefore does not replace the helical coefficient analysis. It shows what that analysis must control after summing over the full convolution network.

## 5. Source-rigidity formulation

The ledger theorem reduces finite-time escape to

\[
\int E(\Gamma_{\rm esc})_+dt=\infty.
\]

The transfer-moment representation says that this can happen only if the full signed Euler transfer repeatedly creates a large positive second moment in `t`, despite

\[
\sum\tau=0,
\qquad
\sum h\tau=0,
\]

and despite the Spin-Shadow / Composition constraints on the same triad currents.

The remaining theorem should therefore be phrased as a **signed moment rigidity theorem for the exact convolution network**, not as a generic bound on a new cubic expression.
