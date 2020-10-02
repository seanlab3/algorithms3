'''
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of t
he array to the very right. You can only see the k numbers in the window. Each time the sliding 
window moves right by one position. Your job is to output the median array for each window in 
the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty 
array.


'''

# from heapq import *
#
# def median_sliding_window_v2(nums, k):
#     result = []
#     window = nums[:k-1]
#     window.sort()
#     for i in range(k - 1, len(nums)):
#         bisect.insort(window, nums[i])
#         mid = len(window) // 2
#         if k % 2: result.append(float(window[mid]))
#         else: result.append((window[mid] + window[mid - 1]) / 2)
#         window.remove(nums[i - k + 1])
#
#     return result
from algorithms3.heaps import sliding_window_median
a=[1,3,-1,-3,5,3,6,7]
k=3
print(sliding_window_median.median_sliding_window_v2(a,k))