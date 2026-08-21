# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:09:54 2026

@author: Saurabh
"""

my_set= {1,2,3,3,3,3,4,4,5}
my_list=[1,2,3,4,5,6,6,6,6,6]
print(my_list)      #[1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
print(my_set)       #{1, 2, 3, 4, 5}
print(set(my_list)) #{1, 2, 3, 4, 5, 6}

print(5 in my_set)   #true
print(22 in my_list) #false

my_set.add(22)
print(my_set) #{1, 2, 3, 4, 5, 22}

new_set= my_set.copy()
my_set.clear()
print(my_set)  #set()
print(new_set) #{1, 2, 3, 4, 5, 22}

