#!/bin/python3

import sys
from time import strptime, strftime

def timeConversion(s):
    return strftime("%H:%M:%S", strptime(s,"%I:%M:%S%p"))

s = input().strip()
result = timeConversion(s)
print(result)
