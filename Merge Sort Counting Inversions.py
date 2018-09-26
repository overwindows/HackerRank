#!/bin/python3
# Tricky!  Passed all testcases under Pypy3
'''
def countInversions(arr):
    arr_len = len(arr) -1
    swap = 0
    for i in range(arr_len):
        for j in range(arr_len - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap += 1
    return swap
'''

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr,begin,end):
    if end-begin < 2:
        return 0
    
    mid = (end+begin)//2
    swap = 0
    
    swap0 = countInversions(arr, begin, mid)
    swap1 = countInversions(arr, mid, end)
    
    tmp = []
    i = begin
    j = mid

    while i < mid and j < end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i = i+1
        else:
            tmp.append(arr[j])
            j = j+1
            swap += (mid-i)
    
    for k in range(i, mid):
        tmp.append(arr[k])
    
    for k in range(j, end):
        tmp.append(arr[k])
    
    k=0
    for m in range(begin, end):
        arr[m] = tmp[k]
        k += 1        
    return swap + swap0 + swap1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr,0,n)

        fptr.write(str(result) + '\n')

    fptr.close()
