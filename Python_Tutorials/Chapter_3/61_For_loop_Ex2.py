# sum of digits of number with more than 2 digits

total = 0
number = input("enter a number : ") # not changing it into integer because we have to work with indexing
for i in range(0, len(number)):
    total += int(number[i])
print(total)
