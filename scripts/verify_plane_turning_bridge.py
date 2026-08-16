#!/usr/bin/env python3
"""Numerical falsification aid for the Plane-Turning Bridge Lemma."""

import math
import numpy as np
from verify_helical_coefficients import pair_coefficient

SQRT2 = math.sqrt(2.0)


def unit(v):
    return v / np.linalg.norm(v)


def audit(samples=20000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_triple_error = 0.0
    min_area_margin = float("inf")
    min_coeff_margin = float("inf")
    accepted = 0

    while accepted < samples:
        # Ordered radii with independent random directions.
        radii = np.sort(rng.uniform(0.5, 3.0, size=3))
        k, q, r = radii
        K = k * unit(rng.normal(size=3))
        Q = q * unit(rng.normal(size=3))
        R = r * unit(rng.normal(size=3))

        A1 = np.linalg.norm(np.cross(Q, K))
        A2 = np.linalg.norm(np.cross(R, Q))
        if min(A1, A2) < 1e-8:
            continue

        n1 = np.cross(Q, K) / A1
        n2 = np.cross(R, Q) / A2
        sin_delta = np.linalg.norm(np.cross(n1, n2))

        triple = abs(np.dot(Q, np.cross(R, K)))
        triple_pred = A1 * A2 * sin_delta / q
        max_triple_error = max(max_triple_error, abs(triple - triple_pred))

        A3 = np.linalg.norm(np.cross(R, K))
        area_lower = A1 * A2 * sin_delta / (q * q)
        min_area_margin = min(min_area_margin, A3 - area_lower)

        sin1 = A1 / (q * k)
        sin2 = A2 / (r * q)
        s = 1
        got = abs(pair_coefficient(R, -K, s, s, s))
        lower = (r - k) * sin1 * sin2 * sin_delta / SQRT2
        min_coeff_margin = min(min_coeff_margin, got - lower)

        accepted += 1

    print(f"samples: {samples}")
    print(f"max scalar-triple identity abs error: {max_triple_error:.3e}")
    print(f"minimum cross-area lower-bound margin: {min_area_margin:.3e}")
    print(f"minimum bridge-coefficient lower-bound margin: {min_coeff_margin:.3e}")

    assert max_triple_error < 1e-10
    assert min_area_margin > -1e-10
    assert min_coeff_margin > -1e-10


if __name__ == "__main__":
    audit()
