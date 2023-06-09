#https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    topics_prep = [int(x, 2) for x in topic]
    tops = Counter()
    for i in topics_prep:
        for j in topics_prep:
            if i != j:
                tops[(i | j).bit_count()] += 1
    max_ = max(list(tops))
    return [max_, tops[max_]//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
