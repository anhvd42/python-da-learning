# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 16:51:48 2025

@author: vandu
"""

x = 1 
print(type(x))

x = 1.0
print(type(x))

x = 1+2j
print(type(x))

x = True
print(type(x))

x = 'abc'
print(type(x))

x = None
print(type(x))

e = 2.72
pi = '3.14'
text = 'Hello world!'

print("Type data variable e:", type(e),
      ", Type data variable text: ",type(text),
      ", Type data variable pi: ",type(pi))

a = 5
b = 2.0
c =a / b
print(c)
print("Kieu du lieu cua a: ", type(a))
print("Kieu du lieu cua b: ", type(b))
print("Kieu du lieu cua c: ", type(c))

n = 100
m = "200"
print(n+int(m))
print(str(n)+m)