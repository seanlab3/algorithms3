'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous 
row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

# def search_matrix(matrix, target):
#     left, right = 0, len(matrix)*len(matrix[0])-1
#     while left <= right:
#         mid = (left+right) // 2
#         row = mid // len(matrix[0])
#         col = mid % len(matrix[0])
#
#         if matrix[row][col] == target:
#             return True
#         elif matrix[row][col] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return False
from algorithms3.binarysearch import search_2d_matrix

matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3
print(search_2d_matrix(matrix,target))
