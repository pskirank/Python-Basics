"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""
sea_level = 0
valley_count = 0
array = ['U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U']

for i in array:
    if i == 'U':
        sea_level += 1
    elif i == 'D':
        sea_level -= 1
        if sea_level == -1:
            valley_count += 1
print(valley_count)
