# Ternary Search - divide our array in three parts
# Time Complexity: O(log3 n)

def ternary_search(array, start, end, target):
    while start <= end:
        # divide array in three parts
        mid1 = start + (end - start)//3
        mid2 = end - (end-start)//3
        
        # target is found at mid1
        if array[mid1] == target:
            return mid1
        
        # target is found at mid2
        elif array[mid2] == target:
            return mid2
            
        # target is less than element at mid1
        elif target < array[mid1]:
            return ternary_search(array, start, mid-1, target)
        
        # target is greater than element at mid2
        elif target > array[mid2]:
            return ternary_search(array, mid2+1, end, target)
        
        # target is in between element at mid 1 and element at mid 2
        else:
            return ternary_search(array, mid1+1, mid2-1, target)
            
    # target is not found
    return -1

# Input
array = [1,2,3,4,5,6,7,8,9,10]
start = 0
end = len(array) - 1
target = 9

# Result
result = ternary_search(array, start, end, target)
print("Target Element at index", result)
