#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/lilys-homework/problem
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    return min(map(min_swap, [arr, list(reversed(arr))]))

def min_swap(arr):
    swap = 0
    sorted_arr = sorted(arr)
    idx_dict = {e: i for i, e in enumerate(arr)}
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            idx = idx_dict[sorted_arr[i]]
            idx_dict[arr[i]] = idx_dict[arr[idx]]
            arr[i], arr[idx] = arr[idx], arr[i]
            swap += 1
    
    return swap
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
