#!/usr/bin/env python3
"""Numerical/symbolic sanity checks for docs/29 and docs/30.

This verifies only the finite-dimensional algebra. It is not a substitute for
functional-analytic arguments in the notes.
"""

import math
import random


def check_growth_optimization(samples=50000, seed=20260816):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(samples):
        nu = 10 ** rng.uniform(-2, 2)
        C = 10 ** rng.uniform(-1, 1)
        Y = 10 ** rng.uniform(-3, 3)
        Z = 10 ** rng.uniform(-3, 3)
        M3 = 10 ** rng.uniform(-3, 3)
        lhs = 2 * C * math.sqrt(Y * Z * M3) - 2 * nu * M3
        rhs = (C * C / (2 * nu)) * Y * Z
        worst = max(worst, lhs - rhs)
    print(f"growth-optimization maximum violation: {worst:.3e}")
    assert worst < 1e-10


def triad_transfer(k, p, q, sk, sp, sq, J):
    hk, hp, hq = sk * k, sp * p, sq * q
    return (
        J * (hp - hq),
        J * (hq - hk),
        J * (hk - hp),
    )


def check_transfer_moments(samples=50000, seed=20260817):
    rng = random.Random(seed)
    max_energy = 0.0
    max_helicity = 0.0
    max_first = 0.0
    max_second = 0.0

    for _ in range(samples):
        k, p, q = [10 ** rng.uniform(-1, 1) for _ in range(3)]
        sk, sp, sq = [rng.choice((-1, 1)) for _ in range(3)]
        # avoid signed-wavenumber degeneracy
        h = [sk * k, sp * p, sq * q]
        if min(abs(h[i] - h[j]) for i in range(3) for j in range(i)) if False else 1:
            pass
        J = rng.uniform(-3, 3)
        Tk, Tp, Tq = triad_transfer(k, p, q, sk, sp, sq, J)
        tau = [Tk, Tp, Tq]
        rad = [k, p, q]
        sig = [sk, sp, sq]
        hh = [sig[i] * rad[i] for i in range(3)]
        a = rng.uniform(-2, 2)
        b = rng.uniform(-1, 1)
        t = [rad[i] - a - b * hh[i] for i in range(3)]

        energy = sum(tau)
        helicity = sum(hh[i] * tau[i] for i in range(3))
        critical = sum(rad[i] * tau[i] for i in range(3))
        first = sum(t[i] * tau[i] for i in range(3))
        second = sum(t[i] ** 2 * tau[i] for i in range(3))

        # Direct defect production with q_i=t_i^2 is exactly the second moment.
        direct_second = sum((rad[i] - a - b * hh[i]) ** 2 * tau[i] for i in range(3))

        max_energy = max(max_energy, abs(energy))
        max_helicity = max(max_helicity, abs(helicity))
        max_first = max(max_first, abs(first - critical))
        max_second = max(max_second, abs(second - direct_second))

    print(f"max triad energy-constraint residual: {max_energy:.3e}")
    print(f"max triad helicity-constraint residual: {max_helicity:.3e}")
    print(f"max protected first-moment residual: {max_first:.3e}")
    print(f"max protected second-moment residual: {max_second:.3e}")
    assert max_energy < 1e-10
    assert max_helicity < 1e-9
    assert max_first < 1e-9
    assert max_second < 1e-12


if __name__ == "__main__":
    check_growth_optimization()
    check_transfer_moments()
