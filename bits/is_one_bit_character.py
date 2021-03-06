'''
We have two special characters. The first character can be represented by one bit 0. The second character
 can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit 
character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit 
character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit
 character.
'''

def is_one_bit_character(bits):
    for i in range(len(bits) - 1):
        if bits[i] == 1: bits[i + 1] = None
    return True if bits[-1] == 0 else False

# def is_one_bit_character_v2(bits):
#     parity = bits.pop()
#     while bits and bits.pop(): parity ^= 1
#     return parity == 0