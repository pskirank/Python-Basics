#https://www.hackerrank.com/challenges/np-inner-and-outer/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy
a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))
print(numpy.inner(a,b))
print(numpy.outer(a,b))
