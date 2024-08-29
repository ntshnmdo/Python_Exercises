def reverse_list(l):
    reverse = []
    for i in range(1, len(l)+1):
        reverse.append(l.pop())
    return reverse

numbers = [1,2,3,4]
print(reverse_list(numbers))
