# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
    for i in range(0, len(arr) ):
        if arr[i] == target:
          return i

    return -1   # not found
print(linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -6))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  while high > low:
      midpoint = (high + low) // 2
      if arr[midpoint] == target:
          return midpoint
      elif arr[midpoint] < target:
          low = midpoint
      elif arr[midpoint] > target:
        high = midpoint
  # TO-DO: add missing code
  return -1 # not found

print(binary_search([1,2,3,4,5], 3))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0:
      return -1
  if len(arr) == 1 and arr[0] != target:
      return -1
  else: 
      middle = (low+high)//2
      if arr[middle] == target:
          return middle
      elif arr[middle] < target:
          return binary_search_recursive(arr[middle:], target, middle, high)
      elif arr[middle] > target:
         return binary_search_recursive(arr[:middle], target, low, middle)

print(binary_search_recursive([1,2,3,4,5,6], 7, 0, 5))
