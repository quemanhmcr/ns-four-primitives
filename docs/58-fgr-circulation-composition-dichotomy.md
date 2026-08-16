# FGR Circulation / Composition Dichotomy at a Protected Reset

**Claim level:** exact finite-dimensional inequalities at a nondegenerate protected reset, plus a theorem target for scale-uniform closure.

The passive Feshbach response can be weak even when the direct protected-to-bath coupling is nonzero, because conservative bath dynamics may rapidly recirculate the leakage. This note turns that possibility into an explicit positive quantity rather than a new vague loophole.

## 1. Bath spectral measure

Use the viscously whitened bath variables from `56-exact-fgr-renormalization.md`:

\[
C=D^{-1/2}AD^{-1/2},
\qquad C^*=-C,
\qquad G=D^{-1/2}B.
\]

Define the self-adjoint bath circulation operator

\[
\boxed{H:=iC.}
\]

For a protected vector `v`, put

\[
g:=Gv,
\qquad
m_0:=\|g\|^2,
\qquad
m_2:=\|Hg\|^2=\|Cg\|^2.
\]

When `m_0>0`, define the effective bath circulation frequency

\[
\boxed{
\Omega_{\rm bath}^2(v)
:=\frac{m_2}{m_0}.
}
\]

The renormalized zero-frequency FGR response is

\[
\mathcal R_\varepsilon(v)
:=\langle v,\varepsilon^{-1}\Sigma_\varepsilon v\rangle
=\langle g,(\varepsilon^2I+H^2)^{-1}g\rangle.
\]

## 2. Exact moment lower bound

By the variational formula for the inverse of a positive operator,

\[
\langle g,M^{-1}g\rangle
\ge
\frac{|\langle g,g\rangle|^2}{\langle g,Mg\rangle},
\qquad M=\varepsilon^2I+H^2.
\]

Therefore

\[
\boxed{
\mathcal R_\varepsilon(v)
\ge
\frac{m_0^2}{\varepsilon^2m_0+m_2}
=\frac{\|Gv\|^2}
{\varepsilon^2+\Omega_{\rm bath}^2(v)}.
}
\]

Equivalently,

\[
\boxed{
\|Gv\|^2
\le
(\varepsilon^2+\Omega_{\rm bath}^2(v))
\mathcal R_\varepsilon(v).
}
\]

Thus weak passive damping in the presence of nontrivial direct coupling forces a large conservative bath frequency.

## 3. Spectral concentration version

Let `Pi_L` be the spectral projector of `H` onto `|H|<=L`. Since

\[
(\varepsilon^2+H^2)^{-1}
\ge
\frac1{\varepsilon^2+L^2}\Pi_L,
\]

we have

\[
\boxed{
\|\Pi_LGv\|^2
\le
(\varepsilon^2+L^2)
\mathcal R_\varepsilon(v).
}
\]

Hence if `Gv` has fixed size but the FGR response is small, most of the coupling vector must lie at high bath-circulation frequency.

This is an exact spectral meaning of the coherent recirculation branch.

## 4. Protected reset and opening force

At a nondegenerate exact protected reset,

\[
P=\ker T,
\qquad u\in P,
\qquad F=\mathcal A_\omega u.
\]

With `Q=I-P`,

\[
\boxed{Bu=QF.}
\]

Since `T` vanishes on `P`,

\[
\boxed{
TF=T_QBu=T_QD^{1/2}Gu.
}
\]

The protected opening acceleration is

\[
\boxed{
\frac12\mathcal Y''=\|TF\|^2.
}
\]

Consequently

\[
\|TF\|^2
\le
\|T_QD^{1/2}\|^2\,\|Gu\|^2.
\]

Combining with the moment lower bound gives

\[
\boxed{
\frac12\mathcal Y''
\le
\|T_QD^{1/2}\|^2
(\varepsilon^2+\Omega_{\rm bath}^2(u))
\mathcal R_\varepsilon(u).
}
\]

## 5. Combine with the Protected Reset Inequality

The exact reset theorem `28-protected-reset-trichotomy.md` gave

\[
\mathcal M_{\rm twin}
\le
\frac12\mathcal Y''
+\mathfrak D_{\rm open}.
\]

Therefore

\[
\boxed{
\mathcal M_{\rm twin}
\le
\|T_QD^{1/2}\|^2
(\varepsilon^2+\Omega_{\rm bath}^2(u))
\mathcal R_\varepsilon(u)
+\mathfrak D_{\rm open}.
}
\]

This is the exact **FGR circulation / Composition dichotomy**.

A protected reset carrying nontrivial cross-spin pair mass can hide from passive damping only by paying in at least one of two ways:

1. large opening Composition defect;
2. large conservative bath-circulation frequency.

There is no third zero-cost channel.

## 6. Exact dark-state reduction for the actual state

For every `epsilon>0`,

\[
\mathcal R_\varepsilon(u)=0
\iff
Gu=0
\iff
Bu=0.
\]

At an exact protected reset,

\[
Bu=0
\iff
QF=0
\iff
TF=0
\iff
\mathcal Y''=0.
\]

The Protected Reset Trichotomy therefore gives

\[
\boxed{
\mathcal R_\varepsilon(u)=0
\Longrightarrow
\mathfrak D_{\rm open}>0
\quad\text{or}\quad
F=0.
}
\]

If also `D_open=0`, the state is the already classified zero-cost heat endpoint.

Thus the exact dark branch of the passive bath is already closed at the reset level by the deterministic Composition theorem.

## 7. Why high circulation is the correct remaining branch

The quantity

\[
\|CGu\|
\]

contains one more conservative bath excursion after the initial leakage `Gu`. It is therefore the resolvent analogue of the next protected bracket in the earlier depth-two Gramian tests.

The existing large-shell audits show the expected pattern:

- dense protected backgrounds on shell ratios `10,20,40,80` had a collapsing depth-one gap but an audited depth-two normalized gap between approximately `0.110` and `0.119`;
- a sparse genuinely three-dimensional branch had smaller depth-two gaps, approximately `0.046 -> 0.034`, while its global planarity defect simultaneously decreased approximately `0.091 -> 0.012`.

These are numerical observations, not theorems. They suggest that the high-circulation branch splits further into

\[
\boxed{
\text{dense bracket opening}
\quad\text{or}\quad
\text{sparse / near-planar structure}.
}
\]

Both alternatives already have corresponding deterministic machinery in the repository.

## 8. Mori/Lanczos interpretation

The response

\[
\mathcal R_\varepsilon(v)
=\langle g,(\varepsilon^2+H^2)^{-1}g\rangle
\]

is a Stieltjes transform of the spectral measure generated by `g` under the self-adjoint bath operator `H`.

The sequence

\[
g,\ Hg,\ H^2g,\ldots
\]

is the associated Krylov chain. Finite-depth bracket tests and the full Feshbach resolvent are therefore two views of the same object:

- brackets expose successive spectral moments;
- the resolvent resums the entire chain.

This motivates a Mori/Lanczos continued-fraction treatment of the remaining high-circulation branch. No closure theorem from that formalism is imported here.

## 9. Revised closing target

The remaining theorem can now be stated more sharply:

**Bath-Circulation Rigidity.** On normalized protected packets away from the classified safe set, prove a scale-uniform alternative

\[
\boxed{
\Omega_{\rm bath}^2(u)\le C_0
\quad\text{or}\quad
\mathscr F_{\rm comp}(u)
+\mathscr F_{\rm plane}(u)
\ge c_0\,\mathcal M_{\rm twin}(u).
}
\]

On the first branch, the exact inequality in Section 5 turns pair mass into passive FGR damping plus Composition cost. On the second branch, the existing dense/sparse Composition and planarity mechanisms take over.

If this theorem is achieved with constants independent of physical scale, the coherent protected-reset blind spot is reduced to the already regular heat endpoint.
