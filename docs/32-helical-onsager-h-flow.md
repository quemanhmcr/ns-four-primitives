# Helical Onsager H-Flow: an Auxiliary Curvature Flow on a Triad Network

**Claim level:** finite-dimensional theorem. This is an auxiliary flow built from the exact helical transfer geometry. It is **not** asserted to be the Navier-Stokes time evolution or the historical MRC closure equation.

The purpose of this note is to isolate the part of the Markovian/H-theorem physics that can be made exact without any statistical approximation.

## 1. Finite helical transfer network

Let the modal labels be `i=1,...,N`. Each mode has signed frequency

\[
h_i=\sigma_i |k_i|.
\]

For every oriented nondegenerate helical triad `tau=(i,j,k)`, define the transfer vector

\[
\lambda^\tau_i=h_j-h_k,
\qquad
\lambda^\tau_j=h_k-h_i,
\qquad
\lambda^\tau_k=h_i-h_j,
\]

with all other entries zero. Then

\[
\lambda^\tau\cdot \mathbf 1=0,
\qquad
\lambda^\tau\cdot h=0.
\]

Let `A` be the matrix whose rows are the vectors `(lambda^tau)^T`, and let

\[
W=\operatorname{diag}(w_\tau),
\qquad w_\tau>0.
\]

The weights are arbitrary positive mobilities. In applications they may be chosen from exact helical geometric coefficients and a normalized triad time, but none of the theorems below requires such a choice.

Define the positive semidefinite network operator

\[
\boxed{L:=A^T W A.}
\]

Every vector `phi in ker A` is a diagonal quadratic invariant weight for this triad network. In particular

\[
\mathbf 1,h\in\ker A.
\]

Importantly, `ker A` can be larger than `span{1,h}` on sparse or tree-like subnetworks. The flow below automatically respects that topology; no false global invariant classification is assumed.

## 2. The H-flow

Let

\[
C=(C_1,\ldots,C_N)\in(0,\infty)^N
\]

be positive modal second moments and write componentwise

\[
q_i:=C_i^{-1}.
\]

Define the artificial flow time `s` by

\[
\boxed{
\partial_s C=Lq=A^TWA(C^{-1}).
}
\]

Equivalently, define the triad H-current

\[
\boxed{
J_H:=WAq,
}
\]

so that

\[
\partial_s C=A^T J_H.
\]

This is the simplest Onsager gradient flow whose mobility is the exact triad-transfer Laplacian.

## 3. Exact preservation of every network quadratic invariant

For any `phi in ker A`,

\[
\frac d{ds}(\phi\cdot C)
=\phi^T A^TWAq
=(A\phi)^TWAq
=0.
\]

Hence

\[
\boxed{
\phi\cdot C=\text{constant for every }\phi\in\ker A.
}
\]

In particular,

\[
\boxed{
E:=\sum_i C_i,\qquad
H:=\sum_i h_iC_i
}
\]

are preserved.

Thus the auxiliary flow respects not only energy and helicity but also every extra diagonal invariant created by sparse network topology.

## 4. H-theorem

Define

\[
\boxed{
S(C):=\sum_{i=1}^N\log C_i.
}
\]

Then

\[
\frac{dS}{ds}
=q^T\partial_s C
=q^T Lq
=(Aq)^T W(Aq).
\]

Therefore

\[
\boxed{
\frac{dS}{ds}
=\|W^{1/2}Aq\|_2^2
\ge0.
}
\]

Define the thermodynamic triad curvature

\[
\boxed{
\mathscr R_H(C)
:=\frac12 q^T Lq
=\frac12\|W^{1/2}Aq\|_2^2.
}
\]

Then

\[
\boxed{S'=2\mathscr R_H.}
\]

The zero-curvature set is

\[
\boxed{
\mathscr R_H=0
\iff Aq=0
\iff C^{-1}\in\ker A.
}
\]

This is the exact finite-network analogue of the affine inverse-covariance structure of absolute equilibrium.

## 5. Curvature itself decreases monotonically

Since

\[
q_i=C_i^{-1},
\]

we have

\[
q'_i=-q_i^2(Lq)_i.
\]

Using symmetry of `L`,

\[
\frac d{ds}\mathscr R_H
=q'^T Lq
=-\sum_i q_i^2(Lq)_i^2.
\]

Thus

\[
\boxed{
\mathscr R_H'
=-\|\operatorname{diag}(q)Lq\|_2^2
\le0.
}
\]

Consequently

\[
\boxed{S''=2\mathscr R_H'\le0.}
\]

The auxiliary flow therefore has two simultaneous monotonicities:

- entropy increases;
- thermodynamic triad curvature decreases.

This is the main reason to regard it as a serious geometric comparison flow rather than merely an equilibrium ansatz.

## 6. Exact non-collapse on a finite network

Energy conservation gives

\[
0<C_i\le E.
\]

Since `S(s)>=S(0)`,

\[
\prod_i C_i(s)
\ge e^{S(0)}.
\]

Therefore for every mode

\[
\boxed{
C_i(s)
\ge
\frac{e^{S(0)}}{E^{N-1}}.
}
\]

Hence no modal covariance can collapse to zero along the H-flow.

The vector field remains smooth on a compact subset of the positive cone, so the finite-dimensional solution exists for all artificial times `s>=0`.

This is an exact finite-network no-collapse theorem.

## 7. Canonical equilibrium and topology caveat

On the affine leaf determined by all conserved quantities `phi.C`, the entropy `S` is strictly concave. Therefore there is at most one entropy maximizer `C_*` in the positive cone. Its Euler-Lagrange condition is

\[
\boxed{C_*^{-1}\in\ker A.}
\]

The H-flow has the same stationary condition.

If the network is sufficiently cross-linked that

\[
\ker A=\operatorname{span}\{\mathbf1,h\},
\]

then necessarily

\[
\boxed{
C_{*,i}^{-1}=\alpha+\beta h_i,
}
\]

which is the finite helical Kraichnan form.

If `ker A` is larger, the equilibrium precision is a general element of the larger invariant space. This is not a defect of the theorem: it records the extra protection of sparse networks exactly.

## 8. Convergence

The invariant leaf intersected with the positive cone is compact after the non-collapse estimate. The entropy is bounded above and monotone. Every omega-limit point has

\[
\mathscr R_H=0.
\]

Since the entropy maximizer on the fixed full-invariant leaf is unique,

\[
\boxed{
C(s)\longrightarrow C_*
\qquad(s\to\infty).
}
\]

Near equilibrium, if `L` has a positive spectral gap on `(ker A)^perp`, the linearized flow is strictly parabolic on the invariant tangent space, giving exponential local convergence.

## 9. Relation to historical statistical turbulence

Frisch-Lesieur-Brissaud's Markovian random coupling model gives an exact closed Markovian second-moment dynamics for a stochastic modification of Navier-Stokes that preserves important structural properties. Carnevale-Frisch-Salmon proved H-theorems for broad classes of second-order Markovian turbulence closures, with entropy increasing toward absolute equilibrium. Kraichnan classified the helical energy-helicity absolute equilibrium.

The present flow is not claimed to reproduce those closure coefficients. It extracts a minimal exact structure common to that physical picture:

\[
\boxed{
\text{triad transfer geometry}
+\text{positive mobility}
+\text{entropy gradient}
\Longrightarrow
\text{H-flow with curvature decay}.
}
\]

The next notes connect this auxiliary flow to the critical `V`-geometry and to the exact deterministic Euler currents.

## 10. Spectral-gap smoothing and canonical neighborhoods

Let `lambda_+(L)>0` be the smallest positive eigenvalue of `L` on `(ker A)^perp`. Since energy is fixed and every `C_i<=E`, we have `q_i=C_i^{-1}>=E^{-1}`. The exact curvature identity gives

\[
\mathscr R_H'=-\sum_i q_i^2(Lq)_i^2
\le-E^{-2}\|Lq\|_2^2.
\]

For positive semidefinite `L`,

\[
\|Lq\|_2^2\ge\lambda_+(L) q^TLq
=2\lambda_+(L)\mathscr R_H.
\]

Hence

\[
\boxed{
\mathscr R_H(s)\le\mathscr R_H(0)
\exp\!\left[-\frac{2\lambda_+(L)}{E^2}s\right].
}
\]

Also

\[
q^TLq\ge\lambda_+(L)\operatorname{dist}(q,\ker A)^2,
\]

so

\[
\boxed{
\operatorname{dist}(C^{-1},\ker A)^2
\le\frac{2\mathscr R_H}{\lambda_+(L)}.
}
\]

When `ker A=span{1,h}`, small curvature therefore forces

\[
C_i^{-1}\approx\alpha+\beta h_i.
\]

This is the finite-network canonical-neighborhood theorem for the auxiliary flow.

## 11. Relative H-free energy

Let `C_*` be the unique entropy maximizer on the full invariant leaf and define

\[
\boxed{\mathscr F_H(C):=S(C_*)-S(C)\ge0.}
\]

Exactly,

\[
\boxed{\mathscr F_H'=-2\mathscr R_H.}
\]

Using the exponential decay of `R_H`,

\[
\mathscr F_H(s)=\int_s^\infty2\mathscr R_H(\tau)\,d\tau
\le\frac{E^2}{\lambda_+(L)}\mathscr R_H(s).
\]

Therefore

\[
\boxed{
\mathscr F_H'\le-\frac{2\lambda_+(L)}{E^2}\mathscr F_H.
}
\]

The auxiliary geometry thus has the chain

\[
\boxed{
\text{no collapse}
+\text{free-energy monotonicity}
+\text{curvature decay}
+\text{canonical-neighborhood convergence}.
}
\]
