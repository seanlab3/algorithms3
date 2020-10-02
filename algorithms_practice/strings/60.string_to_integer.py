'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first 
non-whitespace character is found. Then, starting from this character, takes an optional 
initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace 
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of 
representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''


# def string_to_integer(str:str) -> int:
#     str = str.strip()
#     if len(str) == 0:
#         return 0
#     tmp = "0"
#     result = 0
#     i = 0
#     if str[0] in "+-":
#         tmp = str[0]
#         i = 1
#     #print(tmp)
#     MAX_INT = 2147483647
#     MIN_INT = -2147483648
#     for i in range(i, len(str)):
#         if str[i].isdigit():
#             tmp += str[i]
#             #print(tmp)
#         else:
#             break
#     if len(tmp) > 1:
#         result = int(tmp)
#     if result > MAX_INT > 0:
#         return MAX_INT
#     elif result < MIN_INT < 0:
#         return MIN_INT
#     else:
#         return result
from algorithms3.strings import string_to_integer

a="-91283472332"
print(string_to_integer(a))
