#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re
from email.utils import parseaddr
n = int(input())
regex = r'[a-zA-Z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}'
for _ in range(n):
    input_line = input()
    if re.fullmatch(regex, parseaddr(input_line)[1]):
        print(input_line)
