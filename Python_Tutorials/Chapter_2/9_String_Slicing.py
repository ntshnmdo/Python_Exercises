# Slicing/ selecting sub-sequences
lang = "Python" #lang is a variable and python is a string under it.
# we want to print letters py so syntax for it will be. print(variable[start argument:end argument+1])
# To print py . it will print [start argument, (end argument+1)-1]
print(lang[0:2])
# To print thon
print(lang[2:])
# Keeping argument blank, will print all the letters 
print(lang[:])
# Not starting the argument or not ending the argument, 
print(lang[:5])
print(lang[0:])
print(lang[3:])
print(lang[:4])
# We can also give -ve indexing for the letters (from backwards) (more Useful for end letters )
print(lang[-3:])
word = "Mississippi"
print(word[-3:])
