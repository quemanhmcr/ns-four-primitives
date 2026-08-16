#!/usr/bin/env python3
"""Audit quadratic opening of the depth-two protected curvature gap near heat-line states.

For shells (1,n^2), use a collinear protected background on e3 plus an
orthogonal -helicity mode of amplitude eps on n*e1.  The exact no-cutoff
frozen-connection Gramian is accumulated to depth two.  The reported log-log
slope is an empirical stress test, not a theorem.
"""
import importlib.util, numpy as np, math
spec=importlib.util.spec_from_file_location('g','scripts/verify_exact_protected_curvature_gap.py')
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

def setup(n,eps):
    a2,b2=1,n*n; alpha,beta=1.,float(n); N=beta
    aa=2*alpha*beta/(alpha+beta); bb=(alpha-beta)/(alpha+beta)
    Pm=[(k,+1) for k in g.shell(a2)]+[(k,-1) for k in g.shell(b2)]; pidx={m:i for i,m in enumerate(Pm)}; p=len(Pm)
    raw=[((0,0,1),+1,1.),((0,0,n),-1,1.),((n,0,0),-1,eps)]
    z={}
    for k,s,a in raw:
        z[(k,s)]=complex(a); z[(tuple(-x for x in k),s)]=complex(a)
    sc=sum(abs(a)**2 for a in z.values())**-.5; z={k:a*sc for k,a in z.items()}
    omega={}
    for (q,s),amp in z.items():omega[q]=omega.get(q,np.zeros(3,complex))+s*np.linalg.norm(q)*amp*g.h(q,s)
    Y={m:np.eye(p,dtype=complex)[i] for i,m in enumerate(Pm)}
    def tval(k,s): return ((1-bb*s)*np.linalg.norm(k)-aa)/N
    return N,omega,Y,tval,p

def apply_A(Y,omega,N):
    out={}
    for (p,sp),rv in Y.items():
        hp=g.h(p,sp)
        for q,omq in omega.items():
            r=tuple(p[d]+q[d] for d in range(3))
            if r==(0,0,0): continue
            c=np.cross(hp,omq)
            for t in(-1,+1):
                cc=np.vdot(g.h(r,t),c)/N
                if abs(cc)<1e-14: continue
                key=(r,t)
                if key in out: out[key]+=cc*rv
                else: out[key]=cc*rv.copy()
    return out

def gap(n,eps):
    N,omega,Y,tval,p=setup(n,eps); G=np.zeros((p,p),complex)
    for _ in range(2):
        Y=apply_A(Y,omega,N)
        for (k,s),rv in Y.items():
            G+=(abs(tval(k,s))**2)*np.outer(np.conjugate(rv),rv)
    eig=np.linalg.eigvalsh((G+G.conj().T)/2); tol=max(1e-14,1e-10*eig[-1]); pos=eig[eig>tol]
    return len(pos),float(pos[0]/pos[-1]) if len(pos) else 0.

def main():
    eps=np.array([1e-4,3e-4,1e-3,3e-3,1e-2,3e-2])
    for n in [2,3,4]:
        vals=[]
        for e in eps:
            r,eta=gap(n,float(e)); vals.append(eta)
        slope=float(np.polyfit(np.log(eps),np.log(vals),1)[0])
        r0,e0=gap(n,0.0)
        print(f'ratio={n} heat_rank={r0} perturbed_rank={gap(n,1e-3)[0]} loglog_slope={slope:.6f} eta/eps^2 range=[{min(np.array(vals)/eps**2):.6e},{max(np.array(vals)/eps**2):.6e}]')
        assert 1.95 < slope < 2.05
if __name__=='__main__':main()
