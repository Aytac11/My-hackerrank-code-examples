#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    string=list(s.capitalize())
    arr=""
    i=0
    while i<len(string):
        if string[i]==' ' and  string[i+1]!=' ':
            string[i+1]=string[i+1].upper()
        arr+=string[i]
        i+=1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
