'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# def contains_duplicates(nums):
#     seen = set()
#     for i in range(len(nums)):
#         if nums[i] in seen:
#             return True
#         else:
#             seen.add(nums[i])
#     return False
from algorithms3.arrays import contains_duplicate_one

a=[1,1,1,3,3,4,3,2,4,2]

print(contains_duplicate_one(a))