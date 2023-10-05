# Binary Search
# Time Complexity : O(logn)

# Iterative Approch
def binary_iterative(array,i,j,target):
    while i<=j:
        mid = i+(j-i)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            i = mid+1
        elif array[mid] > target:
            j = mid - 1 
    return -1
  
# Recursive Approch  
def binary_recursion(array,i,j,target):
    while i<=j:
        mid = i+(j-i)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary(array,mid+1,j,target)
        elif array[mid] > target:
            return binary(array,i,mid-1,target) 
    return -1

# Input
array = [1,2,3,4,5,6,7,8]
target = 6
start = 0
end = len(array) - 1

# Results
result_iterative = binary_iterative(array, start, end, target)
result_recursion = binary_iterative(array, start, end, target)

print("Search Item is at index(Using Iterative):", result_iterative)
print("Search Item is at index(Using Recursive):", result_recursion)
