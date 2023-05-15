#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&isFullScreen=false

import numpy

n,m = map(int, input().split())
lst1 = []
for i in range(n):
    lst1.append(list(map(int, input().split())))
my_array = numpy.array(lst1)
sum_arr = numpy.sum(my_array, axis = 0)
print(numpy.prod(sum_arr))
