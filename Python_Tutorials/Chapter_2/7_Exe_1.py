# num1 = input("Enter first Num : ")
# num2 = input("Enter second Num : ")
# num3 = input("Enter third Num : ")
# print(f"average of three numbers : {((  int(num1) + int(num2) + int(num3))/3)}") #{} is called placeholder

num1, num2, num3 = input("enter three numbers comma separated : ").split(",")
print(f"average of three numbers : {((int(num1) + int(num2) + int(num3))/3)}")

