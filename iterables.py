# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:23:15 2026

@author: Saurabh
"""

user = {'name' : 'saurabh', 'age' : 24, 'class' : 'mca'}

for item in user.items():   #('name', 'saurabh')
    print(item)          #('age', 24)
                            #('class', 'mca')
    
for item in user.keys():    #name age class
    print(item)
    
for item in user.values():  #saurabh 24 mca
    print(item)
    
for key, value in user.items():
    print(key, '->', value)       # name -> saurabh
                                  # age -> 24
                                  # class -> mca