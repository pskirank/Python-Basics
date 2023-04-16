#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    counter1 = Counter(list(s))
    ctr_vals = list(counter1.values())
    max_val = max(ctr_vals)
    min_val = min(ctr_vals)
    if max_val == min_val:
        return 'YES'
    elif ctr_vals.count(min_val) == 1 and abs(max_val - min_val) == 1:
        return 'YES'
    elif ctr_vals.count(max_val) == 1 and max_val == abs(len(s) - 1):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    if result is None:
        result = ' '
    fptr.write(result + '\n')
    fptr.close()
