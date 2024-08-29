# count
# sort alphabetically
# sorted function
# clear list(empty list)
# copy 
# reverse
fruits = ['apple', 'orange', 'kiwi', 'pear', 'banana', 'mango', 'apple', 'guava', 'papaya', 'watermelon']

# Count - it counts no of argument in the list.
# print(fruits.count('guava'))

# sort - it will sort the arguments in alphabetical order. This sort method will do sorting in the original list. it will change original list.
# fruits.sort()
# print(fruits)

# numbers = [1,5,3,6,2,9]
# numbers.sort()
# print(numbers) 

# sorted function - this function will also sort but will not change the original list.

numbers = [6,4,8,2,9,1,0]
# print(sorted(numbers))

# clear method
# numbers.clear()
# fruits.clear()
# print(numbers)
# print(fruits)

# copy list
numbers_copy = numbers.copy()
numbers_copy.sort()
# print(numbers_copy)

# reverse function
numbers_copy.reverse()
print(numbers_copy)

