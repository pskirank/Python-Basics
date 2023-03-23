#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    substrings1 = []
    dict1 = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            x = "".join(sorted(s[i : j + 1]))
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
            substrings1.append(x)
    count = 0
    for x in dict1:
        if dict1[x] > 1:
            count += dict1[x] * (dict1[x] - 1) // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
