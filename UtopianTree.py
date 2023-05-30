#https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    x = 1
    seq = [1]
    for i in range(n):
        ele1 = 2*x
        ele2 = 2*x+1
        seq.extend([ele1,ele2])
        x = ele2
    return seq[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')
    fptr.close()
