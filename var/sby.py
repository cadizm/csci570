#!/usr/bin/env python

import random

def byx(a, b):
    """Sort by x component for params of the form:
            a = (x, y), b = (x, y)"""
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0

def byy(a, b):
    """Sort by y component for params of the form:
            a = (x, y), b = (x, y)"""
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0

def randpairs(n, lim):
    L = {}
    while len(L) < n:
        L[(random.randint(0, lim), random.randint(0, lim))] = 1

    return L.keys()

if __name__ == '__main__':
    L = [(1, 100), (22, 99)]
    print "In:  %s" % (L)
    L.sort(byx)
    print "Out: %s" % (L)
    L.sort(byy)
    print "Out: %s" % (L)

    p = randpairs(10, 25)
    print p
