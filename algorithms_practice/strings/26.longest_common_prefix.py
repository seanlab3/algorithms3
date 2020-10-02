'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

# def longest_common_prefix(m):
#     if not m: return ''
#     s1 = min(m)
#     s2 = max(m)
#
#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i]
#     return s1
from algorithms3.strings import longest_common_prefix
a=["flower","flow","flight"]
print(longest_common_prefix(a))
