#https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    val = 0
    freq = defaultdict(int)
    pairs = defaultdict(int)
    for element in arr:
        if element % r == 0:
            val += pairs[element//r]
            pairs[element] += freq[element // r]
        freq[element] += 1
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()
