# Frequency-Resolved Passive FGR Response

**Claim level:** exact finite-dimensional operator theorem. It closes the temporal-resonance loophole of the zero-frequency Feshbach test. Uniform infinite-bath estimates remain open.

The protected block can carry nonzero conservative self-motion for some protected shell geometries. Therefore the physically relevant bath response is frequency resolved rather than always evaluated at zero temporal frequency.

## 1. Dynamic bath impedance

Let

\[
A^*=-A,\qquad D=D^*>0,
\]

be the frozen bath connection and dissipation, and let `B` map the protected sector into the bath. For real temporal frequency `omega`, define

\[
K_{\varepsilon,\omega}
:=\varepsilon D-A+i\omega I.
\]

The dissipative part of the protected self-energy is

\[
\boxed{
\Sigma_\varepsilon(\omega)
:=B^*K_{\varepsilon,\omega}^{-*}
(\varepsilon D)
K_{\varepsilon,\omega}^{-1}B
\ge0.
}
\]

## 2. Exact viscous whitening at every frequency

Set

\[
G=D^{-1/2}B,
\]

and

\[
\boxed{
C_\omega
:=D^{-1/2}(A-i\omega I)D^{-1/2}.
}
\]

Because both `A` and `-i omega I` are skew-adjoint,

\[
C_\omega^*=-C_\omega.
\]

Moreover

\[
K_{\varepsilon,\omega}
=D^{1/2}(\varepsilon I-C_\omega)D^{1/2}.
\]

Hence exactly

\[
\boxed{
\varepsilon^{-1}\Sigma_\varepsilon(\omega)
=G^*(\varepsilon^2I-C_\omega^2)^{-1}G.
}
\]

Thus every temporal frequency sees the same positive Lorentzian bath geometry, only with the skew connection shifted by the temporal phase.

## 3. No temporal creation of exact dark states

For every `epsilon>0` and every real `omega`, the operator

\[
(\varepsilon^2I-C_\omega^2)^{-1}
\]

is strictly positive definite. Therefore

\[
\boxed{
\ker\Sigma_\varepsilon(\omega)
=\ker G
=\ker B,
}
\]

independently of `omega`.

A protected mode cannot tune its temporal frequency to become exactly dark. Exact darkness is geometric Euler decoupling from the bath.

This rules out a bound-state-in-the-continuum type loophole at finite viscosity in the frozen passive-bath model.

## 4. Strong-coupling monotonicity at every frequency

For fixed `omega`, if

\[
0<\varepsilon_1<\varepsilon_2,
\]

then

\[
\boxed{
\varepsilon_1^{-1}\Sigma_{\varepsilon_1}(\omega)
\ge
\varepsilon_2^{-1}\Sigma_{\varepsilon_2}(\omega).
}
\]

Hence strong RG coupling cannot weaken the renormalized bath response at any fixed temporal frequency.

## 5. Protected on-shell frequencies

Let `A_PP` be the frozen protected skew block. Its eigenvalues have the form

\[
A_{PP}v_j=i\mu_jv_j.
\]

The free protected oscillation `v_j` samples the bath on shell at temporal frequency `omega=mu_j` (up to Fourier-sign convention). The exact decay diagnostic is therefore

\[
\boxed{
\gamma_j(\varepsilon)
:=
\langle v_j,
\varepsilon^{-1}\Sigma_\varepsilon(\mu_j)v_j
\rangle.
}
\]

The kernel theorem above implies

\[
\gamma_j(\varepsilon)=0
\iff
Bv_j=0.
\]

Thus nonzero protected self-motion does not add a new exact dark mechanism.

## 6. Numerical gate test

For the protected shell pair `(1,2)` the audited frozen protected block is zero, so the zero-frequency test is already exactly on shell.

The first audited full-shell case with nonzero protected self-motion is `(2,3)`. For the normalized full protected background,

\[
\|A_{PP}\|\approx0.567,
\qquad
\max_j|\mu_j|\approx0.156.
\]

On expanding bath cutoffs `R=4,5,6`, all `36/36` protected eigenmodes have positive on-shell response. At `epsilon=0.1`, the smallest renormalized on-shell responses were approximately

\[
4.67,\qquad3.85,\qquad4.13.
\]

This is numerical evidence only, but it falsifies the simplest temporal-resonance escape scenario.

## 7. Remaining frequency problem

Although exact darkness is frequency independent, quantitative response can weaken at very large temporal frequency. The theorem still required for a nonlinear closure is a scale-normalized lower bound over the temporal spectrum actually accessible to the protected Kato dynamics.

The next note avoids a crude uniform frequency bound by using the spectral moments of the actual bath-coupling vector. This produces an exact passive-damping / high-circulation dichotomy.
