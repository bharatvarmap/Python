# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:20:59 2019

@author: Bharath
"""

def compound_interest(p,t,r):
    CI = p*(1+(r/100))**t
    print("The compound interest for a loan of ${} for a period of {} years at a rate of {}% per annum is ${}"
          .format(p,t,r,CI))
    
P = int(input("Enter principal amount: "))
R = float(input("Enter R.O.I: "))
T = int(input("Enter duration of loan(in years): "))

compound_interest(P,T,R)
