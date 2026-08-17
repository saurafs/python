
list1=['aman','baba','chotu','lala','rishab']

#print(list1)

list1[1]='amit' #baba remove with amit

#print(list1)

#newlist1=list1

#print(newlist1) #copy value from list1

#newlist1[0]='sumit' #here changing value of newlist1

#print(list1) #but value of list1 got changed also

#TO PREVENT VALUE CHANGE IN LIST1 AFTER COPYING TO NEWLIST1 USE newlist1=list1[:]\
    
newlist1=list1[:]    
newlist1[0]='sumit'
print(list1)
print(newlist1)