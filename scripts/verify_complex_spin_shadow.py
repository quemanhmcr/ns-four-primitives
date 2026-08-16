#!/usr/bin/env python3
"""Audit the complex double-angle Spin-Shadow identity."""

import math
import random
import numpy as np

SQRT2 = math.sqrt(2.0)


def frame(v):
    v = np.asarray(v, dtype=float)
    khat = v / np.linalg.norm(v)
    refs = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]
    ref = min(refs, key=lambda r: abs(np.dot(r, khat)))
    e1 = np.cross(ref, khat)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(khat, e1)
    return e1, e2


def helical(v, s):
    e1, e2 = frame(v)
    return (e1 + 1j * s * e2) / SQRT2


def pair_coefficient(a, b, t, sa, sb):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    r = a + b
    prefactor = sb * np.linalg.norm(b) - sa * np.linalg.norm(a)
    return prefactor * np.vdot(
        helical(r, t), np.cross(helical(a, sa), helical(b, sb))
    )


def audit(samples=10000, seed=20260820):
    random.seed(seed)
    rng = np.random.default_rng(seed)
    worst = 0.0
    accepted = 0

    while accepted < samples:
        a = rng.normal(size=3)
        b = rng.normal(size=3)
        r = a + b
        if (
            np.linalg.norm(a) < 1e-8
            or np.linalg.norm(b) < 1e-8
            or np.linalg.norm(r) < 1e-8
            or np.linalg.norm(np.cross(a, b)) < 1e-8
            or abs(np.linalg.norm(a) - np.linalg.norm(b)) < 1e-8
        ):
            continue

        s = random.choice([-1, 1])
        csh = pair_coefficient(a, b, s, s, s)
        ccat = pair_coefficient(a, b, -s, s, s)
        if abs(ccat) < 1e-12:
            continue

        e1, e2 = frame(r)
        rh = r / np.linalg.norm(r)
        x = (a - b) / 2.0
        xp = x - np.dot(x, rh) * rh
        if np.linalg.norm(xp) < 1e-10:
            continue
        phi = math.atan2(np.dot(xp, e2), np.dot(xp, e1))

        S = np.linalg.norm(a) + np.linalg.norm(b)
        rho = np.linalg.norm(r)
        pred = ((S + rho) / (S - rho)) * np.exp(-2j * s * phi)
        got = csh / ccat
        err = abs(got - pred) / max(1e-14, abs(pred))
        worst = max(worst, err)
        accepted += 1

    print("samples:", samples)
    print("max complex spin-shadow relative error:", f"{worst:.3e}")
    assert worst < 1e-8


if __name__ == "__main__":
    audit()


def audit_phase_plane_tradeoff(samples=20000, seed=20260821):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(samples):
        n = int(rng.integers(2, 10))
        w = rng.uniform(0.01, 3.0, size=n)
        delta = rng.uniform(-math.pi, math.pi, size=n)
        phi = rng.uniform(-math.pi, math.pi, size=n)
        s = random.choice([-1, 1])
        d_shadow = 0.0
        d_cat = 0.0
        d_plane = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                wij = 2.0 * w[i] * w[j]
                d_shadow += wij * (
                    1.0
                    - math.cos((delta[i] - delta[j]) - 2.0 * s * (phi[i] - phi[j]))
                )
                d_cat += wij * (1.0 - math.cos(delta[i] - delta[j]))
                d_plane += wij * (1.0 - math.cos(2.0 * (phi[i] - phi[j])))
        margin = d_shadow - (0.5 * d_plane - d_cat)
        worst = min(worst, margin)
        assert margin >= -1e-10
    print("phase-plane tradeoff minimum margin:", f"{worst:.3e}")


if __name__ == "__main__":
    audit_phase_plane_tradeoff()
