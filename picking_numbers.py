#https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    start, end, max_length = 0,0,0
    a.sort()
    while end < len(a):
        if abs(a[end] - a[start]) > 1:
            start += 1
        else:
            max_length = max(max_length, end-start+1)
            end += 1
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
