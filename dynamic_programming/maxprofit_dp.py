#!/usr/bin/env python

#
# DP (and alternative) solution(s) to the following problem:
#
# Consider the following scenario, you are given all the daily closing
# prices of shares of Google over a period of n days. You are given a
# chance to buy 100 shares of this stock at any day i, 1 <= i <= n and
# sell at any day j, i <= j <= n. Of course your objective is to maximize
# your profit in this transaction. 
#

import random
import unittest

def naive(L):
    K = [L[i * -1] for i in range(1, len(L) + 1)]
    m = b = s = count = 0
    for i in range(0, len(K) - 1):
        for j in range(i + 1, len(K)):
            count += 1
            if K[i] - K[j] > m:
                m = K[i] - K[j]
                b = j
                s = i
    return m

def unintelligible(L):
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
        if L[i] - L[i-1] > L[i] - b and L[i] - L[i - 1] > s - b:
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
    return s - b

def OPT(L, i, j):
    "Non-memoized version"
    if i < 0:
        return 0
    if j < 1:
        return 0
    return max(L[j] - L[i], OPT(L, i - 1, j - 1), OPT(L, i - 1, j))

def MOPT(L, M, i, j):
    """Memoized version.  As usual, trace back through M to get the i's, j's
    of the actual solution"""
    if i < 0:
        return 0
    if j < 1:
        return 0
    if M[i][j] != None:
        return M[i][j]
    else:
        M[i][j] = max(L[j] - L[i],
                MOPT(L, M, i - 1, j - 1),
                MOPT(L, M, i - 1, j))
    return M[i][j]


class TestMaxProfit(unittest.TestCase):
    def test_maxprofit(self):
        for i in range(random.randint(0, 100)):
            L = [random.randint(0, 100) for i in range(100)]
            self.assertEqual(naive(L), unintelligible(L))
            # Could make table size tighter than n^2.
            M = [[None for j in L] for i in L]
            self.assertEqual(naive(L), MOPT(L, M, len(L) - 2, len(L) - 1))


if __name__ == '__main__':
    unittest.main()
