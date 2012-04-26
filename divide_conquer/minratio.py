#!/usr/bin/env python

import random

def naive(L):
    m = float(L[0])/L[1]
    for i in range(len(L)-1):
        if float(L[i])/L[i+1] < m:
            m = float(L[i])/L[i+1]
    return m

def minratio(L):
    if len(L) == 2:
        return float(L[0])/L[1]

    mid = len(L)/2
    Q = L[:mid]
    R = L[mid:]

    m = float(L[mid-1])/L[mid]
    q = minratio(Q)
    r = minratio(R)

    return min(m, q, r)

if __name__ == '__main__':
    pop = [i for i in range(100)]
    n = 32
#    L = [11, 10, 14, 14]
    L = random.sample(pop, n)
    print L
    print minratio(L)
    print naive(L)
