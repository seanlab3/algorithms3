'''
Given an arbitrary ransom note string and another string containing letters 
from all the magazines, write a function that will return true if the ransom note 
can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
# from collections import Counter
# def ransom_note(note, magazine):
#     count = Counter(magazine)
#     for char in note:
#         if char in count and count[char] > 0:
#             count[char] -= 1
#         else:
#             return False
#     return True
from algorithms3.strings import ransom_note

a="aa"
b="ab"
print(ransom_note(a,b))



