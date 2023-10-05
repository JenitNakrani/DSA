#Linear Search
# Time Complexity : O(n)

# function defination of linear search
def linearSearch(array, target):
    for i in range(len(array)):
        # If target found
        if array[i] == target:
            return i

    # If target Not found in array
    return -1

# Input
array = [1,4,2,10,4,7,2,9]
target = 10

# Result
result = linearSearch(array, target)
print("Search Item is at index:", result)
