#!/usr/bin/env python3
"""Finite-dimensional audit of the protected output moment hierarchy."""

import numpy as np


def audit(samples=10000, seed=20260816):
    rng=np.random.default_rng(seed)
    max_identity=0.0
    min_variance=float('inf')
    for _ in range(samples):
        n=int(rng.integers(3,50))
        t=rng.normal(size=n)
        # complex forcing amplitudes
        F=rng.normal(size=n)+1j*rng.normal(size=n)
        w=np.abs(F)**2
        N0=float(w.sum())
        N1=float((t*w).sum())
        N2=float(((t*t)*w).sum())
        kprime=N1
        y2=2*N2
        max_identity=max(max_identity,abs(y2/2-N2),abs(kprime-N1))
        var=N2/N0-(N1/N0)**2
        min_variance=min(min_variance,var)
    print(f"samples: {samples}")
    print(f"max moment identity abs error: {max_identity:.3e}")
    print(f"minimum forcing-output variance: {min_variance:.3e}")
    assert max_identity<1e-12
    assert min_variance>-1e-12


if __name__=='__main__':
    audit()
