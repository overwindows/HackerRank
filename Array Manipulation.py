#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0 for i in range(0, n+1)]
    for query in queries:
        start, end, val = query
        a[start] += val
        a[end] -= val
    
    _max = 0
    _sum = 0
    for i in range(0, n+1):
        _sum += a[i]
        if _sum > _max:
            _max = _sum
    return _max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
