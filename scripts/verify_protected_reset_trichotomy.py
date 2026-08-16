#!/usr/bin/env python3
"""Numerical audit for the protected reset pair lower bound."""

import math
import numpy as np
from verify_helical_coefficients import pair_coefficient

SQRT2=math.sqrt(2.0)


def unit(v):
    return v/np.linalg.norm(v)


def phi(s):
    return s*(1.0-math.sqrt(max(0.0,1.0-s*s)))


def audit(samples=30000,seed=20260816):
    rng=np.random.default_rng(seed)
    min_margin=float('inf')
    for _ in range(samples):
        alpha=float(rng.uniform(.1,6)); beta=float(rng.uniform(.1,6))
        A=alpha*unit(rng.normal(size=3)); B=beta*unit(rng.normal(size=3))
        area=np.linalg.norm(np.cross(A,B))
        if area<1e-10: continue
        sangle=area/(alpha*beta)
        rp=np.linalg.norm(A+B); rm=np.linalg.norm(A-B)
        roots2=np.array([alpha*alpha,beta*beta])
        dp=float(np.min(np.abs(rp*rp-roots2)))
        dm=float(np.min(np.abs(rm*rm-roots2)))
        Bb=B if dp>=dm else -B
        rho=np.linalg.norm(A+Bb)
        m=min(alpha,beta); M=max(alpha,beta)
        c=(m/M)**4/(6*SQRT2)
        pi=math.sqrt(alpha*beta) # choose |z_A|=|z_B|=1
        lower=c*M*phi(sangle)*pi

        tp=abs(2*beta*(rho-alpha)/(alpha+beta))
        tm=abs(2*alpha*(rho-beta)/(alpha+beta))
        xp=tp*abs(pair_coefficient(A,Bb,+1,+1,-1))
        xm=tm*abs(pair_coefficient(A,Bb,-1,+1,-1))
        min_margin=min(min_margin,xp-lower,xm-lower)

    print(f"samples: {samples}")
    print(f"minimum protected-reset pair lower-bound margin: {min_margin:.3e}")
    assert min_margin>-1e-10


if __name__=='__main__':
    audit()
