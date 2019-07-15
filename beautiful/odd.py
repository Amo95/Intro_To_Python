numbers = [1,56,234,87,4,76,24,69,90,135]
def its_even(a):
        return (a%2 != 0)
result= list(map(its_even,numbers))
print(result)
