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

### Lemma C2 — Plane propagation / plane turning — open

Show that the large-additive-energy branch cannot preserve scale-critical positive flux across infinitely many generations without a non-summable loss in phase/projective compatibility.

Lemma B, the parabolic split, and the exact pair-heat observability kernel are now established. The current research bottleneck is to control the nonlinear compensation cost between separated heat-rate classes and to prove that the locally preferred planes forced by resonant cancellation either lock into the globally regular planar endpoint or incur a quantitative plane-turning cost. A scale-invariant closure of those two branches, followed by a standard PDE continuation argument, is the current research program.
