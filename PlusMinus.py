#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive, negative, zero = 0, 0, 0
    for i in arr:
        if (i > 0):
            positive += 1
        elif (i < 0):
            negative += 1
        else:
            zero += 1

    print(positive / float(len(arr)))
    print(negative / float(len(arr)))
    print(zero / float(len(arr)))


if __name__ == '__main__':
    # n = int(input().strip())
    n = 6
    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
