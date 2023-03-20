#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, my_list):
    # Write your code here
    counter = 0

    try:
        while (True):
            sorted(my_list)
            if (my_list[0] >= k and my_list[1] >= k):
                print(counter)
                return counter
            new_val = my_list[0] + 2 * my_list[1]
            my_list.append(new_val)
            counter += 1
            del(my_list[0])
            del (my_list[0])
    except Exception as e:
        print(e)
        return -1


def binary_search(arr, val, start, end):
    # we need to distinguish whether we
    # should insert before or after the
    # left boundary. imagine [0] is the last
    # step of the binary search and we need
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # this occurs if we are moving
    # beyond left's boundary meaning
    # the left boundary is the least
    # position to find a number greater than val
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


if __name__ == '__main__':
    k = int(6)
    A = [1, 2, 3, 9, 10, 12]
    result = cookies(k, A)