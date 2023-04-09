#Problem-1: https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
import re
regex = r"^[+-]?\d*\.\d+$"
T = int(input())
for i in range(T):
    print(True if re.match(regex, input()) else False)


#Problem-2: https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
regex_pattern = r"[,.]"	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))


#Problem-3: https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re

pattern = r"([a-z0-9A-Z])\1+"
s = input()
match = re.search(pattern, s)
if match:
    print(match.group(1))
else:
    print(-1)
