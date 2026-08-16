# The Four Primitives

The point of the four primitives is to formulate the regularity problem before choosing a favorite norm, shell model, or decomposition.

## I. Transfer

The Euler part of incompressible Navier–Stokes redistributes what is already present. In rotational form

\[
F=P(u\times\omega).
\]

The two basic quadratic tangencies are

\[
\langle u,F\rangle=0,
\qquad
\langle\omega,F\rangle=0.
\]

Thus the inviscid motion lies tangent to energy–helicity level sets. A hypothetical singularity must therefore arise by reorganization toward finer structure, not by unconstrained radial growth of kinetic energy.

## II. Dissipation

Viscosity acts diagonally in Fourier space:

\[
-\nu\Lambda^2\widehat u(k)=-\nu|k|^2\widehat u(k).
\]

Finer scales are destroyed faster. Any singular escape must therefore transfer structure toward high frequency rapidly enough to overcome an increasingly fast local sink.

This is the primitive competition behind every later critical-balance identity.

## III. Selection

The quadratic nonlinearity is not an arbitrary bilinear energy-transfer machine.

A pair can interact only through exact convolution closure, and its strength is constrained by

- incompressibility,
- wavevector geometry,
- helical polarization,
- radial mismatch,
- complex phase.

The helical pair coefficient derived in `01-nonlinear-base.md` is our first exact selection law.

Selection explains why large amplitudes alone are insufficient for dangerous transfer.

## IV. Composition

A single dangerous transfer is not a singularity.

Finite-time singular escape requires an unbounded chain

\[
N_1\to N_2\to N_3\to\cdots\to\infty
\]

whose transfer times remain summable.

The output of one selected interaction must therefore remain compatible with the inputs and cancellation requirements of later interactions. Shared Fourier modes and shared phases make these local choices dependent.

The core conjectural principle of this repository is:

\[
\boxed{\text{local dangerous transfer need not be infinitely composable}.}
\]

The proof program is to replace this sentence by quantitative lemmas derived from the full convolution algebra.

## Why later quantities are secondary

Spectral defects, critical norms, helicity balance, additive energy, and phase curvature are not themselves primitives. They are instruments that quantify one of the four primitive mechanisms.

A useful test for every proposed new quantity is therefore:

> Which primitive does it measure, and what obstruction does it make quantitative?
