marks = int(input("enter your marks: "))

if marks<=100 and marks>=90:
    grade = "ex"

elif marks<=89 and marks>=80:
    grade = "a"
elif marks<=79 and marks>=70:
    grade = "b"
elif marks<=69 and marks>=60:
    grade = "c"
elif marks<=59 and marks>=50:
    grade = "d"
else:
    grade = "f"

print("your grade is:",grade)
