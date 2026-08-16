#!/usr/bin/env python3
"""Contrast planar sparse and genuinely-3D sparse protected backgrounds.

Both branches use + helicity on |k|=1 and - helicity on |k|=n with exact
reality pairing and no output cutoff.  The planar branch has one high-shell
axis pair; the 3D branch adds a second orthogonal high-shell axis pair while
keeping the two helicity sectors energy-balanced.

The audit asks whether depth-two protected observability distinguishes the
known 2D3C-safe geometry from a genuinely 3D perturbation.
"""
import importlib.util, math, numpy as np

spec = importlib.util.spec_from_file_location(
    "d", "scripts/verify_exact_protected_bracket_depth.py"
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
g = d.g


def audit(n, three_d):
    alpha, beta, N = 1.0, float(n), float(n)
    aa = 2 * alpha * beta / (alpha + beta)
    bb = (alpha - beta) / (alpha + beta)
    Pm = [(k, +1) for k in g.shell(1)] + [(k, -1) for k in g.shell(n * n)]
    pidx = {m: i for i, m in enumerate(Pm)}
    p = len(Pm)

    if three_d:
        raw = [
            ((1, 0, 0), +1, 1.0),
            ((0, n, 0), -1, 1 / math.sqrt(2)),
            ((0, 0, n), -1, 1 / math.sqrt(2)),
        ]
    else:
        raw = [
            ((1, 0, 0), +1, 1.0),
            ((0, n, 0), -1, 1.0),
        ]

    z = {}
    for k, s, amp in raw:
        z[(k, s)] = complex(amp)
        z[(tuple(-x for x in k), s)] = complex(amp)
    sc = sum(abs(a) ** 2 for a in z.values()) ** -0.5
    z = {k: a * sc for k, a in z.items()}

    omega = {}
    for (q, s), amp in z.items():
        omega[q] = omega.get(q, np.zeros(3, complex)) + s * np.linalg.norm(q) * amp * g.h(q, s)
    Y = {m: np.eye(p, dtype=complex)[i] for i, m in enumerate(Pm)}
    wc = np.zeros(p, complex)
    for (k, s), amp in z.items():
        wc[pidx[(k, s)]] = s * np.linalg.norm(k) * amp

    def tval(k, s):
        return ((1 - bb * s) * np.linalg.norm(k) - aa) / N

    G = np.zeros((p, p), complex)
    eta = None
    rank = None
    align = None
    for _ in range(2):
        Y = d.apply_A(Y, omega, N)
        for (k, s), row in Y.items():
            tr = tval(k, s)
            if abs(tr) > 1e-14:
                G += abs(tr) ** 2 * np.outer(np.conjugate(row), row)
        eig, vec = np.linalg.eigh((G + G.conj().T) / 2)
        tol = max(1e-12, 1e-9 * max(float(eig[-1]), 1e-30))
        pos = eig[eig > tol]
        rank = len(pos)
        eta = float(pos[0] / pos[-1]) if len(pos) else 0.0
        nv = vec[:, 0]
        align = abs(np.vdot(nv, wc)) / (np.linalg.norm(nv) * np.linalg.norm(wc))

    A = np.zeros((3, 3), float)
    trA = 0.0
    for (k, s), amp in z.items():
        r = np.linalg.norm(k)
        kh = np.asarray(k, float) / r
        w = r * abs(amp) ** 2
        A += w * np.outer(kh, kh)
        trA += w
    pi = float(np.linalg.eigvalsh(A)[0] / trA)
    return p, pi, eta, rank, float(align)


def main():
    planar = []
    spatial = []
    for n in [10, 20, 40, 80]:
        p0, pi0, e0, r0, a0 = audit(n, False)
        p1, pi1, e1, r1, a1 = audit(n, True)
        planar.append(e0)
        spatial.append(e1)
        print(
            f"ratio={n:3d} planar(pi={pi0:.3e},eta2={e0:.6e},rank={r0}/{p0}) "
            f"3D(pi={pi1:.3e},eta2={e1:.6e},rank={r1}/{p1}) "
            f"omega=({a0:.12f},{a1:.12f})"
        )
    assert max(abs(x) for x in [audit(10, False)[1], audit(20, False)[1]]) < 1e-14
    slope = -float(np.polyfit(np.log(np.array([10.,20.,40.,80.])), np.log(np.array(planar)), 1)[0])
    print(f'planar depth-two decay exponent: {slope:.6f}')
    assert 3.9 < slope < 4.1
    assert planar[-1] < planar[0] / 50
    assert min(spatial) > 0.03
    assert spatial[-1] > 100 * planar[-1]


if __name__ == "__main__":
    main()
