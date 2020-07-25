#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np

def max_n_argmax(vec):
#"""
#get the max value and max argument from a vector
#input:
#vec = vector
#output:
#max_value = number ; max value from vector
#max_arg   = int ; max argment from a vector
#"""
    max_value = max(vec)
    for i in range(len(vec)):
        if max_value == vec[i]:
            max_arg=i
    return max_value,max_arg

# Complete the stockmax function below.
def stockmax(prices):
#"""
#max profit from a forcasted time series
#input:
#prices = time serie
#output:
#profit = maximum profit
#"""
    # get the max value and max argument
    max_price, max_arg_price=max_n_argmax(prices)
    #profit calculation
    profit=0
    for i in range(max_arg_price):
        profit = profit+max_price-prices[i]
    #looping calculation
    while (1):
        #storing the old argmax
        old_max_arg_price =max_arg_price
        #foward cutting the price vector
        prices = prices[old_max_arg_price+1:]
        if len(prices)>1:
            max_price, max_arg_price=max_n_argmax(prices)
            for i in range(max_arg_price):
                profit = profit+max_price-prices[i]
        else:
            break
    
    return profit
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()

