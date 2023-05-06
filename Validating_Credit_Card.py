#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

pattern = r'(?!.*(\d)(-?\1){3}.*)^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'

for _ in range(int(input())):
    if re.match(pattern, input()):
        print('Valid')
    else:
        print('Invalid')
