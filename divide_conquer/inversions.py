#!/usr/bin/env python

#
# Divide & Conquer algorithm for figuring out the number of
# inversions in a list.
#

import unittest

def inversions(L):
    if len(L) == 0 or len(L) == 1:
        return (0, L)
    else:
        A = L[:len(L)/2]
        B = L[len(L)/2:]
        (ra, A) = inversions(A)
        (rb, B) = inversions(B)
        (r, L) = merge(A, B)

    return (ra + rb + r, L)

def merge(A, B):
    L = []
    inversions = 0
    while len(A) > 0 and len(B) > 0:
        if B[0] < A[0]:
            inversions += len(A)
            L.append(B.pop(0))
        else:
            L.append(A.pop(0))
        if len(A) == 0:
            L.extend(B)
        if len(B) == 0:
            L.extend(A)

    return (inversions, L)


class TestInversions(unittest.TestCase):
    def test_inversions(self):
        self.assertEqual(inversions([])[0], 0)
        self.assertEqual(inversions([1])[0], 0)
        self.assertEqual(inversions([1, 2, 3])[0], 0)
        self.assertEqual(inversions([3, 2, 1])[0], 3)
        self.assertEqual(inversions([5, 6, 1, 4, 3, 0, 2])[0], 16)


if __name__ == '__main__':
    unittest.main()
