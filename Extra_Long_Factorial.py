#https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    val = 1
    for i in range(1, n+1):
        val *= i
    print(val)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
