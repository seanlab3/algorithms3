'''
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime 
number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. 
For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
'''

# def count_prime_set_bits(L, R):
#     primes = {2,3,5,7,11,13,17,19}
#     return sum(bin(x).count('1') in primes for x in range(L, R + 1))
#
# def count_prime_set_bits_v2(L, R):
#
#     def count_set_bits(n):
#         count = 0
#         while n:
#             n &= (n-1)
#             count += 1
#         return count
#
#     primes = {2,3,5,7,11,13,17,19}
#     return sum(count_set_bits(x) in primes for x in range(L, R + 1))
#
#
# def count_prime_set_bits_v3(L, R):
#
#     def count_set_bits(n):
#         count = 0
#         while n:
#             count += (n & 1)
#             n >>= 1
#         return count
#
#     count = 0
#     primes = {2, 3, 5, 7, 11, 13, 17, 19}
#     for i in range(L, R + 1):
#         set_bits = count_set_bits(i)
#         if set_bits in primes: count += 1
#
#     return count
from algorithms3.bits import count_set_bits_prime,count_set_bits_prime_v2,count_set_bits_prime_v3
L = 6
R = 10
print(count_set_bits_prime(L,R))

print(count_set_bits_prime_v2(L,R))


print(count_set_bits_prime_v3(L,R))

    