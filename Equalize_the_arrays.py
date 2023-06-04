#https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true


#Solution-1
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    keys_to_remove, vals = [], []
    dict1 = dict(Counter(arr))
    for key, value in dict1.items():
        if value == max(dict1.values()):
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del dict1[key]
    for key, value in dict1.items():
        vals.append(value)
    return sum(vals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

#Solution - 2

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    max = 0
    for i in arr:
        if arr.count(i) > max:
            max = arr.count(i)
    return len(arr) - max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
