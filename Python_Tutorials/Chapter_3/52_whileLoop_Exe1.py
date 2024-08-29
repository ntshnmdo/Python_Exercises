# Exercise 1 for while loop
# Sum of n natural numbers, input from user a natural number.

n = int(input("enter a natural number : "))
total = 0
i = 1
while i<=n:
    total += i
    i += 1
print(total)