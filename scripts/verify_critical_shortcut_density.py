#!/usr/bin/env python3
"""Falsification aid for the critical-amplitude shortcut identities."""

import numpy as np


def audit(samples=10000, seed=20260816):
    rng = np.random.default_rng(seed)
    max_identity_error = 0.0
    min_pair_margin = float("inf")
    min_sum_margin = float("inf")

    for _ in range(samples):
        n = int(rng.integers(4, 20))
        # Construct positive amplitudes and then rescale neighboring pairs so
        # the uniform lower bound P is explicit.
        x = np.exp(rng.normal(size=n))
        pis = x[:-1] * x[1:]
        P = float(np.min(pis))
        betas = x[:-2] * x[2:]

        for j in range(n - 3):
            lhs = betas[j] * betas[j + 1]
            rhs = pis[j] * pis[j + 2]
            max_identity_error = max(max_identity_error, abs(lhs - rhs))
            min_pair_margin = min(min_pair_margin, max(betas[j], betas[j + 1]) - P)

        # Pair (beta_0,beta_1), (beta_2,beta_3), ... .
        lower = 2.0 * P * ((len(betas)) // 2)
        min_sum_margin = min(min_sum_margin, float(np.sum(betas)) - lower)

    print(f"samples: {samples}")
    print(f"max shortcut product identity abs error: {max_identity_error:.3e}")
    print(f"minimum consecutive-shortcut margin: {min_pair_margin:.3e}")
    print(f"minimum shortcut-sum margin: {min_sum_margin:.3e}")

    assert max_identity_error < 1e-9
    assert min_pair_margin > -1e-10
    assert min_sum_margin > -1e-10


if __name__ == "__main__":
    audit()
