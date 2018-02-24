#!/bin/python

import sys

def diagonalDifference(a):
    ver_a = ver_b = j = 0
    for i in range(len(a)):
        ver_a += a[i][i]
        j = j - 1
        ver_b += a[i][j]

    return abs(ver_a - ver_b)

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result