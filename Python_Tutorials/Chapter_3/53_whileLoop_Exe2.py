# Exercise in which we have to 
# 1) input the number with more than two digits 
# 2) add those 2 digits.

number = input("enter a number with more than two digits : ")
#1256
total = 0 # varaible total starting with 0

i = 0 

while i < len(number):
    total += int(number[i])
    i += 1
print(total)