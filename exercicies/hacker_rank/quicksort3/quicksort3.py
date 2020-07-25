#!/bin/python3

import math
import os
import random
import re
import sys

def partition(A,lo,hi):
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        if A[j] < pivot:
            Aiswap = A[i]
            Ajswap = A[j]
            A[i] = Ajswap
            A[j] = Aiswap
            i=i+1
    Aiswap = A[i]
    Ahiswap = A[hi]
    A[i] = Ahiswap
    A[hi] = Aiswap
    fptr.write(str(A) + '\n')
    return i

def quicksort3(A,lo,hi):
    if lo < hi:
        p = partition(A, lo, hi)
        if lo < hi:
            Alo = A[lo:p]    
            Alo.sort()
            Ahi = A[p:hi+1]
            A = Alo+Ahi
            fptr.write(str(A) + '\n')
            Ahi.sort()
            A = Alo+Ahi
            fptr.write(str(A) + '\n')
    return A
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    n_vec = input().split()
    n=[]
    for t_itr in range(t):
        n.append(int(n_vec[t_itr]))
    
    
    result = quicksort3(n,0,t-1)
    
    fptr.write(str(result) + '\n')

    fptr.close()
