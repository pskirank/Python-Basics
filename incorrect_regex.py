#https://www.hackerrank.com/challenges/incorrect-regex/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

import re

t = int(input())
for i in range(t):
    try:
        s = input()
        re.compile(s)
        print("True")
    except re.error:
        print("False")
