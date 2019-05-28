# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:37:28 2019

@author: Bharath
"""

def selectionSort(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        maxpos = 0
        for q in range(1,i+1):
            if alist[q] > alist[maxpos]:
                maxpos = q
                
        temp = alist[i]
        alist[i] = alist[maxpos]
        alist[maxpos] = temp
        
    return alist