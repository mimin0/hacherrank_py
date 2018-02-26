#!/usr/bin/python3
import sys

def miniMaxSum(arr):
    summ = 0
    all_summ = []
    for i in arr:
        summ += i

    for i in arr:
        all_summ.append(summ - i)
    print(min(all_summ), max(all_summ))


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)