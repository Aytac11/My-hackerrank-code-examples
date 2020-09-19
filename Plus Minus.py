#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    a=0; c=0; d=0
    for i in arr:
        if i>0:
            a+=1
        elif i<0:
            d+=1
        else:
            c+=1
    print(a/len(arr))
    print(d/len(arr))
    print(c/len(arr))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
