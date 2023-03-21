from itertools import combinations_with_replacement

s, k = input().split()
text = sorted([x.upper() for x in s])
for i in list(combinations_with_replacement(text, int(k))):
    print(''.join(i))
