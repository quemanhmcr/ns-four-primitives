#!/usr/bin/env python3
"""Audit the large-shell-separation depth-two protected-curvature plateau.

This reuses the exact no-output-cutoff frozen protected connection from
verify_exact_protected_bracket_depth.py.  For dense random reality-constrained
protected backgrounds on shells (1,n^2), first curvature becomes badly
conditioned as n grows, while the depth-two Gramian recovers an order-one
normalized gap in the audited range.

This is numerical evidence, not a uniform-in-n theorem.
"""
import importlib.util

spec = importlib.util.spec_from_file_location(
    "d", "scripts/verify_exact_protected_bracket_depth.py"
)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


def main():
    rows = []
    for n in [10, 20, 40, 80]:
        p, res = d.audit_pair(1, n * n, 11, "random", 2)
        (d1, r1, e1, a1, reach1), (d2, r2, e2, a2, reach2) = res
        rows.append((n, p, e1, e2, r1, r2, a1, a2, reach1, reach2))
        print(
            f"ratio={n:3d} P={p:3d} "
            f"eta1={e1:.6e} eta2={e2:.6e} "
            f"rank1={r1}/{p} rank2={r2}/{p} "
            f"null~omega=({a1:.12f},{a2:.12f}) "
            f"reach=({reach1},{reach2})"
        )

    eta1 = [x[2] for x in rows]
    eta2 = [x[3] for x in rows]
    assert all(x[4] == x[1] - 1 and x[5] == x[1] - 1 for x in rows)
    assert all(abs(x[6] - 1.0) < 1e-10 and abs(x[7] - 1.0) < 1e-10 for x in rows)
    assert eta1[-1] < eta1[0] / 50.0
    assert min(eta2) > 0.10
    assert eta2[-1] > 100.0 * eta1[-1]

    print(f"first-gap collapse factor: {eta1[0] / eta1[-1]:.3f}")
    print(f"minimum audited depth-two gap: {min(eta2):.6f}")


if __name__ == "__main__":
    main()
