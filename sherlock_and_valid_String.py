#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Solution-1

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq = {}

    for c in s:
        if freq.get(c):
            freq[c] += 1
        else:
            freq[c] = 1

    frequencies = list(freq.values())
    prev_frequency = frequencies[0]

    removed_character = False

    for i in range(1, len(frequencies)):
        if prev_frequency != frequencies[i]:
            if removed_character:
                return 'NO'
            else:
                removed_character = True
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

#Solution-2

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
