# print count of each letter of the word
# Example 
# Name = Nitish Namdeo
# N = 2
# i = 2
# t = 1
# s = 1
# h = 1
# a = 1
# m = 1
# d = 1
# e = 1
# o = 1

name = input("enter your name : ")
temp_var = "" # We are using temp variable to avoid counting letters more than one. for ex i (it is type of a hash map)
i = 0
while i < len(name): 
    if name[i] not in temp_var: # this will add letter to temp_var if the letter is not present in it.
        temp_var += name[i] 
        print(f"{name[i]} : {name.count(name[i])}") # using count function 
    i += 1
