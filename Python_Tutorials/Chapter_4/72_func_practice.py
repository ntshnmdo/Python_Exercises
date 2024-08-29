### function practice 

#1) Defining a character

# def last_char(name):
#     return name[-1]

# print(last_char("Nitish"))

#2) Odd_Even

# def odd_even(num):
#     if (num%2 == 0):   # % is to get remainder of a number by 2(here) if number is even then rem is 0  # For odd number num%2 !=0  (!=0 is not equal to zero)      
#         return "even"
#     else:
#         return "odd"
# print(odd_even(7))

#3) without using else
# def odd_even(num):
#     if (num%2==0):
#         return "even"
#     return "odd" # so if number is not even then it will return "odd" which is outside the block.
# print(odd_even(8))

#4) Using boolean function (True, False)
# def is_even(num):
#     if num%2==0:
#         return True
#     return False
# print(is_even(8))

#5) Directly using return 

# def is_even(num): # num is called parameter, 
#     return num%2 == 0
# print(is_even(7)) # and input number is argument.

#6) Without defining parameter we can also return directly

# def season():
#     return "winter"
# print(season())