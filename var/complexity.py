#!/usr/bin/env python

import math

def a(n, k):
  return 2**n * n**k

def b(n, k):
  return 2**n * n**(2*k)

def a1(n, k):
  return (math.log(n, 2))**k

def b1(n, c):
  return c * n

def four(n):
  X = 0
  for i in range(1, n+1):
    for j in range(1, n+1):
      X += 1
  return X

if __name__ == '__main__':
  print four(10)
