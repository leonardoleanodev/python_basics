#!/bin/python3

import math
import os
import random
import re
import sys

def find_value(edges,s):
    '''
    inputs:
    edges = [[i,j,d],...]; i,j,d = int
    s = value to find in i and j
    output:
    result = list of integer indices where s was found
    '''
    result = []
    for i in range(len(edges)):
        if s == edges[i][0]:
            result.append(i)
        elif s == edges[i][1]:
            result.append(i)
    return result

def short_path(n,edges,start,stop):
    d_old = 10000000#large number
    d_new = 0
    walk_from = start
    walks = [start]
    distance=0
    walk_to=1
    for _ in range(n):
        for i in find_value(edges, walk_from):
            d_new = edges[i][2]
            if d_old > d_new:
                walk_to = i
                d_old = d_new
        distance = distance + d_old
        walks.append(walk_to)
        if walk_to== stop:
            return walks, distance
            break
    return walks, distance
        
# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    destiny = [i for i in range(n)]
    destiny.remove(s)
    shortest =[]
    for stops in destiny:
        _, d = short_path(n,edges,s,stops)
        shortest.append(d)
    return shortest

if __name__ == '__main__':
    fptr = open('input00.txt', 'w')

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

    
#from wickpedia https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
