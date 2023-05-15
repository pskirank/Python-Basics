#https://www.hackerrank.com/challenges/np-min-and-max/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true

import numpy

n,m = map(int, input().split())
lst1 = []
for i in range(n):
    lst1.append(list(map(int, input().split())))
my_array = numpy.array(lst1)
min_array = numpy.min(my_array, axis = 1)
print(numpy.max(min_array, axis = None))
