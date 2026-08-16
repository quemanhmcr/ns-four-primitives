#!/usr/bin/env python3
"""Audit the exact viscous-whitened FGR renormalization identity.

This checks both generic skew+dissipative matrices and one actual helical
finite-bath compression imported from verify_feshbach_passive_bath.py.
"""

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from verify_feshbach_passive_bath import (
    build_operator,
    pair_background,
)


def generic_audit(samples=200, seed=20260816):
    rng = np.random.default_rng(seed)
    max_identity = 0.0
    max_kernel = 0.0
    min_monotone = np.inf

    for _ in range(samples):
        nq = int(rng.integers(4, 12))
        np_ = int(rng.integers(2, 7))
        M = rng.normal(size=(nq, nq)) + 1j * rng.normal(size=(nq, nq))
        A = M - M.conj().T
        d = rng.uniform(0.2, 3.0, size=nq)
        D = np.diag(d)
        B = rng.normal(size=(nq, np_)) + 1j * rng.normal(size=(nq, np_))

        ds = np.sqrt(d)
        C = (A / ds[:, None]) / ds[None, :]
        G = B / ds[:, None]

        epsilons = [0.7, 0.2, 0.05]
        prev = None
        for eps in epsilons:
            K = eps * D - A
            X = la.solve(K, B)
            Sigma = X.conj().T @ (eps * D) @ X
            Sigma = 0.5 * (Sigma + Sigma.conj().T)

            R = la.inv(eps * eps * np.eye(nq) - C @ C)
            exact = G.conj().T @ R @ G
            err = la.norm(Sigma / eps - exact) / max(1.0, la.norm(exact))
            max_identity = max(max_identity, err)

            if prev is not None:
                # eps is decreasing, so exact-prev should be PSD.
                mineig = np.min(np.linalg.eigvalsh(exact - prev))
                min_monotone = min(min_monotone, mineig)
            prev = exact

        # Kernel equivalence checked by singular values for one epsilon.
        eig = np.linalg.eigvalsh(prev)
        sv = np.linalg.svd(G, compute_uv=False)
        tol_e = max(1e-10, eig[-1] * 1e-9)
        tol_s = max(1e-10, sv[0] * 1e-9)
        null_exact = np.sum(eig <= tol_e)
        null_G = np_ - np.sum(sv > tol_s)
        max_kernel = max(max_kernel, abs(int(null_exact) - int(null_G)))

    print(f"generic samples: {samples}")
    print(f"max renormalization relative error: {max_identity:.3e}")
    print(f"minimum monotonicity eigenvalue: {min_monotone:.3e}")
    print(f"max kernel-dimension mismatch: {max_kernel:.0f}")

    assert max_identity < 1e-10
    assert min_monotone > -1e-9
    assert max_kernel == 0


def helical_audit():
    alpha, beta, radius = 1, 2, 7
    bg = pair_background(alpha, beta, (1, 0, 0), (0, 2, 0))
    modes, A, protected = build_operator(alpha, beta, radius, bg)

    # Compression of a skew operator should remain skew up to cutoff effects.
    skew_res = spla.norm(A + A.getH()) / max(1.0, spla.norm(A))

    mask = np.ones(len(modes), dtype=bool)
    mask[protected] = False
    bath = np.where(mask)[0]
    B = A[bath, :][:, protected].toarray()
    Aqq = A[bath, :][:, bath].toarray()
    d = np.asarray([(np.linalg.norm(modes[i][0]) / beta) ** 2 for i in bath])
    ds = np.sqrt(d)
    C = (Aqq / ds[:, None]) / ds[None, :]
    G = B / ds[:, None]

    epsilons = [0.3, 0.1, 0.03]
    mins = []
    prev = None
    min_mon = np.inf
    max_err = 0.0

    for eps in epsilons:
        K = eps * np.diag(d) - Aqq
        X = la.solve(K, B, assume_a="gen")
        Sigma = X.conj().T @ (eps * d[:, None] * X)
        Sigma = 0.5 * (Sigma + Sigma.conj().T)
        direct = Sigma / eps

        R = la.inv(eps * eps * np.eye(len(bath)) - C @ C)
        exact = G.conj().T @ R @ G
        exact = 0.5 * (exact + exact.conj().T)
        err = la.norm(direct - exact) / max(1.0, la.norm(exact))
        max_err = max(max_err, err)

        eig = np.linalg.eigvalsh(exact)
        pos = eig[eig > max(1e-10, eig[-1] * 1e-9)]
        mins.append(pos[0])

        if prev is not None:
            min_mon = min(min_mon, np.min(np.linalg.eigvalsh(exact - prev)))
        prev = exact

    print(f"helical skew-compression residual: {skew_res:.3e}")
    print(f"helical max renormalization relative error: {max_err:.3e}")
    print(f"helical minimum monotonicity eigenvalue: {min_mon:.3e}")
    print("helical renormalized minima:", " ".join(f"{x:.6e}" for x in mins))

    # The finite ball compression is exactly skew for this construction to numerical accuracy.
    assert skew_res < 1e-10
    assert max_err < 1e-9
    assert min_mon > -1e-8
    assert mins[2] >= mins[1] - 1e-8
    assert mins[1] >= mins[0] - 1e-8


def main():
    generic_audit()
    helical_audit()


if __name__ == "__main__":
    main()
