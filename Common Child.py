#!/bin/python3
#Pypy 3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    common = [[0 for c in range(5001)] for r in range(5001)]
    s1_arr = list(s1)
    s2_arr = list(s2)
    s1_len = len(s1_arr)
    s2_len = len(s2_arr)
    _max = 0
    
    for i in range(s1_len):
        for j in range(s2_len):
            if s1_arr[i] == s2_arr[j]:
                common[i][j] = 1
    
    for i in range(s1_len):
        for j in range(s2_len):
            v = 0
            if i > 0 and j > 0:
                v = common[i][j] + common[i-1][j-1]
                common[i][j] = max(common[i-1][j], common[i][j-1], v)
            else:
                if i == 0:
                    if j==0: #[0,0]
                        pass 
                    else: #[0,j]
                        common[0][j] = max(common[0][j-1], common[0][j])
            
            _max = max(_max,common[i][j])
    
    return _max
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
