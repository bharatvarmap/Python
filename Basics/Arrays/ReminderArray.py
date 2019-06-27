# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:28:55 2019

@author: Bharath
"""

def remainder(arr,n):
    l = len(arr)
    temp = arr[0]
    for i in range(1,l):
        temp = temp * a[i]
    rem = temp % n
    return rem, temp

a = [2,45,21,54,21,84,32,48,21,5,3,57,12]
remainder(a,123)