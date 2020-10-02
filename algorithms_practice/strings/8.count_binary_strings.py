'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 
0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", 
"1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
'''

# def count_binary_strings(s):
#     prev, current, result = 0, 1, 0
#
#     for i in range(1, len(s)):
#         if s[i] != s[i - 1]:
#             result += min(prev, current)
#             prev, current = current, 1
#         else:
#             current += 1
#
#     return result + min(prev, current)
#
# def count_binary_strings_v2(s):
#     groups = [1]
#     for i in range(1, len(s)):
#         if s[i - 1] != s[i]:
#             groups.append(1)
#         else:
#             groups[-1] += 1
#
#     result = 0
#     for i in range(1, len(groups)):
#         result += min(groups[i], groups[i - 1])
#
#     return result
#
from algorithms3.strings import count_binary_strings

a="00110011"
print(count_binary_strings(a))