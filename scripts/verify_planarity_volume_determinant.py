#!/usr/bin/env python3
"""Numerical audit for the critical planarity determinant identities."""

import itertools
import numpy as np


def audit(samples=3000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_cb_error = 0.0
    min_triple_margin = float("inf")
    min_visc_margin = float("inf")
    max_v_fraction = 0.0
    max_weighted_visc_error = 0.0

    for _ in range(samples):
        n = int(rng.integers(3, 10))
        vecs = rng.normal(size=(n, 3))
        vecs /= np.linalg.norm(vecs, axis=1)[:, None]
        masses = rng.random(n) + 0.05

        A = sum(m * np.outer(v, v) for m, v in zip(masses, vecs))
        detA = float(np.linalg.det(A))

        cb = 0.0
        for i, j, k in itertools.combinations(range(n), 3):
            triple = float(np.dot(vecs[i], np.cross(vecs[j], vecs[k])))
            cb += masses[i] * masses[j] * masses[k] * triple * triple
        max_cb_error = max(max_cb_error, abs(detA - cb))

        # Triple lower bound for lambda_min.
        ids = rng.choice(n, size=3, replace=False)
        vv = vecs[ids]
        mm = masses[ids]
        A3 = sum(m * np.outer(v, v) for m, v in zip(mm, vv))
        lam3 = float(np.linalg.eigvalsh(A3)[0])
        tau = abs(float(np.dot(vv[0], np.cross(vv[1], vv[2]))))
        lower = 4.0 * np.prod(mm) * tau * tau / (np.sum(mm) ** 2)
        min_triple_margin = min(min_triple_margin, lam3 - lower)

        # Build an artificial H satisfying the directional lower bound in the
        # eigenbasis, then audit the cofactor trace inequality.
        evals, Q = np.linalg.eigh(A)
        E = float(rng.random() + 1.0)
        Hdiag = evals * evals / E + rng.random(3)
        H = Q @ np.diag(Hdiag) @ Q.T
        cof = detA * np.linalg.inv(A) if detA > 1e-10 else np.zeros((3, 3))
        lhs = float(np.trace(cof @ H))
        rhs = float(np.trace(A) * detA / E)
        min_visc_margin = min(min_visc_margin, lhs - rhs)

        # Exact volume-weighted viscous spectrum identity.
        radii = rng.uniform(0.5, 4.0, size=n)
        Hvol = sum((rad * rad) * m * np.outer(v, v)
                   for rad, m, v in zip(radii, masses, vecs))
        if detA > 1e-10:
            cofA = detA * np.linalg.inv(A)
        else:
            # adjugate via eigen-decomposition, stable enough for audit
            ev, QQ = np.linalg.eigh(A)
            cofA = QQ @ np.diag([ev[1]*ev[2], ev[0]*ev[2], ev[0]*ev[1]]) @ QQ.T
        lhs_vol = float(np.trace(cofA @ Hvol))
        rhs_vol = 0.0
        for i, j, k in itertools.combinations(range(n), 3):
            triple = float(np.dot(vecs[i], np.cross(vecs[j], vecs[k])))
            rhs_vol += ((radii[i]**2 + radii[j]**2 + radii[k]**2)
                        * masses[i] * masses[j] * masses[k] * triple * triple)
        max_weighted_visc_error = max(max_weighted_visc_error, abs(lhs_vol-rhs_vol))

        K = float(np.trace(A))
        V = 27.0 * detA / (K ** 3)
        max_v_fraction = max(max_v_fraction, V)

    print(f"samples: {samples}")
    print(f"max Cauchy-Binet determinant abs error: {max_cb_error:.3e}")
    print(f"minimum triple lambda_min lower-bound margin: {min_triple_margin:.3e}")
    print(f"minimum cofactor viscous-bound margin: {min_visc_margin:.3e}")
    print(f"maximum normalized volume fraction: {max_v_fraction:.6f}")
    print(f"max volume-weighted viscous identity abs error: {max_weighted_visc_error:.3e}")

    assert max_cb_error < 1e-10
    assert min_triple_margin > -1e-10
    assert min_visc_margin > -1e-9
    assert max_v_fraction <= 1.0 + 1e-10
    assert max_weighted_visc_error < 1e-9


if __name__ == "__main__":
    audit()
