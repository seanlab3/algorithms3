'''
Find the minimum length word from a given dictionary words, which has all the letters from the string 
licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in 
the array.

The license plate might have the same letter occurring multiple times. For example, given a 
licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
'''

# from collections import Counter
# def shortest_completing_word(lp, words):
#     lp = ''.join([x.lower() for x in lp if x.isalpha()])
#     words.sort(key = len)
#
#     def check(count_lp, count_word):
#         for char in count_lp:
#             if char in count_word:
#                 count_word[char] -= count_lp[char]
#                 if count_word[char] < 0: return False
#             else:
#                 return False
#
#         return True
#
#     count_lp = Counter(lp)
#     for word in words:
#         count_word = Counter(word)
#         if check(count_lp, count_word):
#             return word
from algorithms3.hashtables import shortest_completing_word
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(shortest_completing_word(licensePlate,words))


