# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:57:01 2019

@author: Bharath
"""

def maxSum(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n):
        
        for j in range(i,n):
            sum1 = 0
            for k in range(i,j+1):
                sum1 += arr[k]
               
            if sum1 >= temp:
                temp = sum1
                q = arr[i:k+1]
    return temp,q    
            
a = [1,2,3]
maxSum(a)