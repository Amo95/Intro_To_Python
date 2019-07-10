import math
import time
#printing the radian of 32 degrees
degree = 32
print(math.radians(degree))

#taking input to calculate for area and volume of a sphere

rad =float(input("Enter radius number"))

vol = (float(4)/float(3)* math.pi * (rad*rad*rad))

sa = (4 * math.pi * (rad *rad))

print ("Volume of a sphere is : "+ str(vol))
print ("Surface area of a sphere is : " +str(sa))

#Printing time in a readable format
print(time.ctime())


#Spliting words
words = "I love to code in python"
print(words.split())

#joining two words
fname = "Seth"
lname = "Gregory"
print (fname + " " + lname)

