#https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
str1, val = input().split()
for _ in range(1, int(val)+1):
    comb_list = list(combinations(sorted([i.upper() for i in str1]), _))
    for i in comb_list:
        print(''.join(i))
