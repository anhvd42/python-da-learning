# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 20:15:49 2025

@author: vandu
"""

import math

x = float(input("x: "))
print("PI = ", math.pi)
print("|x| = ", math.fabs(x))
print("sqrt(x) = ",math.sqrt(x))
print("ceil(x) = ",math.ceil(x))
print("floor(x) = ",math.floor(x))



x = input ("Nhập vào số nguyên: ")
x = int(x)
kq = "Chẵn" if (x%2==0) else"Lẻ"
print (x, "là số",kq)