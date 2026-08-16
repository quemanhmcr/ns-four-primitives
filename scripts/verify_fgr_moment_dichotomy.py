#!/usr/bin/env python3
"""Audit the FGR spectral-moment lower bound and reset-style circulation dichotomy."""

import numpy as np
import scipy.linalg as la

from verify_feshbach_passive_bath import (
    build_operator,
    full_shell_background,
    pair_background,
)


def matrices(alpha, beta, radius, bg):
    modes, A_sp, protected = build_operator(alpha, beta, radius, bg)
    A = A_sp.toarray()
    mask = np.ones(len(modes), dtype=bool)
    mask[protected] = False
    bath = np.where(mask)[0]
    B = A[np.ix_(bath, protected)]
    Aqq = A[np.ix_(bath, bath)]
    d = np.asarray([(np.linalg.norm(modes[i][0]) / beta) ** 2 for i in bath])
    ds = np.sqrt(d)
    C = (Aqq / ds[:, None]) / ds[None, :]
    G = B / ds[:, None]
    H = 1j * C
    return G, H


def audit_generic(samples=500, seed=20260816):
    rng = np.random.default_rng(seed)
    min_margin = np.inf
    max_threshold_violation = 0.0

    for _ in range(samples):
        n = int(rng.integers(4, 16))
        p = int(rng.integers(2, 8))
        X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        H = 0.5 * (X + X.conj().T)
        G = rng.normal(size=(n, p)) + 1j * rng.normal(size=(n, p))
        v = rng.normal(size=p) + 1j * rng.normal(size=p)
        g = G @ v
        m0 = float(np.real(np.vdot(g, g)))
        if m0 < 1e-12:
            continue
        Hg = H @ g
        m2 = float(np.real(np.vdot(Hg, Hg)))
        eps = 10 ** rng.uniform(-2.0, 0.0)
        R = float(np.real(np.vdot(g, la.solve(eps * eps * np.eye(n) + H @ H, g))))
        bound = m0 * m0 / (eps * eps * m0 + m2)
        min_margin = min(min_margin, R - bound)

        L = rng.uniform(0.2, 3.0)
        ew, V = la.eigh(H)
        coeff = V.conj().T @ g
        low = float(np.sum(np.abs(coeff[np.abs(ew) <= L]) ** 2))
        max_threshold_violation = max(
            max_threshold_violation, low - (eps * eps + L * L) * R
        )

    print(f"generic samples: {samples}")
    print(f"minimum moment-bound margin: {min_margin:.3e}")
    print(f"maximum spectral-threshold violation: {max_threshold_violation:.3e}")
    assert min_margin > -1e-9
    assert max_threshold_violation < 1e-8


def audit_helical():
    cases = [
        ("full", full_shell_background(1, 2)),
        ("noncollinear", pair_background(1, 2, (1, 0, 0), (0, 2, 0))),
    ]
    eps = 0.1
    for name, bg in cases:
        G, H = matrices(1, 2, 6, bg)
        M = eps * eps * np.eye(H.shape[0]) + H @ H
        Resp = G.conj().T @ la.solve(M, G)
        Resp = 0.5 * (Resp + Resp.conj().T)
        eig, vec = la.eigh(Resp)
        tol = max(1e-10, eig[-1] * 1e-9)
        ids = np.where(eig > tol)[0]
        j = ids[0]
        v = vec[:, j]
        g = G @ v
        m0 = float(np.real(np.vdot(g, g)))
        m2 = float(np.real(np.vdot(H @ g, H @ g)))
        R = float(eig[j])
        bound = m0 * m0 / (eps * eps * m0 + m2)
        Omega2 = m2 / m0
        print(
            f"{name:12s} weakest_R={R:.6e} moment_bound={bound:.6e} "
            f"ratio={R/bound:.3f} Omega2={Omega2:.6e} coupling={m0:.6e}"
        )
        assert R + 1e-10 >= bound


if __name__ == "__main__":
    audit_generic()
    audit_helical()
