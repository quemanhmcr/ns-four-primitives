#!/usr/bin/env python3
"""Audit the chiral zero-diagonal Lanczos representation of the FGR bath."""

import numpy as np
import scipy.linalg as la

from verify_feshbach_passive_bath import (
    build_operator,
    full_shell_background,
    pair_background,
    sphere,
    canonical,
    reality_component,
    normalize_background,
)


def bath(alpha, beta, radius, bg):
    modes, A_sp, p = build_operator(alpha, beta, radius, bg)
    A = A_sp.toarray()
    mask = np.ones(len(modes), dtype=bool)
    mask[p] = False
    q = np.where(mask)[0]
    B = A[np.ix_(q, p)]
    Aqq = A[np.ix_(q, q)]
    d = np.asarray([(np.linalg.norm(modes[i][0]) / beta) ** 2 for i in q])
    ds = np.sqrt(d)
    G = B / ds[:, None]
    H = 1j * ((Aqq / ds[:, None]) / ds[None, :])
    H = 0.5 * (H + H.conj().T)
    v = np.asarray([bg.get(modes[i], 0j) for i in p])
    g = G @ v
    return H, g


def lanczos(H, g, steps=12):
    ng = np.linalg.norm(g)
    if ng < 1e-14:
        return [], []
    q = g / ng
    qprev = np.zeros_like(q)
    beta_prev = 0.0
    basis = []
    aa, bb = [], []
    for j in range(steps):
        basis.append(q.copy())
        w = H @ q - beta_prev * qprev
        a = float(np.real(np.vdot(q, w)))
        w -= a * q
        # Full reorthogonalization for the numerical audit.
        for z in basis:
            w -= np.vdot(z, w) * z
        b = float(np.linalg.norm(w))
        aa.append(a)
        if j < steps - 1:
            bb.append(b)
        if b < 1e-13:
            break
        qprev, q = q, w / b
        beta_prev = b
    return aa, bb


def random_background(alpha, beta, rng):
    z = {}
    for radius, spin in [(alpha, 1), (beta, -1)]:
        for k in sphere(radius):
            if canonical(k) != tuple(k):
                continue
            amp = rng.normal() + 1j * rng.normal()
            z.update(reality_component(k, spin, amp))
    return normalize_background(z)


def audit():
    rng = np.random.default_rng(20260816)
    max_a = 0.0
    for alpha, beta, radius in [(1, 2, 6), (2, 3, 6)]:
        for _ in range(10):
            bg = random_background(alpha, beta, rng)
            H, g = bath(alpha, beta, radius, bg)
            aa, bb = lanczos(H, g, 10)
            max_a = max(max_a, max(abs(x) for x in aa))
            assert len(bb) > 0
            # First spectral second moment equals b1^2 because a0=0.
            q0 = g / np.linalg.norm(g)
            Omega2 = float(np.real(np.vdot(H @ q0, H @ q0)))
            assert abs(Omega2 - (aa[0] ** 2 + bb[0] ** 2)) < 1e-10

    print(f"max reality-compatible Lanczos diagonal |a_n|: {max_a:.3e}")
    assert max_a < 1e-10

    cases = [
        ("full12", 1, 2, 6, full_shell_background(1, 2)),
        ("non12", 1, 2, 6, pair_background(1, 2, (1, 0, 0), (0, 2, 0))),
        ("col12", 1, 2, 6, pair_background(1, 2, (1, 0, 0), (2, 0, 0))),
        ("full23", 2, 3, 6, full_shell_background(2, 3)),
    ]
    for name, a, b, R, bg in cases:
        H, g = bath(a, b, R, bg)
        aa, bb = lanczos(H, g, 8)
        if not aa:
            print(f"{name:8s} coupling=0 (dark chain)")
            continue
        print(
            f"{name:8s} b1={bb[0]:.6f} b2={bb[1]:.6f} "
            f"max|a|={max(abs(x) for x in aa):.3e}"
        )

    # Exact continued-fraction reconstruction on a generic finite chiral chain.
    b = np.asarray([0.7, 1.2, 0.45, 0.9, 0.3])
    J = np.diag(b, 1) + np.diag(b, -1)
    eps = 0.17
    direct = float(np.real(la.inv(eps * eps * np.eye(len(J)) + J @ J)[0, 0]))
    y = 1.0 / eps
    for bj in b[::-1]:
        y = 1.0 / (eps + bj * bj * y)
    continued = y / eps
    print(f"continued-fraction reconstruction error: {abs(direct-continued):.3e}")
    assert abs(direct - continued) < 1e-10


if __name__ == "__main__":
    audit()
