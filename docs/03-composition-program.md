# Composition Program: From Sparse Leakage to Dense Rigidity

The fourth primitive, Composition, is where the regularity problem remains open.

## 1. Sparse branch

Suppose a positive critical event is carried by a sparse family of same-spin handoffs.

Each selected handoff creates a same-wavevector spin shadow. If output multiplicities stay uniformly small, cancellation capacity is limited and one expects a quantitative lower bound on actual off-skeleton forcing.

The desired theorem is a weighted form of

\[
\text{positive critical flux}
\Longrightarrow
\text{shadow leakage}
\quad\text{or}\quad
\text{large additive multiplicity}.
\]

This statement must be scale invariant and must use amplitudes and exact helical coefficients, not support cardinality alone.

## 2. Additive-energy branch

For an active Fourier set `A`, the unweighted additive energy is

\[
E_{\rm add}(A)
=
\#\{a+b=c+d:\ a,b,c,d\in A\}.
\]

The PDE problem requires a weighted analogue incorporating

- modal amplitudes,
- helicity labels,
- exact coefficient magnitudes,
- localization to a critical shell or adjacent shells.

High weighted additive energy means the convolution graph contains many diamonds/parallelograms and therefore many shared phase constraints.

## 3. Dense cancellation and Pexider structure

At a fixed output `r`, cancellation of many large pair contributions requires

\[
\sum_{a+b=r}
C_{r;a,b}^{t,s_a,s_b}
 z_{s_a}(a)z_{s_b}(b)
\approx0.
\]

Writing `z_s(k)=A_s(k)e^{i\phi_s(k)}`, coherent cancellation imposes relations among

\[
\phi_{s_a}(a)+\phi_{s_b}(b)+\arg C_{r;a,b}^{t,s_a,s_b}.
\]

Ignoring the coefficient phase for one moment gives the Pexider skeleton

\[
f(a)+g(b)\approx h(a+b).
\]

On a dense additive set, approximate Pexider relations tend to force low-complexity phase structure. The exact Navier–Stokes problem includes a nontrivial coefficient phase that may obstruct such a global phase assignment.

## 4. Phase curvature on additive loops

A parallelogram

\[
a+b=c+d
\]

creates a discrete loop. The gauge-invariant object to investigate is not an individual coefficient phase but a loop combination in which helical-basis gauge choices cancel.

Schematic target:

\[
\mathfrak C_{\square}
=
\arg C_1+\arg C_2-\arg C_3-\arg C_4.
\]

If dangerous forward transfer requires incompatible loop phases on a sufficiently dense network, then local optimal transfers cannot be globally composed.

This is currently a **research target**, not an established theorem.

## 5. Desired endgame

A possible closure would have three steps.

### Lemma A — Spin Shadow

Already exact at the pair-coefficient level:

\[
|C_{\rm shadow}|\ge|C_{\rm catalyst}|.
\]

### Lemma B — Leakage / Composition-Defect Dichotomy — proved

The exact result in `05-leakage-composition-defect.md` is

\[
\boxed{\mathcal L+\mathfrak D_{\rm comp}
\ge \kappa_{\mathcal T}^2/(4\mathcal W_{\mathcal T})}.
\]

Thus quantified positive critical production forces either actual shadow leakage or a positive gauge-invariant cancellation defect supported on additive collisions.

### Lemma B2 — Parabolic transversality — proved

For two cancelling pair contributions on `a+b=c+d`, viscosity is transverse to the cancellation manifold by

\[
\mathcal Q_\square=|a|^2+|b|^2-|c|^2-|d|^2.
\]

The zero-curvature exceptional set consists exactly of rectangular additive diamonds. See `06-parabolic-diamond-curvature.md`.


### Lemma B3 — Pair-heat observability — proved

At a fixed output, pair products carry viscous rates `lambda_ab=|a|^2+|b|^2`. Persistent cancellation under pure viscosity is possible only after cancellation is resolved separately inside each equal-rate class. For `a+b=r`, these classes are spheres centered at `r/2`. See `07-pair-heat-observability.md`.

### Lemma B4 — Two-rate parabolic control cost — proved

For two heat-rate class resultants separated by `delta N^2`, hidden cancellation over a parabolic window `T=c/(nu N^2)` forces either observed forcing action or nonlinear control action with constants independent of `N`. See `10-two-rate-control-cost.md`.

### Lemma C1 — Complex Spin-Shadow plane rigidity — proved

For same-spin pairs sharing one output, the full complex ratio is

\[
C_{\rm sh}/C_{\rm cat}=((S+\rho)/(S-\rho))e^{-2is\phi}.
\]

Thus catalyst coherence plus small shadow composition forces concentration of pair-plane orientations; the coordinate-free defect is measured by a projective plane-order tensor. See `08-complex-spin-shadow.md`.

### Lemma C1b — Plane-Turning Bridge — proved

For consecutive same-spin backbone modes `K,Q,R`, a projective turn `delta` between the two handoff planes forces the cross-generation pair `R,-K` to have

\[
|C_{\rm bridge}|
\ge
\frac{r-k}{\sqrt2}
\sin\theta_1\sin\theta_2|\sin\delta|.
\]

Thus definite turning of two nondegenerate local handoffs creates an order-frequency shortcut coupling. Avoiding actual bridge leakage requires applying the same full-output composition machinery at the bridge output.

### Lemma C1c — Critical shortcut density — proved

For critical modal amplitudes `a_j=sqrt(k_j)|z_j|`, adjacent products `pi_j=a_j a_{j+1}` and skip-one products `beta_j=a_j a_{j+2}` obey

\[
\beta_j\beta_{j+1}=\pi_j\pi_{j+2}.
\]

Hence a backbone with `pi_j >= P` cannot have two consecutive skip-one products below `P`. Combined with the Plane-Turning Bridge Lemma, two consecutive definite plane turns cannot both be hidden by amplitude zig-zag. The remaining structured loophole is isolated weak-turn shortcuts and their coarse-grained propagation.

### Lemma C1d — Resonant diamond cross-closure — proved

Inside one equal-heat midpoint sphere, two same-spin decompositions with different pair planes force a quantitative cross-output same-spin coefficient unless the original radial/angular Selection factors degenerate. Thus heat resonance plus plane dispersion cannot remain closed at one output; avoiding leakage requires further convolution closure.

### Lemma C1e — Active-frame planar rigidity — proved at finite-frame level

Package sequential and resonant-cancellation handoffs into a projective plane graph. The normalized bridge/cross-closure coefficients control the sine of the projective angle on every graph edge. Therefore zero defect on a connected finite frame forces one exact global plane; if every edge defect is at most `epsilon` and graph diameter is `D`, all planes lie within `D arcsin(epsilon)` of a root plane.

The remaining issue is critical active-frame compactness: rule out escape through graph diameter tending to infinity while local edge defects tend to zero.

### Lemma C1f — Strong-path compactness — proved

Inside a normalized local frequency window with total critical mass `M`, any handoff carrying fixed normalized production has a critical parent product bounded below by `kappa_0/(C sqrt(M))`. A path with adjacent critical products `>= P` has length at most `M/P`. Hence unbounded active-frame diameter cannot be carried by uniformly strong handoffs at bounded local critical mass; the remaining compactness branch is flux fragmentation among many weak handoffs.

### Lemma C1g — Global planarity tensor and volume determinant — proved

The local plane geometry is carried globally by

\[
\mathsf A=\sum_k |k||z(k)|^2\,\widehat k\otimes\widehat k.
\]

Its minimum eigenvalue is `min_n ||partial_n u||_{H^{-1/2}}^2` and vanishes exactly on fixed Fourier-plane states. Its determinant is the Cauchy-Binet sum of weighted squared 3D volumes of all Fourier triples. Both quantities have exact viscous damping and commutator-form Euler production; see `16-global-planarity-defect.md` and `17-planarity-volume-determinant.md`.

### Lemma C1h — Two-spin and joint danger balances — proved

The global unsigned two-spin defect `B=K^2-H^2=4K_+K_-` satisfies

\[
\mathcal B'=4K\kappa-2\nu(\Omega_+^2+\Omega_-^2)\mathcal B.
\]

Combining it with the planarity determinant gives `J=sqrt(B)(det A)^(1/3)`, a finite-action scalar vanishing on either the pure-spin or planar boundary and damped at the sum of the two spin and volume parabolic frequencies. See `18-two-spin-self-balancing.md` and `19-joint-danger-action.md`.

### Lemma C1i — Within-spin radial gate — proved

For each helicity sector, center the radial spectrum at `m_sigma=K_sigma/E_sigma`. The scale-critical defect

\[
\mathcal R_{\rm rad}=\sum_\sigma(E_\sigma Z_\sigma-K_\sigma^2)
\]

vanishes only when both sectors are individually monochromatic; in that case the exact energy/helicity collapse forces `kappa=0`. The widths satisfy exact viscous Riccati balances. Combining this radial gate with the spin and planarity factors gives a finite-action three-gate geometry variable. See `20-within-spin-radial-gate.md`.

### Lemma C1j — Optimal protected escape defect — proved

Project `Lambda u` orthogonally away from the two Euler-conservation directions `u,omega`: `r=Lambda u-a u-b omega`. Then `kappa=<r,F>` exactly. The critical defect `X=E||r||_2^2` has finite action and exact Riccati/linear viscous damping, while

\[
|\nu_E|\le C_*\sqrt{K\chi_{\rm esc}},
\qquad
\chi_{\rm esc}=\|r\|_2^2/Z.
\]

Thus `K'>0` forces `X>(nu^2/C_*^2)K`. The residual is a Gram-determinant quotient and its zero set unifies pure-spin and within-spin monochromatic protection. See `21-optimal-protected-escape-defect.md`.

### Lemma C1k — Optimal-defect triad source factorization — proved

Freeze the globally minimizing protected multiplier `T=Lambda-a-b curl`. On one helical triad the quadratic defect weight is `q_sigma(k)=((1-b sigma)k-a)^2`. Homochiral Euler production factors into a full radial Vandermonde, while a heterochiral same-spin handoff has

\[
\dot{\mathcal Y}_\triangle=(k-q)J\,\mathfrak B_{a,b}(k,q,p),
\]

so it uses exactly the same radial transfer current as `dot K_triangle`. The coefficient is the failure of the opposite-spin defect weight to lie on the affine secant through the two same-spin endpoint weights. See `22-optimal-defect-triad-source.md`.

### Lemma C2 — Global source / fragmentation rigidity — open

The remaining obstruction is no longer an unidentified geometric channel. It is the global summation/compactness problem for two exact sources:

1. reopening of the optimal protected defect `X`, whose triad source has already been factored into the same heterochiral currents that produce `K`;
2. regeneration of global nonplanarity (`P` or `det A`) against exact parabolic-frequency damping.

If positive flux fragments among many weak handoffs instead of forming a strong finite path, that fragmentation must be converted into weighted additive/composition structure with scale-uniform constants. A clean closure may then proceed either by a direct source inequality or by a periodic blow-up compactness argument forcing a limiting protected/planar profile.
