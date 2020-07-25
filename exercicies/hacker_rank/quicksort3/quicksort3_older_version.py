#!/bin/python3

import math
import os
import random
import re
import sys

def quicksort3(t,n):
    pivot = n[-1]
    i_low = -1
    i_upper = -1
    for i in range(t):
        if n[i] > pivot:
            i_low=i
        elif n[i] < pivot and i_low !=-1:
            i_upper = i
        elif i_low !=-1 and i_upper !=-1:
            n_swap_low = n[i_low]
            n_swap_upper = n[i_upper]
            n[i_low] = n_swap_upper
            n[i_upper] = n_swap_low
        
    
    sorted_vec = n
    return sorted_vec
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    n_vec = input().split()
    n=[]
    for t_itr in range(t):
        n.append(int(n_vec[t_itr]))
    
    
    result = quicksort3(t,n)
    
    fptr.write(str(result) + '\n')

    fptr.close()
