# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:26:08 2026

@author: Saurabh
"""

list1=['aman','baba','chotu','lala','rishab']


#list1.append(1,2,3)  list.append() takes exactly one argument
#list1.extend(1,2,3)  list.extend() takes exactly one argument
#list1.extend([1,2,3]) ['aman', 'baba', 'chotu', 'lala', 'rishab', 1, 2, 3]
#list1.extend(1) 'int' object is not iterable
#list1.extend([[1]]) ['aman', 'baba', 'chotu', 'lala', 'rishab', [1]]
#list1.insert(0,[1,2,3]) [[1, 2, 3], 'aman', 'baba', 'chotu', 'lala', 'rishab']
#list1.remove('aman') 
#list1.pop(3)
#list1.clear()
#list1.count('aman')
#list1.reverse()
newlist=list1.copy()
print(list1) 