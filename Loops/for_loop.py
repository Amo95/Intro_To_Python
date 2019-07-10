for i in range(1,11):
	print(i)

for j in [1,2,3]:
	print(j)

#using the range
for j in range(1,4):
	print(j)


#using range to return the list [0,2,4,6,8,10,12,14,16,18]
for j in range(0,18):
	if(j % 2 == 0):
		print(j)
	j += 1
print(j)

for q in [1,2,3,4]:
	print("****")


def check():
	char = input("Enter any character: ")
	bool = True
	no_bool = False
	if char == 'a':
		print(bool)
	else:
		print(no_bool)

check()



def next():
        char = input("Enter any character: ")
        bool = True
        no_bool = False
        if char == 's' or char == 'm':
                print(bool)
        else:
                print(no_bool)

next()
