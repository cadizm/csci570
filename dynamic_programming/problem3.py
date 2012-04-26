#!/usr/bin/env python

#
# Assume that you have an n by n checkerboard. You must move a checker from
# the bottom left corner square of the board to the top right corner square.
# In each step you may either 1) move the checker up one square, or 2) move
# the checker diagonally one square up and to the right, or 3) move the
#checker right one square. If you move a checker from square x to square y
# you get p(x, y) dollars. You are told all of the p(x, y) a priori. The
# p(x, y) may be negative, zero or positive. You want to get as much money
# as possible. Give an efficient algorithm, for this problem.
#

import sys
import random
from decimal import Decimal
import unittest

# Size of the matrix
n = 8
# Initialize the 'p(x, y)' table P.  P[x][y] holds the dollar amount for
# the entry at row x, column y
P = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
# Table used for DP algorithm
M = [[None for j in range(n)] for i in range(n)]

def p((x1, y1), (x2, y2)):
    return P[x2][y2]

def MOPT((x1, y1), (x2, y2)):
    if x2 == n or y2 == n:
        return Decimal('-Infinity')

    if M[x2][y2]:
        return M[x2][y2]

    if x2 == n - 1 and y2 == n - 1:
        M[x2][y2] = p((x1, y1), (x2, y2))

    else:
        M[x2][y2] = p((x1, y1), (x2, y2)) + max(
                MOPT((x2, y2), (x2 + 1, y2)),
                MOPT((x2, y2), (x2 + 1, y2 + 1)),
                MOPT((x2, y2), (x2, y2 + 1)))

    return M[x2][y2]

def traceback(x, y, L):
    L.append(P[x][y])
    if x == n or y == n:
        return
    if x == n - 1 and y == n - 1:
        return

    right = down = diag = None

    if y + 1 < n and M[x][y] - P[x][y] == M[x][y + 1]:
        right = M[x][y + 1]
    if x + 1 < n and M[x][y] - P[x][y] == M[x + 1][y]:
        down = M[x + 1][y]
    if x + 1 < n and y + 1 < n and M[x][y] - P[x][y] == M[x + 1][y + 1]:
        diag = M[x + 1][y + 1]

    if right and diag and right == diag:
        R = []
        traceback(x, y + 1, R)
        D = []
        traceback(x + 1, y + 1, D)
        if sum(L + R) == M[0][0]:
            L.extend(R)
        else:
            L.extend(D)
        return
    if right and down and right == down:
        R = []
        traceback(x, y + 1, R)
        D = []
        traceback(x + 1, y, D)
        if sum(L + R) == M[0][0]:
            L.extend(R)
        else:
            L.extend(D)
        return
    if diag and down and diag == down:
        D1 = []
        traceback(x + 1, y + 1, D1)
        D2 = []
        traceback(x + 1, y, D2)
        if sum(L + D1) == M[0][0]:
            L.extend(D1)
        else:
            L.extend(D2)
        return

    if x + 1 < n and M[x][y] - P[x][y] == M[x + 1][y]:
        traceback(x + 1, y, L)
    if x + 1 < n and y + 1 < n and M[x][y] - P[x][y] == M[x + 1][y + 1]:
        traceback(x + 1, y + 1, L)
    if y + 1 < n and M[x][y] - P[x][y] == M[x][y + 1]:
        traceback(x, y + 1, L)

def pprint(P):
    for p in P:
        for d in p:
            sys.stdout.write("%4s" % (d))
        print '\n'


class TestMaxCheckerboard(unittest.TestCase):
    def test_maxcheckerboard(self):
        L = []
        pprint(P)                       # Print the problem space
        soln = MOPT((0, 0), (0, 0))     # Start at ``left corner square''
        print "Solution: %s\n" % (soln) # Print the value of the optimal soln
        pprint(M)                       # Print the DP table
        traceback(0, 0, L)              # Recover the actual solution
        print "=> %s" % (', '.join([str(e) for e in L]))
        print "\nTraceback: %s" % (sum(L))
        self.assertEqual(soln, sum(L))


if __name__ == '__main__':
    unittest.main()
