#!/usr/bin/env python3
"""Finite Fourier audit for the global critical planarity tensor."""

import numpy as np


def audit(samples=5000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_trace_error = 0.0
    min_psd = float("inf")
    min_riccati_margin = float("inf")
    max_planar_eig = 0.0

    for _ in range(samples):
        m = int(rng.integers(3, 20))
        ks = []
        amps = []
        while len(ks) < m:
            k = rng.integers(-5, 6, size=3).astype(float)
            if np.linalg.norm(k) < 0.5:
                continue
            ks.append(k)
            amps.append(float(rng.random() + 0.05))
        ks = np.array(ks)
        amps = np.array(amps)
        norms = np.linalg.norm(ks, axis=1)

        A = np.zeros((3, 3))
        K = 0.0
        E = float(np.sum(amps))
        for k, w, kn in zip(ks, amps, norms):
            A += w * np.outer(k, k) / kn
            K += w * kn

        evals, evecs = np.linalg.eigh(A)
        min_psd = min(min_psd, float(np.min(evals)))
        max_trace_error = max(max_trace_error, abs(np.trace(A) - K))

        n = evecs[:, 0]
        P = float(n @ A @ n)
        H = float(np.sum(amps * norms * (ks @ n) ** 2))
        min_riccati_margin = min(min_riccati_margin, E * H - P * P)

        # Exact planar sample: all modes have k_3=0.
        kp = rng.integers(-5, 6, size=(m, 2)).astype(float)
        kp = np.column_stack([kp, np.zeros(m)])
        keep = np.linalg.norm(kp, axis=1) > 0.5
        kp = kp[keep]
        if len(kp):
            wp = rng.random(len(kp)) + 0.05
            Ap = np.zeros((3, 3))
            for k, w in zip(kp, wp):
                Ap += w * np.outer(k, k) / np.linalg.norm(k)
            max_planar_eig = max(max_planar_eig, abs(np.linalg.eigvalsh(Ap)[0]))

    print(f"samples: {samples}")
    print(f"max trace identity abs error: {max_trace_error:.3e}")
    print(f"minimum tensor eigenvalue: {min_psd:.3e}")
    print(f"minimum E*H-P^2 margin: {min_riccati_margin:.3e}")
    print(f"max planar minimum-eigenvalue error: {max_planar_eig:.3e}")

    assert max_trace_error < 1e-10
    assert min_psd > -1e-10
    assert min_riccati_margin > -1e-9
    assert max_planar_eig < 1e-10


if __name__ == "__main__":
    audit()
