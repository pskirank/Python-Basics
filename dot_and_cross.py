#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

n = int(input())
a = numpy.array([input().split() for i in range(n)], int)
b = numpy.array([input().split() for i in range(n)], int)
print(numpy.dot(a,b))
