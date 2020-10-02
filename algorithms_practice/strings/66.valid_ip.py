'''Write a function to check whether an input string is a valid IPv4 
address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which 
consists of four decimal numbers, each ranging from 0 to 255, separated by 
dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 
172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, 
each group representing 16 bits. The groups are separated by colons (":"). 
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid 
one. Also, we could omit some leading zeros among four hexadecimal digits and 
some low-case characters in the address to upper-case ones, so 
2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading z
eros and using upper cases).

However, we don't replace a consecutive group of zero value with a single 
empty group using two consecutive colons (::) to pursue simplicity. For 
example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, 
the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in
 the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
'''

# def valid_ip(IP):
#
#     def isIPv4(s):
#             try: return str(int(s)) == s and 0 <= int(s) <= 255
#             except: return False
#
#     def isIPv6(s):
#         if len(s) > 4: return False
#         try: return int(s, 16) >= 0 and s[0] != '-'
#         except: return False
#
#     if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
#         return "IPv4"
#     if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
#         return "IPv6"
#     return "Neither"


# def valid_ip_v2(IP):
#     if '.' in IP and len(IP.split('.')) == 4:
#         for number in IP.split('.'):
#             try:
#                 if not str(int(number)) == number:
#                     return 'Neither'
#             except: return 'Neither'
#             if not 0 <= int(number) <= 255:
#                 return 'Neither'
#         return 'IPv4'
#     elif len(IP.split(':')) == 8:
#         for number in IP.split(':'):
#             if len(number) == 0 or len(number) > 4 or number[0] == '-':
#                 return 'Neither'
#             try: int(number, 16)
#             except: return 'Neither'
#         return 'IPv6'
#     else:
#         return 'Neither'
from algorithms3.strings import valid_ip,valid_ip_v2
a="256.256.256.256"
print(valid_ip(a))

print(valid_ip_v2(a))