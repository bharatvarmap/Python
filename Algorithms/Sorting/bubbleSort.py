# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:13:21 2019

@author: Bharath
"""

def bubbleSort(alist):
    n = len(alist)
    for num in range(n-1,0,-1):
        for i in range(num):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
    return alist
