#!/usr/bin/env python3
"""Audit linear opening of the depth-two gap against sector-normalized 3D span.

For shells (1,R^2), start from a planar sparse protected background and add a
second orthogonal high-shell -helicity axis with relative amplitude eps.  The
sector-normalized directional tensor is

  Q_dir = 1/2 ( Q_+ / E_+ + Q_- / E_- ),

whose minimum eigenvalue is zero exactly for a common Fourier plane.  In this
family q_dir = eps^2/[2(1+eps^2)].  We audit that the depth-two protected
curvature gap, after subtracting its small planar baseline, opens linearly in
q_dir for R=80.

This is a numerical discovery test, not an exact coercivity theorem.
"""
import importlib.util, math, numpy as np

spec = importlib.util.spec_from_file_location(
    "d", "scripts/verify_exact_protected_bracket_depth.py"
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
g = d.g


def gap(R, eps):
    alpha, beta, N = 1.0, float(R), float(R)
    aa = 2 * alpha * beta / (alpha + beta)
    bb = (alpha - beta) / (alpha + beta)
    Pm = [(k, +1) for k in g.shell(1)] + [(k, -1) for k in g.shell(R * R)]
    pidx = {m: i for i, m in enumerate(Pm)}
    p = len(Pm)

    den = math.sqrt(1 + eps * eps)
    raw = [
        ((1, 0, 0), +1, 1.0),
        ((0, R, 0), -1, 1.0 / den),
        ((0, 0, R), -1, eps / den),
    ]
    z = {}
    for k, s, amp in raw:
        z[(k, s)] = complex(amp)
        z[(tuple(-x for x in k), s)] = complex(amp)
    # Equalize the two helicity-sector energies after reality duplication.
    Ep = sum(abs(a) ** 2 for (k, s), a in z.items() if s == +1)
    Em = sum(abs(a) ** 2 for (k, s), a in z.items() if s == -1)
    for key in list(z):
        if key[1] == +1:
            z[key] *= math.sqrt(0.5 / Ep)
        else:
            z[key] *= math.sqrt(0.5 / Em)

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
    for _ in range(2):
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

    Qp = np.zeros((3, 3), float)
    Qm = np.zeros((3, 3), float)
    Ep = Em = 0.0
    for (k, s), amp in z.items():
        kh = np.asarray(k, float) / np.linalg.norm(k)
        w = abs(amp) ** 2
        if s == +1:
            Qp += w * np.outer(kh, kh)
            Ep += w
        else:
            Qm += w * np.outer(kh, kh)
            Em += w
    Q = 0.5 * (Qp / Ep + Qm / Em)
    qdir = float(np.linalg.eigvalsh(Q)[0])
    return eta, qdir, float(align)


def main():
    R = 80
    eps = np.array([0.0, 0.003, 0.01, 0.03, 0.1])
    vals = []
    for e in eps:
        eta, qdir, align = gap(R, float(e))
        vals.append((e, qdir, eta, align))
        print(f"eps={e:.3e} qdir={qdir:.9e} eta2={eta:.9e} null~omega={align:.12f}")

    base = vals[0][2]
    x = np.array([v[1] for v in vals[1:]])
    y = np.array([v[2] - base for v in vals[1:]])
    slope = float(np.polyfit(np.log(x), np.log(y), 1)[0])
    ratio = y / x
    candidate = 1.0 - 1.0 / math.sqrt(2.0)
    print(f"loglog slope (eta2-base vs qdir): {slope:.6f}")
    print(f"linear coefficient range: [{ratio.min():.6f},{ratio.max():.6f}]")
    print(f"candidate 1-1/sqrt(2): {candidate:.9f}")

    assert 0.95 < slope < 1.05
    assert ratio.min() > 0.25
    assert ratio.max() < 0.40
    assert all(abs(v[3] - 1.0) < 1e-10 for v in vals)


if __name__ == "__main__":
    main()
