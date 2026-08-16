#!/usr/bin/env python3
"""Audit algebraic identities of the finite-network V-H flow.

The tests are finite-dimensional and do not assert equivalence with Navier-Stokes.
"""

import itertools
import math
import numpy as np
from scipy.integrate import solve_ivp


def transfer_row(h, tri):
    i, j, k = tri
    row = np.zeros(len(h))
    row[i] = h[j] - h[k]
    row[j] = h[k] - h[i]
    row[k] = h[i] - h[j]
    return row


def nullspace(A, tol=1e-10):
    u, s, vh = np.linalg.svd(A, full_matrices=True)
    rank = np.sum(s > tol)
    return vh[rank:].T


def weighted_distance_to_kernel(A, C, v):
    N = nullspace(A)
    if N.shape[1] == 0:
        return float(np.sum(C * v * v))
    G = N.T @ (C[:, None] * N)
    rhs = N.T @ (C * v)
    coeff = np.linalg.solve(G, rhs)
    r = v - N @ coeff
    return float(np.sum(C * r * r))


def audit(seed=20260816):
    rng = np.random.default_rng(seed)

    # Signed frequencies with both helicities and no accidental duplicates.
    h = np.array([-5.2, -3.1, -1.4, 0.9, 2.3, 4.7, 6.4], dtype=float)
    n = len(h)
    tris = list(itertools.combinations(range(n), 3))
    A = np.vstack([transfer_row(h, t) for t in tris])
    w = rng.uniform(0.3, 2.0, size=len(tris))
    W = np.diag(w)
    L = A.T @ W @ A

    one = np.ones(n)
    assert np.linalg.norm(A @ one) < 1e-12
    assert np.linalg.norm(A @ h) < 1e-12

    # A complete triple network should have only the two affine invariants.
    ns = nullspace(A)
    kernel_dim = ns.shape[1]
    print(f"complete-network kernel dimension: {kernel_dim}")
    assert kernel_dim == 2

    C = rng.uniform(0.4, 1.8, size=n)
    q = 1.0 / C
    flow = L @ q

    # Invariants.
    e_res = abs(one @ flow)
    h_res = abs(h @ flow)
    print(f"energy derivative residual: {e_res:.3e}")
    print(f"helicity derivative residual: {h_res:.3e}")
    assert e_res < 1e-10
    assert h_res < 1e-10

    # Entropy production.
    sdot = q @ flow
    sdot_rhs = (A @ q) @ (W @ (A @ q))
    print(f"entropy identity residual: {abs(sdot-sdot_rhs):.3e}")
    assert abs(sdot - sdot_rhs) < 1e-10
    assert sdot_rhs >= -1e-12

    # Curvature decay.
    qdot = -(q * q) * flow
    Rdot = qdot @ (L @ q)
    Rdot_rhs = -np.sum((q * flow) ** 2)
    print(f"curvature-decay identity residual: {abs(Rdot-Rdot_rhs):.3e}")
    assert abs(Rdot - Rdot_rhs) < 1e-9
    assert Rdot_rhs <= 1e-12

    evals = np.linalg.eigvalsh(L)
    lam_plus = np.min(evals[evals > 1e-9])
    R = 0.5 * q @ (L @ q)
    E = float(np.sum(C))
    gap_margin = (-Rdot_rhs) - (2.0 * lam_plus / (E * E)) * R
    print(f"spectral-gap curvature-decay margin: {gap_margin:.3e}")
    assert gap_margin >= -1e-7

    Nker = nullspace(A)
    Pker = Nker @ Nker.T
    dist_q2 = np.sum((q - Pker @ q) ** 2)
    canonical_margin = 2.0 * R / lam_plus - dist_q2
    print(f"canonical-neighborhood margin: {canonical_margin:.3e}")
    assert canonical_margin >= -1e-8

    # V-curvature: homochiral flatness and heterochiral kink formula.
    # Synthetic triad h=(k,q,-p).
    k, qq, p = 2.0, 5.0, 3.0
    hh = np.array([k, qq, -p])
    lam = transfer_row(hh, (0, 1, 2))
    vv = np.abs(hh)
    got = lam @ vv
    pred = 2.0 * p * (k - qq)
    print(f"heterochiral V-curvature residual: {abs(got-pred):.3e}")
    assert abs(got - pred) < 1e-12

    hh2 = np.array([1.0, 2.5, 4.2])
    lam2 = transfer_row(hh2, (0, 1, 2))
    assert abs(lam2 @ np.abs(hh2)) < 1e-12

    # Densification monotonicity of network-protected V defect.
    v = np.abs(h)
    A_sparse = A[:4]
    A_mid = A[:12]
    y_sparse = weighted_distance_to_kernel(A_sparse, C, v)
    y_mid = weighted_distance_to_kernel(A_mid, C, v)
    y_full = weighted_distance_to_kernel(A, C, v)
    print("network V-defects sparse/mid/full:", y_sparse, y_mid, y_full)
    assert y_mid + 1e-10 >= y_sparse
    assert y_full + 1e-10 >= y_mid

    # H-flow critical-speed inequality.
    cV = A @ v
    Kdot = cV @ (W @ (A @ q))
    DV = cV @ (W @ cV)
    DH = (A @ q) @ (W @ (A @ q))
    margin = DV * DH - Kdot * Kdot
    print(f"H-flow critical-speed Cauchy margin: {margin:.3e}")
    assert margin >= -1e-8

    # Exact deterministic/H-current split with arbitrary triad current.
    JE = rng.normal(size=len(tris))
    JH = W @ (A @ q)
    Jc = JE - JH
    euler = A.T @ JE
    split = L @ q + A.T @ Jc
    print(f"current split residual: {np.linalg.norm(euler-split):.3e}")
    assert np.linalg.norm(euler - split) < 1e-10

    DE = q @ euler
    coh_term = (A @ q) @ Jc
    print(f"deterministic entropy split residual: {abs(DE-(DH+coh_term)):.3e}")
    assert abs(DE - (DH + coh_term)) < 1e-10

    CH = Jc @ np.linalg.solve(W, Jc)
    coh_bound_margin = DH * CH - coh_term * coh_term
    print(f"coherence Cauchy margin: {coh_bound_margin:.3e}")
    assert coh_bound_margin >= -1e-8

    # Integrate a short H-flow trajectory and verify monotonic S/R and invariants.
    E0 = float(np.sum(C))
    H0 = float(h @ C)

    def rhs(_s, x):
        return L @ (1.0 / x)

    sol = solve_ivp(rhs, (0.0, 0.02), C, rtol=1e-10, atol=1e-12, max_step=2e-4)
    assert sol.success
    X = sol.y.T
    Ss = np.sum(np.log(X), axis=1)
    Rs = []
    for x in X:
        qqv = 1.0 / x
        Rs.append(0.5 * qqv @ (L @ qqv))
    Rs = np.asarray(Rs)
    print(f"min entropy increment: {np.min(np.diff(Ss)):.3e}")
    print(f"max curvature increment: {np.max(np.diff(Rs)):.3e}")
    print(f"max energy drift: {np.max(np.abs(np.sum(X,axis=1)-E0)):.3e}")
    print(f"max helicity drift: {np.max(np.abs(X@h-H0)):.3e}")
    assert np.min(np.diff(Ss)) >= -1e-9
    assert np.max(np.diff(Rs)) <= 1e-7
    assert np.max(np.abs(np.sum(X, axis=1) - E0)) < 1e-8
    assert np.max(np.abs(X @ h - H0)) < 1e-8


if __name__ == "__main__":
    audit()
