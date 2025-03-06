'''
l = ["Harry", "rohan", "shubham", "nitish"]
'''

def rem(l, word):
    n = []

    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "rohan", "shubham", "nitish", "an"]
print(rem(l, "an"))