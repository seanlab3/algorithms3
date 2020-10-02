'''Count the number of segments in a string, where a segment is defined to 
be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''

# def count_segments(s):
#     return len(s.split())
from algorithms3.strings import number_of_segments_string

a="Hello, my name is John"

print(number_of_segments_string.count_segments(a))

