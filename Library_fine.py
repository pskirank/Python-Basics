#https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 > y2:
        fine = 10000
    elif y2 == y1:
        if m2 < m1:
            fine = abs(m 2 -m1 ) *500
        elif m2 == m1:
            if d2 < d1:
                fine = abs(d2 - d1 ) *15
            else:
                return 0
        else:
            return 0
    else:
        return 0
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])
    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    fptr.write(str(result) + '\n')
    fptr.close()
