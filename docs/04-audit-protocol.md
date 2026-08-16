# Audit Protocol

This repository treats falsification as part of the proof architecture.

## 1. Fix conventions before comparing formulas

Every helical coefficient statement must specify

- Fourier sign convention,
- helical eigenvector convention,
- normalization of `h_s`,
- whether an expression is an ordered-pair coefficient or the symmetrized pair contribution,
- whether a statement concerns complex coefficient, magnitude, forcing, or energy transfer.

A sign mismatch in the output helicity changes `S+rho` into `S-rho` and can reverse a proposed structural conclusion.

## 2. Separate four evidence levels

### Exact identity

Derived symbolically from Navier–Stokes with stated conventions.

### Numerical algebra audit

Random or explicit configurations reproduce an exact identity to floating-point accuracy. This catches sign and normalization mistakes but is not a proof by itself.

### Structural reduction

A logically valid implication whose endpoint is still an open estimate.

### Open target

A conjectural rigidity or inequality that has not been proved.

No document should silently promote an item from one level to another.

## 3. Stress tests for every proposed closing estimate

At minimum test against

- equal-radius parents,
- nearly collinear parents,
- local comparable triads,
- strongly nonlocal triads,
- pure-helicity states,
- balanced two-spin states,
- a single isolated triad,
- a triad tree,
- a diamond with two representations of one output,
- many-to-one convolution cancellation.

## 4. Full-network rule

A sparse selected triad family is not dynamically closed unless the full quadratic convolution preserves it.

Whenever a model selects a parent pair for one desired output, all other helical outputs created by that same parent pair must be checked. The spin-shadow mechanism is the first example of why this rule matters.

## 5. Reproducibility

Run

```bash
python scripts/verify_helical_coefficients.py
```

The script checks

- the helical eigenvector relation,
- the exact same-spin coefficient magnitude,
- the catalyst/shadow ratio,
- the inequality `|C_shadow| >= |C_catalyst|`.
