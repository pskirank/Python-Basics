set1 = set([x for x in range(1,10)])
set2 = set([y for y in range(2,15)])
print(set1)
print(set2)
#print(set1.union(set2))
#print(set1.intersection(set2))
print(list(zip(set1, set2)))
print(dict(zip(set1, set2)))