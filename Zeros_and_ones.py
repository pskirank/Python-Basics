#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

t = tuple(map(int,input().split()))
print(numpy.zeros(t, int), sep = '\n')
print(numpy.ones(t, int), sep = '\n')
