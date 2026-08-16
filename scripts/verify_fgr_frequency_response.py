#!/usr/bin/env python3
"""Frequency-resolved Feshbach/FGR audit on frozen protected packets."""

import numpy as np
import scipy.linalg as la

from verify_feshbach_passive_bath import (
    build_operator,
    full_shell_background,
    pair_background,
)


def response(alpha, beta, radius, bg, epsilon, omega):
    modes, A_sp, protected = build_operator(alpha, beta, radius, bg)
    A = A_sp.toarray()
    mask = np.ones(len(modes), dtype=bool)
    mask[protected] = False
    bath = np.where(mask)[0]
    B = A[np.ix_(bath, protected)]
    Aqq = A[np.ix_(bath, bath)]
    App = A[np.ix_(protected, protected)]
    d = np.asarray([(np.linalg.norm(modes[i][0]) / beta) ** 2 for i in bath])
    ds = np.sqrt(d)
    G = B / ds[:, None]
    Comega = ((Aqq - 1j * omega * np.eye(len(bath))) / ds[:, None]) / ds[None, :]
    R = la.inv(epsilon * epsilon * np.eye(len(bath)) - Comega @ Comega)
    H = G.conj().T @ R @ G
    H = 0.5 * (H + H.conj().T)
    return H, App


def on_shell(alpha, beta, radius, bg, epsilon=0.1):
    H0, App = response(alpha, beta, radius, bg, epsilon, 0.0)
    # i*App is Hermitian with eigenvalues -mu if App eigenvalue i*mu; sign is immaterial.
    freqs, vecs = la.eigh(1j * App)
    values = []
    for j, om in enumerate(freqs):
        H, _ = response(alpha, beta, radius, bg, epsilon, float(-om))
        v = vecs[:, j]
        values.append(float(np.real(np.vdot(v, H @ v))))
    return np.asarray(freqs), np.asarray(values), np.linalg.eigvalsh(H0)


def audit():
    cases = [
        ("full", full_shell_background(1, 2)),
        ("noncollinear", pair_background(1, 2, (1, 0, 0), (0, 2, 0))),
        ("collinear", pair_background(1, 2, (1, 0, 0), (2, 0, 0))),
    ]
    for name, bg in cases:
        freqs, vals, eig0 = on_shell(1, 2, 6, bg, 0.1)
        nz = vals[vals > 1e-10]
        print(
            f"{name:12s} max|omega_P|={np.max(np.abs(freqs)):.6f} "
            f"on-shell-positive={len(nz)}/{len(vals)} "
            f"min_on_shell={np.min(nz) if len(nz) else 0:.6e} "
            f"median={np.median(nz) if len(nz) else 0:.6e}"
        )
        # Full and noncollinear packets should not lose all positive response on protected free modes.
        if name != "collinear":
            assert len(nz) >= len(vals) - 1
            assert np.min(nz) > 1e-4

    # Algebraic identity at arbitrary frequencies on a generic random matrix.
    rng = np.random.default_rng(123)
    nq, np_ = 9, 4
    M = rng.normal(size=(nq, nq)) + 1j * rng.normal(size=(nq, nq))
    A = M - M.conj().T
    d = rng.uniform(0.3, 2.0, size=nq)
    D = np.diag(d)
    B = rng.normal(size=(nq, np_)) + 1j * rng.normal(size=(nq, np_))
    ds = np.sqrt(d)
    G = B / ds[:, None]
    maxerr = 0.0
    minmon = np.inf
    for omega in [-3.1, -0.7, 0.0, 1.4, 4.2]:
        Cw = ((A - 1j * omega * np.eye(nq)) / ds[:, None]) / ds[None, :]
        previous = None
        for eps in [0.5, 0.1, 0.02]:
            K = eps * D - A + 1j * omega * np.eye(nq)
            X = la.solve(K, B)
            Sigma = X.conj().T @ (eps * D) @ X
            Sigma = 0.5 * (Sigma + Sigma.conj().T)
            exact = G.conj().T @ la.inv(eps * eps * np.eye(nq) - Cw @ Cw) @ G
            exact = 0.5 * (exact + exact.conj().T)
            maxerr = max(maxerr, la.norm(Sigma / eps - exact) / max(1.0, la.norm(exact)))
            if previous is not None:
                minmon = min(minmon, np.min(np.linalg.eigvalsh(exact - previous)))
            previous = exact
    print(f"frequency identity max relative error: {maxerr:.3e}")
    print(f"frequency monotonicity min eigenvalue: {minmon:.3e}")
    assert maxerr < 1e-10
    assert minmon > -1e-9


if __name__ == "__main__":
    audit()
