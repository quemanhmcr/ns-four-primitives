#!/usr/bin/env python3
"""Finite-dimensional audits of the protected connection-curvature identities."""

import numpy as np
from scipy.linalg import expm


def audit(seed=20260816, n=9):
    rng = np.random.default_rng(seed)
    nu = 0.23

    # Skew Euler connection.
    M = rng.normal(size=(n, n))
    A = M - M.T

    # Fourier-like positive Lambda and a self-adjoint T commuting with it.
    lam = rng.uniform(0.5, 3.0, size=n)
    D = np.diag(lam)
    D2 = D @ D
    tdiag = rng.normal(size=n)
    T = np.diag(tdiag)
    Tdot = np.diag(rng.normal(size=n))

    L = A - nu * D2
    u = rng.normal(size=n)
    r = T @ u
    K = Tdot + T @ A - A @ T

    # Covariant defect equation.
    rdot_direct = Tdot @ u + T @ (L @ u)
    rdot_cov = L @ r + K @ u
    err_cov = np.linalg.norm(rdot_direct - rdot_cov)

    # Defect energy balance.
    ydot_direct = 2.0 * np.dot(r, rdot_direct)
    ydot_cov = 2.0 * np.dot(r, K @ u) - 2.0 * nu * np.dot(D @ r, D @ r)
    err_energy = abs(ydot_direct - ydot_cov)

    # Static-T cocycle/Duhamel curvature identity.
    Tdot0 = np.zeros_like(T)
    K0 = T @ A - A @ T
    L0 = L
    horizon = 0.17
    U = expm(L0 * horizon)
    C_exact = T @ U - U @ T

    # Midpoint quadrature of integral U(t,tau) K U(tau,s) d tau.
    m = 4000
    dt = horizon / m
    C_quad = np.zeros_like(T)
    for j in range(m):
        tau = (j + 0.5) * dt
        C_quad += expm(L0 * (horizon - tau)) @ K0 @ expm(L0 * tau) * dt
    err_duhamel = np.linalg.norm(C_exact - C_quad) / max(1.0, np.linalg.norm(C_exact))

    # Protected reset: choose kernel coordinates of T and support u there.
    Tprot = np.diag([0.0, 0.0] + list(rng.uniform(0.4, 2.0, size=n - 2)))
    uprot = np.zeros(n)
    uprot[:2] = rng.normal(size=2)
    rprot = Tprot @ uprot
    Kprot = Tprot @ A - A @ Tprot
    Fprot = A @ uprot
    open1 = Kprot @ uprot
    open2 = Tprot @ Fprot
    err_reset = np.linalg.norm(open1 - open2)
    accel = 2.0 * np.dot(open1, open1)

    print(f"covariant defect residual: {err_cov:.3e}")
    print(f"defect energy-balance residual: {err_energy:.3e}")
    print(f"Duhamel curvature relative residual: {err_duhamel:.3e}")
    print(f"protected reset opening residual: {err_reset:.3e}")
    print(f"sample protected opening acceleration: {accel:.6e}")

    assert err_cov < 1e-11
    assert err_energy < 1e-10
    assert err_duhamel < 2e-7
    assert err_reset < 1e-11
    assert np.linalg.norm(rprot) < 1e-14


if __name__ == "__main__":
    audit()
