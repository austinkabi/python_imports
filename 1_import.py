'''a program to find area of a cylinder'''
from math import pi
print("enter the radius")
r=float(input())
print("enter the height")
h=float(input())
SA=(2*pi*r*h)+2*pi*r*r
print("the radius of a cylinder is {} and the height is {} hence area is {}".format(r,h,SA))
