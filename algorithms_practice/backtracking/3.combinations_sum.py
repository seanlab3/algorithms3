'''
Given a set of candidate numbers (candidates) (without duplicates) and a 
target number (target), find all unique combinations in candidates where the 
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

# def combinations_sum(nums:list, target:int) -> list:
#     result = []
#     nums.sort()
#
#     def backtrack(temp, start, remain):
#         if remain < 0: return
#         if remain == 0: result.append(temp[:])
#         else:
#             for i in range(start, len(nums)):
#                 temp.append(nums[i])
#                 backtrack(temp, i, remain-nums[i])
#                 temp.pop()
#
#     backtrack([], 0, target)
#     return result
#
#
#
from algorithms3.backtracking import combinations_sum

candidates = [2,3,6,7]
target = 7
print(combinations_sum(candidates,target))