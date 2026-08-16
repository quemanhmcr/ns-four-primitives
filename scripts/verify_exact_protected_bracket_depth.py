#!/usr/bin/env python3
"""Exact finite-depth bracket Gramian for a frozen protected two-shell state.

No Fourier output cutoff is imposed.  Starting from ker(T), iteratively apply
A_omega/N where N=max(alpha,beta), and accumulate
  G_m = sum_{j=1}^m || (T/N) (A_omega/N)^j v ||^2.
This tests whether higher protected-connection brackets repair weak first-order
curvature directions.  It is a frozen-state experiment, not a PDE theorem.
"""
import importlib.util, math, numpy as np
spec=importlib.util.spec_from_file_location('g','scripts/verify_exact_protected_curvature_gap.py')
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

def setup(a2,b2,seed=11,style='random'):
    alpha=math.sqrt(a2); beta=math.sqrt(b2); N=max(alpha,beta)
    aa=2*alpha*beta/(alpha+beta); bb=(alpha-beta)/(alpha+beta)
    Pm=[(k,+1) for k in g.shell(a2)]+[(k,-1) for k in g.shell(b2)]
    pidx={m:i for i,m in enumerate(Pm)}; p=len(Pm)
    z=g.background(a2,b2,seed,style); omega={}
    for (q,s),amp in z.items():omega[q]=omega.get(q,np.zeros(3,complex))+s*np.linalg.norm(q)*amp*g.h(q,s)
    Y={m:np.eye(p,dtype=complex)[i] for i,m in enumerate(Pm)}
    wc=np.zeros(p,complex)
    for (k,s),amp in z.items():wc[pidx[(k,s)]]=s*np.linalg.norm(k)*amp
    def tval(k,s):return ((1-bb*s)*np.linalg.norm(k)-aa)/N
    return N,omega,Y,wc,tval

def apply_A(Y,omega,N):
    out={}
    for (p,sp),rowvec in Y.items():
        hp=g.h(p,sp)
        for q,omq in omega.items():
            r=tuple(p[d]+q[d] for d in range(3))
            if r==(0,0,0):continue
            c=np.cross(hp,omq)
            for t in(-1,+1):
                coeff=np.vdot(g.h(r,t),c)/N
                if abs(coeff)<1e-14:continue
                key=(r,t)
                if key in out:out[key]+=coeff*rowvec
                else:out[key]=coeff*rowvec.copy()
    return out

def audit_pair(a2,b2,seed=11,style='random',maxdepth=4):
    N,omega,Y,wc,tval=setup(a2,b2,seed,style); p=len(wc); G=np.zeros((p,p),complex); result=[]
    for depth in range(1,maxdepth+1):
        Y=apply_A(Y,omega,N)
        for (k,s),row in Y.items():
            tr=tval(k,s)
            if abs(tr)>1e-14:G+=(abs(tr)**2)*np.outer(np.conjugate(row),row)
        Gh=(G+G.conj().T)/2; eig,vec=np.linalg.eigh(Gh)
        tol=max(1e-12,1e-9*max(float(eig[-1]),1e-30)); pos=eig[eig>tol]
        rank=len(pos); eta=float(pos[0]/pos[-1]) if len(pos) else 0.
        nv=vec[:,0]; align=abs(np.vdot(nv,wc))/(np.linalg.norm(nv)*np.linalg.norm(wc))
        result.append((depth,rank,eta,align,len(Y)))
    return p,result

def main():
    # Depth two is the decisive finite-cost audit.  Deeper exact expansion
    # grows combinatorially and is deliberately not used as a brute-force test.
    for n in [2,4,6,8,10]:
        p,res=audit_pair(1,n*n,11,'random',2)
        print(f'ratio={n:2d} P={p:3d} '+ ' '.join(f'm{d}:r={r}/{p},eta={e:.2e},om={a:.6f},reach={nr}' for d,r,e,a,nr in res))
if __name__=='__main__':main()
