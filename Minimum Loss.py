#!/bin/python3

import math
import os
import random
import re
import sys

# 20 7 8 2 5
# 13 -1 6 -3

# Complete the minimumLoss function below.
def minimumLoss(price):
    idx = {}
    
    for i in range(len(price)):
        idx[price[i]] = i
    
    price.sort(reverse=True)

    minLoss = sys.maxsize
    for j in range(1,len(price)):
        if idx[price[j-1]] < idx[price[j]]:
            minLoss = min(minLoss, price[j-1] - price[j])
    
    return minLoss
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
