'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with 
any positive integer, replace the number by the sum of the squares of its digits, and repeat 
the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

# def happy_numbers(n):
#     mem = set()
#
#     while True:
#         n = sum([int(x)**2 for x in str(n)])
#         if n in mem:
#             return False
#         elif n == 1:
#             return True
#         mem.add(n)
#
# def happy_numbers_v2(n):
#     orig = set()
#     while 1:
#         sum = 0
#         while n > 0:
#             sum += (n % 10) ** 2
#             n /= 10
#         if sum == 1:
#             return True
#         else:
#             if sum in orig:
#                 return False
#             orig.add(sum)
#             n = sum
#
from algorithms3.math import happy_numbers,happy_numbers_v2

print(happy_numbers(19))

#print(happy_numbers_v2(19))