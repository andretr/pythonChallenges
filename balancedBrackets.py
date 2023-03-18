#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    my_map = { 
        "]":"[", 
        ")": "(", 
        "}": "{" 
    }
    my_stack = []
    for idx, val in enumerate(s):
        if idx == 0:
            my_stack.append(val)
            continue
        else:
            if(my_map.get(val) and peek_stack(my_stack) == my_map[val] ):
                my_stack.pop()
            else:
                my_stack.append(val)
    
    if(len(my_stack) == 0):
        print("YES")
        return "YES"
    print("NO")
    return "NO"
                
def peek_stack(stack):
    if stack:
        return stack[-1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     s = input()
    s = "{{[[(())]]}}"
    result = isBalanced(s)

        # fptr.write(result + '\n')

    # fptr.close()
