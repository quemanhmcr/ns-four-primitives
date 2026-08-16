# The Planar Endpoint Is Regular

The complex Spin-Shadow law identifies local Fourier-plane concentration as the low-cost exceptional geometry. This note records why a **globally fixed** Fourier plane is not a dangerous endpoint.

## 1. Fixed Fourier plane

Suppose the Fourier support of a divergence-free solution lies in a fixed two-dimensional linear plane through the origin. After a rigid rotation, take this plane to be

\[
k_3=0.
\]

Then the velocity is independent of `x_3` and can be written

\[
u(x,t)=(v_1(x_1,x_2,t),v_2(x_1,x_2,t),w(x_1,x_2,t)).
\]

Incompressibility gives

\[
\nabla_h\cdot v=0.
\]

Because convolution of wavevectors in the plane remains in the plane, this support condition is preserved by the Navier-Stokes nonlinearity and by viscosity.

## 2. Reduced equations

The horizontal component satisfies exactly the two-dimensional incompressible Navier-Stokes equation

\[
\partial_t v+v\cdot\nabla_hv
=-\nabla_h p+\nu\Delta_hv,
\qquad
\nabla_h\cdot v=0.
\]

The transverse component satisfies the linear advection-diffusion equation driven by that two-dimensional velocity,

\[
\partial_t w+v\cdot\nabla_hw
=\nu\Delta_hw.
\]

Thus the system is the standard `2D3C` reduction: a globally regular two-dimensional Navier-Stokes flow coupled to a passive diffusive scalar.

Therefore a globally fixed Fourier plane cannot support a three-dimensional finite-time singularity.

## 3. Consequence for the Composition program

Combining this endpoint with the complex Spin-Shadow law gives a sharper target.

At each output, low-cost coherent cancellation forces the weighted pair-plane normal tensor

\[
\mathsf Q_r
\]

close to rank one. If these local preferred planes lock to one global plane across the active cascade network, the solution approaches the regular planar class.

Hence the genuinely dangerous alternative is not simply "near planarity". It is **plane turning**:

\[
\boxed{
\text{the preferred local pair plane must keep changing across outputs/scales}.
}
\]

The next target is a Plane-Propagation / Plane-Turning Lemma: prove that a connected critical cascade which changes its preferred plane by a definite projective angle must regenerate a quantitative composition defect, phase dispersion, or off-plane forcing.

Such a lemma would turn the remaining exceptional geometry into a dichotomy:

\[
\boxed{
\text{low composition cost}
\Rightarrow
\text{global planarization}
\quad\text{or}\quad
\text{non-summable plane-turning cost}.
}
\]

The first branch is regular by this note. The second branch is the remaining target.
