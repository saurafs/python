# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:48:06 2026

@author: Saurabh
"""

my_tuple =(1,2,3,4,5)

#my_tuple[1]=8  'tuple' object does not support item assignment

print(my_tuple.count(3)) #1
print(my_tuple.index(4)) #3
print(my_tuple[3:4])    #slicing from index 3 to 4 --> (4,)