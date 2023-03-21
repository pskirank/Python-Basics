from itertools import groupby
list1 = []
s = input()
for i, j in groupby(s):
    list1.append((len(list(j)), int(i)))
for _ in list1:
    print(_, end=' ')
