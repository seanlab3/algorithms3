'''
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may
 not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

# def two_sum_sorted(numbers, target):
#     left, right = 0, len(numbers)-1
#
#     while left < right:
#         candidate_sum = numbers[left] + numbers[right]
#         if candidate_sum == target:
#             return [left+1, right+1]
#         elif candidate_sum < target:
#             left += 1
#         else:
#             right -= 1
#
#     return []
#
from algorithms3.arrays import two_sum_sorted_array
numbers = [2,7,11,15]
target = 9

print(two_sum_sorted_array(numbers,target))