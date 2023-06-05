#https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    result1 = [list(row) for row in grid]
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            depth = int(grid[i][j])
            if depth > int(grid[i-1][j]) and depth > int(grid[i+1][j]) and depth > int(grid[i][j-1]) and depth > int(grid[i][j+1]):
                result1[i][j] = 'X'
    return list(''.join(row) for row in result1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
