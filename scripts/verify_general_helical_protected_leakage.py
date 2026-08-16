#!/usr/bin/env python3
"""Audit the general helical magnitude and protected cross-spin leakage formulas."""

import math
import random
import numpy as np
from verify_helical_coefficients import pair_coefficient

SQRT2=math.sqrt(2.0)


def audit(samples=30000,seed=20260816):
    rng=np.random.default_rng(seed); rr=random.Random(seed)
    max_general=0.0; max_leak=0.0
    for _ in range(samples):
        a=rng.normal(size=3); b=rng.normal(size=3); r=a+b
        aa=np.linalg.norm(a); bb=np.linalg.norm(b); rho=np.linalg.norm(r)
        area=np.linalg.norm(np.cross(a,b))
        if min(aa,bb,rho,area)<1e-8: continue
        sa=rr.choice([-1,1]); sb=rr.choice([-1,1]); t=rr.choice([-1,1])
        got=abs(pair_coefficient(a,b,t,sa,sb))
        pred=(abs(sb*bb-sa*aa)*area*abs(sa*aa+sb*bb+t*rho)
              /(2*SQRT2*rho*aa*bb))
        max_general=max(max_general,abs(got-pred)/max(1e-12,got,pred))

        # Treat current radii as protected + and - shell radii and audit T*C.
        alpha=aa; beta=bb
        gotp=abs(pair_coefficient(a,b,+1,+1,-1))
        gotm=abs(pair_coefficient(a,b,-1,+1,-1))
        tplus=2*beta*(rho-alpha)/(alpha+beta)
        tminus=2*alpha*(rho-beta)/(alpha+beta)
        leakp=area*abs(rho-alpha)*(rho+alpha-beta)/(SQRT2*rho*alpha)
        leakm=area*abs(rho-beta)*(rho-alpha+beta)/(SQRT2*rho*beta)
        max_leak=max(max_leak,
                     abs(abs(tplus)*gotp-leakp)/max(1e-12,leakp,abs(tplus)*gotp),
                     abs(abs(tminus)*gotm-leakm)/max(1e-12,leakm,abs(tminus)*gotm))
    print(f"samples: {samples}")
    print(f"max general helical magnitude relative error: {max_general:.3e}")
    print(f"max protected leakage relative error: {max_leak:.3e}")
    assert max_general<1e-8
    assert max_leak<1e-8


if __name__=='__main__':
    audit()
