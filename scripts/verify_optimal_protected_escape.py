#!/usr/bin/env python3
"""Finite-dimensional Gram audit for the optimal protected escape defect."""

import numpy as np


def audit(samples=10000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_normal_error = 0.0
    max_gram_error = 0.0
    min_residual = float("inf")

    for _ in range(samples):
        # Abstract Hilbert vectors are sufficient to audit the projection/Gram algebra.
        dim = 8
        u = rng.normal(size=dim)
        w = rng.normal(size=dim)
        l = rng.normal(size=dim)
        E = float(u @ u)
        H = float(u @ w)
        Z = float(w @ w)
        K = float(u @ l)
        C = float(w @ l)
        L2 = float(l @ l)
        Delta = E * Z - H * H
        if Delta < 1e-8:
            continue
        a = (K * Z - H * C) / Delta
        b = (E * C - H * K) / Delta
        r = l - a * u - b * w
        Y = float(r @ r)
        min_residual = min(min_residual, Y)
        max_normal_error = max(max_normal_error, abs(r @ u), abs(r @ w))

        G3 = np.array([[E, H, K], [H, Z, C], [K, C, L2]])
        Ygram = float(np.linalg.det(G3) / Delta)
        max_gram_error = max(max_gram_error, abs(Y - Ygram))

    print(f"samples: {samples}")
    print(f"max projection normal-equation error: {max_normal_error:.3e}")
    print(f"max Gram-Schur residual abs error: {max_gram_error:.3e}")
    print(f"minimum residual norm squared: {min_residual:.3e}")
    assert max_normal_error < 1e-10
    assert max_gram_error < 1e-9
    assert min_residual > -1e-12


if __name__ == "__main__":
    audit()
