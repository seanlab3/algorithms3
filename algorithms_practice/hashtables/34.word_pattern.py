'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase 
letters that may be separated by a single space.
'''

# def word_pattern(pattern, words):
#     word_map = {}
#     seen = set()
#
#     words = words.split()
#     if len(pattern) != len(words):
#         return False
#
#     for i in range(len(pattern)):
#         if pattern[i] in word_map:
#             if words[i] != word_map[pattern[i]]:
#                 return False
#         else:
#             if words[i] in seen:
#                 return False
#             word_map[pattern[i]] = words[i]
#             seen.add(words[i])
#     return True
#

from algorithms3.hashtables import word_pattern
pattern = "abba"
str = "dog cat cat dog"
print(word_pattern(pattern,str))































































