#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    # solve here
    _arr = []
    root = {}
    _maxlen = 0
    
    for x in arr:
        _x = list(bin(x).replace('0b',''))
        if len(_x) > _maxlen:
            _maxlen = len(_x)
        _arr.append(_x)
        
    for _x in _arr:
        delta = _maxlen - len(_x)
        node = root
        for _ in range(delta):
            if 0 not in node:
                node[0] = {}
            node = node[0]
        
        for __x in _x:
            if int(__x) not in node:
                node[int(__x)] = {}
            node = node[int(__x)]
            
    _max = []
    result = []
    for query in queries:
        _query = list(bin(query).replace('0b',''))
        delta  = len(_query) - _maxlen
        
        if delta >= 0:
            for _ in range(delta):
                _max.append(_query.pop(0))
        else:
            for _ in range(-delta):
                _query = ['0'] + _query
    
        node = root
        for q in _query:
            if 1-int(q) in node:
                node = node[1-int(q)]
                _max.append('1')
            elif int(q) in node:
                node = node[int(q)]
                _max.append('0')
        result.append(int(''.join(_max),2))
        _max.clear()
    
    '''
    result = []
    for query in queries:
        _max = 0
        for a in arr:
            if _max < a^query:
                _max = a^query
        result.append(_max)
    '''
    return result   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
