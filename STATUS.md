# Research Status

**Date:** 2026-08-16

**Claim level:** structural research program; no global-regularity proof is claimed.

## Established / audited in this repository

- Finite-network Helical Onsager H-flow: for triad-transfer matrix `A`, positive mobility `W`, covariance `C>0`, and `L=A^TWA`, the auxiliary flow `partial_s C=L(C^{-1})` preserves every diagonal network invariant, satisfies `S'=||W^(1/2)A C^{-1}||^2>=0`, and has decreasing thermodynamic curvature `R_H'= -||diag(C^{-1})L(C^{-1})||^2<=0`; entropy monotonicity plus fixed energy gives exact finite-network no-collapse. Stationary states satisfy `C^{-1} in ker A`; if `ker A=span{1,h}`, then `C_i^{-1}=alpha+beta h_i`.
- Network V-curvature/protection duality: with `v_i=|h_i|`, `c_V=Av` is the discrete kink curvature; homochiral rows annihilate `v`, while a `(+,+,-)` row gives exactly `lambda.v=2p(k-q)`. The covariance-weighted distance of `v` to `ker A` is the network-protected critical defect, and it is monotone nondecreasing when convolution rows are added.
- Exact deterministic/H-current split: for exact Euler current `J_E`, define `J_H=WA(n^{-1})`, `J_coh=J_E-J_H`. Then `dot n_E=L(n^{-1})+A^T J_coh` identically, and the coherence action `C_H=J_coh^T W^{-1}J_coh` gives `dot S_E >= D_H-sqrt(D_H C_H)`. Failure of the H-theorem direction therefore requires a coherence current comparable to the H-current in the natural current metric.
- Full periodic Galerkin diagonal-invariant theorem: for every spherical cutoff containing `|k|^2<=2`, the full noncollinear two-helicity convolution network satisfies `ker A=span{1,h}`. The proof uses a local six-mode Walsh-affine lemma plus connectivity of the geometric lattice-triad graph; one shared geometric wavevector propagates both affine coefficients because it carries the two signed points `+|k|,-|k|`.
- Clock-optimized H-projection: after minimizing over the artificial H-flow clock, the exact Euler current decomposes orthogonally as `J_E=gamma_* J_H+J_perp`, with `gamma_*=(dot S_E)_+/D_H`. The residual action is the time-scale-independent coherence measure; on the positive branch its fraction equals `sin^2 Theta_H` in the `W^{-1}` current metric.
- Normalized geometric H-flow gap audit: with `h/N` and `w_tau=|g_tau|^2`, the clock-invariant ratio `eta=lambda_+/lambda_max` was audited on full Galerkin balls through `|k|^2<=9` and remained between about `0.125` and `0.258`. This supports, but does not prove, a uniform H-expansion theorem.
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
  \[
  |C_{\rm bridge}|\ge (r-k)\sin\theta_1\sin\theta_2|\sin\delta|/\sqrt2.
  \]
- Exact critical-amplitude shortcut identity: for a same-spin backbone with `a_j=sqrt(k_j)|z_j|`, adjacent products `pi_j=a_j a_{j+1}` and two-step products `beta_j=a_j a_{j+2}` satisfy `beta_j beta_{j+1}=pi_j pi_{j+2}`; uniformly strong adjacent products therefore forbid two consecutive weak two-step shortcuts.
- Exact Resonant Diamond Cross-Closure Lemma: two equal-heat same-spin decompositions of one output with nonzero radial defect and different pair planes necessarily generate a quantitative same-spin cross-output coefficient; the equal-rate sphere is therefore not closed under plane-dispersed cancellation.
- Zero-Defect Active-Frame Rigidity: on a connected nondegenerate finite handoff graph, vanishing normalized bridge/cross-closure obstructions force every handoff plane to equal one global plane; with edge defects `<= epsilon` and graph diameter `D`, all planes lie within `D arcsin(epsilon)` of a root plane.
- Strong-Handoff Path Compactness: in a scale-normalized local packet with critical mass `M`, a path whose adjacent critical parent products are all at least `P` has length at most `M/P`; a handoff carrying normalized production `>= kappa_0` has `P >= kappa_0/(C sqrt(M))`.
- Global critical planarity tensor
  \[
  \mathsf A(u)=\sum_{k\ne0}\frac{k\otimes k}{|k|}|\widehat u(k)|^2,
  \qquad \mathcal P=\lambda_{\min}(\mathsf A)
  =\min_{|n|=1}\|\partial_nu\|_{\dot H^{-1/2}}^2,
  \]
  with exact zero set equal to the fixed Fourier-plane (`2D3C`) class, modulated evolution, commutator collapse, and torus Riccati damping `D^+ P <= 2 Gamma_n-2 nu P^2/E`.
- Exact planarity-volume determinant identity
  \[
  \det\mathsf A=\sum_{i<j<\ell}m_im_jm_\ell[\widehat k_i\cdot(\widehat k_j\times\widehat k_\ell)]^2,
  \]
  plus viscous damping `tr(cof(A) H) >= (K/E) det(A)` and cofactor-weighted commutator collapse of the Euler volume source.
- Quantitative two-rate parabolic observability/control inequality on one scale-invariant parabolic window.
- Exact resonant-sphere selection factor for same-spin inputs, including the `|sin 2 theta|` angular gate.
- Exact complex Spin-Shadow law with double-angle pair-plane phase twist.
- Exact phase-plane tradeoff and projective plane-order tensor identity.
- Fixed Fourier-plane (`2D3C`) endpoint reduction.
- Exact two-spin self-balancing law `B=K^2-H^2=4K_+K_-`:
  \[
  \mathcal B'=4K\kappa-2\nu(\Omega_+^2+\Omega_-^2)\mathcal B.
  \]
- Joint spin-volume danger action `J=sqrt(B)(det A)^(1/3)`, with `0<=J<=K^2/3`, finite lifetime action, and exact combined source/parabolic-damping balance.
- Exact within-spin radial gate `R_rad=sum_sigma(E_sigma Z_sigma-K_sigma^2)`: `R_rad=0` forces `kappa=0`; each sector width has exact balance `W_sigma'=2 Gamma_sigma-2 nu H_sigma` and Riccati damping, while `int R_rad dt <= E(0)^2/(4 nu)`.
- Full three-gate geometry factor `G=sqrt(r_rad) sqrt(b_spin) V^(1/3)` and finite-action scalar `J_full=(K^2/3)G`, vanishing on the radial, pure-spin, or planar safe/depleted boundaries.
- Optimal protected escape residual `r=Lambda u-a u-b omega`, the orthogonal projection defect of the critical gradient away from the energy-helicity conservation span. It satisfies `kappa=<r,F>`, a Gram-determinant formula, exact Riccati/linear viscous damping, and the sharpened barrier
  \[
  |\nu_E|\le C_*\sqrt{K\chi_{\rm esc}},\qquad
  K'>0\Rightarrow E\|r\|_2^2>(\nu^2/C_*^2)K.
  \]
- Exact triad source factorization for the optimal defect: homochiral recharge carries a three-radial-difference Vandermonde; heterochiral recharge carries the same `(q-k)J` current as critical production, with an explicit signed-spectral secant-curvature coefficient.
- Protected-manifold acceleration: on the nondegenerate optimal-defect zero set, `a'=b'=0`, `r_t=TF`, and
  \\[
  \mathcal Y''=2\|TF\|_2^2,
  \\]
  so zero opening acceleration is exactly the two-shell convolution-closure condition `TF=0`; viscosity contributes no opening acceleration.
- General arbitrary-helicity coefficient magnitude and protected cross-spin leakage: same-spin pairs vanish pairwise on the protected shells; every noncollinear cross-spin pair creates nonzero `TF` in at least one output helicity unless the two shell radii and output radius are all equal.
- Protected output moment hierarchy: at a protected instant, `kappa'=<F,TF>` and `Y''=2||TF||^2`; these are the first and second signed moments of the actual nonlinear forcing relative to the protected shell coordinate, with `|kappa'|^2 <= ||F||^2 Y''/2`.
- Higher-order protected contact hierarchy: if `TF^(j)=0` for `j<n-1` and `TF^(n-1) != 0`, then the first nonzero defect derivative is
  \\[
  \mathcal Y^{(2n)}=\binom{2n}{n}\|TF^{(n-1)}\|_2^2>0,
  \\]
  and viscosity does not contribute to the first nonzero opening jet.
- Exact Defect-Growth Ledger: with `beta=2 nu^2/C_*^2` and `L=X+beta K`,
  \\[
  \mathscr L'\le 2E\Gamma_{\rm esc}-2\nu E\|\Lambda r\|_2^2-\nu(Z/E)\mathcal X.
  \\]
  Hence unbounded critical escape forces `integral E (Gamma_esc)_+ dt = infinity`, and equivalently infinite excess action of the defect-regeneration coefficient `nu_R=(E/Z)(Gamma_esc/Y)`.
- Exact global transfer-moment representation: if `tau_i` are helical modal Euler energy-transfer rates and `t_i=|k_i|-a-b sigma_i|k_i|`, then `2 kappa=sum_i t_i tau_i` and `2 Gamma_esc=sum_i t_i^2 tau_i`.
- Noetherian finite-contact principle on each fixed nondegenerate protected shell pair: the infinite family of reset-contact constraints `T F^(j)=0` is finitely determined in the finite polynomial ring of shell amplitudes. Thus arbitrarily high finite contact order at fixed shell geometry is impossible unless the protected branch persists locally.
- Conceptual separation between pair forcing and modal energy transfer.

- Reality-Twin Protected Leakage: for every noncollinear real cross-spin parent pair on protected shells, at least one of the twin outputs `A+B,A-B` has squared-radius distance at least `min(alpha,beta)^2` from the protected shell set, giving a quantitative lower bound on both protected multiplier symbols.
- Protected Reset Trichotomy: a nondegenerate protected state must pay either positive opening acceleration `Y''`, positive opening composition defect, or else `F=0`; the zero-cost `F=0` endpoint evolves exactly by global heat decay and is regular.
- Regression-shell structure of the optimal protected defect: `|b|<=1`, `0<=a<=2K/E`; away from the pure-spin boundary, `r_+=(1-b)(Lambda-m_+)u_+`, `r_-=(1+b)(Lambda-m_-)u_-` for positive optimal roots `m_+=a/(1-b)`, `m_-=a/(1+b)`, giving exact near-protected annular concentration.
## Structural reductions currently used

- Dangerous critical transfer requires radial mismatch inside a helicity sector.
- Opposite-spin participation is required for heterochiral critical production.
- A sparse same-spin handoff necessarily creates an off-channel same-spin shadow at the catalyst wavevector.
- Avoiding actual shadow leakage requires cancellation by additional convolution pairs, hence additive structure in the active Fourier set.

## Open targets

1. **Coherence-to-Composition bridge.** Bound the clock-optimized orthogonal current action `C_perp=||J_perp||_{W^{-1}}^2` from below by the exact Spin-Shadow / additive / phase-plane composition defects on the coherent branch. This is now the primary deterministic bridge.
2. **Uniform H-expansion theorem.** Prove or disprove `inf_N lambda_+(L_N)/lambda_max(L_N)>0` for the normalized full periodic helical Galerkin operators with geometric mobility `|g_tau|^2`. A positive theorem gives scale-uniform canonicalization; failure must expose an asymptotic near-invariant.
3. **Renormalized packet H-functional.** Construct a moving-packet relative entropy/free-energy compatible with physical viscosity and boundary flux, rather than using the cutoff-dependent raw `sum log n_i`.
4. **Thermal branch damping.** If the exact current stays close to the optimally clocked H-direction, transfer the finite-network canonicalization to a scale-local Navier-Stokes damping statement without assuming phenomenological eddy viscosity.
5. **Coherent branch rigidity.** If the orthogonal current stays large, combine its phase representation with Spin-Shadow, cross-closure, plane rigidity, protected-reset trichotomy, and the Defect-Growth Ledger to preclude infinite critical escape.
6. **Periodic blow-up compactness / PDE closure.** Once the two branches are controlled, connect the result to a continuation or periodic minimal-singularity argument.

## Explicit non-claims

- A single helical triad does not model the full nonlinear network.
- Large pair forcing does not by itself imply large instantaneous modal energy transfer.
- High additive energy does not by itself imply regularity.
- Phase frustration is currently a research target, not a theorem.
