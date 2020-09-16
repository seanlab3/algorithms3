'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one 
number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def max_product(nums):
    result = prev_max = prev_min = nums[0]
        
    for i in range(1, len(nums)):
        candidates = (nums[i], nums[i] * prev_max, nums[i] * prev_min)
        prev_max = max(candidates)
        prev_min = min(candidates)
        
        result = max(result, prev_max)
    
    return result 