#https://www.hackerrank.com/challenges/word-order/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import Counter

n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
print(len(Counter(list1)))
for j in Counter(list1).values():
    print(j, end=' ')
