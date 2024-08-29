# break in the output numbers

# for i in range (1, 11):
#     if i==5: # here every condition is being printed if i = 1, then it will check for i==5 condition for break otherwise it will print it goes with every number
#         break 
#     print(i)

    # continue function
    # to print 1 to 10 but not 5
for i in range (1, 11):
    if i==5:
        continue # when i==5 comes, the execution doesnot goes to print, rather the continue function again goes to for loop.
    print(i)