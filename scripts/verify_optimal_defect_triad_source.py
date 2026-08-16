#!/usr/bin/env python3
"""Symbolic/numerical audit for optimal-defect triad factorization."""

import random
import sympy as sp


def symbolic_audit():
    k, q, p, a, b, J = sp.symbols('k q p a b J')
    qp = lambda x: ((1-b)*x-a)**2
    qm = lambda x: ((1+b)*x-a)**2

    Tk=(q+p)*J
    Tq=-(p+k)*J
    Tp=(k-q)*J
    got=sp.factor(qp(k)*Tk+qp(q)*Tq+qm(p)*Tp)
    B=(1-b)**2*(p+k)*(p+q)+4*p*(b*p-a)
    expected=sp.factor((k-q)*J*B)
    assert sp.simplify(got-expected)==0

    Thk=(p-q)*J
    Thp=(q-k)*J
    Thq=(k-p)*J
    hom=sp.factor(qp(k)*Thk+qp(p)*Thp+qp(q)*Thq)
    hom_expected=sp.factor((1-b)**2*(p-k)*(q-k)*(p-q)*J)
    assert sp.simplify(hom-hom_expected)==0

    # Secant identity at h=-p.
    h=sp.symbols('h')
    fk=qp(k); fq=qp(q)
    ell=fk+(fq-fk)*(h-k)/(q-k)
    sec=sp.factor(qm(p)-ell.subs(h,-p))
    assert sp.simplify(sec-B)==0


def numerical_audit(samples=10000, seed=20260816):
    rng=random.Random(seed)
    max_error=0.0
    for _ in range(samples):
        k=rng.uniform(0.2,2.0)
        q=rng.uniform(k+1e-3,3.0)
        p=rng.uniform(max(1e-3,q-k),q+k)
        a=rng.uniform(-3,3)
        b=rng.uniform(-2,2)
        J=rng.uniform(-2,2)
        qp=lambda x: ((1-b)*x-a)**2
        qm=lambda x: ((1+b)*x-a)**2
        got=qp(k)*(q+p)*J+qp(q)*(-(p+k)*J)+qm(p)*(k-q)*J
        B=(1-b)**2*(p+k)*(p+q)+4*p*(b*p-a)
        expected=(k-q)*J*B
        max_error=max(max_error,abs(got-expected))
    print(f"samples: {samples}")
    print(f"max heterochiral factorization abs error: {max_error:.3e}")
    assert max_error<1e-10


if __name__=='__main__':
    symbolic_audit()
    numerical_audit()
