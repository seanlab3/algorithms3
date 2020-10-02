'''
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the 
original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new 
length of the array.
Follow up:
Could you solve it using only O(1) extra space?

Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: 
["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.

Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
'''

# def compress_string(chars):
#     index = write_index = 0
#
#     while index < len(chars):
#         count = 1
#         char_at_index = chars[index]
#         while index+1 < len(chars) and chars[index] == chars[index+1]:
#             index += 1
#             count += 1
#         index += 1
#         chars[write_index] = char_at_index
#         write_index += 1
#
#         if count > 1:
#             for char in str(count):
#                 chars[write_index] = char
#                 write_index += 1
#
#     return write_index
from algorithms3.strings import string_compression
a=["a","a","b","b","c","c","c"]
print(string_compression.compress_string(a))

