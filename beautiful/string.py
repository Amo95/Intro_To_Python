from functools import reduce

words = ["hello", "world"]

def join_strings(string):
        return reduce(lambda x, y: x +' '+ y, string, ' ')

print(join_strings(words))


#print (reduce(join_strings, words, x))
