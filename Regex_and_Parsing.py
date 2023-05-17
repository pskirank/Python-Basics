#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re
s, k = input(), input()

current = 0
m = re.search(k, s[current:])
if not m:
    print("(-1, -1)")
else:
    while m:
        print(f"({current + m.start()}, {current + m.end() - 1})")
        current = current + m.start() + 1
        m = re.search(k, s[current:])
