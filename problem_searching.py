# Find a position of first infinite number
# Input: [20,-30,10,8,7,0,29,infinite,infinite,infinite,infinite]
# Output: 7

# Binary Search to find infinite number
# Time Complexity: O(logn)
def binary_search(array,i,j,target):
    while  i <= j:
        mid = i + (j-i) // 2
        if array[mid] != target:
            return binary_search(array,mid+1,j,target)
        else:
            if array[mid-1] < target:
                return mid
            else:
                return binary_search(array,i,mid-1,target)
    return -1

# Linear Search to find infinite number
# Time Complexity: O(n)
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Inputs
array = [20,-30,10,8,7,0,29,float('inf'),float('inf')float('inf'),float('inf')]
start = 0
end = 10
target = float('inf')

# Results
result_linear_search = linearSearch(array, target)
result_binary_search = binary_search(array, start, end, target)

print("First infinite number is at index(Linear Search):",result_linear_search)
print("First infinite number is at index(Binary Search):",result_binary_search)
