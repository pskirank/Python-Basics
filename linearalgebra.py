#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

list1 = []
size = int(input())
for i in range(size):
    list1.append(list(map(float, input().split())))
print(round(numpy.linalg.det(numpy.array(list1)),2))
