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

### Lemma B — Leakage / Additive-Energy Dichotomy

Quantify:

\[
\text{critical escape}
\Rightarrow
\text{actual leakage}
\quad\text{or}\quad
\text{large weighted additive energy}.
\]

### Lemma C — Dense Composition Rigidity

Show that the large-additive-energy branch cannot preserve scale-critical positive flux across infinitely many generations without a non-summable loss in phase/projective compatibility.

A proof of B and C with scale-invariant constants, followed by a standard PDE continuation argument, is the current research program.
