#https://www.hackerrank.com/challenges/non-divisible-subset/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    rem_freq = [0]*k
    for n in s:
        rem_freq[n % k] += 1
    subsets = 0
    if rem_freq[0] > 0:
        subsets = 1
    if k % 2 == 0 and rem_freq[k // 2] > 0:
        subsets += 1
    for i in range(1, (k+1) // 2):
        subsets += max(rem_freq[i], rem_freq[k-i])
    return subsets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    fptr.write(str(result) + '\n')
    fptr.close()
