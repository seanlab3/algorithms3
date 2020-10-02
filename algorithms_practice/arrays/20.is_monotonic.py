'''

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone 
decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
'''

# def monotonic_array(A):
#     if len(A) == 1: return True
#     down, up = False, False
#
#     for i in range(len(A) - 1):
#         if A[i] > A[i + 1]:
#             if up: return False
#             down = True
#         elif A[i] < A[i + 1]:
#             if down: return False
#             up = True
#
#     return False if up and down else True
from algorithms3.arrays import is_monotonic

a=[1,2,2,3]

b=[1,3,2]

print(is_monotonic(a))

print(is_monotonic(b))

