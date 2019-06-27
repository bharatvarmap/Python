# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:45:27 2019

@author: Bharath
"""
# Calculate the order of number i.e; the number of digits in the number
def order(x): 
    n = 0
    while (x!=0): 
        n = n+1
        x = x//10
#        print(n)
    return n 

#Calculate power
def power(x,y):
    if y==0:
        return 1
    return x**y

def armstrong(x):
    n = order(x)
    sum1 = 0
    temp = x
    while(temp != 0):
        p = temp % 10
        sum1 = sum1 + power(p,n)
        temp = temp // 10
        
    if sum1==x:
        print("Yes, {} is an Armstrong number." .format(x))
    else:
        print("No, {} is not an Armstrong number." .format(x))
    
#Example
x = int(input("Enter number: "))
armstrong(x)