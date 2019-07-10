
#i= 10
#while(i<20):
#	i=i+2
#	print(i)

def evens():
	start = int(input("Enter range Start :" ))
	stop = int(input("Enter range Stop :" ))
	while(start < stop):
		if(start % 2 == 0):
			print(start)
		start+=1

evens()

