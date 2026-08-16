#!/usr/bin/env python3
"""Audit the combinatorial first-opening derivative for ||r(t)||^2."""

import math
import numpy as np


def audit(samples=10000, seed=20260816):
    rng=np.random.default_rng(seed)
    max_error=0.0
    for _ in range(samples):
        n=int(rng.integers(1,8))
        v=rng.normal(size=6)
        # r(t)=v t^n/n! + higher terms irrelevant to derivative 2n.
        predicted=math.comb(2*n,n)*float(v@v)
        # coefficient of t^(2n) in ||r||^2 is ||v||^2/(n!)^2.
        coeff=float(v@v)/(math.factorial(n)**2)
        recovered=math.factorial(2*n)*coeff
        max_error=max(max_error,abs(predicted-recovered))
    print(f"samples: {samples}")
    print(f"max first-opening combinatorial identity abs error: {max_error:.3e}")
    assert max_error<1e-9


if __name__=='__main__':
    audit()
