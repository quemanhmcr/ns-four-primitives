# Passive Feshbach Bath for the Protected Navier–Stokes Geometry

**Claim level:** exact frozen-operator algebra plus a new theorem target. No nonlinear Navier–Stokes regularity claim is made here.

The protected-connection calculation rewrites the nonlinear source as curvature work,

\[
\Gamma_{\rm esc}=\langle r,\mathfrak K u\rangle,
\qquad
\mathfrak K=\dot T+[T,\mathcal A_\omega],
\]

with

\[
\mathcal A_\omega v=P(v\times\omega),
\qquad
\mathcal A_\omega^*=-\mathcal A_\omega.
\]

This note asks a different physical question. Instead of trying to dissipate the protected sector by an auxiliary entropy flow, treat the Fourier complement as an **actual lossy bath**. Euler skew coupling moves amplitude between the protected sector and the bath, while viscosity dissipates the bath. Feshbach/Schur elimination then produces an effective positive self-energy on the protected sector.

## 1. Frozen protected split

Freeze a protected state and let `P` be the orthogonal projection onto the protected shell subspace. Put

\[
Q=I-P.
\]

In normalized variables write the frozen skew-dissipative generator as

\[
L_\varepsilon=\mathcal A-\varepsilon D,
\qquad
\mathcal A^*=-\mathcal A,
\qquad
D=D^*>0,
\]

where `epsilon=1/c` in the fast RG clock and `D` is the normalized Laplacian. Since the protected projection is spectral, it commutes with `D` at an exact two-shell reset.

Define

\[
B:=Q\mathcal A P.
\]

Skew-adjointness gives

\[
P\mathcal A Q=-B^*.
\]

Thus for `x=Pu`, `y=Qu`,

\[
\dot x=(\mathcal A_{PP}-\varepsilon D_P)x-B^*y,
\]

\[
\dot y=Bx+(\mathcal A_{QQ}-\varepsilon D_Q)y.
\]

The protected sector is therefore coupled to a genuinely dissipative bath by the exact Euler connection.

## 2. Time-domain passivity

The bath energy obeys exactly

\[
\frac12\frac d{dt}\|y\|^2
=\operatorname{Re}\langle y,Bx\rangle
-\varepsilon\langle y,D_Qy\rangle.
\]

If the bath starts empty, `y(0)=0`, then

\[
\boxed{
\int_0^T\operatorname{Re}\langle x,B^*y\rangle\,dt
=
\frac12\|y(T)\|^2
+\varepsilon\int_0^T\langle y,D_Qy\rangle\,dt
\ge0.
}
\]

The memory force `-B^*y` in the protected equation therefore performs non-positive net work. The memory kernel need not be pointwise positive; the **input-output system is passive**.

This is the first reason the bath formulation is stronger than a raw Mori–Zwanzig rewriting: positivity is carried by the storage-plus-dissipation identity, not by the sign of the time kernel.

## 3. Feshbach self-energy

For `Re z>=0`, define the bath resolvent

\[
K_\varepsilon(z)
:=z+\varepsilon D_Q-\mathcal A_{QQ}.
\]

Its Hermitian part is

\[
\operatorname{Sym}K_\varepsilon(z)
=(\operatorname{Re}z)I+\varepsilon D_Q>0.
\]

For any invertible operator `K`,

\[
\operatorname{Sym}(K^{-1})
=K^{-*}\operatorname{Sym}(K)K^{-1}.
\]

Hence

\[
\boxed{
\operatorname{Sym}K_\varepsilon(z)^{-1}
=K_\varepsilon(z)^{-*}
\big((\operatorname{Re}z)I+\varepsilon D_Q\big)
K_\varepsilon(z)^{-1}
\ge0.
}
\]

The Feshbach self-energy on the protected sector is therefore

\[
\boxed{
\Sigma_\varepsilon(z)
:=B^*\operatorname{Sym}K_\varepsilon(z)^{-1}B
\ge0.
}
\]

At `z=0`,

\[
\boxed{
\Sigma_\varepsilon(0)
=B^*K_\varepsilon(0)^{-*}
(\varepsilon D_Q)
K_\varepsilon(0)^{-1}B.
}
\]

Because `epsilon D_Q` is strictly positive,

\[
\boxed{
\ker\Sigma_\varepsilon(0)=\ker B.
}
\]

Thus eliminating arbitrarily many repeated excursions through the frozen bath creates **no new dark directions**. The dark sector is exactly the sector that fails to couple at first curvature order.

## 4. Strong-coupling scaling

In the RG theta-clock, the frozen operator has the form

\[
L_c=c\mathcal A-D,
\qquad c=\varepsilon^{-1}.
\]

The corresponding zero-frequency Feshbach correction is

\[
\Sigma_c^{(\theta)}
=c^2B^*\operatorname{Sym}(D_Q-c\mathcal A_{QQ})^{-1}B.
\]

Since

\[
D_Q-c\mathcal A_{QQ}
=c(\varepsilon D_Q-\mathcal A_{QQ}),
\]

we have the exact scaling relation

\[
\boxed{
\Sigma_c^{(\theta)}
=c\,\Sigma_\varepsilon(0)
=\varepsilon^{-1}\Sigma_\varepsilon(0).
}
\]

Therefore the decisive strong-coupling question is not whether `Sigma_epsilon` stays order one. The correct target is

\[
\boxed{
\lambda_{\min,+}(\Sigma_\varepsilon)
\gtrsim \varepsilon.
}
\]

Such a bound would produce **order-one effective damping in the theta-clock** even as `c -> infinity`.

## 5. Relation to protected curvature

At an exact protected reset the optimal-shell coefficients satisfy

\[
a'=b'=0.
\]

Thus the protected geometry is stationary to first order and

\[
\mathfrak Ku=[T,\mathcal A]u=T\mathcal A u.
\]

Since `T` is invertible on the spectral complement of its two roots,

\[
\ker(T\mathcal A P)=\ker(Q\mathcal A P)=\ker B.
\]

So the curvature dark space and the Feshbach dark space are the same.

This is important for No-Zeno resets: the bath mechanism is not spoiled at leading order by motion of the protected frame. A reset starts in an adiabatically frozen geometry. It must either couple to the lossy bath or lie in a dark configuration.

## 6. New proof architecture

The proposed replacement for the coherent blind branch is

\[
\boxed{
\text{protected coherent state}
\to
\text{Euler excursion into }Q
\to
\text{viscous bath loss}
\to
\text{Feshbach positive self-energy on }P.
}
\]

The desired dichotomy is

\[
\boxed{
\text{effective passive damping}
\quad\text{or}\quad
\text{dark state}.
}
\]

The dark-state branch is then sent back to the exact deterministic rigidity machinery:

- protected reset trichotomy;
- Spin-Shadow leakage;
- additive/composition cancellation;
- plane/cross closure;
- zero-cost heat-line classification.

This is complementary to the H-flow rather than a replacement for its thermodynamic branch. The Feshbach bath is specifically designed to attack the **coherent** branch because it uses the actual skew Euler coupling and actual viscous dissipation.

## 7. The theorem that would matter

A scale-invariant closing statement would have the schematic form

\[
\boxed{
\varepsilon^{-1}
\langle v,\Sigma_\varepsilon(u)v\rangle
+ C\,\mathscr F_{\rm comp}(u,v)
\ge
\gamma\,d(u,\mathcal M_{\rm safe})^2
\|v_{\rm protected\setminus dark}\|^2,
}
\]

uniformly as `epsilon -> 0` and uniformly in physical frequency scale.

Here

- `M_safe` contains the already classified heat-line / degenerate protected strata;
- `F_comp` measures exact deterministic cancellation needed to create additional dark directions;
- the first term is the actual passive-bath self-energy.

Such a theorem would convert the coherent source problem into a **passive-system/dark-state classification problem**.

## 8. What is still open

The following gaps remain substantial:

1. the exact theorem above is only proved here at the frozen finite-dimensional operator-algebra level;
2. uniformity in the full infinite Fourier bath is open;
3. time-dependent protected projections introduce nonadiabatic pumping terms away from exact resets;
4. a robust soft projection for near-protected, rather than exactly protected, states remains to be constructed;
5. the RG gauge terms must be included in the final non-autonomous Schur-complement argument.

The numerical note `47-feshbach-bath-gate-test.md` tests whether the frozen mechanism survives expanding Fourier baths and whether its dark set matches the previously identified safe geometry.
