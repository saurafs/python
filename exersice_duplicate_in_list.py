# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:54:24 2026

@author: Saurabh
"""

li =['a', 'b', 'k', 'l', 'l', 'k', 'p', 'n', '9', 'u', 'a']

new_li=[]

for item in li:
    if li.count(item)>1:
        if item not in new_li:
            new_li.append(item)
        
        
print(new_li)