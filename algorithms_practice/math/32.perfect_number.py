'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive 
divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false 
when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

'''

# def perfect_number(num):
#     if num <= 1: return False
#
#     factors = set([1])
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             factors.add(i)
#             factors.add(num//i)
#
#     return sum(factors) == num

from algorithms3.math import perfect_number

a=28
print(perfect_number(a))