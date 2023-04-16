#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the 'makeAnagram' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b

def makeAnagram(a, b):
    # Write your code here
    count = 0
    a_list = Counter(sorted(list(a)))
    b_list = Counter(sorted(list(b)))
    for key in a_list:
        if key in b_list:
            count += abs(a_list[key] - b_list[key])
        else:
            count += abs(a_list[key])
    for key in b_list:
        if key not in a_list:
            count += b_list[key]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
