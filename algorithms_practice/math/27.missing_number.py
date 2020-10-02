'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find 
the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant extra space complexity?
'''

# def missing_number(nums):
#     sumx = 0
#     for number in nums:
#         sumx += number
#
#     total = (len(nums)*(len(nums)+1)) // 2
#     return total-sumx
from algorithms3.math import missing_number

a=[9,6,4,2,3,5,7,0,1]

print(missing_number(a))
