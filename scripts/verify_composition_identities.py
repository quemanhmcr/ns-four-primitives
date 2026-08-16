#!/usr/bin/env python3
"""Falsification checks for the exact Composition identities."""

import random
import numpy as np


def test_composition_defect(samples=10000, seed=20260816):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(samples):
        n = int(rng.integers(1, 10))
        x = rng.normal(size=n) + 1j * rng.normal(size=n)
        F = np.sum(x)
        envelope = np.sum(np.abs(x)) ** 2
        defect = envelope - abs(F) ** 2
        pair_formula = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(x[i]) == 0 or abs(x[j]) == 0:
                    continue
                dtheta = np.angle(x[i]) - np.angle(x[j])
                pair_formula += 2.0 * abs(x[i]) * abs(x[j]) * (1.0 - np.cos(dtheta))
        worst = max(worst, abs(defect - pair_formula))
        assert defect >= -1e-10

        # Any selected subset has square mass bounded by the full envelope.
        mask = rng.random(n) < 0.5
        selected_mass = np.sum(np.abs(x[mask]) ** 2)
        assert selected_mass <= envelope + 1e-10

    return worst


def test_parabolic_curvature(samples=10000, seed=20260817):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(samples):
        a = rng.integers(-20, 21, size=3).astype(float)
        b = rng.integers(-20, 21, size=3).astype(float)
        c = rng.integers(-20, 21, size=3).astype(float)
        d = a + b - c
        h = a - c
        q1 = np.dot(a, a) + np.dot(b, b) - np.dot(c, c) - np.dot(d, d)
        q2 = 2.0 * np.dot(h, c - b)
        worst = max(worst, abs(q1 - q2))
        assert abs(q1 - q2) < 1e-9
    return worst


if __name__ == "__main__":
    w1 = test_composition_defect()
    w2 = test_parabolic_curvature()
    print("composition-defect identity max abs error:", f"{w1:.3e}")
    print("parabolic-curvature identity max abs error:", f"{w2:.3e}")
