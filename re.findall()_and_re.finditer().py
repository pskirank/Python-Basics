#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

import re

vowels = '[aeiouAEOIU]'
consos = '[^aeiouAEIOU]'

S = input()
regexp = r'(?=(' + consos + ')(' + vowels + '{2,})(' + consos + '))'
match = re.findall(regexp, S)
if match:
    for _ in match:
        print(_[1])
else:
    print(-1)
