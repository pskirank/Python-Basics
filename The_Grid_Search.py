#https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    for i in range(len(G) - (len(P)-1)):
        begin=None
        counter=0
        for element in P:
            x = re.finditer("(?=" + element + ")", G[i + counter])
            x= [match.start() for match in x]
            if x:
                if begin==None:
                    begin = set(x)
                else:
                    begin = begin & set(x)
                    if not begin:
                        break
                counter+=1
            else:
                break
        if counter==len(P):
            return "YES"    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
