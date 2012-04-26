#!/usr/bin/env python

def buysell(L):
    """Divide and conquer soln to stock buy/sell problem with recurrence
    of the form: T(n) = 2 T(n/2) cn. As a result, we have a complexity
    of n log n. See ../dynamic_programming/problem4.py for description"""

    if len(L) == 1:
        return 0

    if len(L) == 2:
        return max(L[1] - L[0], 0)

    Q = L[:len(L)/2]
    R = L[len(L)/2:]

    q = buysell(Q)
    r = buysell(R)

    return max(q, r, max(R) - min(Q))
    

if __name__ == '__main__':
#    L = [0, 1, 1, 22]
    L = [44, 16, 27, 6, 10, 25, 14]
    print buysell(L)
