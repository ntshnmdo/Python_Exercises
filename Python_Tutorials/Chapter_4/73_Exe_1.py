def greater(a, b):
    if a > b:
        return a
    else:
        return b
    
num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
bigger = greater(num1, num2) # bigger is a variable, in which we are calling function greater. # num1 and num2 are arguments whichever is greater will go to bigger named variable.
print(f"{bigger} is greater") 