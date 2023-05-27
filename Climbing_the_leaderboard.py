#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_ranks = sorted(set(ranked), reverse=True)
    i = len(unique_ranks) - 1
    ranks = []
    for score in player:
        while i >= 0 and score > unique_ranks[i]:
            i -= 1
        if i == -1:
            ranks.append(1)
        elif score == unique_ranks[i]:
            ranks.append(i+1)
        else:
            ranks.append(i+2)
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
