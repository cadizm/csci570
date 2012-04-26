#!/usr/bin/env python

##
## Sun Jun 17 11:22:04 PDT 2007
##

import random

def naive(L):
    K = L[:]
    K.reverse()
    m = 0
    b = s = 0
    count = 0
    for i in range(0, len(K)-1):
        for j in range(i+1, len(K)):
            count += 1
            if K[i] - K[j] > m:
                m = K[i] - K[j]
                b = j
                s = i

#    print K[s], K[b]
    print "Naive iterations: %d" % (count)
    print "Naive answer: %d" % (m)
    return m

def algorithm1(L):
    if len(L) < 2:
        return 0
    elif len(L) == 2:
        if L[1] - L[0] > 0:
            return L[1] - L[0]
        else:
            return 0
    if L[1] - L[0] < 0:
        b = s = q = min(L[0], L[1])
    else:
        b = L[0]
        s = L[1]
        q = L[0]
    count = 0
    # Basic idea of the for loop is to check and store the max
    # for the 3 possible options, making sure it is better than
    # what we currently have:
    #    L[i] - L[i-1]
    #    L[i] - b
    #    L[i] - q
    for i in range(2, len(L)):
        count += 1
        # If we encounter a new low,
        # save it just in case
        if L[i] < b and L[i] < q:
            q = L[i]
        # If If the new price and the prev price
        # are the new best sell/buy pair
        if L[i] - L[i-1] > L[i] - b and \
                L[i] - L[i-1] > s - b:
            s = L[i]
            b = L[i-1]
        # If the new price beats cur price
        if L[i] - b > s - b:
            s = L[i]
        # If the new price in combination with
        # a low previously seen is the best pair
        if L[i] - q > s - b:
            s = L[i]
            b = q

#    print s, b
    print "algorithm1 iterations: %d" % (count)
    print "algorithm1 answer: %d" % (s-b)
    return s - b

def singletest(L):
    if algorithm1(L) != naive(L):
        print "INPUT: %s" % (L)
        print "ALGORITHM1 Answer: %d " % (algorithm1(L))
        print "NAIVE Answer: %d" % (naive(L))

def whiletest():
    L = [random.randint(0, 100) for i in range(100)]
    while algorithm1(L) == naive(L):
        L = [random.randint(0, 100) for i in range(100)]
    print "INPUT: %s" % (L)
    print "algorithm1: %d " % (algorithm1(L))
    print "NAIVE: %d" % (naive(L))

def MOPT(L, M, i, j):
    """Dynamic Programming Solution to the following optimization problem:
    Consider the following scenario, you are given all the daily closing prices
    of shares of Microsoft over a period of n days. You are given a chance to
    buy 100 shares of this stock at any day i, 1 <= i <= n and sell at any day
    j, i <= j <= n. Of course your objective is to maximize your profit in this
    transaction. There is a simplistic O(n^2) algorithm that tries all possible
    pairs of buy/sell days to find the optimal solution. Develop an algorithm
    that accomplishes this in O(n) time."""
    if i < 0:
        return 0
    if j < 1:
        return 0
    if M[i][j] != None:
        return M[i][j]
    else:
        M[i][j] = max(L[j]-L[i], MOPT(L, M, i-1, j-1), MOPT(L, M, i-1, j))
    return M[i][j]

def OPT(L, i, j):
    """Non-memoized version veeerrrrryyyyy slooooowwwww"""
    if i < 0:
        return 0
    if j < 1:
        return 0
    return max(L[j]-L[i], OPT(L, i-1, j-1), OPT(L, i-1, j))

if __name__ == '__main__':
#    L = [23, 38, 10, 16, 96]
#    L = [random.randint(0, 100) for i in range(20)]
    L = [random.randint(0, 100) for i in range(7)]
    print "Input: %s" % (L)
#    singletest(L)
#    whiletest()

#    L = [99, 100, 0, 10]
    # Should probably make the table size tighter, it is not O(n^2).
    # To get the actual solution, trace back through M to get the
    # i,j (which contain the answer) where MOPT was first computed
    M = [[None for y in L] for x in L]
    print MOPT(L, M, len(L)-2, len(L)-1)
    print algorithm1(L)
    print OPT(L, len(L)-2, len(L)-1)

    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == None:
                print "00",
            elif M[i][j] == 0:
                print "00",
            else: print "%02d" % (M[i][j]),
        print
