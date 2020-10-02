'''
Write a function that takes an unsigned integer and return the number of '1' bits it has 
(also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''

# def hamming_weight(n):
#     count = 0
#     while n:
#         n &= (n - 1)
#         count += 1
#
#     return count
#
# def hamming_weight_v2(n):
#     return bin(n).count('1')
from algorithms3.bits import hamming_weight,hamming_weight_v2
#a=1111111111111111111111111111110
a=2147483646   # 30
print(hamming_weight(a))

print(hamming_weight_v2(a))
