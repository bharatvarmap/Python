# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:37:23 2019

@author: Bharath
"""

def missingNumber(arr,n):
    l = len(arr)
    for i in range(1,l+1):
        if i != arr[i-1]:
            return i
        
ar = [1,2,3,4,5,6,8,9,10]


print("The missing number in the array is {}." .format(missingNumber(ar,10)))
