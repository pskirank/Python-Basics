#https://www.hackerrank.com/challenges/validating-uid/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

T = int(input())
regex = r'^(?=[a-zA-Z0-9]{10}$)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?!.*(.).*\1)[a-zA-Z0-9]+$'
for i in range(T):
    if re.match(regex, input()):
        print('Valid')
    else:
        print('Invalid')
