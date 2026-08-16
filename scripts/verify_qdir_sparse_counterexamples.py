#!/usr/bin/env python3
"""Reality-constrained sparse counterexamples to qdir-only depth-two coercivity.

The sector-normalized directional tensor Q_dir correctly detects a common
Fourier plane, but by itself it does not control the depth-two protected
curvature gap on very sparse coherent states.  These hand-picked states were
found by an adversarial complexified search and then reality-paired here.

This script is a falsification guard: it prevents upgrading the empirical
near-planar law eta2 ~ qdir into a global theorem without a density/coherence
hypothesis.
"""
import importlib.util, math, numpy as np

spec = importlib.util.spec_from_file_location(
    "d", "scripts/verify_exact_protected_bracket_depth.py"
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
g = d.g


def audit(R, kp, q1, q2, w):
    alpha, beta, N = 1.0, float(R), float(R)
    aa = 2 * alpha * beta / (alpha + beta)
    bb = (alpha - beta) / (alpha + beta)
    Pm = [(k, +1) for k in g.shell(1)] + [(k, -1) for k in g.shell(R * R)]
    pidx = {m: i for i, m in enumerate(Pm)}
    p = len(Pm)

    raw = [
        (kp, +1, 1.0),
        (q1, -1, math.sqrt(w)),
        (q2, -1, math.sqrt(1.0 - w)),
    ]
    z = {}
    for k, s, amp in raw:
        z[(k, s)] = complex(amp)
        z[(tuple(-x for x in k), s)] = complex(amp)

    Ep = sum(abs(a) ** 2 for (k, s), a in z.items() if s > 0)
    Em = sum(abs(a) ** 2 for (k, s), a in z.items() if s < 0)
    for key in list(z):
        z[key] *= math.sqrt((0.5 / Ep) if key[1] > 0 else (0.5 / Em))

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
        ww = abs(amp) ** 2
        if s > 0:
            Qp += ww * np.outer(kh, kh)
            Ep += ww
        else:
            Qm += ww * np.outer(kh, kh)
            Em += ww
    qdir = float(np.linalg.eigvalsh(0.5 * (Qp / Ep + Qm / Em))[0])
    return eta, qdir, float(align), len(pos), p


def main():
    cases = [
        (10, (0, 0, -1), (-6, 0, 8), (0, 6, 8), 0.4344171682597496),
        (20, (0, 0, 1), (16, -12, 0), (20, 0, 0), 0.3017761666481661),
        (40, (1, 0, 0), (0, -32, -24), (0, 32, -24), 0.3288037688593499),
    ]
    ratios = []
    for case in cases:
        R = case[0]
        eta, qdir, align, rank, p = audit(*case)
        ratio = eta / qdir
        ratios.append(ratio)
        print(
            f"R={R:2d} eta2={eta:.9e} qdir={qdir:.9e} "
            f"eta2/qdir={ratio:.9e} rank={rank}/{p} null~omega={align:.12f}"
        )
    assert ratios[-1] < 0.1
    assert ratios[-1] < ratios[0] / 5
    print("qdir-only global coercivity: falsified by sparse coherent branch")


if __name__ == "__main__":
    main()
