# with nested for loop

def insertion_sort(A):
    for i in range(1, len(A)): # outer loop, with loop variable i, and it starts with 2nd item of the list all the way to end of the list.
        for j in range(i-1, 0, -1): # inner loop starts from i-1 and goes left to 0 with a step of -1.
            if A[j] > A[j+1]: # comparing if item on rt is less than item on left they swap
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break # else break from inner loop, bcz items found in its correct position, and we go to next value in i outer loop

# cleaner with while loop

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i-1
        while A[j] > A[j+1] and j>=0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
        
# bts in python in swaping method, 
# each we swap, three operations takes place

# temp = x # x assigned to temp
# x = y # y assigned to x
# y = temp # temp assigned to y

# list = 7 8 5 4 9 2

# shifting method ( faster 2 times)
# we can cut that down byh copying 2 to curNum temp var
# curNum = 2
# comparisons, if 2 is less than 9, we write 9 over top of 2, if 2<8, write 7 over 8, if 2<7, write 5 over 7 so on
# so we got sorted list in one go instead of 3 steps

def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range (i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break