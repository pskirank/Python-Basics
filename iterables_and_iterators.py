#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

N = int(input())
list1 = list(input().split())
k = int(input())
word_combs = list(combinations(list1, k))
cnt = 0
for i in word_combs:
    if 'a' in i:
        cnt += 1
print(round((cnt / len(word_combs)), 4))
