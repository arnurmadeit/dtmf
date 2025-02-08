# Write a Python program to convert degree to radian.

import math

def DtoR():
    d = int(input("Enter the degree number: "))
    r = d * math.pi / 180
    return r

print(DtoR())
