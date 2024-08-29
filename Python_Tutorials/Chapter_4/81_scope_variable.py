# def func():
#     x = 7 #local variable we cannot use it outside this block
#     return x

# def func2():
#     print(x)

# func2() 
# it will give error because x = 7 was a local variable and calling it in other func will give error.

# def func():
#     x = 7
#     return x
# print(x) 

# it is giving error because x is local variable but we are printing it outside block which will give error.
# instead we can print func , putside block but not variable.
# def func(): 
#     x = 7
#     return x

# print(func())

# we can change value of global variable in local variable .
x = 5 # global variable
def func(): 
    global x
    x = 7
    return x
print(x) # it is printing global value of x = 5 
print(func()) # after we call func x = 7
print(x) # it will change x value to 7