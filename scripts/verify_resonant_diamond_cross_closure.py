#!/usr/bin/env python3
"""Numerical falsification aid for resonant diamond cross-closure."""

import math
import numpy as np
from verify_helical_coefficients import pair_coefficient

SQRT2 = math.sqrt(2.0)


def unit(v):
    return v / np.linalg.norm(v)


def audit(samples=30000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_heat_error = 0.0
    max_triple_error = 0.0
    max_radial_error = 0.0
    min_coeff_margin = float("inf")
    accepted = 0

    while accepted < samples:
        r = rng.normal(size=3)
        rho = np.linalg.norm(r)
        if rho < 1e-8:
            continue
        Rmag = rng.uniform(0.2, 3.0)
        x = Rmag * unit(rng.normal(size=3))
        y = Rmag * unit(rng.normal(size=3))

        xi = float(np.dot(r, x))
        ups = float(np.dot(r, y))
        chi = abs(np.dot(r, np.cross(x, y))) / rho
        if chi < 1e-10:
            continue

        ap = r / 2 + x
        am = r / 2 - x
        cp = r / 2 + y
        cm = r / 2 - y
        heat_x = np.dot(ap, ap) + np.dot(am, am)
        heat_y = np.dot(cp, cp) + np.dot(cm, cm)
        max_heat_error = max(max_heat_error, abs(heat_x - heat_y))

        eps = 1 if xi >= 0 else -1
        eta = -1 if ups >= 0 else 1
        A = r / 2 + eps * x
        C = r / 2 + eta * y
        aa = np.linalg.norm(A)
        cc = np.linalg.norm(C)
        B = A - C
        bb = np.linalg.norm(B)
        if min(aa, cc, bb) < 1e-8:
            continue

        triple = abs(np.dot(r, np.cross(A, C)))
        max_triple_error = max(max_triple_error, abs(triple - rho * chi))

        sqdiff = abs(aa * aa - cc * cc)
        max_radial_error = max(max_radial_error, abs(sqdiff - (abs(xi) + abs(ups))))
        delta = sqdiff / (aa + cc)

        got = abs(pair_coefficient(A, -C, 1, 1, 1))
        area = np.linalg.norm(np.cross(A, C))
        lower = delta * area / (SQRT2 * aa * cc)
        min_coeff_margin = min(min_coeff_margin, got - lower)

        accepted += 1

    print(f"samples: {samples}")
    print(f"max equal-heat identity abs error: {max_heat_error:.3e}")
    print(f"max cross scalar-triple identity abs error: {max_triple_error:.3e}")
    print(f"max maximizing radial-square identity abs error: {max_radial_error:.3e}")
    print(f"minimum cross-coefficient lower-bound margin: {min_coeff_margin:.3e}")

    assert max_heat_error < 1e-10
    assert max_triple_error < 1e-10
    assert max_radial_error < 1e-10
    assert min_coeff_margin > -1e-10


if __name__ == "__main__":
    audit()
