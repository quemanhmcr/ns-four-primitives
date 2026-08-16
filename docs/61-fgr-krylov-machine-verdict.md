# FGR–Krylov Machine Verdict

**Claim level:** synthesis of exact operator theorems and numerical gate tests on the experiment branch. No Navier–Stokes regularity theorem is claimed.

## 1. What has been eliminated as an independent obstruction

The passive-bath program began with three apparent difficulties:

1. strong RG coupling `c -> infinity`;
2. temporal resonance inside the protected sector;
3. coherent repeated bath recirculation.

The first two are now resolved at the frozen operator level.

### Strong coupling

With `epsilon=1/c`,

\[
\varepsilon^{-1}\Sigma_\varepsilon
=G^*(\varepsilon^2I-C^2)^{-1}G,
\]

and the right side is monotone increasing as `epsilon` decreases. Strong coupling cannot weaken the renormalized FGR response.

### Temporal resonance

At every real temporal frequency,

\[
\varepsilon^{-1}\Sigma_\varepsilon(\omega)
=G^*(\varepsilon^2I-C_\omega^2)^{-1}G,
\]

with

\[
\ker\Sigma_\varepsilon(\omega)=\ker B.
\]

Protected self-oscillation cannot create a new exact dark state by frequency tuning.

## 2. Exact dark branch for the actual reset state

At a protected reset,

\[
Bu=QF,
\qquad
TF=T_QBu.
\]

Hence

\[
\mathcal R_\varepsilon(u)=0
\iff
TF=0
\iff
\mathcal Y''=0.
\]

The already proved Protected Reset Trichotomy then implies

\[
\boxed{
\text{FGR-dark actual reset}
\Longrightarrow
\text{positive opening Composition defect}
\quad\text{or}\quad
F=0.
}
\]

The zero-Composition endpoint is the exact heat-decay solution already classified in the repository.

Thus the exact zero set of the FGR machine does not introduce a new uncontrolled singular geometry.

## 3. The remaining coherent branch is spectral circulation

For a non-dark protected direction,

\[
\mathcal R_\varepsilon(v)
\ge
\frac{\|Gv\|^2}
{\varepsilon^2+\Omega_{\rm bath}^2(v)}.
\]

Weak passive response therefore forces large bath circulation frequency. This is not an arbitrary signed source; it is a positive spectral moment of the self-adjoint viscously whitened bath operator.

## 4. Chiral Krylov reduction

Reality gives the antiunitary symmetry

\[
JHJ=-H.
\]

For physical coupling vectors the Lanczos chain has

\[
a_n=0
\]

at every level. Therefore the entire bath response is encoded by

\[
\boxed{b_1,b_2,b_3,\ldots\ge0.}
\]

The FGR response is the boundary Green function of this exact chiral Jacobi chain.

The old coherent-network problem has therefore been transformed into a one-dimensional spectral-recursion problem.

## 5. Numerical branch separation

The existing no-output-cutoff large-shell tests show two distinct hopping patterns.

Dense protected states:

\[
b_2/b_1\approx2.8,3.9,4.4,4.6
\]

for shell ratios `10,20,40,80`, while the depth-two gap remains order one in the audited normalization.

A sparse genuinely three-dimensional family instead has

\[
b_2/b_1\approx0.44
\]

while its global planarity defect tends toward zero.

This is not yet a theorem, but it gives a concrete scalar signature for the dense/sparse split that previously required a large Fourier interaction graph.

## 6. The new blind spot

The blind spot is no longer

\[
\Gamma_{\rm esc}
\]

as an arbitrary cubic source.

It is no longer strong coupling.

It is no longer temporal resonance.

It is now:

\[
\boxed{
\text{Can a genuinely three-dimensional, non-safe protected sequence
sustain a Krylov hopping profile }
(b_1,b_2,\ldots)
\text{ whose boundary Green function remains too small?}
}
\]

This is a spectral-recursion rigidity problem.

## 7. Next theorem target

A plausible closing theorem is a **Krylov/Composition alternative**.

For normalized protected states carrying a fixed amount of dangerous cross-spin pair mass, prove that either

\[
\boxed{
\mathcal R_\varepsilon(u)
\ge c_0\,\mathcal M_{\rm twin}
}
\]

after the theta-clock normalization, or the hopping profile enters a structured regime that forces

\[
\boxed{
\mathscr F_{\rm comp}
+\mathscr F_{\rm plane}
\ge c_1\,\mathcal M_{\rm twin}.
}
\]

The first branch is passive-bath decay. The second is deterministic Composition/planarity rigidity. The exact dark zero-cost state is already the heat endpoint.

A more local version suggested by the first two hopping audits is

\[
\boxed{
 b_2\gtrsim b_1
\quad\text{or}\quad
\mathscr F_{\rm comp}+\mathscr F_{\rm plane}
\gtrsim \mathcal M_{\rm twin}.
}
\]

This formulation must be proved or falsified. The observed dense/sparse split makes it a natural first target, but no universal two-hop theorem is claimed yet.

## 8. Why this machine is worth keeping

The FGR–Krylov machine has survived the following falsification tests:

- no artificial mobility is introduced;
- actual Euler coupling and actual viscosity define the bath;
- strong-coupling renormalization is exact and monotone;
- moving protected frames preserve passivity by Kato transport;
- temporal frequency tuning cannot create exact darkness;
- heat-line safe states remain dark;
- leaving the heat-line opens FGR damping quadratically in the audited perturbation;
- full-convolution outputs are essential and remove false cutoff nullspaces;
- coherent bath complexity is compressed into positive scalar hoppings.

The remaining question is sufficiently sharp that this representation can now be judged by a real theorem rather than by further analogy.
