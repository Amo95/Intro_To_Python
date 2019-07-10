#!/usr/bin/python
import math

pi = math.pi
radius = float(input("Please enter the value for radius: "))
SA = (4 * pi) * radius**2 #SA for Surface area
V = (4.0/3) * pi * radius**3 #V for volume

print ("The Surface Area of a Sphere is: ", SA) 
print ("The Volume of a Sphere is: ", V)
