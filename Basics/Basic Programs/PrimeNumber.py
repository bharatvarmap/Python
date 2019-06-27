# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:46:47 2019

@author: Bharath
"""

def prime(n):
    if n <= 1:
        print("Not a prime")
    
    for i in range(2,n):
        if n % 2== 0:
            return False
    return True