#https://www.hackerrank.com/challenges/ctci-merge-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    count = 0

    def merge(arr):
        nonlocal count
        if len(arr) < 2:
            return arr
        L = merge(arr[:len(arr) // 2])
        R = merge(arr[len(arr) // 2:])
        n = m = 0
        C = []
        while n < len(L) and m < len(R):
            if L[n] <= R[m]:
                C.append(L[n])
                n += 1
            else:
                C.append(R[m])
                m += 1
                count += len(L) - n
        return C + L[n:] + R[m:]

    merge(arr)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
