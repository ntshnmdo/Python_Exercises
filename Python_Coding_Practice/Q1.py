# Q. Write a function to count the frequency of each element in a list (use dictionary)
# Dictionary can be used as frequency counter

arr = [1,2,3,4,2,3,1,4,3,2,3,2,1]
frequencyDict = {}  # dict
for i in arr: # iterating
    if i in frequencyDict: # TC for this searching is O(1)
        frequencyDict[i] += 1
    else:
        frequencyDict[i] = 1 # key[] = value
print(frequencyDict)