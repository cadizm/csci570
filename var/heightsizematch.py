#!/usr/bin/env python

H = [10, 22, 53, 1]
S = [2, 4, 54, 18]

# O(2nlogn + n)
H.sort()
S.sort()
sum = 0
for i, e in enumerate(H):
    sum += abs(e - S[i])
print sum * 1.0/len(H)
