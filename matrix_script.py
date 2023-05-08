#https://www.hackerrank.com/challenges/matrix-script/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Solution-1
import re
n, m = map(int, input("Enter number of rows and columns:").rstrip().split())
matrix = []
for i in range(n):
    for j in range(m):
        matrix_element = input("Enter Elements of the matrix:")
        matrix.append(matrix_element)
input_str = ''.join(matrix)
regex = r'[^a-zA-Z0-9#!%]+'
print(re.sub(regex, ' ', input_str))

#Solution#2
from re import sub
from itertools import chain

n, m = [int(x) for x in input().split()]
encoded_msg = "".join(chain.from_iterable(zip(*[input() for _ in range(n)])))

print(sub(r"([A-Za-z0-9])(?:\W|\s)+([A-Za-z0-9])", lambda x: f"{x.group(1)} {x.group(2)}", encoded_msg))
