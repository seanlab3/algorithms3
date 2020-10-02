'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, 
otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may 
contain duplicates.
Would this affect the run-time complexity? How and why?
'''

# def sorted_array_rotated_duplicates(nums, target):
#     left, right = 0, len(nums) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target: return True
#
#         if nums[left] == nums[mid] and nums[right] == nums[mid]:
#             left += 1
#             right -= 1
#
#         if nums[left] <= nums[mid]:
#             if nums[left] <= target and nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if nums[mid] < target and nums[right] >= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#     return False
from algorithms3.binarysearch import search_rotated_array_2

nums = [2,5,6,0,0,1,2]
target = 3
print(search_rotated_array_2(nums,target))



