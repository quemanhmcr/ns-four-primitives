#!/usr/bin/env python3
"""Algebraic audit for the within-spin radial gate identities."""

import numpy as np


def audit(samples=20000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_collapse_error = 0.0
    min_defect = float("inf")

    for _ in range(samples):
        ep = float(rng.random() + 0.05)
        em = float(rng.random() + 0.05)
        # positive random radial distributions produce valid moments
        rp = rng.uniform(0.2, 5.0, size=5)
        rm = rng.uniform(0.2, 5.0, size=5)
        wp = rng.random(5); wp *= ep / np.sum(wp)
        wm = rng.random(5); wm *= em / np.sum(wm)
        kp = float(np.sum(wp * rp)); zp = float(np.sum(wp * rp * rp))
        km = float(np.sum(wm * rm)); zm = float(np.sum(wm * rm * rm))
        dp = ep * zp - kp * kp
        dm = em * zm - km * km
        min_defect = min(min_defect, dp, dm)

        mp = kp / ep; mm = km / em
        kappa = float(rng.normal())
        bplus = float(rng.normal())
        bminus = -bplus
        aplus = aminus = kappa / 2.0
        cplus = aplus - mp * bplus
        cminus = aminus - mm * bminus
        recovered = 2.0 * (mm * cplus + mp * cminus) / (mp + mm)
        max_collapse_error = max(max_collapse_error, abs(recovered - kappa))

    print(f"samples: {samples}")
    print(f"minimum sector critical radial defect: {min_defect:.3e}")
    print(f"max kappa-collapse identity abs error: {max_collapse_error:.3e}")
    assert min_defect > -1e-12
    assert max_collapse_error < 1e-10


if __name__ == "__main__":
    audit()
