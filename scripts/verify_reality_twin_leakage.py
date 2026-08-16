#!/usr/bin/env python3
"""Numerical audit for the reality-twin protected leakage geometry."""

import numpy as np


def unit(v):
    return v/np.linalg.norm(v)


def audit(samples=30000,seed=20260816):
    rng=np.random.default_rng(seed)
    max_para=0.0
    min_sq_margin=float('inf')
    min_rad_margin=float('inf')
    min_t_margin=float('inf')
    for _ in range(samples):
        alpha=float(rng.uniform(.1,6)); beta=float(rng.uniform(.1,6))
        A=alpha*unit(rng.normal(size=3)); B=beta*unit(rng.normal(size=3))
        rp=np.linalg.norm(A+B); rm=np.linalg.norm(A-B)
        max_para=max(max_para,abs(rp*rp+rm*rm-2*(alpha*alpha+beta*beta)))
        roots2=np.array([alpha*alpha,beta*beta])
        dp=float(np.min(np.abs(rp*rp-roots2)))
        dm=float(np.min(np.abs(rm*rm-roots2)))
        m=min(alpha,beta); M=max(alpha,beta)
        min_sq_margin=min(min_sq_margin,max(dp,dm)-m*m)
        rho=rp if dp>=dm else rm
        dr=min(abs(rho-alpha),abs(rho-beta))
        min_rad_margin=min(min_rad_margin,dr-m*m/(3*M))
        tp=abs(2*beta*(rho-alpha)/(alpha+beta))
        tm=abs(2*alpha*(rho-beta)/(alpha+beta))
        min_t_margin=min(min_t_margin,min(tp,tm)-m**3/(3*M*M))
    print(f"samples: {samples}")
    print(f"max parallelogram identity abs error: {max_para:.3e}")
    print(f"minimum squared-distance lower-bound margin: {min_sq_margin:.3e}")
    print(f"minimum radial-distance lower-bound margin: {min_rad_margin:.3e}")
    print(f"minimum T-symbol lower-bound margin: {min_t_margin:.3e}")
    assert max_para<1e-10
    assert min_sq_margin>-1e-10
    assert min_rad_margin>-1e-10
    assert min_t_margin>-1e-10


if __name__=='__main__':
    audit()
