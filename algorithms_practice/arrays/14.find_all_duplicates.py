'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

# def find_all_duplicates(nums):
#     result = list()
#     for i, x in enumerate(nums):
#         if nums[abs(x) - 1] < 0:
#             result.append(abs(x))
#         else:
#             nums[abs(x) - 1] = -nums[abs(x) - 1]
#
#     return result
#
from algorithms3.arrays import find_all_duplicates

a=[4,3,2,7,8,2,3,1]
print(find_all_duplicates(a))
