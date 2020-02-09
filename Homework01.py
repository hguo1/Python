#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:34:15 2020

@author: heguo
"""
import math
#1. Creating Python lists. There is more than one way to do these! 
#To check out the available list methods in a Python console type you need a list object.
#For all of these you may not just type in the whole list. Find a way to generate them. 
#Your script for part 1 can just print these lists out after they are generated:


#(a) [1,2,3,...,19,20]
#create a empty list
list_1a = []
# This for loop append integer 1 through 20 into the empty list
for i in range(1,21) :
    list_1a.append(i)
    
print(list_1a)

#(b) [20,19,...,2,1]
#create a empty list
list_1b = []
# This for loop append the result of 21 subtract integer 1 through  21
for j in range(1,21) :
    list_1b.append(21-j)
    
print(list_1b)

#(c) [1,2,3,...,19,20,19,18,...,2,1]
##create a empty list, and copy the value of list_1a to list_1c
list_1c = list_1a.copy()
##add integer 19 through 1 to  list_1c
for k in range(1,21) :
    list_1c.append(list_1b[k])
    
print(list_1c)  

##For parts (d) and (e) try the syntax “N * [val1,val2]” and the del command.

#(d) [4,6,3, 4,6,3,...,4,6,3] where there are 10 occurrences of 4.
##create a list with 10 occurrences of 4
list_1d = 10*[4,6,3]
print(list_1d)

#(e) [4,6,3, 4,6,3,...,4,6,3,4] where there are 11 occurrences of 4, 10 occurrences of 6 and 10 occur- rences of 3.
##create a list with  11 occurrences of 4, 10 occurrences of 6 and 10 occur- rences of 3.
list_1e = 10*[4,6,3]
print(list_1d)

#2. Create a list of the values of:
## create a list x from 3 to 6 with 0.1 increament
list_x = []
for i in range (3,6):
    for j in range (1,11):
        list_x.append(3+i-3+j/10)
        
list_x.insert(0, 3)       
print(list_x) 

## compute the result of the e^x*cos(x)
getXlist = []
for i in range(31):
    getXlist.append(math.exp(list_x[i])*math.cos(list_x[i]))
print(getXlist)


#3. Create a list of the values of: [2,22 ,23 ,...,225 ]
from fractions import Fraction as frac
##create a empty list and add value into that list
list_3 = []
for i in range(2,26):
    list_3.append(math.pow(2,i)/i)
    
list_3.insert(0, 2)  
print(list_3) 

#4. Re-use your list from 1(a) as variable a. It has length n. Create these lists:

##(a) [a0 – an, a1 – an-1,...,an-a0]
###create a list and put the value of [a0 – an, a1 – an-1,...,an-a0] into the new list
list_4a = []
for num in range(20):
    list_4a.append(list_1a[num]-list_1a[19-num])
print(list_4a)

##(b) A Boolean list where even values of a are True and odd values are False: [False, True,...].

###create a empty list and store the wither or not is a even number
list_4b = [None] * 20
for i in range(20):
    if list_4a[i] % 2 == 0:
      list_4b[i]  = True
    else:
       list_4b[i]  = False  
#5. Write a Python script that will open the file lorem.txt. 
#This is a bit of the “lorem ipsum”, nonsense Latin that’s used as a placeholder in publishing and graphic design. 

#(a) The number of strings whose lengths are: between 1 and 4, between 4 and 7, and 8 or greater.
       
## write the fie into list
with open('lorem.txt','r') as f:
    all_lines = f.readlines()
    f.close()

##create three list to count number
num_14 = []
num_47 = []
num_8 = []


##For loop.  For each line in the file
for line in all_lines:
    ## split each line into words
    str_vals = line.split(" ")
   ## for each word in the line
    for one_str in str_vals:
        ##Count the number of letter in this word
        int_val = len(one_str) 
        if int_val>=1 and int_val<=4 :
            num_14.append(int_val)
        elif int_val>=4 and int_val<=7 :
            num_47.append(int_val)
        else:
            num_8.append(int_val)


#(b) The number of capitalized characters in the file.
import re 
##define a number to count the number of capitalized characters
num_upper  = 0   
## count the number of capitalized characters for each line and sum thoes up
for line in all_lines:  
    num_upper += len(re.findall(r'[A-Z]',line))








