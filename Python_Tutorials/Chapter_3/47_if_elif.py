# we use if elif for multiple if commands.

# show ticket pricing 
# age(yrs)     price 
# 1-3          free
# 4-10         150
# 11-60        250
# 60 above     200  

age = int(input(" enter your age : "))

if age==0 or age < 0:
    print("you are not eligible")
elif 0<age<=3:
    print("Ticket price : Free ")
elif 4<age<=10:
    print("ticket price : 150rs")
elif 11<age<=60:
    print("ticket price : 250rs")
elif age>60:
    print("ticket price : 200rs")
# else:
#     print("ticket price : 200rs")