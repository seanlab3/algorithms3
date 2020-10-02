'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

# def sort_parity_even(A):
#     even, odd = 0, 1
#     while even < len(A):
#         while A[even] % 2 == 0: even += 2
#         while A[odd] % 2 == 1: odd += 2
#
#         A[even], A[odd] = A[odd], A[even]
#         even += 2
#         odd += 2
#
#     return A
from algorithms3.sort import sort_array_parity_II
a=[4,2,5,7]
print(sort_array_parity_II.sort_parity_even(a))