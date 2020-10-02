'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

# from collections import deque
# def jump_game_two(nums):
#     if len(nums) < 2: return 0
#
#     que = deque([(0, nums[0])])
#     level = 0
#     while que:
#         node_count, max_reachable, start_index = len(que), 0, que[0][0]
#         for _ in range(node_count):
#             index, val = que.popleft()
#             if index == len(nums) - 1: return level
#             max_reachable = max(index+val, max_reachable)
#
#         max_reachable = min(max_reachable, len(nums) - 1)
#         for i in range(start_index + 1, max_reachable + 1):
#             que.append((i, nums[i]))
#         level += 1
#
#     return 0
#
#
# def jump_game_two_v2(nums):
#     if len(nums) < 2: return 0
#     level = current_max = next_max = index = 0
#
#     while current_max - index + 1 > 0:
#         level += 1
#         for index in range(current_max + 1):
#             next_max = max(next_max, nums[index] + index)
#             if next_max >= len(nums) - 1:
#                 return level
#         current_max = next_max
#
#     return 0
#
#
# def jump(sA):
#     memo = {}
#
#     def dp(n):
#         if n >= len(A) - 1:
#             return 0
#         if n in memo:
#             return memo[n]
#
#         val = float('inf')
#         max_jump = min(n + A[n], len(A) - 1)
#         for i in range(n + 1, max_jump + 1):
#             val = min(val, dp(i))
#
#         val += 1
#         memo[n] = val
#         return val
#
#     result = dp(0)
#     if result == float('inf'): return -1
#     return result
from algorithms3.dp import jump_game_II
a=[2,3,1,1,4]


print(jump_game_II.jump_game_two(a))

print(jump_game_II.jump_game_two_v2(a))