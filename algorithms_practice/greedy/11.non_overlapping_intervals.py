'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
 

Example 1:

Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
 

Example 2:

Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
 

Example 3:

Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''

# def erase_overlap(intervals):
#     intervals.sort(key = lambda x: (x[1], x[0]))
#
#     erase, i = 0, 0
#     while i < len(intervals) - 1:
#         j = i + 1
#         while j < len(intervals) and intervals[i][1] > intervals[j][0]:
#             erase += 1
#             j += 1
#         i = j
#
#     return erase
from algorithms3.greedy import non_overlapping_intervals
a=[ [1,2], [2,3], [3,4], [1,3] ]
print(non_overlapping_intervals.erase_overlap(a))