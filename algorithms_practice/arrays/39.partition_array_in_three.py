'''
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
'''

# def partition_three(A):
#     sumx = sum(A)
#     if sumx % 3: return False
#     sumx //= 3
#
#     targets = [2 * sumx, sumx]
#
#     target = 0
#     for num in A:
#         target += num
#         if target == targets[-1]:
#             targets.pop()
#         if not targets: return True
#
#     return False
#
from algorithms3.arrays import partition_array_in_three

a=[0,2,1,-6,6,-7,9,1,2,0,1]
print(partition_array_in_three(a))