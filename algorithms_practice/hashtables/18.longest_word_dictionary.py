'''
Given a list of strings words representing an English Dictionary, find the longest word in words that 
can be built one character at a time by other words in words. If there is more than one possible answer, 
return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is 
lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''

# def longest_word(words):
#     result = ''
#     words = set(words)
#     for word in words:
#         if len(word) > len(result) or len(word) == len(result) and word < result:
#             if all(word[:k] in words for k in range(1, len(word))):
#                 result = word
#
#     return result
from algorithms3.hashtables import longest_word_dictionary
a=["w","wo","wor","worl", "world"]
print(longest_word_dictionary.longest_word(a))


