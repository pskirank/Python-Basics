#https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    if a == b:
        return [(n-1)*a]
    diff = abs(a-b)
    start = min(a,b)*(n-1)
    end = max(a,b)*(n-1)
    ans = []
    for i in range(start, end+1, diff):
        ans.append(i)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
