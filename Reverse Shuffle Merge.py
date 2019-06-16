#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    _s = [c for c in s]
    _s.reverse()
    
    _d_chk = {}
    cnt_d = {}
    dup_d = {}
    stack = []

    for c in _s:
        dup_d[c] = 0
        if c not in cnt_d:
            cnt_d[c] = 1
        else:
            cnt_d[c] += 1

    for k,v in cnt_d.items():
        _d_chk[k] = v//2    
    '''
    print(_d_chk)
    print(_d)
    # print(__d)m
    '''
    for ch in _s:
        #print(stack)
        if not stack:
            stack.append(ch)
            dup_d[ch] += 1
        else:
            while ch < stack[-1]:
                # check replace condition
                # cnt_d[stack[-1]] > _d_chk[stack[-1]] means still buffer
                # dup_d[ch] < _d_chk[ch] means duplicate char should not be added
                # print(cnt_d[stack[-1]], stack[-1], _d_chk[stack[-1]], ch)
                if cnt_d[stack[-1]] > _d_chk[stack[-1]] and dup_d[ch] < _d_chk[ch]:
                    cnt_d[stack[-1]] -= 1
                    dup_d[stack[-1]] -= 1
                    stack.pop()
                else:
                    break
                
                if not stack:
                    break
            
            if dup_d[ch] < _d_chk[ch]:
                stack.append(ch)
                dup_d[ch] += 1
            else:
                cnt_d[ch] -= 1

    return ''.join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
