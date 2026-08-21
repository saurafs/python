# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:28:43 2026

@author: Saurabh
"""

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8}

print(my_set.difference(your_set))    #{1,2,3} only my_set
print(your_set.difference(my_set))    #{8,6,7} only your_set
print(my_set.union(your_set))         #{1, 2, 3, 4, 5, 6, 7, 8}

#my_set.discard(5)
#print(my_set)                        #{1, 2, 3, 4}

#my_set.difference_update(your_set)
#print(my_set)                        #{1,2,3} unique part or uncommon 
#your_set.difference_update(my_set)
#print(your_set)                      #{6, 7, 8}
union={1,2,3,4,5,6,7,8,9,10}
print(union)
print(my_set.intersection(your_set))  #only common {4,5}
print(my_set.issubset(your_set))      #false
print(your_set.issubset(union))       #true
print(union.issuperset(my_set))       #true
print(my_set.isdisjoint(your_set))    #false
print(my_set | your_set)              #union