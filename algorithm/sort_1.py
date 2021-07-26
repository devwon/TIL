#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/countingsort4/problem
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    res = ''
    for i in range(int(len(arr)/2)):
        arr[i][1] = '-'
    arr.sort(key=lambda x: int(x[0]))

    for i in range(len(arr)):
        res += arr[i][1] + ' '

    print(res)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
