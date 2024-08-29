# user input
# input function
# To take input from user we use input function,
# Input func always takes input from user in str func.

name = input("Type Your Name ") # name is a string.
print("Hello " + name) # here we concatenate Input func with Hello. and Print 

#Input func is always in Strings itself ("" '') and therefore it will even take number as a string.

# For Example

age = input("What is your Age ? ")
print("Your Age is " + age)

# here age is a number but since age is used as an input func therefore it is taken as str.

# if we want to input number we use int(input("")), int is integer