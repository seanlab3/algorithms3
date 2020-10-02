'''
Suppose an array sorted in ascending order is rotated at 
some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array 
return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

# def search_rotated(nums, target):
#     left, right = 0, len(nums)-1
#
#     while left <= right:
#         mid = (left+right) // 2
#         if nums[mid] == target:
#             return mid
#
#         if nums[left] <= nums[mid]:
#             if nums[left] <= target <= nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if nums[mid] <= target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#     return -1
from algorithms3.binarysearch import search_rotated_array

nums = [4,5,6,7,0,1,2]
target = 3

print(search_rotated_array(nums,target))