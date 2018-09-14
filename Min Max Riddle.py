#!/bin/python3

# TimeoutError IV
'''
def riddle(a):
    # complete this function
    n = len(a)
    # init
    wnd_size_max = [0] * n
    wnd_min = {}
    prev_list = []
        
    #iterate the element array 
    for i in range(n):
        wnd_size_max[0] = max(wnd_size_max[0], a[i])
        for j in range(1, i+1):
            val = min(a[i-j], a[i])
            wnd_size_max[j] = max(wnd_size_max[j],val)
            a[i-j] = val

    return wnd_size_max
'''

# TimeoutError III
'''
wnd_size_max[0] = max(wnd_size_max[0], a[i])
prev_list.append(a[i])

for j in range(1, i+1): 
    #prev = prev_list.pop(0)
    val = min(prev_list.pop(0), a[i])
    wnd_size_max[j] = max(wnd_size_max[j],val)
    prev_list.append(val)
'''

# TimeoutError II
'''
if j not in wnd_min:
    wnd_min[j] = []
if j > 0:
    wnd_min[j].append(min(a[i],wnd_min[j-1][i-j])) 
    wnd_size_max[j] = max(wnd_size_max[j], min(a[i],wnd_min[j-1][i-j]))
else:
    wnd_min[j].append(a[i])                
    wnd_size_max[j] = max(wnd_size_max[j], a[i])
#print(wnd_min)
'''

# TimeoutError
'''  
if j in wnd_min:
    while(len(wnd_min[j]) > 0 and wnd_min[j][-1] > a[i]):
        wnd_min[j].pop()
else:
    wnd_min[j] = []
wnd_min[j].append(a[i])

if i < j:
    wnd_size_max[j] = wnd_min[j][0]
else:                
    if len(wnd_min[j]) > 0 and wnd_min[j][0] == a[i-j]:
        wnd_min[j].pop(0)
    wnd_size_max[j] = max(wnd_size_max[j], wnd_min[j][0])
'''
#print(prev_list)

#res = []
#for i in range(n):
#    res.append(wnd_size_max[i])
#return res


# 3 5 4 7 6 2
#   3 4 4 6 2
#     3 4 4 2
#       3 4 2
#         3 2
#           2

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(a):
    # complete this function
    n = len(a)
    # init
    wnd_size_max = {}
    wnd_min = {}
    stack = []
    fwd = [1] * n
    back = [1] * n     
    res = []
    #iterate the element array
    for i in range(n):
        while stack:
            if a[i] > a[stack[-1]]:
                break
            else: # a[i]
                ix = stack.pop()
                fwd[i] += fwd[ix]
        stack.append(i)
    
    stack.clear()
    
    for i in range(n-1,-1,-1):
        while stack:
            if a[i] > a[stack[-1]]:
                break
            else:
                ix = stack.pop()
                back[i] += back[ix]
        stack.append(i)
    
    stack.clear()
    
    for i in range(n):
        if a[i] not in wnd_min:
            wnd_min[a[i]] = fwd[i] + back[i] -1
        else:
            wnd_min[a[i]] = max(wnd_min[a[i]], fwd[i] + back[i] -1)
    
    # invert
    for k,v in wnd_min.items():
        if v not in wnd_size_max:
            wnd_size_max[v] = k
        else:
            wnd_size_max[v] = max(k, wnd_size_max[v])
    
    largest = 0
    for i in range(n,0,-1):            
        if i in wnd_size_max and wnd_size_max[i] > largest:
                largest = wnd_size_max[i]
        else:
            if largest == 0:
                print(i)
                largest = wnd_size_max[i]
        res.append(largest)

    res.reverse()
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
