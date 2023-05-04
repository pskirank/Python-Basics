#https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#Solution-1:
n = int(input())
for _ in range(n):
    bin_number = bin(int(input()))[2:].zfill(32)
    str1 = ''
    for i in str(bin_number):
        if i == '1':
            str1 += '0'
        elif i == '0':
            str1 += '1'
    print(int(str1, 2))

#Solution-2:
def flippingBits(n):
    # Write your code here
    return n ^ 0xFFFFFFFF
