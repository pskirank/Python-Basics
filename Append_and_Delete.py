#https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    val = min(len(s), len(t))
    cl = 0
    for i in range(val):
        if s[i] != t[i]:
            break
        cl = i + 1
    ops = k - (len(s) + len(t) - (2*cl))
    if ops >= 0 and (ops%2 == 0 or ops > 2 * cl):
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    fptr.write(result + '\n')
    fptr.close()
