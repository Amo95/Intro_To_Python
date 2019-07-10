#!/usr/bin/python
import time
#import datetime

uname = input("Please enter your name here: ")
print ("Hello",uname,", your current time is: ", time.asctime()) 
#we can also use time.ctime/time.asctime/time.asctime(time.localtime(time.time())) for current time
