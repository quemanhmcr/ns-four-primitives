# Research Status

**Date:** 2026-08-16

**Claim level:** structural research program; no global-regularity proof is claimed.

## Established / audited in this repository

- Rotational/Leray form of the incompressible Navier–Stokes nonlinearity.
- Energy and helicity tangency of the Euler forcing.
- Exact helical pair coefficient for `a+b=r`.
- Exact same-spin coefficient magnitude
  \[
  |C^{t,s,s}|=(2\sqrt2)^{-1}\Delta A(\rho\alpha\beta)^{-1}(S+ts\rho).
  \]
- Exact same-wavevector spin-shadow ratio
  \[
  |C_P^s|/|C_P^{-s}|=(S+p)/(S-p)\ge1.
  \]
- Numerical audit script reproducing these identities on random nondegenerate triads.
- Exact Leakage / Composition-Defect Lemma:
  \[
  \mathcal L+\mathfrak D_{\rm comp}\ge\kappa_{\mathcal T}^2/(4\mathcal W_{\mathcal T}).
  \]
- Exact parabolic transversality identity for two-pair cancellation; zero viscous curvature occurs exactly on rectangular additive diamonds.
- Exact pair-heat observability theorem: persistent cancellation under pure viscosity splits class-by-class by equal pair heat rate; the unobservable classes are midpoint spheres.
- Exact Plane-Turning Bridge Lemma: two consecutive nondegenerate same-spin handoff planes turning by `delta` force the cross-generation coefficient
  \\[
  |C_{\rm bridge}|\ge (r-k)\sin\theta_1\sin\theta_2|\sin\delta|/\sqrt2.
  \\]
- Exact critical-amplitude shortcut identity: for a same-spin backbone with `a_j=sqrt(k_j)|z_j|`, adjacent products `pi_j=a_j a_{j+1}` and two-step products `beta_j=a_j a_{j+2}` satisfy `beta_j beta_{j+1}=pi_j pi_{j+2}`; uniformly strong adjacent products therefore forbid two consecutive weak two-step shortcuts.
- Exact Resonant Diamond Cross-Closure Lemma: two equal-heat same-spin decompositions of one output with nonzero radial defect and different pair planes necessarily generate a quantitative same-spin cross-output coefficient; the equal-rate sphere is therefore not closed under plane-dispersed cancellation.
- Zero-Defect Active-Frame Rigidity: on a connected nondegenerate finite handoff graph, vanishing normalized bridge/cross-closure obstructions force every handoff plane to equal one global plane; with edge defects `<= epsilon` and graph diameter `D`, all planes lie within `D arcsin(epsilon)` of a root plane.
- Strong-Handoff Path Compactness: in a scale-normalized local packet with critical mass `M`, a path whose adjacent critical parent products are all at least `P` has length at most `M/P`; a handoff carrying normalized production `>= kappa_0` has `P >= kappa_0/(C sqrt(M))`.
- Global critical planarity tensor
  \\[
  \mathsf A(u)=\sum_{k\ne0}\frac{k\otimes k}{|k|}|\widehat u(k)|^2,
  \qquad \mathcal P=\lambda_{\min}(\mathsf A)
  =\min_{|n|=1}\|\partial_nu\|_{\dot H^{-1/2}}^2,
  \\]
  with exact zero set equal to the fixed Fourier-plane (`2D3C`) class, modulated evolution, commutator collapse, and torus Riccati damping `D^+ P <= 2 Gamma_n-2 nu P^2/E`.
- Exact planarity-volume determinant identity
  \\[
  \det\mathsf A=\sum_{i<j<\ell}m_im_jm_\ell[\widehat k_i\cdot(\widehat k_j\times\widehat k_\ell)]^2,
  \\]
  plus viscous damping `tr(cof(A) H) >= (K/E) det(A)` and cofactor-weighted commutator collapse of the Euler volume source.
- Quantitative two-rate parabolic observability/control inequality on one scale-invariant parabolic window.
- Exact resonant-sphere selection factor for same-spin inputs, including the `|sin 2 theta|` angular gate.
- Exact complex Spin-Shadow law with double-angle pair-plane phase twist.
- Exact phase-plane tradeoff and projective plane-order tensor identity.
- Fixed Fourier-plane (`2D3C`) endpoint reduction.
- Exact two-spin self-balancing law `B=K^2-H^2=4K_+K_-`:
  \\[
  \mathcal B'=4K\kappa-2\nu(\Omega_+^2+\Omega_-^2)\mathcal B.
  \\]
- Joint spin-volume danger action `J=sqrt(B)(det A)^(1/3)`, with `0<=J<=K^2/3`, finite lifetime action, and exact combined source/parabolic-damping balance.
- Exact within-spin radial gate `R_rad=sum_sigma(E_sigma Z_sigma-K_sigma^2)`: `R_rad=0` forces `kappa=0`; each sector width has exact balance `W_sigma'=2 Gamma_sigma-2 nu H_sigma` and Riccati damping, while `int R_rad dt <= E(0)^2/(4 nu)`.
- Full three-gate geometry factor `G=sqrt(r_rad) sqrt(b_spin) V^(1/3)` and finite-action scalar `J_full=(K^2/3)G`, vanishing on the radial, pure-spin, or planar safe/depleted boundaries.
- Conceptual separation between pair forcing and modal energy transfer.

## Structural reductions currently used

- Dangerous critical transfer requires radial mismatch inside a helicity sector.
- Opposite-spin participation is required for heterochiral critical production.
- A sparse same-spin handoff necessarily creates an off-channel same-spin shadow at the catalyst wavevector.
- Avoiding actual shadow leakage requires cancellation by additional convolution pairs, hence additive structure in the active Fourier set.

## Open targets

1. **Flux fragmentation / active-frame compactness.** In a bounded-mass normalized local packet carrying fixed positive critical production, show that fragmentation among many weak handoffs either yields a bounded effective active frame carrying a fixed flux fraction or forces quantitatively large additive/composition structure.
2. **Many-rate dense-cancellation control.** Extend the two-rate parabolic estimate to rate clusters and control the aggregate nonlinear compensation terms without losing critical scaling.
3. **Global planarity-volume production.** Control the positive Euler sources of `P` or `det A` using the exact helical/composition structure, or use a minimal-counterexample compactness argument to force a zero-defect planar critical profile.
4. **PDE closure.** Connect the resulting global rigidity to a standard continuation / minimal-singularity argument for smooth 3D Navier-Stokes solutions.

## Explicit non-claims

- A single helical triad does not model the full nonlinear network.
- Large pair forcing does not by itself imply large instantaneous modal energy transfer.
- High additive energy does not by itself imply regularity.
- Phase frustration is currently a research target, not a theorem.
