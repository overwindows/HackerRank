#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    forward = [1] * n
    backward = [1] * n
    res = [0] * n
    
    #forward
    #forward[0] = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            forward[i] = forward[i-1] + 1
        else:
            forward[i] = 1
    #print(forward)
    #backward
    #backward[n-1] = 0
    for j in range(2,n+1):
        if arr[n-j] > arr[n-j+1]:
            backward[n-j] = backward[n-j+1] + 1
        else:
            backward[n-j] = 1
    #print(backward)
    for i in range(n):
        res[i] = max(forward[i],backward[i])    
    
    return sum(res)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
