#!/usr/bin/env python3
"""Finite-dimensional least-squares audit of protected-manifold acceleration."""

import numpy as np


def residual_sq(u, w, ell):
    G=np.array([[u@u,u@w],[u@w,w@w]],dtype=float)
    rhs=np.array([u@ell,w@ell],dtype=float)
    coeff=np.linalg.solve(G,rhs)
    r=ell-coeff[0]*u-coeff[1]*w
    return float(r@r), r


def audit(samples=5000, seed=20260816):
    rng=np.random.default_rng(seed)
    max_ratio_error=0.0
    for _ in range(samples):
        d=8
        u=rng.normal(size=d); w=rng.normal(size=d)
        if np.linalg.det(np.array([[u@u,u@w],[u@w,w@w]]))<1e-4:
            continue
        a,b=rng.normal(size=2)
        ell=a*u+b*w   # exactly protected at t=0
        du=rng.normal(size=d); dw=rng.normal(size=d); dell=rng.normal(size=d)
        raw=dell-a*du-b*dw
        G=np.array([[u@u,u@w],[u@w,w@w]],dtype=float)
        c=np.linalg.solve(G,np.array([u@raw,w@raw]))
        proj=raw-c[0]*u-c[1]*w
        predicted=2.0*(proj@proj)
        # symmetric finite difference for Y''(0)
        h=1e-5
        yp,_=residual_sq(u+h*du,w+h*dw,ell+h*dell)
        ym,_=residual_sq(u-h*du,w-h*dw,ell-h*dell)
        y0,_=residual_sq(u,w,ell)
        numeric=(yp-2*y0+ym)/(h*h)
        denom=max(1e-8,abs(predicted))
        max_ratio_error=max(max_ratio_error,abs(numeric-predicted)/denom)
    print(f"samples: {samples}")
    print(f"max relative second-derivative audit error: {max_ratio_error:.3e}")
    assert max_ratio_error<2e-4


if __name__=='__main__':
    audit()
