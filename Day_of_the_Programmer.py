#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=false

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    result = ''
    leap_date = '12.09.'
    non_leap_date = '13.09.'

    if year == 1918:
        result = '26.09.1918'
    elif (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        result = leap_date + str(year)
    elif (year % 4 == 0) and (year <= 1917):
        result = leap_date + str(year)
    else:
        result = non_leap_date + str(year)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
