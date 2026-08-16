# Full Periodic Galerkin Diagonal-Invariant Theorem

**Claim level:** proved finite-dimensional theorem for spherical periodic Galerkin cutoffs containing the `|k|^2<=2` shell.

This note closes the topology gap left open by the numerical rank audit.

## 1. Statement

Let

\[
\mathcal K_R
=\{k\in\mathbb Z^3\setminus\{0\}:|k|\le R\},
\qquad R^2\ge2,
\]

with the reality identification `k~-k`. Each representative has helicities `sigma=+/-` and signed frequency

\[
h_{k,\sigma}=\sigma|k|.
\]

Include every noncollinear Fourier triad

\[
k+p+q=0
\]

inside the cutoff and every helical assignment with nonzero exact coupling. Let `A_R` be the resulting transfer matrix.

Then

\[
\boxed{
\ker A_R
=\operatorname{span}\{\mathbf1,h\}.
}
\]

Equivalently, every diagonal quadratic invariant weight of the full helical Galerkin network has the form

\[
\boxed{
q_{k,\sigma}=A+B\sigma|k|.
}
\]

Thus the only global diagonal quadratic invariants of the full finite network are energy and helicity.

## 2. Local six-mode affine lemma

Fix one noncollinear geometric triad with radii

\[
r_1,r_2,r_3>0.
\]

Let `q_{i,+},q_{i,-}` be a diagonal invariant weight on the two helicities of each geometric mode. Write uniquely

\[
q_{i,s}=A_i+B_i(sr_i),
\]

where

\[
A_i=\frac{q_{i,+}+q_{i,-}}2,
\qquad
B_i=\frac{q_{i,+}-q_{i,-}}{2r_i}.
\]

For a helicity assignment `(s_1,s_2,s_3)`, the transfer row is

\[
\lambda=
(s_2r_2-s_3r_3,
 s_3r_3-s_1r_1,
 s_1r_1-s_2r_2).
\]

The invariant condition is

\[
\lambda_1q_{1,s_1}
+\lambda_2q_{2,s_2}
+\lambda_3q_{3,s_3}=0.
\]

Substitution gives the Walsh polynomial

\[
\begin{aligned}
0={}&r_1r_2(B_1-B_2)s_1s_2
-r_1r_3(B_1-B_3)s_1s_3\\
&+r_2r_3(B_2-B_3)s_2s_3\\
&+r_1(A_3-A_2)s_1
+r_2(A_1-A_3)s_2
+r_3(A_2-A_1)s_3.
\end{aligned}
\]

It vanishes for all eight sign choices. The six nonconstant Walsh characters are linearly independent on `{+/-1}^3`, so every coefficient vanishes. Since all radii are positive,

\[
A_1=A_2=A_3,
\qquad
B_1=B_2=B_3.
\]

Hence there exist `A_tau,B_tau` such that on all six helical modes of the geometric triad

\[
\boxed{
q_{i,s}=A_\tau+B_\tau s r_i.
}
\]

This proof includes equal-radius and equilateral cases without a separate argument.

### Why all helicity sign constraints are available

For a noncollinear Fourier triangle, the exact helical geometric triple factor contains the area factor and a signed triangle factor. The area is nonzero, and strict triangle inequalities exclude vanishing of the signed triangle factor except in the collinear boundary case. Thus the mixed-helicity channels needed above are genuinely present. A transfer row may have a zero component in a radius-degenerate case, but the full Walsh system remains valid; the all-equal homochiral row can be identically zero without affecting the conclusion.

## 3. Propagation through one shared geometric wavevector

Suppose two noncollinear geometric triads `tau,tau'` share one wavevector `k`.

The local lemma gives

\[
q_{k,+}=A_\tau+B_\tau|k|
=A_{\tau'}+B_{\tau'}|k|,
\]

and simultaneously

\[
q_{k,-}=A_\tau-B_\tau|k|
=A_{\tau'}-B_{\tau'}|k|.
\]

Adding and subtracting gives

\[
\boxed{
A_\tau=A_{\tau'},
\qquad
B_\tau=B_{\tau'}.
}
\]

This is the crucial full-helicity correction to the false one-signed-mode connectivity argument: one shared **geometric** wavevector supplies two distinct signed-frequency points `+|k|` and `-|k|`.

## 4. Connectivity of the spherical lattice triad graph

Make a graph whose vertices are nonzero lattice wavevectors modulo reality and whose hyperedges are noncollinear Fourier triads inside `K_R`.

We show every vertex is connected to a unit axis.

### Non-axis mode

Suppose `k` has at least two nonzero coordinates. Choose `j` with `k_j !=0` and let

\[
\varepsilon=\operatorname{sgn}(k_j).
\]

Set

\[
p=-\varepsilon e_j,
\qquad
q=-k+\varepsilon e_j.
\]

Then

\[
k+p+q=0.
\]

Also

\[
|q|^2
=|k|^2-2|k_j|+1
\le |k|^2,
\]

so all three modes lie inside the cutoff. Since `k` has another nonzero coordinate, the triad is noncollinear. Thus `k` is connected directly to the unit-axis mode `e_j`.

### Axis mode

Let `k=m e_j` after the reality identification.

If `m=1`, it is already a unit axis. If `m>=2`, choose `ell != j` and set

\[
p=-e_j+e_\ell,
\qquad
q=-(m-1)e_j-e_\ell.
\]

Then

\[
k+p+q=0,
\]

\[
|p|^2=2\le m^2,
\qquad
|q|^2=(m-1)^2+1\le m^2,
\]

and the triad is noncollinear. Hence the axis mode connects to a non-axis mode, which by the previous step connects to a unit axis.

### Unit axes are mutually connected

For `i != j`,

\[
e_i+e_j-(e_i+e_j)=0
\]

is a noncollinear triad with diagonal radius `sqrt(2)`. The assumption `R^2>=2` keeps it inside the cutoff.

Therefore the full geometric triad graph is connected.

## 5. Global conclusion

By the local six-mode lemma, every geometric triad carries an affine law

\[
q=A_\tau+B_\tau h.
\]

By connectedness and the one-shared-wavevector propagation lemma, all `A_tau,B_tau` are identical throughout the full Galerkin network.

Thus

\[
\boxed{
q_{k,\sigma}=A+B\sigma|k|
}
\]

for every helical mode, proving

\[
\boxed{
\ker A_R=\operatorname{span}\{\mathbf1,h\}.
}
\]

## 6. Consequence for the H-flow

For every such full periodic Galerkin cutoff, the Helical Onsager H-flow has a unique zero-curvature precision of the form

\[
\boxed{
C_{k,\sigma}^{-1}=\alpha+\beta\sigma|k|,
}
\]

subject to the fixed energy and helicity values and positivity.

Hence the finite-network canonical state is no longer only numerically consistent with Kraichnan geometry; it follows from the exact full-helicity convolution topology.
