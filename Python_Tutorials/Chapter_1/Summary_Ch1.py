
#print function
print("hello")
print('hello')
print('hello "hello" ')
print("hello 'hello' ")

#escape sequence
print("hello \"hello\" ")
print("hello \"hello\' ")
print("line A \n line B")
print("line A \t line B")
print("this is backslash \\")
print("this is double backslash \\\\")

#escape sequence as normal text
print("line A \\n line B")
print(r"line A \n line B") # r is a raw string which makes any text under "" as normal text.

#python as calculator
print(2+3)
'''
    () highest
    **  # Exponent  #right to left
    *,/,//,%   #left to right

    *,+,-   #left to right
'''
print(4/2) #float division - includes decimal 
print(4//2) #floor division - doesnt include decimal(integer division)
print((2+3)*4/2)

#variables
name="harshit"
print(name)
name=123 # number doesnt require to be written in ""
print(name)

#naming rules for variable
xyz="harshit"
xyz123="harshit"
_xyz="harshit"
Xyz="harshit"

#convention for variable naming
user_one="Harshit"  "snake case writing"
userOne="Harshit"  "camel case writing"

'''
nitsih 
nandjnfj
16546
nkanf = lkadfk64
''' #we can use ''' MATTER ''', it will not run
