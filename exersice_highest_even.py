# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:56:57 2026

@author: Saurabh
"""

li =[2,10,4,623,9,21,92,83] 

def highest_even (*args):
    even=[]
    for item in args:
        if item % 2 == 0:
            even.append(item)
    return max(even)

print(highest_even(2,10,4,623,9,21,92,83))


# numbers = [1, 3, 5, 8, 6, 10, 7]
# highest_even = max([x for x in numbers if x % 2 == 0])
# print(highest_even)  # Output: 10   