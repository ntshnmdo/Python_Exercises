def merge_sort(A):
    merge_sort2(A, 0, len(A)-1) #recursive function (pass in list A, with start index, end index)

def merge_sort2(A, first, last):
    if first < last: # if there is more than one element in list
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)
    
def merge(A, first, middle, last):
    L = A[first:middle] # first half of the list into variable L
    R = A[middle:last+1] # second half of the list into var R
    L.append(999999999)
    R.append(999999999) # append v large number 
    i = j = 0 # indexes for L, R
    # we will fill A empty list with smaller elements of L, R
    for k in range (first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1