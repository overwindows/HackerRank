#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    _dict = {}
    for i in range(len(cost)):
        if cost[i] in _dict:
            _dict[cost[i]].append(i)
        else:
            _dict[cost[i]] = []
            _dict[cost[i]].append(i)
    
    for x in cost:
        if money > x and (money - x) in _dict:
            id1 = _dict[x][0]
            if x == money-x:
                if len(_dict[x]) > 1:
                    id2 = _dict[x][1]
                    break
                else:
                    pass
            else:
                id2 = _dict[money - x][0]
                break
    print(id1+1,id2+1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
