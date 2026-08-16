#!/usr/bin/env python3
"""Rank audit for periodic helical Galerkin transfer networks."""

import itertools
import math
import numpy as np

SQRT2 = math.sqrt(2.0)


def helical(v, s):
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
    return (e1 + 1j * s * e2) / SQRT2


def canonical_reality_rep(k):
    k = tuple(int(x) for x in k)
    for x in k:
        if x > 0:
            return k
        if x < 0:
            return tuple(-y for y in k)
    raise ValueError("zero wavevector")


def build_network(radius_squared):
    rr = int(math.sqrt(radius_squared)) + 1
    vectors = [
        k
        for k in itertools.product(range(-rr, rr + 1), repeat=3)
        if k != (0, 0, 0) and sum(x * x for x in k) <= radius_squared
    ]
    vset = set(vectors)
    reps = sorted({canonical_reality_rep(k) for k in vectors})
    modes = [(r, s) for r in reps for s in (-1, 1)]
    index = {m: i for i, m in enumerate(modes)}

    rows = []
    seen_geom = set()
    zero_geometry = 0

    for ia, a in enumerate(vectors):
        for b in vectors[ia + 1 :]:
            c = tuple(-a[d] - b[d] for d in range(3))
            if c not in vset:
                continue
            key = tuple(sorted((a, b, c)))
            if key in seen_geom:
                continue
            seen_geom.add(key)
            if np.linalg.norm(np.cross(a, b)) < 1e-12:
                continue

            radii = [np.linalg.norm(a), np.linalg.norm(b), np.linalg.norm(c)]
            reps3 = [
                canonical_reality_rep(a),
                canonical_reality_rep(b),
                canonical_reality_rep(c),
            ]

            for spins in itertools.product((-1, 1), repeat=3):
                g = np.vdot(
                    helical(a, spins[0]),
                    np.cross(helical(b, spins[1]), helical(c, spins[2])),
                )
                if abs(g) < 1e-10:
                    zero_geometry += 1
                    continue

                h = [spins[j] * radii[j] for j in range(3)]
                lam = [h[1] - h[2], h[2] - h[0], h[0] - h[1]]
                row = np.zeros(len(modes))
                for j in range(3):
                    row[index[(reps3[j], spins[j])]] += lam[j]
                if np.linalg.norm(row) > 1e-12:
                    rows.append(row)

    return modes, np.asarray(rows), zero_geometry


def audit():
    for radius_squared in [2, 3, 4, 5, 6]:
        modes, A, zero_geometry = build_network(radius_squared)
        rank = np.linalg.matrix_rank(A, tol=1e-9)
        kernel_dim = len(modes) - rank

        h = np.asarray([s * np.linalg.norm(k) for k, s in modes])
        one = np.ones(len(modes))
        one_res = np.linalg.norm(A @ one)
        h_res = np.linalg.norm(A @ h)

        print(
            f"R2={radius_squared} modes={len(modes)} rows={len(A)} "
            f"kernel={kernel_dim} zero_geom={zero_geometry} "
            f"one_res={one_res:.3e} h_res={h_res:.3e}"
        )

        assert kernel_dim == 2
        assert one_res < 1e-9
        assert h_res < 1e-8


if __name__ == "__main__":
    audit()
