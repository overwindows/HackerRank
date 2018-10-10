#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    cnt = n
    arr = list(s)
    _arr = []
    _idx_dict = {} 
    
    for x in arr:
        if len(_arr) == 0:
            _arr.append(x)
            _idx_dict[len(_arr)-1] = 1
        else:
            if _arr[-1] == x:
                _idx_dict[len(_arr)-1] += 1
            else:
                _arr.append(x)
                _idx_dict[len(_arr)-1] = 1
    
    #print(_arr)
    #print(_idx_dict)
    for _, v in _idx_dict.items():
        if v > 1:
            cnt += v*(v-1)//2
    
    l = len(_arr)
    
    for i in range(1,l-1):
        if _idx_dict[i] == 1 and _arr[i-1] == _arr[i+1]:
            cnt += min(_idx_dict[i-1],_idx_dict[i+1])
          
    return cnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
