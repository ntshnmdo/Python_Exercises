def square_list(l): # l is the input for list square_list
    square = []
    for i in l:
        square.append(i**2)  # appending the square of the elements of list l in the square list
    return square

# list, str dont use these as in input

numbers = list(range(1,11))
print(square_list(numbers))