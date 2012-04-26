#!/usr/bin/env python

#
# Assume that you have a list of n numbers, both positive and negative.
# Give an efficient algorithm to find the value of the maximum contiguous
# sum. For example, the maximum contiguous sum in the sequence (-2, -2, 5,
# 7, -3, 4, -4) will be 13.
#

import unittest

def OPT(i, j, L):
    "Non-memoized exponential-time DP solution"
    if i < 0 or j >= len(L) or j < i:
        return 0

    return max(sum(L[i:j]), OPT(i, j + 1, L), OPT(i + 1, i + 2, L))

def MOPT(i, j, L, M):
    "Memoized polynomial-time DP solution"
    if i < 0 or j >= len(L) or j < i:
        return 0

    if not M[i][j]:
        M[i][j] = sum(L[i:j])

    if j + 1 < len(L) and not M[i][j + 1]:
        Q = M[i][j + 1] = MOPT(i, j + 1, L, M)
    else:
        Q = 0

    if i + 2 < len(L) and not M[i + 1][i + 2]:
        R = M[i + 1][i + 2] = MOPT(i + 1, i + 2, L, M)
    else:
        R = 0

    return max(M[i][j], Q, R)

def prettyprint(M):
    s = ''
    for m in M:
        s += ' '.join(["%4s" % (e) for e in m if e]) + '\n'

    return s


class TestContiguousSum(unittest.TestCase):
    def test_contiguoussum(self):
        L = [-2, -2, 5, 7, -3, 4, -4]
        M = [[None for j in range(len(L))] for j in range(len(L))]
        self.assertEqual(MOPT(0, 1, L, M), 13)


if __name__ == '__main__':
    unittest.main()
