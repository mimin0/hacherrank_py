#!/usr/bin/python

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    summ = 0
    for i in range(n):
        summ += ar[i]
    
    return summ

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
