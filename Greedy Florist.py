#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    n = len(c)
    if k==n:
        return sum(c)
    else:
        m = n // k
        if m == 0:
            ix = n - k
            return sum(c[ix:]) + c[:ix] * 2
        else:
            _sum = 0
            r = n % k
            _sum += sum(c[:r]) * (m + 1)
            for i in range(m):
                if i == 0:
                    _sum += sum(c[-k:])
                else:
                    _sum += sum(c[-k*(i+1): -k*i]) * (i+1) 
            return _sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
