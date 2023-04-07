#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

k = int(input())
room_nos_list = Counter(list(map(int, input().split())))
for i in room_nos_list:
    if room_nos_list[i] == 1:
        print(i)
