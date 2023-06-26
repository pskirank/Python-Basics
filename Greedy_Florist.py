#https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse = True)
    total_cost, prev_purchase = 0,0
    for i in range(len(c)):
        current_purchase = (prev_purchase // k) + 1
        total_cost += current_purchase * c[i]
        prev_purchase += 1
    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
