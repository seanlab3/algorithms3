'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, 
one of the numbers in the set got duplicated to another number in the set, which results in 
repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to 
firstly find the number occurs twice and then find the number that is missing. Return them in the
 form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
'''

# def find_set_mismatch(nums):
#     nums.append(1)
#     result = []
#     for i in range(len(nums)-1):
#         if nums[abs(nums[i])] < 0:
#             result.append(i)
#             continue
#         nums[abs(nums[i])] = -nums[abs(nums[i])]
#
#     for i in range(1, len(nums)):
#         if nums[i] > 0:
#             result.append(i)
#             break
#
#     return result
from algorithms3.arrays import find_set_mismatch
nums = [1,2,2,4]

print(find_set_mismatch(nums))
