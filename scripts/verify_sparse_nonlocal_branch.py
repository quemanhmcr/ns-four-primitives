#!/usr/bin/env python3
"""Audit a sparse genuinely-3D protected branch at large shell separation.

The background uses one + helical axis pair on |k|=1 and two - helical axis
pairs on |k|=n, with equal sector energies.  The support spans R^3, but the
high-shell sector is confined to a plane and the critical planarity defect
shrinks as n grows.  We compare this structured sparse branch to the dense
plateau audit.

Numerical evidence only; no uniform theorem is claimed.
"""
import importlib.util, math, numpy as np

spec = importlib.util.spec_from_file_location(
    "d", "scripts/verify_exact_protected_bracket_depth.py"
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
g = d.g


def setup_sparse(n):
    a2, b2 = 1, n * n
    alpha, beta, N = 1.0, float(n), float(n)
    aa = 2 * alpha * beta / (alpha + beta)
    bb = (alpha - beta) / (alpha + beta)
    Pm = [(k, +1) for k in g.shell(a2)] + [(k, -1) for k in g.shell(b2)]
    pidx = {m: i for i, m in enumerate(Pm)}
    p = len(Pm)

    # Reality-paired amplitudes. Plus sector raw energy = 2.
    # Each minus axis pair raw energy = 1, so total minus energy = 2.
    raw = [
        ((1, 0, 0), +1, 1.0),
        ((0, n, 0), -1, 1 / math.sqrt(2)),
        ((0, 0, n), -1, 1 / math.sqrt(2)),
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

    # Critical planarity tensor A=sum |k||z_k|^2 khat otimes khat.
    A = np.zeros((3, 3), float)
    tr = 0.0
    for (k, s), amp in z.items():
        r = np.linalg.norm(k)
        kh = np.asarray(k, float) / r
        w = r * abs(amp) ** 2
        A += w * np.outer(kh, kh)
        tr += w
    pi = float(np.linalg.eigvalsh(A)[0] / tr)
    return N, omega, Y, wc, tval, p, pi


def gap(n, depth=2):
    N, omega, Y, wc, tval, p, pi = setup_sparse(n)
    G = np.zeros((p, p), complex)
    result = []
    for j in range(1, depth + 1):
        Y = d.apply_A(Y, omega, N)
        for (k, s), row in Y.items():
            tr = tval(k, s)
            if abs(tr) > 1e-14:
                G += abs(tr) ** 2 * np.outer(np.conjugate(row), row)
        eig, vec = np.linalg.eigh((G + G.conj().T) / 2)
        tol = max(1e-12, 1e-9 * max(float(eig[-1]), 1e-30))
        pos = eig[eig > tol]
        eta = float(pos[0] / pos[-1]) if len(pos) else 0.0
        nv = vec[:, 0]
        align = abs(np.vdot(nv, wc)) / (np.linalg.norm(nv) * np.linalg.norm(wc))
        result.append((j, len(pos), eta, float(align)))
    return p, pi, result


def main():
    rows = []
    for n in [10, 20, 40, 80]:
        p, pi, res = gap(n, 2)
        e1 = res[0][2]
        e2 = res[1][2]
        rows.append((n, pi, e1, e2))
        print(
            f"ratio={n:3d} P={p:3d} planarity={pi:.6e} "
            f"eta1={e1:.6e} eta2={e2:.6e} "
            f"rank2={res[1][1]}/{p} null~omega={res[1][3]:.12f}"
        )
    assert all(r[1] > 0 for r in rows)  # genuinely 3D support
    assert rows[-1][1] < rows[0][1] / 5
    assert rows[-1][2] < rows[0][2] / 50
    assert min(r[3] for r in rows) > 0.03


if __name__ == "__main__":
    main()
