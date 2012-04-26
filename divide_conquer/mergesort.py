#!/usr/bin/env python

#
# Standard mergesort
#

import random
import unittest

def mergesort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        L1 = mergesort(L[:len(L)/2])
        L2 = mergesort(L[len(L)/2:])
        L3 = []
        while L1 and L2:
            if L1[0] < L2[0]:
                L3.append(L1.pop(0))
            else:
                L3.append(L2.pop(0))
            if len(L1) == 0:
                L3.extend(L2)
            if len(L2) == 0:
                L3.extend(L1)

        return L3


class TestMergesort(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(mergesort([3, 2, 1, 0]), [0, 1, 2, 3])
        L = S = [random.randint(-1000, 1000) for i in range(1001)]
        S.sort()
        self.assertEqual(mergesort(L), S)


if __name__ == '__main__':
    unittest.main()
