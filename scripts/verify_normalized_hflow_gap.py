#!/usr/bin/env python3
"""Audit the clock-invariant spectral gap ratio of full helical Galerkin H-flow operators."""

import itertools
import math
import numpy as np

SQRT2=math.sqrt(2.0)


def helical(v,s):
    v=np.asarray(v,float); kh=v/np.linalg.norm(v)
    refs=[np.array([1.,0.,0.]),np.array([0.,1.,0.]),np.array([0.,0.,1.])]
    ref=min(refs,key=lambda r:abs(np.dot(r,kh)))
    e1=np.cross(ref,kh); e1/=np.linalg.norm(e1); e2=np.cross(kh,e1)
    return (e1+1j*s*e2)/SQRT2


def canon(k):
    k=tuple(int(x) for x in k)
    for x in k:
        if x>0:return k
        if x<0:return tuple(-y for y in k)
    raise ValueError


def operator(radius_squared):
    top=math.sqrt(radius_squared)
    rr=int(top)+1
    vec=[k for k in itertools.product(range(-rr,rr+1),repeat=3)
         if k!=(0,0,0) and sum(x*x for x in k)<=radius_squared]
    vset=set(vec); reps=sorted({canon(k) for k in vec})
    modes=[(r,s) for r in reps for s in(-1,1)]
    idx={m:i for i,m in enumerate(modes)}
    rows=[]; weights=[]; seen=set()
    for ia,a in enumerate(vec):
        for b in vec[ia+1:]:
            c=tuple(-a[d]-b[d] for d in range(3))
            if c not in vset:continue
            key=tuple(sorted((a,b,c)))
            if key in seen:continue
            seen.add(key)
            if np.linalg.norm(np.cross(a,b))<1e-12:continue
            rad=[np.linalg.norm(a),np.linalg.norm(b),np.linalg.norm(c)]
            reps3=[canon(a),canon(b),canon(c)]
            for ss in itertools.product((-1,1),repeat=3):
                g=np.vdot(helical(a,ss[0]),np.cross(helical(b,ss[1]),helical(c,ss[2])))
                if abs(g)<1e-12:continue
                h=[ss[j]*rad[j]/top for j in range(3)]
                lam=[h[1]-h[2],h[2]-h[0],h[0]-h[1]]
                row=np.zeros(len(modes))
                for j in range(3):row[idx[(reps3[j],ss[j])]]+=lam[j]
                if np.linalg.norm(row)>1e-12:
                    rows.append(row); weights.append(abs(g)**2)
    A=np.asarray(rows); w=np.asarray(weights)
    L=A.T@(w[:,None]*A)
    return len(modes),len(rows),L


def audit():
    etas=[]
    for r2 in [2,3,4,5,6,8,9]:
        modes,rows,L=operator(r2)
        eig=np.linalg.eigvalsh(L)
        pos=eig[eig>1e-9]
        assert len(eig)-len(pos)==2
        eta=float(pos[0]/pos[-1])
        etas.append(eta)
        print(f"R2={r2} modes={modes} rows={rows} eta={eta:.6f}")
    print(f"minimum audited eta: {min(etas):.6f}")
    assert min(etas)>0.1


if __name__=='__main__':
    audit()
