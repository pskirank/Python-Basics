#https://www.hackerrank.com/challenges/piling-up/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

t = int(input())
for _ in range(t):
    block_size = int(input())
    block = list(map(int, input().split()))
    result_arr = []
    block_start = 0
    block_end = len(block) - 1
    for i in range(len(block)):
        if block[block_start] >= block[block_end]:
            result_arr.append(block[block_start])
            block_start += 1
        else:
            result_arr.append(block[block_end])
            block_end -= 1
    if result_arr == sorted(result_arr, reverse=True):
        print('Yes')
    else:
        print('No')
