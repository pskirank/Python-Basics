#https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen

#Approach-1 - My own method. Some TCs failed due to timeout using this method
#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    combs, lengths = [],[]
    for i in range(1, len(prices)+1):
        for j in itertools.combinations(prices, i):
            if sum(j) <= k:
                combs.append(j)
    for each in combs:
        lengths.append(len(each))
    return max(lengths)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
#----------------------------------------------------------------------------------------------------------------------
#Approach-2
import re
import sys
import itertools

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    total_val, toy_cnt = 0,0
    for i in prices:
        if i+total_val <= k:
            total_val += i
            toy_cnt += 1
    return toy_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
