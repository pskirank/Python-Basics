#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

#Solution-1:
A,B = list(map(int, input().split()))
list_a,list_b = [],[]
for i in range(A):
    list_a.append(input())
for i in range(B):
    list_b.append(input())
for j in list_b:
    if j in list_a:
        index_list = list(map(str, [k+1 for k in range(len(list_a)) if list_a[k]==j]))
        print(" ".join(index_list))
    else:
        print('-1')

#Solution-2:
from collections import defaultdict

A,B = list(map(int, input().split()))
C = defaultdict(list)
for i in range(A):
    C[input()].append(i+1)
for i in range(B):
    print(*C.get(input(),[-1]))
