#!/bin/python3

'''
def activityNotifications(expenditure, d):
    n = len(expenditure)
    cnt = 0
    for i in range(n-d):
        if i==0:
            buf = expenditure[i:d+i]
            buf.sort()
        else:
            buf.remove(expenditure[i-1])
            buf.append(expenditure[i+d-1])
            for j in range(1,d):
                if buf[d-j] < buf[d-j-1]:
                    buf[d-j], buf[d-j-1] = buf[d-j-1], buf[d-j]

        if d%2:
            median = buf[d//2] * 2
        else:
            median = (buf[d//2]+buf[d//2+1])            
        if expenditure[d+i] >= median:
            cnt += 1

    return cnt
'''

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    n = len(expenditure)
    cnt = 0
    arr = [0] * 201
    
    # init
    for i in range(d):
        arr[expenditure[i]] += 1
    
    for j in range(d,n):
        #get median
        #print(arr)
        v = 0
        m = d//2
        if d%2:
            for i in range(201):
                v += arr[i]
                if v > m:
                    median = i
                    break
        else:
            k = -1
            for i in range(201):
                v+= arr[i]
                if v > m:
                    #print(k,i)
                    if v - arr[i] == m:
                        median = (i+k)/2
                    else:
                        median = i
                    break
                #if arr[i] > 0:
                if v == m:
                    k = i
        #print(median)
        if expenditure[j] >= median*2:
            cnt += 1
        
        arr[expenditure[j]] += 1
        arr[expenditure[j-d]] -= 1
        
    return cnt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
