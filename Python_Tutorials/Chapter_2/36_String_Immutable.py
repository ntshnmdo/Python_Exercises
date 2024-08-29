# Strings are Immutable meaning that if the string is defined then we cannot change the letter/character of the string
string = "string"
# print(string[1], "T") # output will not give T, Thats why strings are immutable.
print(string.replace('t', 'T')) # This print has created new string where it replaces t with T. That means original string has not changed.

# see proof

print(string)

