#!/usr/bin/python

import sys

def plusMinus(arr):
    positive_count = negative_count = zero_count = 0
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1
    pos = positive_count / float(n)
    neg = negative_count / float(n)
    zer = zero_count / float(n)
    print pos
    print neg
    print zer

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
