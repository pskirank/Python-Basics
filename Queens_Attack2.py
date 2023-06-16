#https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

#Solution-1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    if len(obstacles) != k:
        raise ValueError
    attacked_squares = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    obstacle_set = {(obstacle[0], obstacle[1]) for obstacle in obstacles}
    for dx, dy in directions:
        x, y = r_q, c_q
        while True:
            x += dx
            y += dy
            if x > n or x < 1 or y > n or y < 1 or (x, y) in obstacle_set:
                break
            attacked_squares += 1
    return attacked_squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()


#Solution-2

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    attack_points = []
    cnt_up, cnt_down, cnt_left, cnt_right, diag_up_left, diag_up_right, diag_down_left, diag_down_right = 0, 0, 0, 0, 0, 0, 0, 0
    for j in range(n):
        if j != c_q - 1:
            attack_points.append((r_q, j + 1))
        if j != r_q - 1:
            attack_points.append((j + 1, c_q))
    for j in range(1, n):
        if r_q - j > 0 and c_q - j > 0:
            attack_points.append((r_q - j, c_q - j))
        if r_q + j <= n and c_q + j <= n:
            attack_points.append((r_q + j, c_q + j))
        if r_q - j > 0 and c_q + j <= n:
            attack_points.append((r_q - j, c_q + j))
        if r_q + j <= n and c_q - j > 0:
            attack_points.append((r_q + j, c_q - j))
    o = set([(r, c) for r, c in obstacles])
    for i in range(1, n):
        if (r_q - i, c_q) in o:
            cnt_up += 1
        elif (r_q - i, c_q + i) in o:
            diag_up_right += 1
        elif (r_q, c_q + i) in o:
            cnt_right += 1
        elif (r_q + i, c_q + i) in o:
            diag_down_right += 1
        elif (r_q + i, c_q - i) in o:
            diag_down_left += 1
        elif (r_q + i, c_q) in o:
            cnt_down += 1
        elif (r_q, c_q - i) in o:
            cnt_left += 1
        elif (r_q - i, c_q - i) in o:
            diag_up_left += 1
        else:
            break
    missed = cnt_up + cnt_down + cnt_left + cnt_right + diag_up_left + diag_up_right + diag_down_left + diag_down_right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    obs_set = set(obstacles)
    obs_missed = 0
    for direction in directions:
        dx, dy = direction
        x, y = r_q + dx, c_q + dy
        while 1 <= x <= n and 1 <= y <= n and (x, y) not in obs_set:
            x += dx
            y += dy
        if (x, y) in obs_set:
            obs_missed += 1
    return (len(attack_points) - missed - obs_missed)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()
