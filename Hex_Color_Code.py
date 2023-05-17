#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

n = int(input())
regex1 = re.compile(r'[ \:]+(\#[a-fA-F0-9]{3,6})')
for _ in range(n):
    for i in regex1.findall(input()):
        print(i)
