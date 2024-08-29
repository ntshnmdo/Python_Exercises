name = "Nitish"
age = 26 #Dont put integer under brackets
print("Hello " + name + " Your age is " + str(age)) #Old and Ugly syntax

# therefore we use string formatting 
# For python 3
print("Hello {} Your age is {} ".format(name, age)) 

# For python 3.6
print(f"Hello {name} Your age is {age} ") #very simple but you should know all.

# we can also use maths operators for adding, subtracting, dividing, or multiplication.
# In python 3
print("Hello {} Your age is {}".format(name, age + 2)) 

# Also in python 3.6
print(f"Hello {name} Your age is {age + 2}")