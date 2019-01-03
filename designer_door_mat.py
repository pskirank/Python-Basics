"""
https://www.hackerrank.com/challenges/designer-door-mat/problem
"""

size = input().split()
rows = int(size[0])
length = int(size[1])
chars = '.|.'
#top
for i in range(0,rows // 2):
    print((chars*(2*i+1)).center(length,'-'))
#center
print('WELCOME'.center(length, '-'))
#bottom
for i in range(0, rows // 2):
    print((chars * (rows//2*2 - 2*i -1)).center(length, '-'))
