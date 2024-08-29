# fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 ...
# to print numbers in a line -

# for i in range (1,11):
    # print(i, end = " ") # this is the default code for writing numbers 

    # for example if we put \n in "". numbers will print in new line
    # print(i, end = "\n")

def fibb_ser(n): # n is parameter we want to print
    a = 0 # first number
    b = 1 # second number
    if n == 1:
        print(a) # 0
    elif n == 2:
        print(a, b) # it will print like - a b (2 numbers) # 1
    else: # now to print rest of the numbers
        print(a,b, end = " ")
        for i in range(n-2): # n-2 because we want to now print rest of the numbers
            c = a + b # 1 # 2
            a = b # 1 #1 
            b = c # 1 #3
            print(b , end = " ")

fibb_ser(20)