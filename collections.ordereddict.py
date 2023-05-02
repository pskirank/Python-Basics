#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import OrderedDict
N = int(input())

ordered_dict = OrderedDict()
for i in range(N):
    *name, price = input().split()
    name = ' '.join(name)
    price = int(price)
    if name not in ordered_dict:
        ordered_dict[name] = price
    elif name in ordered_dict:
        ordered_dict[name] += price
for j in ordered_dict:
    print(j, ordered_dict[j])
