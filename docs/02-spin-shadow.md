# The Spin-Shadow Mechanism

This note records the first exact composition obstruction derived directly from the helical pair coefficient.

## 1. Same-spin radial handoff

Let `Q^s` and `(-K)^s` be two same-helicity parents. Set

\[
P=Q-K,
\qquad
q=|Q|>k=|K|,
\qquad
p=|P|,
\qquad
S=q+k.
\]

The output wavevector `P` has two helical polarizations.

The opposite-spin coefficient is

\[
\boxed{
|C_P^{-s}|
=
\frac{1}{2\sqrt2}
(q-k)\frac{|Q\times K|}{pqk}(S-p).
}
\]

The same-spin coefficient at the **same wavevector** is

\[
\boxed{
|C_P^{s}|
=
\frac{1}{2\sqrt2}
(q-k)\frac{|Q\times K|}{pqk}(S+p).
}
\]

Therefore

\[
\boxed{
\frac{|C_P^s|}{|C_P^{-s}|}
=
\frac{S+p}{S-p}
\ge1.
}
\]

We call `P^s` the **spin shadow** of the opposite-spin catalyst `P^{-s}`.

## 2. Interpretation

A heterochiral critical handoff uses an opposite-spin catalyst. But the exact parent pair that drives that catalyst cannot isolate it: the same pair drives the other helicity at the same output wavevector with at least as large a coefficient magnitude.

Thus a sparse cascade skeleton has an intrinsic leakage tendency.

This is a statement about **pair forcing**, not immediately about energy transfer.

If the shadow amplitude initially vanishes, then

\[
\frac d{dt}|z_s(P)|^2
=2\operatorname{Re}(\overline{z_s(P)}\,\dot z_s(P))
\]

vanishes at that instant even when `dot z_s(P)` is large. The shadow first appears in amplitude and only then in modal energy.

## 3. Relation to critical production

For a heterochiral triad with same-spin endpoints and opposite-spin catalyst, energy and helicity conservation reduce the triad transfer to one signed current. In an orientation where the opposite-spin catalyst transfer is `T_P`, the critical production satisfies

\[
\dot K_\triangle=2pT_P.
\]

Moreover the two spin sectors receive equal critical production on the triad:

\[
\dot K_{s,\triangle}
=
\dot K_{-s,\triangle}
=
pT_P.
\]

Thus positive critical production necessarily involves the opposite-spin catalyst, while the exact convolution simultaneously forces its same-wavevector shadow.

## 4. First composition dichotomy

Let the full same-spin shadow forcing at `P` be

\[
F_s(P)=\sum_{a+b=P}g_{a,b}^s(P).
\]

If one dangerous pair contributes a large shadow term, there are only two possibilities:

1. **Leakage:** the total `F_s(P)` remains large.
2. **Cancellation:** other convolution pairs contribute comparably at the same output.

Cancellation means multiple representations of the same output:

\[
a+b=c+d.
\]

Equivalently,

\[
a-c=d-b,
\]

so Fourier parallelograms are forced into the active network.

This is the bridge from exact helical selection to additive structure.

## 5. What is not yet proved

The ratio above alone does not exclude singular escape. A successful proof must quantify at least one of the following:

- actual shadow forcing accumulated across a critical family;
- growth of representation multiplicity / weighted additive energy required to cancel shadows;
- rigidity of phases in the high-multiplicity branch;
- a non-summable cost when the mechanism is iterated across scales.
