#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

n, x = map(int, input().split())
list1 = []
for i in range(x):
    list1.append(list(map(float, input().split())))
print(*map(lambda i: sum(i)/x, zip(*list1)), sep='\n')
