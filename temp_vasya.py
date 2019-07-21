#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:08:33 2019

@author: irinasm
"""


#def arr_to_str(array):
    #perevesti massiv v string
    #myString = '_'.join(array)
            
#array = [100, 200, 300] 
#print (array)
#array2 = arr_to_str(array)
#print (array2)

myList = ['str1', 'str2', 'str3']
myString = ', '.join(myList) # '' - разделитель между элементами списка соответственно
print (myString)

#lines_sibling = "aaa"
#b = "bb"
#print (my_person.sibling)
#for each in my_person.sibling:
#lines_sibling.join(b)
#print ("lines_sibling :", lines_sibling)

my_person = [1, 2, 3, 4, 5]
print (my_person)
for i in my_person:
    lines_sibling = my_person[i-1]
    print (lines_sibling)
 