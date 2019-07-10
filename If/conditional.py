i = 8
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")


#age
def tell_age():
	age = int(input("Enter your age: "))
	if (age <= 16):
		print("You are young")
	elif (age >= 17 and age <= 45):
		print("You are an adult")
	else:
		print("You are old")
tell_age()

#birth
import datetime

def birth():
	year = int(input("Enter year of birth: "))
	cyear = datetime.date.today().year
	print(cyear - year)
birth()

#leap year
def leap_year():
	year = int(input("Enter year here: "))
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		print ("It is a leap year")
   	else:

        	print ("It is a not a leap year")
leap_year()
