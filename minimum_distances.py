#https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#Solution-1:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    ans = []
    for i,x in enumerate(a):
        if x in a[i+1:]:
            ans.append(abs(i - (a[i+1:].index(x) + i +1)))
    if len(ans) > 0:
        return min(ans)
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()



#Solution-2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    n = len(a)
    list1 = []
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                list1.append(j-1)
    if len(list1) == 0:
        return -1
    else:
        return min(list1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
