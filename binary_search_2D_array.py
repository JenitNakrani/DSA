# Search in 2D Array using Binary Search
# Time Complexity: O(log mn)

def searchInSortedMatrix(matrix, target):
    # length of a row
    m = len(matrix)
    if m == 0:
        return False
        
    # number of columns
    n = len(matrix[0])
    
    # Binary Implementation
    start, end = 0,m*n-1
    while start <= end:
        mid = start + (end - start) // 2
        
        # Extract a dimention from 2D Array
        # row_number = index // n
        # column_number = index % n
        mid_element = matrix[mid//n][mid%n]
        if mid_element == target:
            return True
        elif mid_element > target:
            end = mid - 1
        else:
            start = mid+1
    return False

# Input
matrix = [[1,3,5,7],[9,11,13,15],[17,19,21,23]]
target = 21

# Result
result = searchInSortedMatrix(matrix, target)
print("Is target element is in matrix ? :", result)
