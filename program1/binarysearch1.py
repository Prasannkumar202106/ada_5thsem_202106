# implement binary search
#first we will be using recursion-
def binary_search(arr, first, last, key):
 
    # Check base case
    if last >= first:
 
        mid = (last + first) // 2
 
        # If element is present at the middle itself
        if arr[mid] == key:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > key:
            return binary_search(arr, first, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, last, x)
 
    else:
        # Element is not present in the array
        return -1
 

arr = [ 21, 23, 34, 45, 100, 400, 678 ]
x = 400
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
#print the desired result or by seeing the inputs

print("searching is done through binary search method")
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



    #now implement binary search in python using iterative method-
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# to check the correctness
arr = [ 24, 37, 49, 100, 234, 567, 890 ]
x = 100
 
# for getting result printed
result = binary_search(arr, x)

print("searching is done through iterative search method")
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
