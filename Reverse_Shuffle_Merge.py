#https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# !/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations


#
# Complete the 'reverseShuffleMerge' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def getFrecuency(s):
    result = {}
    for char in s:
        result[char] = result[char] + 1 if char in result else 1
    for k, v in result.items():
        result[k] = v / 2
    return result


def reverseShuffleMerge(s):
    # Write your code here
    frecuency = getFrecuency(s)
    inserted = dict(zip(frecuency.keys(), [0 for _ in frecuency.keys()]))
    discarded = frecuency.copy()
    result = [s[-1]]
    inserted[s[-1]] += 1
    for c in s[-2::-1]:
        if (inserted[c] < frecuency[c]):  
            while len(result) > 0:
                if result[-1] > c and discarded[result[-1]] - 1 >= 0:
                    removed = result.pop()
                    discarded[removed] -= 1
                    inserted[removed] -= 1
                else:
                    break
            result.append(c)
            inserted[c] += 1
        else:
            discarded[c] -= 1
    return "".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = reverseShuffleMerge(s)
    fptr.write(result + '\n')
    fptr.close()
