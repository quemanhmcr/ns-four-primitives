#!/usr/bin/env python3
"""Numerical audit of the local six-mode affine/Walsh identity."""

import numpy as np


def invariant_expression(r, A, B, s):
    h = np.asarray(s, dtype=float) * np.asarray(r, dtype=float)
    q = np.asarray(A, dtype=float) + np.asarray(B, dtype=float) * h
    lam = np.array([h[1]-h[2], h[2]-h[0], h[0]-h[1]])
    return float(lam @ q)


def walsh_formula(r, A, B, s):
    r1,r2,r3=r; A1,A2,A3=A; B1,B2,B3=B; s1,s2,s3=s
    return (
        r1*r2*(B1-B2)*s1*s2
        -r1*r3*(B1-B3)*s1*s3
        +r2*r3*(B2-B3)*s2*s3
        +r1*(A3-A2)*s1
        +r2*(A1-A3)*s2
        +r3*(A2-A1)*s3
    )


def audit(samples=10000, seed=20260816):
    rng=np.random.default_rng(seed)
    maxerr=0.0
    for _ in range(samples):
        r=rng.uniform(0.2,5.0,size=3)
        A=rng.normal(size=3); B=rng.normal(size=3)
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    s=(s1,s2,s3)
                    x=invariant_expression(r,A,B,s)
                    y=walsh_formula(r,A,B,s)
                    maxerr=max(maxerr,abs(x-y))
    print(f"samples: {samples}")
    print(f"max Walsh identity abs error: {maxerr:.3e}")
    assert maxerr < 1e-10

    # Equal-radius cases are included explicitly.
    for r in [(1.,1.,1.),(2.,2.,3.),(2.,4.,2.),(5.,3.,3.)]:
        A=np.array([1.2,1.2,1.2]); B=np.array([-0.7,-0.7,-0.7])
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    assert abs(invariant_expression(r,A,B,(s1,s2,s3)))<1e-12


if __name__=='__main__':
    audit()
