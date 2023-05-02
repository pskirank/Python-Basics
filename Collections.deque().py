#https://www.hackerrank.com/challenges/py-collections-deque/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        action, val = cmd[0], cmd[1]
    else:
        action = cmd[0]
    if action == 'append':
        d.append(val)
    elif action == 'appendleft':
        d.appendleft(val)
    elif action == 'pop':
        d.pop()
    elif action == 'popleft':
        d.popleft()
    elif action == 'extend':
        d.extend(val)
    elif action == 'extendleft':
        d.extendleft(val)
    elif action == 'remove':
        d.remove(val)
    elif action == 'reverse':
        d.reverse()
    elif action == 'rotate':
        d.rotate(val)
    elif action == 'clear':
        d.clear()
for i in d:
    print(i, end=' ')
