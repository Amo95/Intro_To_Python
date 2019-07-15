from functools import reduce

numbers = [1,56,234,87,4,76,24,69,90,135]

def join_strings(x,y):
	return x+y
print(reduce(join_strings, numbers, 5))






#total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
