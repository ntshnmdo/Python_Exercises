# common methods to delete data from the list
fruits = ['apple', 'mango', 'banana', 'pear', 'kiwi']
fruits.pop()
print(fruits)
# the pop function by default delete last argument of the list, if not mentioned
fruits.pop(2)
print(fruits)

# del operator
# del fruits[1]

# remove method - when we dont know the position of an argument

fruits.remove('pear') # Remove function - remove 1st word that comes in the list 
print(fruits)

# To add data to the list - append, extend, insert
# To delete data from the list - remove , del, pop