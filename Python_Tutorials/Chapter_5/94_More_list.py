# Generate list using range function.

# numbers = list(range(1,21))
# print(numbers)

# More about pop function.
# numbers = list(range(1,11))
# numbers.pop() 
# the pop function pop out the "10" value. that is highest value of the list.
# the number popped out by the pop function, is also return on print.
# print(numbers.pop()) # it returns 10.

# popped_items = numbers.pop()
# popped_items is the variable in which the popped number will be stored

# Index Method - it will tell the position of the element '1'.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(numbers.index(1))

# what if we have two same numbers in the list at different position.
# it will again print the initial value. until not mentioned.
# to mention -
# print(numbers.index(1, 3)) # index function will search after 0 position.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 8, 9, 1] # last 1 position was 10th so , now we search after 10, i.e. 11th
# print(numbers.index(1, 11)) # numbers.index(number, start, stop)
# print(numbers.index(1, 1, 14)

# pass list to a function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i) # we are appending negative values one by one in the negative variable.
    return negative

print(negative_list(numbers)) # input is numbers
