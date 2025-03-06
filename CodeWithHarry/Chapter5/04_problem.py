s = set()

s.add(20)
s.add(20.0)
s.add('30')

print(len(s))

# python donot diff 1 == 1.0
# both are same 
# that's why set 20 donot repeat
