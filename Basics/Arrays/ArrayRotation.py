# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:42:32 2019

@author: Bharath
"""

def rotate(arr,d):
    n = len(arr)
    q = []
    for i in range(d,0,-1):
        temp = arr[0]
        for j in range(n-1):
            
            arr[j] = arr[j+1]
        arr[n-1] = temp
            
    return arr

a = [2,45,21,54,21,84,32,48,21,5,3,57,12]
rotate(a,2)