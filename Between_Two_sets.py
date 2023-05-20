#https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    count = 0
    list1 = [max(sorted(a)), min(sorted(b))]
    for i in range(list1[0], list1[1]+1):
        if all( i % j == 0 for j in a) and all(k % i == 0 for k in b):
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()
