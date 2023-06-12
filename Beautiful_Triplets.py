#https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

#Solution - 1:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    cnt = 0
    for i in arr:
        if i+d in arr and i+(2*d) in arr:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    fptr.write(str(result) + '\n')

    fptr.close()




#Solution - 2:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    cnt = 0
    n = len(arr)
    for i in range(n - 2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[j] - arr[i] == d and arr[k] - arr[j] == d:
                    cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    fptr.write(str(result) + '\n')

    fptr.close()
