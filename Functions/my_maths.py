
def calculate():
	fnum = float(input("Enter first number : "))
	opt = input("Enter operator (i.e add/subtract/multiply/divide) : ")
	snum = float(input("Enter second number : "))

	if opt =='add':
		print(float(fnum) + float(snum))

	if opt =='subtract':
                print(float(fnum) - float(snum))

	if opt =='multiply':
                print(float(fnum) * float(snum))

	if opt =='divide':
                print(float(fnum) /float(snum))
calculate()

