'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different 
order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if 
and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is 
unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the 
blank character which is less than any other character (More info).
'''


# def is_alien(words, order):
#     dictionary = {char:index for index, char in enumerate(order)}
#
#     for i in range(len(words) - 1):
#         for x, y in zip(words[i], words[i + 1]):
#             if x != y:
#                 if dictionary[x] > dictionary[y]:
#                     return False
#                 break
#
#         else:
#             if len(words[i]) > len(words[i + 1]): return False
#
#     return True
from algorithms3.hashtables import verifying_alien_dictionary
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(verifying_alien_dictionary(words,order))
