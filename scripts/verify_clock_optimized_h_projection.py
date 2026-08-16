#!/usr/bin/env python3
"""Audit the clock-optimized H-current projection identities."""

import numpy as np


def audit(samples=20000, seed=20260816):
    rng=np.random.default_rng(seed)
    max_orth=0.0
    max_pyth=0.0
    max_flux_violation=0.0
    for _ in range(samples):
        m=rng.integers(3,12)
        w=rng.uniform(0.2,3.0,size=m)
        a=rng.normal(size=m)
        J=rng.normal(size=m)
        WJ=w*a
        DH=float(np.sum(w*a*a))
        if DH<1e-12:
            continue
        Sdot=float(a@J)
        if Sdot<=0:
            continue
        gamma=Sdot/DH
        Jp=J-gamma*WJ
        orth=float(np.sum(Jp*a))
        max_orth=max(max_orth,abs(orth))
        normJ=float(np.sum(J*J/w))
        Cp=float(np.sum(Jp*Jp/w))
        pyth=abs(normJ-(gamma*gamma*DH+Cp))
        max_pyth=max(max_pyth,pyth)

        c=rng.normal(size=m)
        DV=float(np.sum(w*c*c))
        Kdot=float(c@J)
        bound=np.sqrt(DV)*(abs(Sdot)/np.sqrt(DH)+np.sqrt(Cp))
        max_flux_violation=max(max_flux_violation,Kdot*Kdot-bound*bound if abs(Kdot)>bound else 0.0)
        assert abs(Kdot)<=bound+1e-10

    print(f"samples: {samples}")
    print(f"max optimized orthogonality residual: {max_orth:.3e}")
    print(f"max Pythagoras residual: {max_pyth:.3e}")
    print(f"max critical-flux bound violation: {max_flux_violation:.3e}")
    assert max_orth<1e-10
    assert max_pyth<1e-9
    assert max_flux_violation<1e-8


if __name__=='__main__':
    audit()
