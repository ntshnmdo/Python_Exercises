# Strings 
# Collection of characters inside single quotes or double quotes. 
# Concatenate means to add strings
# We add strings by using + sign between strings

first_name = "Nitish" # 1st string
last_name = "Namdeo" # 2nd string
full_name = first_name+" "+last_name # To give gap between two letters, we've used "". 
# full_name is the new concatenate string of 1st and 2nd string.
print(full_name)

#To add number to a string. Use "". single number will not be read as str
# mark that string can be added to string only, number under "" make it a string or we can use str().
print(first_name + "3")
#or we can also use 'str(number)' 
print(first_name + str(5))

# but we can multiply a number without "" '' , without making it string
print(first_name * 3)