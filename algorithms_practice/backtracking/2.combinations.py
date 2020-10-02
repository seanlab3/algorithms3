'''
Given two integers n and k, return all possible combinations of 
k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# def combinations_numbers(n, k):
#     result = []
#
#     def backtrack(start, temp=[]):
#         if len(temp) == k:
#             result.append(temp[:])
#         else:
#             for i in range(start, n+1):
#                 temp.append(i)
#                 backtrack(i+1, temp)
#                 temp.pop()
#
#     backtrack(1)
#     return result

from algorithms3.backtracking import combinations_numbers

n = 4
k = 2

print(combinations_numbers(n,k))
