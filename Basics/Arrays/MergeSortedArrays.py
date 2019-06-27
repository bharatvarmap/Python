# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:04:49 2019

@author: Bharath
"""

def mergeArray(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i, j =0,0
    res = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
#            print("i: {}".format(i), res)
            
        elif arr2[j] < arr1[i]:
            res.append(arr2[j])
            j += 1
#            print("j: {}".format(j), res)
            
        elif arr1[i] == arr2[j]:
            res.append(arr1[i])
            res.append(arr2[j])
            i += 1
            j += 1
#            print(i,j)
#            print(res)
           
    return res + arr1[i:] + arr2[j:]

a = [1,3,5,7,9,11]
c = [0,2,4,6,7,8,10,12]
print("The merged array is {}" .format(mergeArray(a,c)))