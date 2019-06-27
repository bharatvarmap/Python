# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:27:27 2019

@author: Bharath
"""

def isMonotonic(arr):
    n = len(arr)
    return (all(a[i] >= a[i+1] for i in range(n-1))
            or all(a[i] <= a[i+1] for i in range(n-1)))

a = [2,45,21,54,21,84,32,48,21,5,3,57,12]        
isMonotonic(a)