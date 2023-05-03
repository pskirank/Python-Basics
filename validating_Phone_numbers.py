#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

N = int(input())
for _ in range(N):
    pattern = r'^[7-9]\d{9}$'
    print('YES' if re.match(pattern, input()) else 'NO')
