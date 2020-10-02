'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 
'''

# def defang_ip(address):
#     return ''.join('[.]' if x == '.' else x for x in address)
from algorithms3.strings import defanged_ip_address
address = "1.1.1.1"
print(defanged_ip_address.defang_ip(address))
