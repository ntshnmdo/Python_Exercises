def factorial(n):
    if (n == 0 or n == 1):
        return 1 # base condition
    else:
        return n * factorial(n-1) # function calling itself

n = int(input("enter a number: "))
print(f"The factorial of the number is {factorial(n)}")