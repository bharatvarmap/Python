# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:39:02 2019

@author: Bharath
"""

def subarraySum(s,arr):
    l = len(arr)
    for i in range(l):
        print("i = {}" .format(i))
        sum1 = 0
        for j in range(i+1):
            sum1 += arr[j]
            print(sum1)
            
        if sum1==s:
            print(arr[:i+1])
            
            
a = [1,2,3,4,5,6]
s1 = 10
subarraySum(s1,a)