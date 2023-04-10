#https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3
import os
def freqQuery(queries):
    freq_count, output = {}, []
    for command, value in queries:
        if command == 1: # insert
            # Add to existing freq, if present. Else set as 1
            freq_count[value] = freq_count.get(value, 0) + 1
        if command == 2 and freq_count.get(value,0) > 0: # remove
            # Decriment existing value
            freq_count[value] -= 1
        if command == 3: # check freq
            output.append(1 if value in freq_count.values() else 0)
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
