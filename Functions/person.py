
def get_age():
	age = int( input("Please enter age: "))
	return age


def get_name():
	name = input("Please enter name: ")
	return name
print ("Your name is " + get_name()+" and you are "+ str(get_age()) +" years old")
