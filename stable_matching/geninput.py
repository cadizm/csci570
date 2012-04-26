#!/usr/bin/env python

import sys
import random

N = int(sys.argv[1])
print N
for i in range(2*N):
    seq = [i for i in range(N)]
    random.shuffle(seq)
    seq = ", ".join([str(i) for i in seq])
    print seq
