"""
https://www.hackerrank.com/challenges/ginorts/problem
"""

input = input("Enter the Text:")
list = sorted(input)
lowers, uppers, odds, evens = [], [], [], []
for i in list:
    if i.islower() == True:
        lowers.append(i)
        lowers.sort()
    elif i.isupper() == True:
        uppers.append(i)
        uppers.sort()
    elif int(i) % 2 == 1:
        odds.append(i)
        odds.sort()
    elif int(i) % 2 == 0:
        evens.append(i)
        evens.sort()
print("".join(lowers)+ "".join(uppers) + "".join(odds) + "".join(evens))
