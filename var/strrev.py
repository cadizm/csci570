#!/usr/bin/env python

import re

def swap(i, j, s):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

def rev1(s):
    "in-place reverse of s"
    t = re.findall('\w', s)
    mid = len(s) >> 1
    for i in range(mid):
        swap(i, len(t)-1-i, t)

    return ''.join(t)

def rev2(s):
    t = re.findall('\w', s)
    i = 0
    j = len(t)-1
    while i != j and i < j:
        swap(i, len(t)-1-i, t)
        i += 1
        j -= 1

    return ''.join(t)


if __name__ == '__main__':
    s = "ab"
    print s
    t = rev2(s)
    print t
