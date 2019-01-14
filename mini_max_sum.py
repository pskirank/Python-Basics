#https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    list = [int(sum(sorted(arr)[:4])), int(sum(sorted(arr)[1:]))]
    for i in list:
        print(i, end = ' ')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
