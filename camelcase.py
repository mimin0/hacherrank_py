#!/bin/python
## Problem: https://www.hackerrank.com/challenges/camelcase/problem

import sys

customText = "FistThingsTheSea"

s = customText
wordCounter = 0
if len(s) > 0:
    wordCounter = 1
try:
    xrange
except NameError:
    xrange = range
    
for i in xrange(1, len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        wordCounter += 1
print(wordCounter)
