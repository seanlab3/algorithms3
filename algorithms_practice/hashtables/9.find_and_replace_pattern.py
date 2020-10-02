'''
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x 
in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, 
and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
'''

# def find_replace_pattern(words, pattern):
#     def decode(word):
#         m = {}
#         return [m.setdefault(w, len(m)) for w in word]
#
#     return [word for word in words if decode(word)==decode(pattern)]
#
#
#
# def find_replace_pattern_v2(words, pattern):
#
#     def helper(word):
#         mp = {}
#         for x, y in zip(pattern, word):
#             if mp.setdefault(x, y) != y:
#                 return False
#         return len(set(mp.values())) == len(mp.values())
#
#     res = []
#     for word in words:
#         if helper(word): res.append(word)
#     return res
from algorithms3.hashtables import find_and_replace_pattern
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(find_and_replace_pattern.find_replace_pattern(words,pattern))

print(find_and_replace_pattern.find_replace_pattern_v2(words,pattern))
