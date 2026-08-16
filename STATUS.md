# Research Status

**Date:** 2026-08-16

**Claim level:** structural research program; no global-regularity proof is claimed.

## Established / audited in this repository

- Rotational/Leray form of the incompressible Navier–Stokes nonlinearity.
- Energy and helicity tangency of the Euler forcing.
- Exact helical pair coefficient for `a+b=r`.
- Exact same-spin coefficient magnitude
  \[
  |C^{t,s,s}|=(2\sqrt2)^{-1}\Delta A(\rho\alpha\beta)^{-1}(S+ts\rho).
  \]
- Exact same-wavevector spin-shadow ratio
  \[
  |C_P^s|/|C_P^{-s}|=(S+p)/(S-p)\ge1.
  \]
- Numerical audit script reproducing these identities on random nondegenerate triads.
- Conceptual separation between pair forcing and modal energy transfer.

## Structural reductions currently used

- Dangerous critical transfer requires radial mismatch inside a helicity sector.
- Opposite-spin participation is required for heterochiral critical production.
- A sparse same-spin handoff necessarily creates an off-channel same-spin shadow at the catalyst wavevector.
- Avoiding actual shadow leakage requires cancellation by additional convolution pairs, hence additive structure in the active Fourier set.

## Open targets

1. **Weighted leakage/additive-energy dichotomy.** Convert a quantified amount of positive critical production into either actual shadow forcing or a quantitative lower bound on weighted additive energy.
2. **Dense phase rigidity.** In the high-additive-energy branch, control cancellation through the shared Fourier phases and exact helical coefficient phases.
3. **Scale iteration.** Prove that the structural cost from (1)–(2) cannot remain summable along an infinite critical cascade.
4. **PDE closure.** Connect the resulting network rigidity to a standard continuation criterion for smooth 3D Navier–Stokes solutions.

## Explicit non-claims

- A single helical triad does not model the full nonlinear network.
- Large pair forcing does not by itself imply large instantaneous modal energy transfer.
- High additive energy does not by itself imply regularity.
- Phase frustration is currently a research target, not a theorem.
