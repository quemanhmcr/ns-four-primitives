# Strong-Handoff Path Compactness

The finite-frame rigidity theorem leaves an apparent loophole: the graph diameter might grow without bound while every local plane obstruction becomes small. This note proves that such large diameter is impossible for a uniformly strong handoff path inside a scale-normalized packet with bounded critical mass.

The remaining compactness problem is therefore sharpened to **flux fragmentation into many weak handoffs**, not arbitrary long strong paths.

## 1. Local scale normalization

Fix a local frequency window

\[
\lambda\le |k|\le\Lambda
\]

with constants `0<lambda<Lambda<infinity`. This is the scale-normalized form of a comparable-frequency packet.

For a helical mode define its critical amplitude

\[
a_k:=|k|^{1/2}|z(k)|.
\]

The local critical mass is

\[
M:=\sum_{k\text{ in packet}}a_k^2.
\]

## 2. A universal local coefficient upper bound

For any helical pair coefficient

\[
C_{r;a,b}^{t,s_a,s_b}
=(s_b|b|-s_a|a|)
\overline{h_t(r)}\cdot
(h_{s_a}(a)\times h_{s_b}(b)),
\]

unit normalization of the helical vectors gives

\[
|C_{r;a,b}^{t,s_a,s_b}|
\le |a|+|b|.
\]

Hence inside the normalized local window,

\[
\boxed{|C|\le2\Lambda.}
\]

## 3. Strong critical production forces strong parent product

Consider one same-spin radial handoff with endpoint modes `K,Q` and opposite-spin catalyst `P`, all lying in the local window. Put

\[
\pi_e:=a_Ka_Q.
\]

Its critical production has the form

\[
\kappa_e
=2|P|\operatorname{Re}
\left(\overline{z(P)}\,C_e z(Q)z(-K)\right).
\]

Therefore

\[
|\kappa_e|
\le
2|P|\,|C_e|\,|z(P)z(Q)z(K)|.
\]

Writing every modal amplitude in critical variables gives

\[
|\kappa_e|
\le
2\sqrt{|P|}\,
\frac{|C_e|}{\sqrt{|Q||K|}}
\,a_P\pi_e.
\]

Using the local window and the coefficient upper bound,

\[
\boxed{
|\kappa_e|
\le
C_{\lambda,\Lambda}\,a_P\pi_e,
\qquad
C_{\lambda,\Lambda}
:=\frac{4\Lambda^{3/2}}{\lambda}.
}
\]

Since `a_P <= sqrt(M)`, we obtain

\[
\boxed{
|\kappa_e|
\le
C_{\lambda,\Lambda}\sqrt M\,\pi_e.
}
\]

Consequently a handoff carrying

\[
|\kappa_e|\ge\kappa_0>0
\]

must satisfy

\[
\boxed{
\pi_e
\ge
P_0:=
\frac{\kappa_0}
{C_{\lambda,\Lambda}\sqrt M}.
}
\]

Thus, at fixed local mass, nontrivial normalized flux cannot be carried by a parent pair whose critical product tends to zero.

## 4. Strong-path diameter bound

Let

\[
K_0,K_1,\dots,K_m
\]

be a same-spin handoff path inside the same local packet, with critical amplitudes

\[
a_j=|K_j|^{1/2}|z_s(K_j)|.
\]

Assume every adjacent handoff satisfies

\[
\pi_j=a_ja_{j+1}\ge P>0.
\]

By the arithmetic-geometric mean inequality,

\[
a_j^2+a_{j+1}^2\ge2P.
\]

Summing over the `m` edges gives

\[
2Pm
\le
a_0^2+a_m^2+2\sum_{j=1}^{m-1}a_j^2
\le2\sum_{j=0}^m a_j^2.
\]

Hence

\[
\boxed{
m\le\frac{M_{\rm path}}{P}.}
\]

In particular, since `M_path <= M`,

\[
\boxed{
m\le\frac MP.}
\]

This is the **Strong-Handoff Path Compactness Lemma**.

## 5. Flux-normalized corollary

If every handoff on the path carries

\[
|\kappa_e|\ge\kappa_0
\]

and the total local critical mass is at most `M`, then Section 3 gives `P=P_0`, and therefore

\[
\boxed{
m
\le
\frac{C_{\lambda,\Lambda}M^{3/2}}
{\kappa_0}.}
\]

Thus a scale-normalized packet with bounded critical mass cannot contain an arbitrarily long path whose every edge carries a fixed amount of normalized critical production.

## 6. What remains: fragmentation, not path length

A long critical cascade can evade this theorem only if the flux per individual handoff tends to zero or if the normalized local critical mass itself becomes unbounded.

For a blow-up analysis based on bounded-mass local packets, the remaining branch is therefore

\[
\boxed{
\text{fixed total positive flux}
\quad\text{fragmented among many weak handoffs}.}
\]

This is precisely the regime in which multiplicity, additive collisions, and composition defect become unavoidable. The next compactness target should therefore be a **Flux Fragmentation / Additive Concentration Lemma**: show that a bounded-mass local packet with fixed positive total critical production but no strong finite path must carry quantitatively large weighted additive/composition structure on a bounded effective frame.

That fragmentation lemma is open. The strong-path bound above is proved.
