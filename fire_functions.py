# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 13:49:22 2025

@author: alex
"""
#imports numpy as np

import numpy as np

# define a function that creates a random grid based on a given probability
def ran_grid(x,p):
    """
    This function creates a x by x grid using arrays, thenrandomly assigns
    a value between 0 and 1 to it. If the random value is less than p
    it assigns a 1 to it if it is greater it assigns a 0

    Parameters
    ----------
    x : int
        Sets the length and width of the array.
        
    p : float
        Sets probability 

    Returns
    -------
    Grid L.

    """
    #This creates an array in the form of a x by x matrix with random 
    #numbers between 0 and 1
    L = np.random.rand(x,x)
    
    # this loop goes through the array and assigns a 1 if the random value
    # is less than p and a 0 if the value is greater than p
    for i in range(x):
        for j in range(x):
            if L[i][j] > p:
                L[i][j] = 0 # A 0 represents no tree
            else:
                L[i][j] = 1 # a 1 represents a tree
                
    return L



# define fire burning program
def Burn(L,x):
    """
    This function takes a grid of 1s and 0s and sets 'fire' to them
    this fire works by spreading from an on fire tree, represented by 2,
    to a not burning tree 1. It then puts out any burning trees. The 
    function tracks time saying it takes 1 unit of time for fire to 
    spread from tree to tree.

    Parameters
    ----------
    L : array
        grid that will be burnt containing 1 and 0.
    x : int
        length of grid.

    Returns
    -------
    time of burning.

    """
    time = 1
    
    #  r is a black variable used to control how many rounds the while loop 
    # does
    r = 0

    # w is in place of x-1
    w = x-1
    
    # H is half the area of the matrix
    h = int(x/2)

    # Set the left half of the area on fire
    for i in range(x):
        for j in range(h):
            if L[i][j] == 1:
                L[i][j] = 2
                
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
        
    return time, L

