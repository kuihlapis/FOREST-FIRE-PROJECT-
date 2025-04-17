# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 10:42:09 2025

@author: alann
"""


import numpy as np

#print(random.random())
x = 10
time = 1

#  r is a black variable used to control how many rounds the while loop 
# does
r = 0

# w is in place of x-1
w = x-1

#This creates an array in the form of a x by x matrix with random 
#numbers between 0 and 1
L = np.random.rand(x,x)
l = len(L)

# p sets the probability of there being a tree
p = 0.5


# this loop goes through the array and assigns a 1 if the random value
# is less than p and a 0 if the value is greater than p
for i in range(l):
    for j in range(l):
        if L[i][j] > p:
            L[i][j] = 0 # A 0 represents no tree
        else:
            L[i][j] = 1 # a 1 represents a treee
            
print(L)
print()

# H is half the area of the matrix
h = int(x/2)

# Set the left half of the area on fire
for i in range(x):
    for j in range(h):
        if L[i][j] == 1:
            L[i][j] = 2
print(L)
print()

# This while loop allows for the fire to also spread backwards and upwards,
# against the progression of the for loops
while r < x:
    for j in range(x): 
        for i in range(x):
            
            # Identify a tree on fire
            if L[i][j] == 2:
                
                # checks if the tree is not at the borders of the grid 
                if i < x-1 and j< x-1 and j !=0:
                    if L[i][j-1] == 1: # if it isnt it sets near by trees
                        L[i][j-1] = 2  # on fire 
                        time = time +1 # it also adds 1 to the time
                    if L[i][j+1] == 1:
                        L[i][j+1] = 2
                        time = time +1
                    if L[i-1][j] == 1:
                        L[i-1][j] = 2
                        time = time +1
                    if L[i+1][j] == 1:
                        L[i+1][j] = 2
                        time = time +1
                        
                if i == w:   # checks if a tree is at y border
                    if L[w][j] == 2: # sets burning tree to smoldering
                        L[w][j] = 3
                        if j == x-1: # if tree is at corner it does 
                            L[w][w]= 3 # not spread
                            time = time +1
                        else: # if it is not at corner 
                            if L[w][j-1] == 1: #it spreads up or down
                                L[w][j-1] = 2
                                time = time +1
                            if L[w][j+1] == 1:
                                L[w][j+1] = 2
                                time = time +1
                        
                    
                
                if j == w: # checks if tree is at x border
                    if L[i][w] == 2:# repeats above process
                        L[i][w] = 3
                        if i == w:
                            L[w][w]= 3
                            time = time +1
                        else:
                            if L[i-1][w] == 1:
                                L[i-1][w] = 2
                                time = time +1
                            if L[i+1][w] == 1:
                                L[i+1][w] = 2
                                time = time +1
                        
                
                L[i][j] = 3 # sets tree that caused the spread 
                            #smoldering
            
            if L[i][j] == 3: #if tree is smoldering it goes out
                L[i][j] =0
    
    
    r = r+1 # adds 1 to round 
                
                
        
        
     
    
                
                     
                
                    
                    
                    
                        
            
            
            
            
print(L)
print(time)  #This loop is infinte