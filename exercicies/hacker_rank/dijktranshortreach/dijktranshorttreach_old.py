#!/bin/python3

import math
import os
import random
import re
import sys

#begining of my code
########################

#looking for nodes
def look_for_nodes(edges):
    #get the list of edges
    nodes=[]
    for i in range(len(edges)):
        nodes.append(edges[i][0])
        nodes.append(edges[i][1])
    #clean
    cleaned_nodes = []
    for i in range(max(nodes)+1):
        for node in nodes:
            if i == node:
                cleaned_nodes.append(i)
                break
    return cleaned_nodes

def ditance_xy(egdes,s,destiny_nodes,y):
    

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    print(edges)
    #looking for nodes
    nodes = look_for_nodes(edges)
    #setting destinies
    destiny_nodes = nodes
    destiny_nodes.remove(s)
    #calculate the distances
    
    
    
    
    
    pass
 
#ending of my code
########################

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
