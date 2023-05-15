#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input().strip())
sorted_arr = sorted(arr, key=lambda x: x[k])
for element in sorted_arr:
    print(' '.join(map(str, element)))
