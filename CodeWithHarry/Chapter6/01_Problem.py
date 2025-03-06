a1 = int(input("enter 1st number: "))
a2 = int(input("enter 2nd number: "))
a3 = int(input("enter 3rd number: "))
a4 = int(input("enter 4th number: "))

if (a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1: ", a1)

elif (a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2: ", a2)

elif (a3>a2 and a3>a1 and a3>a4):
    print("greatest number is a3: ", a3)

else:
    print("greatest number is a4: ", a4)