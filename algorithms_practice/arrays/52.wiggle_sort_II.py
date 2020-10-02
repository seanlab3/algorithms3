'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

# def wiggle_sort(nums):
#     sorted_nums = sorted(nums)
#     for i in range(1, len(nums), 2): nums[i] = sorted_nums.pop()
#     for i in range(0, len(nums), 2): nums[i] = sorted_nums.pop()
#
from algorithms3.arrays import wiggle_sort
nums = [1, 3, 2, 2, 3, 1]

print(wiggle_sort(nums))