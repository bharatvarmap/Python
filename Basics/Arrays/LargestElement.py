# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:25:09 2019

@author: Bharath
"""

def largest(arr):
    x = 0
    for i in range(len(arr)):
        if arr[i] > x :
            x = arr[i]
    return x

a = [2,45,21,54,21,84,32,48,21,5,3,57,12]
print("The largest element in the array is {}" .format(largest(a)))