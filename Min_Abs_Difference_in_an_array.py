#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

#Solution-1
# !/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    diffs = arr[-1]
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diffs > diff:
            diffs = diff
    return diffs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

#Solution-2
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr2 = []
    lst1 = list(combinations(arr, 2))
    for i in lst1:
        arr2.append(abs(i[0] - i[1]))
    return min(arr2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
