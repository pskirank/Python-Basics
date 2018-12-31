"""
https://www.hackerrank.com/challenges/python-lists/problem
"""
n = int(input())
arr = []
for _ in range(n):
    cmd = input().split()
    args = cmd[1:]
    if cmd[0] == "print":
        print(arr)
    else:
        eval("arr"+"."+cmd[0]+"("+",".join(args)+")")
