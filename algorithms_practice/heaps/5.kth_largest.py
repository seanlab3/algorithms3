'''
Find the kth largest element in an unsorted array. Note that it is the kth largest 
element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
# import heapq
# def kth_largest(num, k):
#     heapq._heapify_max(num)
#     while k > 1:
#         heapq._heappop_max(num)
#         k -= 1
#
#     return heapq._heappop_max(num)
from algorithms3.heaps import kth_largest

a=[3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest(a,k))

