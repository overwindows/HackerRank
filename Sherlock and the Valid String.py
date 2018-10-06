#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    str_dict = {}
    invert_dict = {}
    str_arr = list(s)
    n = 0

    for c in str_arr:
        if c in str_dict:
            str_dict[c] += 1
        else:
            str_dict[c] = 1
            n += 1
    
    #print(str_dict,n)
    
    max_cnt = 2
    for _, v in str_dict.items():
        if v in invert_dict:
            invert_dict[v] += 1
        else:
            invert_dict[v] = 1
            max_cnt -= 1
    
    #print(invert_dict,max_cnt)
    
    if max_cnt < 0:
        return 'NO'
    
    if max_cnt == 1:
        return 'YES'
    
    assert max_cnt == 0 
    
    x = None
    y = None
    for k, v in invert_dict.items():
        if v == 1:
            x = k
        elif v == n-1:
            y = k
        else:
            return 'NO'
    
    #print(x,y)
    
    if abs(x-y) == 1 or x==1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
