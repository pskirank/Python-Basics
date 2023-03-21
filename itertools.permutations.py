#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations
val1 = input().split()
text = [i.upper() for i in val1[0]]
perm_list = sorted(set(list(permutations(text, int(val1[1])))))
for i in perm_list:
    print(''.join(i))
