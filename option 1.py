# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:08:10 2025

@author: alex
"""

# import nessecary self defined functions from other scripts

import fire_functions as ff

# Set values for probability and grid size 
p = 0.5
x = 20
# Create blank array for values of burn
d = []

# make a loop to run the burn function 100 times
for k in range(100):
    prob =  p
    L = ff.ran_grid(x,prob)
    a = ff.burn(L,x)
    d.append(a)
    
# Get the average burn time from all burn times in array
av= sum(d)/len(d)

# print tha average value
print(av)
    
