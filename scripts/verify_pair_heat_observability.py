#!/usr/bin/env python3
"""Numerical/symbolic-style checks for pair-heat observability identities."""

import numpy as np


def vandermonde_rank(samples=1000, seed=20260818):
    rng = np.random.default_rng(seed)
    min_singular = float("inf")
    for _ in range(samples):
        m = int(rng.integers(1, 8))
        vals = np.sort(rng.choice(np.arange(1, 60), size=m, replace=False)).astype(float)
        V = np.vstack([vals ** n for n in range(m)])
        s = np.linalg.svd(V, compute_uv=False)
        min_singular = min(min_singular, s[-1])
        assert np.linalg.matrix_rank(V, tol=1e-8) == m
    return min_singular


def resonant_geometry(samples=10000, seed=20260819):
    rng = np.random.default_rng(seed)
    worst_rate = 0.0
    worst_area = 0.0
    worst_delta = 0.0
    for _ in range(samples):
        r = rng.normal(size=3)
        x = rng.normal(size=3)
        if np.linalg.norm(r) < 1e-10 or np.linalg.norm(x) < 1e-10:
            continue
        a = r / 2.0 + x
        b = r / 2.0 - x
        aa = np.linalg.norm(a)
        bb = np.linalg.norm(b)
        rho = np.linalg.norm(r)
        R = np.linalg.norm(x)
        rate1 = np.dot(a, a) + np.dot(b, b)
        rate2 = rho * rho / 2.0 + 2.0 * R * R
        worst_rate = max(worst_rate, abs(rate1 - rate2))

        area1 = np.linalg.norm(np.cross(a, b))
        area2 = np.linalg.norm(np.cross(r, x))
        worst_area = max(worst_area, abs(area1 - area2))

        S = aa + bb
        delta1 = abs(aa - bb)
        delta2 = 2.0 * abs(np.dot(r, x)) / S
        worst_delta = max(worst_delta, abs(delta1 - delta2))

    return worst_rate, worst_area, worst_delta


if __name__ == "__main__":
    sigma_min = vandermonde_rank()
    wr, wa, wd = resonant_geometry()
    print("smallest sampled Vandermonde singular value:", f"{sigma_min:.3e}")
    print("midpoint heat-rate identity max abs error:", f"{wr:.3e}")
    print("midpoint area identity max abs error:", f"{wa:.3e}")
    print("midpoint radial-difference identity max abs error:", f"{wd:.3e}")
    assert wr < 1e-10
    assert wa < 1e-10
    assert wd < 1e-10
