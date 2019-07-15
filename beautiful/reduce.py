from functools import reduce

numbers = [-1,0,1,2]

def add(x,y):
	return x + y;
print(reduce(add, numbers, 5))
