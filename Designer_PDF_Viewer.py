#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    word_heights = []
    letter_heights = {chr(ord('a') + i): h[i] for i in range(len(h))}
    for j in word:
        word_heights.append(letter_heights[j])
    return (max(word_heights) * len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()
