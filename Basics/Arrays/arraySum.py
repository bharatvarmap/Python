# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:01:27 2019

@author: Bharath
"""

def arrSum(arr):
    sum1 = 0
    for i in range(0,len(arr)):
        sum1 += arr[i]
    return sum1

a = [5,65,7,32,78,12,9]
arrSum(a)
        