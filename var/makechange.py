#!/usr/bin/env python

import sys

D = [2, 7]

def makechange(n):
  r = n
  for d in D:           # Give each denomination "a chance" to remove
    while r - d >= 0:   # multiples of itself from n
      r = r - d
    if r == 0:          # We went through all denominations as much as
      return True       # we could, see if we were able to make change
  return False


if __name__ == '__main__':
  print makechange(int(sys.argv[1]))
