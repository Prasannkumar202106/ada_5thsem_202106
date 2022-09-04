#Program for implementation of MergeSort
# First subarray thats we work on is arr[l..m]
# Second subarray we work on is arr[m+1..r]
 
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    #empty arrays
    O = [0] * (n1)
    U = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        O[i] = arr[l + i]
 
    for j in range(0, n2):
        U[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if O[i] <= U[j]:
            arr[k] = O[i]
            i += 1
        else:
            arr[k] = U[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = O[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = U[j]
        j += 1
        k += 1
 
# l is for left index and r is right index
def mergeSort(arr, l, r):
    if l < r: 
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# passing the value to sort
arr = [7, 10, 24, 5, 8, 1]
n = len(arr)
print("inserted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n after sorting that is merge resulting array is")
for i in range(n):
    print("%d" % arr[i],end=" ")