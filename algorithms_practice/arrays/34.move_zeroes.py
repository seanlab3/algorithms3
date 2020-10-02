'''
Given an array nums, write a function to move all 0's to the end 
of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# def move_zeroes(nums):
#     zero_position = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[zero_position] = nums[zero_position], nums[i]
#             zero_position += 1
#     return nums
from algorithms3.arrays import move_zeroes

a=[0,1,0,3,12]
print(move_zeroes(a))