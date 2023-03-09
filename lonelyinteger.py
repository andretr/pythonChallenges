#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    unique_set = set()
    my_map = dict()
    for i in a:
        if i not in my_map:
            my_map[i] = True
            unique_set.add(i)
        else:
            my_map[i] = False
            unique_set.discard(i)
    val = unique_set.pop()
    print(val)
    return val

    # for key, value in my_map.items():
    #     if value == True:
    #         print(key)
    #         return key
    # return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))

    a = [4, 4, 3, 2, 6, 9, 2, 8, 8, 3, 9]
    result = lonelyinteger(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()
