#!/usr/bin/env python3
"""Numerical audit for the exact helical pair-coefficient identities.

This is a falsification aid, not a substitute for the derivations in docs/.
"""

import math
import random
import numpy as np

SQRT2 = math.sqrt(2.0)


def helical(v, s):
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n == 0:
        raise ValueError("zero wavevector")
    khat = v / n
    refs = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]
    ref = min(refs, key=lambda r: abs(np.dot(r, khat)))
    e1 = np.cross(ref, khat)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(khat, e1)
    return (e1 + 1j * s * e2) / SQRT2


def pair_coefficient(a, b, t, sa, sb):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    r = a + b
    aa = np.linalg.norm(a)
    bb = np.linalg.norm(b)
    vector_factor = np.cross(helical(a, sa), helical(b, sb))
    return (sb * bb - sa * aa) * np.vdot(helical(r, t), vector_factor)


def same_spin_prediction(a, b, t, s):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    r = a + b
    aa = np.linalg.norm(a)
    bb = np.linalg.norm(b)
    rr = np.linalg.norm(r)
    area = np.linalg.norm(np.cross(a, b))
    S = aa + bb
    Delta = abs(aa - bb)
    return (
        Delta
        * area
        * (S + t * s * rr)
        / (2.0 * SQRT2 * rr * aa * bb)
    )


def relerr(x, y):
    return abs(x - y) / max(1e-14, abs(y))


def audit(samples=5000, seed=20260816):
    random.seed(seed)
    np.random.seed(seed)

    max_eigen = 0.0
    max_formula = 0.0
    max_ratio = 0.0
    min_shadow_ratio = float("inf")
    accepted = 0

    while accepted < samples:
        a = np.random.normal(size=3)
        b = np.random.normal(size=3)
        r = a + b
        if (
            np.linalg.norm(a) < 1e-8
            or np.linalg.norm(b) < 1e-8
            or np.linalg.norm(r) < 1e-8
            or np.linalg.norm(np.cross(a, b)) < 1e-8
        ):
            continue

        s = random.choice([-1, 1])
        t = random.choice([-1, 1])

        h = helical(a, s)
        lhs = 1j * np.cross(a, h)
        rhs = s * np.linalg.norm(a) * h
        max_eigen = max(max_eigen, np.linalg.norm(lhs - rhs))

        got = abs(pair_coefficient(a, b, t, s, s))
        pred = same_spin_prediction(a, b, t, s)
        max_formula = max(max_formula, relerr(got, pred))

        # Treat t=-s as catalyst and t=s as the same-wavevector shadow.
        catalyst = abs(pair_coefficient(a, b, -s, s, s))
        shadow = abs(pair_coefficient(a, b, s, s, s))
        aa = np.linalg.norm(a)
        bb = np.linalg.norm(b)
        rr = np.linalg.norm(r)
        S = aa + bb
        expected_ratio = (S + rr) / (S - rr)
        ratio = shadow / catalyst
        max_ratio = max(max_ratio, relerr(ratio, expected_ratio))
        min_shadow_ratio = min(min_shadow_ratio, ratio)

        accepted += 1

    print(f"samples: {samples}")
    print(f"max helical eigenvector residual: {max_eigen:.3e}")
    print(f"max same-spin formula relative error: {max_formula:.3e}")
    print(f"max spin-shadow ratio relative error: {max_ratio:.3e}")
    print(f"minimum observed |C_shadow|/|C_catalyst|: {min_shadow_ratio:.6f}")

    assert max_eigen < 1e-10
    assert max_formula < 1e-9
    assert max_ratio < 1e-9
    assert min_shadow_ratio >= 1.0 - 1e-12


if __name__ == "__main__":
    audit()
