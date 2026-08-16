# Hypocoercive–Composition Dichotomy

**Claim level:** synthesis and theorem target. The exact curvature identities and finite-packet algebra are established elsewhere; the global dichotomy below is open.

The machine-flow experiments now suggest a sharper division of labor between the new protected-connection geometry and the existing deterministic Composition machinery.

## 1. Exact starting point

The optimal protected residual satisfies

\[
r_t=(\mathcal A_\omega-\nu\Lambda^2)r+\mathfrak K u,
\qquad
\mathfrak K=T'+[T,\mathcal A_\omega],
\]

and

\[
\boxed{\Gamma_{\rm esc}=\langle r,\mathfrak K u\rangle.}
\]

At a protected reset,

\[
\mathfrak K u=TF,
\qquad
\mathcal Y''=2\|\mathfrak K u\|^2.
\]

Thus the difficult positive source is curvature work.

## 2. What the new experiments add

The first curvature layer can become arbitrarily badly conditioned under large protected-shell separation. On dense packets, a second bracket repairs this loss with an audited normalized gap of order `1e-1` out to shell ratio `80`.

The same statement is false as a global scalar theorem on arbitrary sparse coherent states.

Therefore the correct architecture is not

\[
\text{one coercive functional for all states}.
\]

It is

\[
\boxed{
\text{thermal/dense curvature branch}
\quad\text{or}\quad
\text{coherent Composition branch}
\quad\text{or}\quad
\text{safe endpoint}.
}
\]

## 3. Proposed packet trichotomy

For a scale-normalized protected active packet, seek dimensionless functionals

- `D_dense`, measuring enough modal/covariance participation for protected observability;
- `C_comp`, the exact deterministic coherent remainder already represented by shadow, cross-output, phase and additive-collision defects;
- `S_safe`, measuring distance to classified safe strata.

The desired theorem is schematic:

\[
\boxed{
\mathscr G_2(u)
+\mathscr C_{\rm comp}(u)
\ge
c_0\,\operatorname{dist}(u,\mathcal M_{\rm safe})^2,
}
\]

where `G_2` is the depth-two protected observability functional on the dense branch, while `C_comp` takes over precisely when the state is too sparse/coherent for `G_2` to be uniformly coercive.

The exact definition of the right side and the mobility normalization are open.

## 4. Why this is a genuine theory transfer

In the original formulation the source problem was

\[
\int E(\Gamma_{\rm esc})_+dt=\infty.
\]

The new geometry turns it into a controllability question for a skew connection observed through a moving protected multiplier. This imports the logic of finite-index hypocoercivity/Kalman observability:

\[
\text{hidden direction}
\to
\text{skew transport}
\to
\text{observed direction}.
\]

But the deterministic Navier-Stokes network has coherent sparse states that statistical/thermal geometry must not average away. Those states are exactly where the previously developed Composition lemmas are strongest.

So the theory transfer is not replacing Composition. It provides the missing complementary mechanism for the dense branch.

## 5. Next theorem target

The next useful analytic theorem should be finite-packet and exact:

**Protected Kalman–Composition Theorem.** On a normalized protected two-spin packet, prove that either

1. the depth-two protected observability Gramian is coercive modulo `omega` with a scale-independent constant determined by quantitative density/transversality data; or
2. the packet has a quantitative sparse/coherent defect that forces a lower bound in one of the exact Composition functionals; or
3. the packet lies in a classified safe stratum.

A theorem of this form would turn the current source-rigidity gap into a finite-dimensional geometric alternative compatible with RG normalization. The subsequent PDE task would be to make the packet extraction and time integration uniform.
