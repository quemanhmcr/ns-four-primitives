#!/usr/bin/env python3
"""Finite-dimensional gate tests for the passive Feshbach bath.

This is a falsification aid for docs/46--48, not an infinite-dimensional
Navier--Stokes theorem.
"""

import itertools
import math
from functools import lru_cache

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

SQRT2 = math.sqrt(2.0)


@lru_cache(None)
def helical(k, s):
    k = np.asarray(k, dtype=float)
    khat = k / np.linalg.norm(k)
    refs = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]
    ref = min(refs, key=lambda r: abs(np.dot(r, khat)))
    e1 = np.cross(ref, khat)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(khat, e1)
    return (e1 + 1j * s * e2) / SQRT2


def ball(radius):
    rr = int(radius)
    return [
        k
        for k in itertools.product(range(-rr, rr + 1), repeat=3)
        if k != (0, 0, 0) and sum(x * x for x in k) <= radius * radius
    ]


def sphere(radius):
    rr = int(radius)
    return [
        k
        for k in itertools.product(range(-rr, rr + 1), repeat=3)
        if k != (0, 0, 0) and sum(x * x for x in k) == radius * radius
    ]


def canonical(k):
    km = tuple(-x for x in k)
    for x in k:
        if x > 0:
            return tuple(k)
        if x < 0:
            return km
    raise ValueError("zero wavevector")


def reality_component(k, s, amplitude):
    uk = amplitude * helical(tuple(k), s)
    km = tuple(-x for x in k)
    return {
        (tuple(k), s): amplitude + 0j,
        (km, s): np.vdot(helical(km, s), np.conj(uk)),
    }


def normalize_background(z):
    energy = sum(abs(v) ** 2 for v in z.values())
    return {key: val / math.sqrt(energy) for key, val in z.items()}


def full_shell_background(alpha, beta):
    z = {}
    for radius, spin in [(alpha, 1), (beta, -1)]:
        for k in sphere(radius):
            if canonical(k) != tuple(k):
                continue
            z.update(reality_component(k, spin, 1.0))
    return normalize_background(z)


def pair_background(alpha, beta, ka, kb):
    z = {}
    z.update(reality_component(ka, 1, 1.0))
    z.update(reality_component(kb, -1, 1.0))
    return normalize_background(z)


def heatline_perturbation(delta):
    z = {}
    z.update(reality_component((1, 0, 0), 1, 1.0))
    z.update(reality_component((0, 1, 0), 1, delta))
    z.update(reality_component((2, 0, 0), -1, 1.0))
    return normalize_background(z)


def build_operator(alpha, beta, radius, background):
    vectors = ball(radius)
    modes = [(tuple(k), s) for k in vectors for s in (-1, 1)]
    index = {mode: i for i, mode in enumerate(modes)}

    rows, cols, data = [], [], []
    for j, (p, spn) in enumerate(modes):
        hp = helical(p, spn)
        for (q, sq), zq in background.items():
            out = tuple(p[d] + q[d] for d in range(3))
            if out == (0, 0, 0):
                continue
            hq = helical(q, sq)
            for t in (-1, 1):
                i = index.get((out, t))
                if i is None:
                    continue
                coeff = (
                    sq
                    * np.linalg.norm(q)
                    * zq
                    * np.vdot(helical(out, t), np.cross(hp, hq))
                )
                if abs(coeff) > 1e-13:
                    rows.append(i)
                    cols.append(j)
                    data.append(coeff)

    A = sp.coo_matrix(
        (data, (rows, cols)), shape=(len(modes), len(modes)), dtype=complex
    ).tocsc()
    A /= beta

    protected = np.asarray(
        [
            i
            for i, (k, s) in enumerate(modes)
            if (s == 1 and abs(np.linalg.norm(k) - alpha) < 1e-12)
            or (s == -1 and abs(np.linalg.norm(k) - beta) < 1e-12)
        ],
        dtype=int,
    )
    return modes, A, protected


def feshbach_spectrum(alpha, beta, radius, background, epsilon):
    modes, A, protected = build_operator(alpha, beta, radius, background)
    mask = np.ones(len(modes), dtype=bool)
    mask[protected] = False
    bath = np.where(mask)[0]

    B = A[bath, :][:, protected]
    Aqq = A[bath, :][:, bath]
    d2 = np.asarray(
        [(np.linalg.norm(modes[i][0]) / beta) ** 2 for i in bath], dtype=float
    )

    K = (sp.diags(epsilon * d2) - Aqq).tocsc()
    lu = spla.splu(K)
    X = np.column_stack(
        [lu.solve(B[:, j].toarray().ravel()) for j in range(len(protected))]
    )
    Sigma = X.conj().T @ (epsilon * d2[:, None] * X)
    Sigma = 0.5 * (Sigma + Sigma.conj().T)
    eig = np.linalg.eigvalsh(Sigma)
    tol = max(1e-12, eig[-1] * 1e-9)
    positive = eig[eig > tol]
    return positive


def audit_cutoff():
    bg = full_shell_background(1, 2)
    vals = []
    for radius in [4, 5, 6]:
        pos = feshbach_spectrum(1, 2, radius, bg, 0.1)
        eta = pos[0] / pos[-1]
        vals.append((radius, len(pos), eta, pos[0], pos[-1]))
        print(
            f"full R={radius} rank={len(pos)}/12 eta={eta:.6f} "
            f"min={pos[0]:.6f} max={pos[-1]:.6f}"
        )
    assert all(rank == 11 for _, rank, *_ in vals)
    assert abs(vals[-1][3] - vals[-2][3]) < 0.01


def audit_dark_and_noncollinear():
    col = pair_background(1, 2, (1, 0, 0), (2, 0, 0))
    non = pair_background(1, 2, (1, 0, 0), (0, 2, 0))
    pcol = feshbach_spectrum(1, 2, 6, col, 0.1)
    pnon = feshbach_spectrum(1, 2, 6, non, 0.1)
    print(f"collinear rank={len(pcol)}/12")
    print(
        f"noncollinear rank={len(pnon)}/12 eta={pnon[0]/pnon[-1]:.6f} "
        f"min={pnon[0]:.6f}"
    )
    assert len(pcol) == 8
    assert len(pnon) == 11


def audit_strong_coupling():
    bg = pair_background(1, 2, (1, 0, 0), (0, 2, 0))
    ratios = []
    for epsilon in [0.3, 0.1, 0.03, 0.01]:
        pos = feshbach_spectrum(1, 2, 7, bg, epsilon)
        scaled = pos[0] / epsilon
        ratios.append(scaled)
        print(
            f"epsilon={epsilon:.3f} min={pos[0]:.6e} "
            f"min/epsilon={scaled:.6f} eta={pos[0]/pos[-1]:.6f}"
        )
    assert ratios[-1] > 0.5


def audit_heatline_opening():
    deltas = np.asarray([1e-3, 3e-3, 1e-2, 3e-2, 1e-1])
    mins = []
    for delta in deltas:
        pos = feshbach_spectrum(1, 2, 6, heatline_perturbation(float(delta)), 0.1)
        assert len(pos) == 11
        mins.append(pos[0])
    mins = np.asarray(mins)
    slope = np.polyfit(np.log(deltas), np.log(mins), 1)[0]
    ratio = mins / deltas**2
    print(f"heatline loglog slope={slope:.6f}")
    print(
        f"heatline min(lambda/delta^2)={ratio.min():.6f} "
        f"max={ratio.max():.6f}"
    )
    assert abs(slope - 2.0) < 0.01


def main():
    audit_cutoff()
    audit_dark_and_noncollinear()
    audit_strong_coupling()
    audit_heatline_opening()


if __name__ == "__main__":
    main()
