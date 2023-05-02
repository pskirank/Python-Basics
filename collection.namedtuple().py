#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?h_r=next-challenge&h_v=zen

from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input())
print(sum(int(Student(*input().split()).MARKS) for i in range(N)) / N)
