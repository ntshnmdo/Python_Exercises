# replace_method
# string = "she is beautiful and she is a good dancer"
# print(string.replace(" ", "_"))

string = "is she is beautiful and she is a good dancer"
print(string.replace("is", "was", 1)) 
print(string) # strings are not immutable
# number 1 tells that only one 'is' replaced with 'was'.

# find_method - is used to get the position of word or character in the string.

# print(string.find("is", 3)) 
#Number 3 for example here tells that find 'is' after 3rd place. 
# string = "she is beautiful and she is a good dancer"

# Suppose we donot know the position of the 1st 'is'. Then we can define a variable to find position of 'is'.
# is_pos1 = string.find("is")
# is_pos2 = print(string.find("is", is_pos1+1)) #We did +1 because is_pos1 was already in 4th position. therefore +1 took it to 5th position.