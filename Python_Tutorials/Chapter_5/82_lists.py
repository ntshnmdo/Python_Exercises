# List is a Data structure.
# It is an ordered collections of items.
# You can store anything in this list integer, numbers, strings, float numbers.

numbers = [1, 2, 3, 4]
print(numbers[1]) # accessing any number in the list can be done by [indexing]

words = ["word1", "word2", 'word3']
print(words[:2])

mixed = [1, 2, 3, "four", 'five', 6.0, 6.99, None] # None in python is simply nothing
print(mixed[-1])

# to replace any element in the list 

mixed[1] = 'two'
print(mixed)

# to replace more than 2 elements in the list

mixed[1:] = 'two'
print(mixed) 
# here the string will break and each letter will be assigned

# also
mixed[1:] = ['two', 'three', 'four']
print(mixed)