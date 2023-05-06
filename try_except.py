#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as zerr:
        print("Error Code:", zerr)
