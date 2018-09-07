#!/bin/python3

import math
import os
import random
import re
import sys

def root(tree, node):
    while(tree[node] != node):
        node = tree[node]
    return node
    
# Complete the maxCircle function below.
def maxCircle(queries):
    res = []
    g = {}
    m = {}
    _max = 0
    for query in queries:
        a, b = query
        if a not in g:
            g[a] = a
            m[a] = 1
        if b not in g:
            g[b] = b
            m[b] = 1
    
        r_a = root(g, a)
        r_b = root(g, b)
        #print(r_a, m[r_a],r_b, m[r_b])
        
        # Magic Here!!!
        if r_a != r_b:
            if m[r_a] >= m[r_b]:
                g[r_b] = g[r_a]
                m[r_a] += m[r_b]
                if _max < m[r_a]:
                    _max = m[r_a]
            else:
                g[r_a] = g[r_b]
                m[r_b] += m[r_a]
                if _max < m[r_b]:
                    _max = m[r_b]
        res.append(_max)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
