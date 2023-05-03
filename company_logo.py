#https://www.hackerrank.com/challenges/most-commons/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import Counter

str1 = input()
most_common_character = Counter(sorted(str1)).most_common(3)
for i in most_common_character:
    print(*i)
