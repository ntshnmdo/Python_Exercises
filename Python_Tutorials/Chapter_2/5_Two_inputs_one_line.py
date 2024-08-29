# we have used two variables in one line 
# using .split(), tells that name and age are separated by space or comma under bracket of split func.
# we can also use any other character to show gap between name and age.like , comma

# name, age = input("Enter your name and age ").split() 
# print(name)
# print(age)

name, age = input("Enter your name, age :").split(",")
print("Hello " + name)
print("Your age is " + age)

