# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:27:22 2019

@author: mkiad
"""

list1=[1,2,3,4]
list2=[5,1,4,4,5]
l1size=len(list1)
l2size=len(list2)
maxsize=max(l1size, l2size)
#print (maxsize)
for x in range(maxsize-1):
    #print (x)
    try:
        list1[x]
    except:
        pass
    try:
        list2[x]
    except:
        pass
    if list1[x]==list2[x]:
        templst= list1[x:]
        #print (list1[x+1:])
        #print(templst)
        list1[x]=["w"]
        list1=list1[0:x]+list1[x]+templst
        maxsize=maxsize+1
print (list1)
print (list2)