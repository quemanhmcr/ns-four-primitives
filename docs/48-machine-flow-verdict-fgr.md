# Machine-Flow Verdict: From H-Flow to a Passive Feshbach Bath

The current blind spot is the deterministic coherent branch. The H-flow is valuable on entropy-aligned transfer, but its mobility is auxiliary. The Feshbach bath attacks a different branch using only actual Navier–Stokes ingredients.

## 1. Why this machine is different

The new machine is not a new artificial evolution equation for modal energies. It is an exact elimination of part of the existing frozen Navier–Stokes operator:

\[
\boxed{
\text{protected modes }P
\leftrightarrow
\text{Euler skew coupling}
\leftrightarrow
\text{viscous complement }Q.
}
\]

The complement acts as a passive bath. Integrating it out produces a positive self-energy on `P`.

This is the same structural mechanism that appears in resonance/Fermi-golden-rule physics: a nominally protected state acquires a decay width by coupling to a lossy or continuous sector. Here the loss mechanism is not imported; it is viscosity itself.

## 2. Why not simply Mori–Zwanzig

Exact projection gives a memory equation, but a generic memory kernel is not pointwise sign-definite. The useful additional structure here is **passivity**:

\[
\text{memory work}
=
\text{stored bath energy}
+
\text{viscous bath dissipation}.
\]

In Laplace/resolvent variables this becomes the positive-real Feshbach self-energy.

Thus the useful theory transfer is not “memory” by itself. It is

\[
\boxed{
\text{projection + skew coupling + passive bath + positive-real resolvent}.
}
\]

## 3. Why double-bracket flow is not currently first choice

Double-bracket/selective-decay mechanics is a genuine geometric dissipation theory and preserves coadjoint-orbit structure while dissipating a chosen mechanical quantity. It remains a serious conceptual comparison.

For the present gap, however, the passive bath has a stronger mapping back to Navier–Stokes:

- its skew operator is the exact Euler connection;
- its damping is the exact viscous Laplacian;
- its dark space is the exact curvature kernel;
- no auxiliary mobility or dissipation coefficient is chosen.

Therefore Feshbach/passivity currently ranks above double-bracket flow for source rigidity.

## 4. Revised two-machine architecture

The most promising architecture is now not one universal comparison flow but two physically distinct machines.

### Thermal branch

Use the Onsager H-flow where the deterministic current is close to the entropy-gradient direction.

### Coherent branch

Use passive Feshbach elimination where the current remains coherent. The question becomes whether a coherent protected state can remain dark to the actual lossy complement.

Hence

\[
\boxed{
\text{deterministic current}
\Rightarrow
\begin{cases}
\text{H-aligned thermalization},\\
\text{passive-bath damping},\\
\text{dark coherent state}.
\end{cases}
}
\]

The third branch is not left uncontrolled. It is exactly where the existing Composition, reality-twin, plane-closure, and reset-rigidity lemmas apply.

## 5. The proposed decisive theorem

The next theorem should combine the passive bath with deterministic dark-state rigidity:

**Scale-Uniform Passive-Bath / Dark-State Theorem.** On a normalized critical packet, either

\[
\varepsilon^{-1}\Sigma_\varepsilon
\]

has a coercive gap on the protected subspace modulo conservation/safe directions, or the state carries a quantitative Composition defect / lies close to the already classified safe stratum.

The theorem must remain uniform as

\[
\varepsilon=1/c\to0
\]

and as the physical packet frequency tends to infinity.

If such a theorem exists, the coherent branch acquires a genuine physical decay mechanism rather than merely a structural obstruction.

## 6. Current verdict

The Feshbach/passive-bath direction passes the present gate tests better than any machine tried so far:

- exact positivity is algebraic, not statistical;
- exact dark kernel is first-curvature kernel;
- cutoff tests show stabilization on representative packets;
- strong-coupling numerics are consistent with `lambda_min ~ epsilon`;
- dark heat-line states remain dark;
- the gap opens quadratically away from that safe stratum.

The decisive missing step is now very narrow:

\[
\boxed{
\text{prove scale-uniform positive-real bath coercivity,}
\text{ or find the structured dark sequences that defeat it.}
}
\]

Either outcome would materially change the proof program.
