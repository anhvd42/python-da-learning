# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 21:31:12 2025

@author: vandu
"""
print("Vi du ve so sanh")
x = int(input("x: "))
y = int(input("y: "))

print("{0} < {1} là {2} ".format(x, y, x<y ))
print("{0} > {1} là {2} ".format(x, y, x>y ))
print("{0} == {1} là {2} ".format(x, y, x==y ))
print("{0} != {1} là {2} ".format(x, y, x!=y ))
print("{0} <= {1} là {2} ".format(x, y, x<=y ))
print("{0} >= {1} là {2} ".format(x, y, x>=y ))

print("Vi du ve logic: ")
z = int(input("z: "))

print((x<y) and (y<z))
print((x<y) or (y<z))
print(not (x>z))