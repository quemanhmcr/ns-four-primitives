#!/usr/bin/env python3
"""Audit the endpoint Brownian quadratic-variation identities.

This does not simulate the full Constantin-Iyer flow. It verifies the universal
terminal Brownian contribution, which is all that enters the endpoint formula
because the stochastic deformation equals the identity at zero backward lag.
"""

import numpy as np


def audit(samples=10000, seed=20260816):
    rng = np.random.default_rng(seed)
    nu = 0.37
    h = 1.0e-7

    # Random nonzero integer Fourier modes and complex protected-residual data.
    k = rng.integers(-12, 13, size=(samples, 3))
    zero = np.all(k == 0, axis=1)
    k[zero, 0] = 1
    k2 = np.sum(k * k, axis=1).astype(float)
    amp = rng.normal(size=samples) + 1j * rng.normal(size=samples)
    mass = np.abs(amp) ** 2

    # Exact Brownian-translation variance for f=r.
    V = np.sum(mass * (1.0 - np.exp(-2.0 * nu * k2 * h)))
    slope_fd = V / h
    slope_exact = 2.0 * nu * np.sum(k2 * mass)
    rel1 = abs(slope_fd - slope_exact) / slope_exact

    # Precondition by Lambda^{-1}: q_k=r_k/|k|.
    qmass = mass / k2
    Vq = np.sum(qmass * (1.0 - np.exp(-2.0 * nu * k2 * h)))
    slope_q_fd = Vq / h
    slope_q_exact = 2.0 * nu * np.sum(mass)
    rel2 = abs(slope_q_fd - slope_q_exact) / slope_q_exact

    print(f"modes: {samples}")
    print(f"relative error Q endpoint slope: {rel1:.3e}")
    print(f"relative error Lambda^-1 Q endpoint slope: {rel2:.3e}")

    # First-order finite differences have O(h*max|k|^2) truncation error.
    assert rel1 < 5e-5
    assert rel2 < 5e-5


if __name__ == "__main__":
    audit()
