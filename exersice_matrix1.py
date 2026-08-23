# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:40:50 2026

@author: Saurabh
"""

picture = [[0,0,0,1,0,0,0],
           [0,0,1,1,1,0,0],
           [0,1,1,1,1,1,0],
           [1,1,1,1,1,1,1],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0]]


for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    
    
 #OUTPUT
 #    *   
 #   ***  
 #  ***** 
 # *******
 #    *   
 #    *  