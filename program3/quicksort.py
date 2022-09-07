# Implement Quick Sort algorithm with all the necessary functions
def partition(arr, low, high):
  # leftmost element as pivot
  pivot = arr[high]

  # pointer 
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i=i+1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

  # return the position 
  return i + 1

#quicksort function in passed arrray
def QuickSort(arr, low, high):
  if low < high:
    # find pivot element 
   # element smaller than pivot are on the left
        # and the element greater than pivot are on the right
    pivot = partition(arr, low, high)
    #recursive call to sort left and right subarray of pivot
    QuickSort(arr, low, pivot - 1)
    QuickSort(arr, pivot + 1, high)

# to pass the value and check the given sorting
array = [45, 14, 67, 4, 72, 13]
QuickSort(array, 0, len(array) - 1)
print('The Sorted Array:', array)
