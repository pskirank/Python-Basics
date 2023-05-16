#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import re

n = int(input())
for i in range(n):
    print(re.sub(r' \|\|(?= )', ' or', re.sub(r' &&(?= )',' and',input())))
