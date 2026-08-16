# Network V-Curvature and Topological Protection

The H-flow uses the same triad operator that controls critical production. This note makes that duality explicit.

## 1. The critical V-potential

For each helical mode let

\[
h_i=\sigma_i|k_i|,
\qquad
v_i:=|h_i|=|k_i|.
\]

The critical quantity is

\[
K=v\cdot C.
\]

Define the triad V-curvature vector

\[
\boxed{
c_V:=Av.
}
\]

For an arbitrary network current `J`, the Euler-type transfer

\[
\dot C=A^T J
\]

produces

\[
\boxed{
\dot K=c_V^T J.
}
\]

Thus the critical quantity changes only through the failure of the V-potential `|h|` to lie in the network invariant space.

## 2. Homochiral flatness and heterochiral kink detection

On a homochiral triad all signed frequencies have the same sign, so

\[
v=\pm h
\]

on that triad. Since `Ah=0`,

\[
\boxed{(c_V)_\tau=0.}
\]

For a heterochiral triad with signed frequencies

\[
h_i=k>0,\qquad h_j=q>0,\qquad h_k=-p<0,
\]

and transfer row

\[
\lambda=(q+p,-p-k,k-q),
\]

one obtains

\[
\boxed{
\lambda\cdot v=2p(k-q).
}
\]

This is exactly the critical handoff factor already found in the helical triad dynamics.

Therefore `A|h|` is a discrete curvature detector for the kink of `|h|` at helicity reversal.

## 3. Network-protected critical defect

Let

\[
\mathcal I_A:=\ker A
\]

be the full diagonal invariant space of the active network. For fixed positive modal weights `C_i`, define

\[
\boxed{
\mathcal Y_A(C)
:=
\min_{\phi\in\mathcal I_A}
\sum_i C_i(v_i-\phi_i)^2.
}
\]

This is the critical V-potential after quotienting **all diagonal protections actually available on the current network**, not only energy and helicity.

Then

\[
\boxed{
\mathcal Y_A=0
\iff v\in\ker A
\iff Av=0.
}
\]

Hence `Y_A=0` iff `K` is conserved by every possible current supported on that network.

## 4. Recovery of the optimal protected defect

Because

\[
\operatorname{span}\{\mathbf1,h\}\subseteq\ker A,
\]

we always have

\[
\boxed{
\mathcal Y_A
\le
\min_{a,b}\sum_i C_i(v_i-a-bh_i)^2.
}
\]

The right-hand side is precisely the optimal energy-helicity protected defect developed earlier in the repository.

If

\[
\ker A=\operatorname{span}\{\mathbf1,h\},
\]

then the two defects coincide exactly.

Thus the earlier global residual is the **fully cross-linked limit** of a more general network-protected defect.

## 5. Densification monotonicity

Suppose a network is enlarged by adding triad rows:

\[
A_1\subset A_2.
\]

Then

\[
\ker A_2\subseteq\ker A_1.
\]

Distance to the smaller subspace cannot decrease, so

\[
\boxed{
\mathcal Y_{A_2}(C)
\ge
\mathcal Y_{A_1}(C).
}
\]

This is an exact mathematical version of a central Composition principle:

\[
\boxed{
\text{cross-pair densification shrinks the invariant space and exposes more V-curvature.}
}
\]

Sparse/tree subnetworks can hide the critical V-potential inside extra local invariants. Full convolution closure progressively removes that protection.

## 6. Thermodynamic-critical duality

The H-flow equilibrium condition is

\[
\boxed{C_*^{-1}\in\ker A.}
\]

Critical protection is

\[
\boxed{v\in\ker A.}
\]

Thus **the same invariant space** controls both:

1. the thermodynamic precision functions that are zero-curvature for the H-flow;
2. the critical weights that cannot be changed by the network.

This is the precise primal-dual connection between Kraichnan/H-theorem physics and the protected V-geometry.

## 7. H-flow critical-speed inequality

Along the H-flow,

\[
\partial_s C=A^TWAq,
\qquad q=C^{-1}.
\]

Therefore

\[
\frac{dK}{ds}
=(Av)^T W(Aq).
\]

Define the static network V-curvature energy

\[
\boxed{
\mathscr R_V
:=\frac12(Av)^T W(Av).
}
\]

Since

\[
S'=(Aq)^T W(Aq)=2\mathscr R_H,
\]

Cauchy-Schwarz gives

\[
\boxed{
\left|\frac{dK}{ds}\right|^2
\le
4\mathscr R_V\mathscr R_H.
}
\]

Hence the auxiliary flow can move the critical quantity only by pairing

- geometric V-curvature of the network, and
- thermodynamic curvature of the covariance state.

As the H-flow canonicalizes `C`, `R_H -> 0`, and its motion of `K` freezes.

## 8. Why this changes the Composition picture

The old sparse/dense story can now be stated algebraically:

- sparse network: `ker A` is large, so critical weight may enjoy extra local protection;
- cross-pair closure adds rows to `A`;
- the invariant space shrinks;
- the network-protected V-defect grows monotonically;
- on a fully rigid network, only the energy-helicity affine plane remains.

Thus additive densification is not merely a source of more interactions. It performs a **monotone loss of hidden protection**.
