#https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    for i in set(b):
        if b.count('_') == 0:
            if b.index(i) != len(b) - 1 and i != b[b.index(i)+1] or b.count(i) == 1:
                return 'NO'
                break
        elif (b.count(i) == 1 and i != '_'):
            return 'NO'
            break
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        fptr.write(result + '\n')
    fptr.close()
