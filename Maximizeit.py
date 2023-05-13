#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#Solution-1
k, m = map(int, input().split())
fin_list = []
for i in range(k):
    list1 = list(map(int, input().split()))
    fin_list.append(max(list1))
print(sum(x ** 2 for x in fin_list) % m)

#Solution-2

from itertools import product

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]
max_val = -1
for values in product(*lists):
    max_val = max(max_val, sum(v**2 for v in values) % m)
print(max_val)
