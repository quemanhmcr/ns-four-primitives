#!/usr/bin/env python3
"""Algebraic audit for the two-spin self-balancing identities."""

import numpy as np


def audit(samples=20000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_defect_error = 0.0
    max_damping_error = 0.0
    min_normalized_source = float("inf")

    for _ in range(samples):
        kp = float(rng.random() + 1e-3)
        km = float(rng.random() + 1e-3)
        mp = float(rng.random() * 10 + 1e-3)
        mm = float(rng.random() * 10 + 1e-3)
        kappa = float(rng.normal())
        nu = float(rng.random() + 0.1)

        K = kp + km
        H = kp - km
        B = K * K - H * H
        max_defect_error = max(max_defect_error, abs(B - 4.0 * kp * km))

        Kprime = 2.0 * kappa - 2.0 * nu * (mp + mm)
        Hprime = -2.0 * nu * (mp - mm)
        direct = 2.0 * K * Kprime - 2.0 * H * Hprime
        factor = 4.0 * K * kappa - 8.0 * nu * (kp * mm + km * mp)
        max_damping_error = max(max_damping_error, abs(direct - factor))

        op = mp / kp
        om = mm / km
        frequency_form = 4.0 * K * kappa - 2.0 * nu * (op + om) * B
        max_damping_error = max(max_damping_error, abs(direct - frequency_form))

        if kappa >= 0:
            normalized_euler_source = 4.0 * kappa * H * H / (K ** 3)
            min_normalized_source = min(min_normalized_source, normalized_euler_source)

    print(f"samples: {samples}")
    print(f"max K^2-H^2 identity abs error: {max_defect_error:.3e}")
    print(f"max full evolution identity abs error: {max_damping_error:.3e}")
    print(f"minimum normalized Euler polarization source: {min_normalized_source:.3e}")

    assert max_defect_error < 1e-12
    assert max_damping_error < 1e-10
    assert min_normalized_source > -1e-12


if __name__ == "__main__":
    audit()
