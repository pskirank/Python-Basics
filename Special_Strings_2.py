#https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    subs, chars, char = 1, 1, s[0]
    for i in range(1, len(s)):
        if char == s[i]:
            chars += 1
            subs += chars
        else:
            for j in range(i + 1, min(n, i + 1 + chars)):
                if s[j] != char:
                    break
                subs += 1
            char, chars = s[i], 1
            subs += 1
    return subs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = substrCount(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
