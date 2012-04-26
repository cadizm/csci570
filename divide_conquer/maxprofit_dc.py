#!/usr/bin/env python

#
# Divide and conquer solutionn to the following problem:
#
# Consider the following scenario, you are given all the daily closing
# prices of shares of Google over a period of n days. You are given a
# chance to buy 100 shares of this stock at any day i, 1 <= i <= n and
# sell at any day j, i <= j <= n. Of course your objective is to maximize
# your profit in this transaction. 
#
# Solution here is n log n, characterized by the following recurrence:
#   T(n) = 2 T(n/2) cn.
#
# See maxprofit_dp.py for a linear time Dynamic Programming solution.
#

import unittest

def maxprofit(L):
    if len(L) == 0 or len(L) == 1:
        return 0
    if len(L) == 2:
        return max(L[1] - L[0], 0)

    Q = L[:len(L)/2]
    R = L[len(L)/2:]

    q = maxprofit(Q)
    r = maxprofit(R)

    return max(q, r, max(R) - min(Q))


class TestMaxProfit(unittest.TestCase):
    def test_maxprofit(self):
        self.assertEqual(maxprofit([44, 16, 27, 6, 10, 25, 14]), 19)


if __name__ == '__main__':
    unittest.main()
