#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def max_n_argmax(vec):
    '''
    get the max value and max argument from a vector
    input:
    vec = vector
    output:
    int max_arg_delta_pd = best argument
    or
    0 if it is not feaseable
    '''
    max_value = max(vec)
    for i in range(len(vec)):
        if max_value == vec[i]:
            max_arg=i
    return max_value,max_arg

def truckTour(petrolpumps):
    '''
    optimize the gas in a circuit
    input:
    petrolpumps = 2D vector
    output:
    number ; max value from vector
    max_arg   = int ; max argment from a vector
    '''
    #0 is the petrol distance
    #1 is the distance to the next one
    lp = len(petrolpumps)
    delta_pd_array=[0 for _ in range(lp)]#array
    for wtstart in range(lp) :
        petrol_distance=0
        distance =0
        for i in range(lp):
            loc_i = wtstart+i
            #boudary conditions
            if(loc_i>=lp): 
                loc_i = loc_i-lp
            petrol_distance = petrol_distance + petrolpumps[loc_i][0]
            distance = distance + petrolpumps[loc_i][1]
            delta_pd = petrol_distance - distance
            delta_pd_array[wtstart] = delta_pd
            if(delta_pd < 0):
                delta_pd=0
                break
            #this solve the problem but not optimaly
            #elif(delta_pd>0):
            #return wtstart
    max_delta_pd,max_arg_delta_pd = max_n_argmax(delta_pd_array)
    if max_delta_pd>0:
        return max_arg_delta_pd
    else:
        print('it is not posible')
        return 0
    #'''    
    #answer = 573
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
