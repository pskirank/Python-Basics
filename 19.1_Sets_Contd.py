#Problem-11: https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
TCs = int(input())
for i in range(TCs):
    set1_cnt = int(input())
    set1 = set(map(int,input().split()))
    set2_cnt = int(input())
    set2 = set(map(int,input().split()))
    print(set1.issubset(set2))

#Problem-12: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
A = set(map(int, input().split()))
n = int(input())
val1 = True
for i in range(n):
    set1 = set(map(int, input().split()))
    val1 = A.issuperset(set1)
print(val1)
