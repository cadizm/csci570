#!/usr/bin/env python

#
# Gale-Shapley stable matching algorithm as described in Algorithm Design by
# Kleinberg, Tardos. See http://www.aw-bc.com/info/kleinberg/ for more info.
#

import sys

def stable_match(prefsm, prefsw):
    "Gale-Shapley stable matching algorithm"
    M = [i for i in range(len(prefsm))]
    W = [i for i in range(len(prefsw))]
    P = build_index(W, prefsw)
    E = [None for i in range(len(prefsm))]

    while len(M) > 0:
        m = M.pop(0)
        w = prefsm[m].pop(0)
        if W[w] != None:
            W[w] = None
            E[w] = (m, w)
        else:
            if P[w][E[w][0]] < P[w][m]:
                M.insert(0, m)
            else:
                M.insert(0, E[w][0])
                E[w] = (m, w)
    return E

def build_index(W, prefsw):
    "Build an index of women's preferences for improved efficiency"
    prefindex = [[None for j in range(len(prefsw))]
            for i in range(len(prefsw))]
    for w, preflist in enumerate(prefsw):
        for p, m in enumerate(preflist):
            # The lower p is, the more m is preferred by w
            prefindex[w][m] = p
    return prefindex

def run():
    check_args()
    (prefsm, prefsw) = read_infile()
    S = stable_match(prefsm, prefsw)
    for s in S:
        print "(M[%s], W[%s])" % (s[0], s[1])

def usage():
    print "Usage: stable.py <infile>"

def check_args():
    if len(sys.argv) != 2:
        sys.exit(usage())

def read_infile():
    """Read the infile which should have the following format: the first non-
    line should be an integer representing the input size.  The next i lines
    should be the preference list for the ith man, where i is in the range 0
    to n-1. The next i lines should follow the same format for women."""
    f = open(sys.argv[1], 'r')
    n = f.readline()
    while n.startswith("#"):
        n = f.readline().lstrip()
    n = int(n)
    prefsm = [ [int(x.strip()) for x in f.readline().split(",")]
            for i in range(n) ]
    prefsw = [ [int(x.strip()) for x in f.readline().split(",")]
            for i in range(n) ]
    return (prefsm, prefsw)

if __name__ == "__main__":
    run()
