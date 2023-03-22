#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import Counter

def checkMagazine(magazine, note):
    mag_ctr = Counter(magazine)
    note_ctr = Counter(note)
    mag_ctr.subtract(note_ctr)
    if list(filter(lambda x: x < 0, mag_ctr.values())):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
